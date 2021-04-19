
import pandas as pd 
import glob
from datetime import datetime

# +
# Use cleaned dataset as the base datatable 
dataset = pd.read_csv('Clean_data/Kickstarter.csv').drop('Unnamed: 0', axis=1)

dataset.index.name = 'id_row'
dataset = dataset.reset_index()


# -

def combine_multiple_csv(files):
  combined_files = pd.DataFrame()
  for file in files:
    data = pd.read_csv(file)
    if 'Unnamed: 0' in data.columns:
      data = data.drop('Unnamed: 0', axis=1)
    combined_files = combined_files.append(data)
  combined_files['id'] = combined_files['id'].apply(lambda row: int())
  return combined_files

# Add in story text
story_files = glob.glob("Output/Story*.csv")
story = combine_multiple_csv(story_files)


# Add in FAQ
faq = glob.glob("Output/FAQ/FAQ_combined_0to3429.csv")
faq = combine_multiple_csv(faq)

# ## Not using updates anymore
# updates_files = glob.glob("Output/Update/Update*.csv")
# updates = combine_multiple_csv(updates_files)

# Add in comments
comments_files = glob.glob("Output/Comments/Comment*.csv")
comments = combine_multiple_csv(comments_files)

data_to_be_combined = [story, faq, comments] # add in FAQ when data has 'id'

# +
# Story
df1 = data_to_be_combined[0]
del df1['id']
df1.index.name = 'id_row'
df1 = df1.reset_index()

# FAQ
df2 = data_to_be_combined[1]
del df2['id']
df2.index.name = 'id_row'
df2 = df2.reset_index()

# Comments
df3 = data_to_be_combined[2]
del df3['id']
df3.index.name = 'id_row'
df3 = df3.reset_index()
# -

# Merge all df1, df2, df3
from functools import reduce
data_to_be_combined = reduce(lambda left,right: pd.merge(left,right,on='id_row'), [df1,df2,df3])
del data_to_be_combined['id_row']
data_to_be_combined.index.name = 'id_row'
data_to_be_combined = data_to_be_combined.reset_index()
data_to_be_combined.tail(1)

dataset = pd.merge(dataset, data_to_be_combined, on='id_row', how='left')
# dataset = dataset.iloc[:1000]

dataset['duration'] = dataset['deadline'].apply(lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S")) - dataset['launched_at'].apply(lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S"))

dataset['story'] = dataset['story'].fillna('NA')
dataset['faq'] = dataset['faq'].fillna('NA')
dataset['num_faq'] = dataset['num_faq'].fillna(0)
dataset['comments'] = dataset['comments'].fillna(" ")
dataset['n_comments'] = dataset['n_comments'].fillna(str('0'))

dataset.to_csv("Output/Combined_dataset.csv")