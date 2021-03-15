import pandas as pd 
import glob

# Use cleaned dataset as the base datatable 
dataset = pd.read_csv('Clean_data/Kickstarter.csv').drop('Unnamed: 0', axis=1)

def combine_multiple_csv(files):
  combined_files = pd.DataFrame()
  for file in files:
    data = pd.read_csv(file).drop('Unnamed: 0', axis=1)
    combined_files = combined_files.append(data)
  return combined_files

# Add in story text
story_files = glob.glob("Output/Story/Story*.csv")
story = combine_multiple_csv(story_files)

# Add in FAQ/text ? (not sure which one to use here)
# faq = pd.read_csv('Output/FAQ/FAQ_combined_0to1000.csv').drop('Unnamed: 0', axis=1)
# faq_text = pd.read_csv('Output/FAQ/FAQ_text_0-100.csv').drop('Unnamed: 0', axis=1)

# Add in updates
updates_files = glob.glob("Output/Update/Update*.csv")
updates = combine_multiple_csv(updates_files)

# Add in comments
comments_files = glob.glob("Output/Comments/Comment*.csv")
comments = combine_multiple_csv(comments_files)

data_to_be_combined = [story, updates, comments] # add in FAQ when data has 'id'

for data in data_to_be_combined:
  dataset = dataset.merge(data, left_on = 'id', right_on = 'id', how = 'left')

dataset.to_csv("Output/Combined_dataset.csv")