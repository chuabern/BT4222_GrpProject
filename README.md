# Contributing to the repo
Wherever possible, try to push to your respective forked repos (i.e. xxx/BT4222_GrpProject) instead of pushing directly to the main repo.
Once you have pushed to your forked repos, you can create a PR from there to merge your code into the main repo.

## Avoiding Merge Conflicts
I'm not too sure with how well jupyter-notebooks do with Git considering they don't load on the webpage, but wherever possible try to make changes in a different/new *cell* instead of existing cells so the conflicts will be easier to resolve.

# Scraping 
The latest notebook to run your scrapping on is `Scrape Updates.ipynb`

## Raw data files
Raw data files are stored in `Raw Data`.

## Clean data files
The raw data files from `Raw Data` have been cleaned using `clean_data.ipynb` and the cleaned datasets are saved into the `Clean_data` folder.

## Scraped Data
Scraped text data from the datasets in `Clean_data` will be uploaded in `Output`

Please save your scraped output into their respective folders e.g. FAQ/Story/Comments etc,

# Combining Datasets
Once all relevant data has been scraped, we will merge all of them back into one dataset.

This is done with `combined_scraped_data.py`, and the output dataset is saved as `Combined_dataset.csv` (STILL INCOMPLETE)

