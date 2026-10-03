

This project uses the **Company Bankruptcy Prediction** dataset on Kaggle:
https://www.kaggle.com/datasets/fedesoriano/company-bankruptcy-prediction

The data was collected from the Taiwan Economic Journal for the years 1999-2009. Bankruptcy is defined by the business regulations of the Taiwan Stock Exchange.

License: Data files © Original Authors

 How to get the data

1. Open the link above, sign in to Kaggle (free), and click **Download**.
2. Unzip the download. You will get a file called `data.csv`.
3. In the project folder, create a folder `data`, and inside it a folder `raw`.
4. Put the file there so the path is `data/raw/data.csv`.
5. Run `python run_pipeline.py`.

 About the file

It has 6,819 companies and 96 columns (the bankruptcy column plus 95 financial ratios). This project uses only the `Bankrupt?` column plus 10 financial ratios that are relevant to the question. They are listed in `src/config.py`.

The raw file is not stored in this repository. Please download it from Kaggle using the link above.
