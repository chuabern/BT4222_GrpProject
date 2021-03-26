import pandas as pd 
import glob
from datetime import datetime

# Use cleaned dataset as the base datatable 
dataset = pd.read_csv('Clean_data/Kickstarter.csv').drop('Unnamed: 0', axis=1)

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

### Not using updates anymore
# updates_files = glob.glob("Output/Update/Update*.csv")
# updates = combine_multiple_csv(updates_files)

# Add in comments
comments_files = glob.glob("Output/Comments/Comment*.csv")
comments = combine_multiple_csv(comments_files)

data_to_be_combined = [story, faq, comments] # add in FAQ when data has 'id'

for data in data_to_be_combined:
  dataset = dataset.merge(data, left_on = 'id', right_on = 'id', how = 'left')

# We only use 1000 data points
dataset = dataset.iloc[0:1001,]
dataset['duration'] = dataset['deadline'].apply(lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S")) - dataset['launched_at'].apply(lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S"))

dataset.to_csv("Output/Combined_dataset.csv")
