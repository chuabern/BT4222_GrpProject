import pandas as pd 

# Use cleaned dataset as the base datatable 
dataset = pd.read_csv('Clean_data/Kickstarter.csv').drop('Unnamed: 0', axis=1)

# Add in story text
story = pd.read_csv('Output/Story/Story_0-100.csv').drop('Unnamed: 0', axis=1)

# Add in FAQ/text ? (not sure which one to use here)
faq = pd.read_csv('Output/FAQ/FAQ_combined_0to1000.csv').drop('Unnamed: 0', axis=1)
faq_text = pd.read_csv('Output/FAQ/FAQ_text_0-100.csv').drop('Unnamed: 0', axis=1)

# Add in comments
comments = pd.read_csv('Output/Comments/Comments_0-100.csv').drop('Unnamed: 0', axis=1)

data_to_be_combined = [story, comments] # add in FAQ when data has 'id'

for data in data_to_be_combined:
  dataset = dataset.merge(data, left_on = 'id', right_on = 'id', how = 'left')

dataset.to_csv("Output/Combined_dataset.csv")