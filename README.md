# Raw data files
Raw data files are stored in `Raw Data`.

The data file we used is `Kickstarter.csv`

# Clean data files
The raw data files from `Raw Data` have been cleaned using `clean_data.ipynb` and the cleaned datasets are saved into the `Clean_data` folder.

# Scraping 
We scraped the extra text features required using these files:

- Scrap Story.ipynb
- Scrape Comments.ipynb
- Scrape FAQ.ipynb

# Scraped Data
Scraped text data from the datasets in `Clean_data` will be uploaded in `Output`

The outputs are:
- Comments
- FAQ
- Update

# Combining Datasets
Once all relevant data has been scraped, we merged all of them back into one dataset.

This is done with `combined_scraped_data.py`, and the output dataset is saved as `Combined_dataset.csv`

# EDA
We performed EDA on the dataset with `EDA.ipynb`

# Feature Preprocessing
We perform feature preprocesing on the dataset with `Features_Preprocessing.ipynb`

# Models
Our models are:

1. Logistic Regression (`Logreg.ipynb`)

2. Decision Tree (`Decision Tree Final.ipynb`)

3. Random Forest (`Random_Forest.ipynb`)

4. SVM (`TJ_SVM-update.ipynb`)

5. Neural Network (`Neural Network.ipynb`)

Models are saved in output files as `{model}.pckl`

# Stacking
We perform stacking on all our models in `Ensemblestacking.ipynb`