\# Does Cash Keep Companies Alive? A Liquidity vs. Survival Case Study



\*\*Links:\*\* \[Dataset (Kaggle)](https://www.kaggle.com/datasets/fedesoriano/company-bankruptcy-prediction) · \[Kaggle notebook](PASTE-YOUR-KAGGLE-NOTEBOOK-LINK-HERE)



\*\*Analyst:\*\* \_your name\_ · \*\*Tools:\*\* Python (pandas, SciPy, scikit-learn, Matplotlib) · \*\*Type:\*\* portfolio case study



> \*\*Business question:\*\* Do companies with more cash and short-term financial flexibility survive more often than companies with less, and how much does liquidity tell us compared with debt and profitability?



\---



\## 1. Ask

Many businesses fail even when they look profitable on paper, because they run out of cash to pay short-term bills. A bank, an investor, or an owner would want to know:



1\. Are companies that went bankrupt visibly weaker on liquidity than companies that survived?

2\. Which liquidity measure separates them best?

3\. Is liquidity a useful warning signal on its own, or do debt and profit matter more?



\*\*Stakeholder:\*\* a lender or advisor who supports businesses and wants simple early-warning indicators.



\## 2. Prepare



\### About the data

\- \*\*Where it comes from:\*\* I downloaded the \[\*Company Bankruptcy Prediction\* dataset from Kaggle](https://www.kaggle.com/datasets/fedesoriano/company-bankruptcy-prediction), uploaded by fedesoriano. The data was originally collected from the Taiwan Economic Journal for the years 1999 to 2009. Bankruptcy is defined by the business regulations of the Taiwan Stock Exchange.

\- \*\*License:\*\* \_Add the license shown on the Kaggle page.\_

\- \*\*Size:\*\* 6,819 companies and 96 columns (the bankruptcy column plus 95 financial ratios). 220 companies (3.2%) went bankrupt.



\### Which columns I used

I did not use all 96 columns. I kept only the ones relevant to my question: the bankruptcy column plus \*\*10 financial ratios\*\*.

\- \*\*7 liquidity measures:\*\* cash / total assets, cash / current liabilities, current ratio, quick ratio, working capital / assets, cash flow / assets, cash flow / liabilities.

\- \*\*3 debt and profit measures\*\* (for comparison): current liabilities / assets, debt ratio, net income / assets.



\### Limitations of the data

\- These are companies listed in Taiwan, and the dataset does not say how big each one is. I do not claim the results apply to every small business.

\- The source scales most ratios, so values like the current ratio are not literal. I compare companies by \*\*rank and quartile\*\* instead of reading raw numbers.

\- There is no time dimension, so the data shows association, not cause.



\## 3. Process

Implemented in `src/load\_clean.py`:

\- Removed stray spaces in the original column names and renamed them to readable names.

\- Checked for missing values and duplicate rows (there were none in this dataset).

\- Winsorized each ratio at the 1st and 99th percentile so extreme outliers cannot drive the results.

\- Kept all 6,819 companies. An optional sampling setting exists in `src/config.py`.



\## 4. Analyze

Implemented in `src/analyze.py`:

1\. \*\*Quartile analysis:\*\* rank companies from low to high on each measure and compare bankruptcy rates across the four groups.

2\. \*\*Effect size:\*\* Mann-Whitney U test, reported as the chance that a random surviving company scores higher than a random bankrupt one. 0.5 means no difference.

3\. \*\*Correlation check:\*\* many liquidity measures overlap.

4\. \*\*Logistic regression (5-fold cross-validated):\*\* liquidity only vs. debt and profit only vs. all measures, scored with ROC-AUC (0.5 = coin flip, 1.0 = perfect).



\## 5. Share: Key findings

Overall, 3.2% of the companies went bankrupt.



1\. \*\*Companies with the least liquidity went bankrupt far more often.\*\* In the lowest quarter on the quick ratio, 10.0% went bankrupt, compared with 0.5% in the highest quarter. That is about 19 times higher.

2\. \*\*The quick ratio and current ratio separated survivors from bankrupt companies best.\*\* A random surviving company had an 83% chance of a higher quick ratio than a random bankrupt one (81% for the current ratio). Cash relative to total assets was also strong: 7.6% bankrupt in the lowest quarter vs 0.6% in the highest.

3\. \*\*Liquidity alone is a useful warning signal, but debt and profit are stronger.\*\* A model using only liquidity scored an AUC of 0.80. A model using only debt and profitability scored 0.92. Using all measures scored 0.93, so adding liquidity gave only a small improvement.

4\. \*\*Profitability and debt stood out most.\*\* In the lowest quarter on net income / assets, 10.7% of companies went bankrupt, and the highest quarter had none. For each increase of one standard deviation in the debt ratio, the odds of bankruptcy were about 3.7 times higher, with the other measures held fixed.



Charts are in `reports/figures/`:



| | |

|---|---|

| !\[classes](reports/figures/fig01\_class\_balance.png) | !\[quartiles](reports/figures/fig02\_bankruptcy\_by\_quartile.png) |

| !\[distributions](reports/figures/fig03\_survivors\_vs\_failed.png) | !\[corr](reports/figures/fig04\_correlations.png) |

| !\[roc](reports/figures/fig05\_roc\_curves.png) | !\[odds](reports/figures/fig06\_odds\_ratios.png) |



\## 6. Act: Recommendations

1\. \*\*Lenders and advisors:\*\* use the quick ratio and cash / total assets as a quick first screen, because companies at the bottom on these measures went bankrupt many times more often.

2\. \*\*Do not judge on liquidity alone.\*\* Check debt and profitability too, since they predicted bankruptcy better.

3\. \*\*Owners:\*\* keep a cash cushion, and also watch debt and profit. A company with cash but heavy debt and weak earnings was still at high risk.

4\. \*\*Next analysis:\*\* use several years of data per company to see whether liquidity drops before bankruptcy.



\## Limitations

\- Association, not causation. Low cash may be a symptom of trouble rather than its cause.

\- Only 220 companies are bankrupt, so results rest on a modest number of cases.

\- Several liquidity measures overlap, so the odds-ratio chart should not be read one measure at a time. A few liquidity measures show a higher risk there, which comes from that overlap. The quartile results and model scores are more reliable.

\- The model is a simple screening tool, not a production credit model.



\## Reproduce

```bash

git clone <your-repo-url>

cd financial-survival-case-study

pip install -r requirements.txt

\# put the Kaggle CSV at data/raw/data.csv  (see data/README.md)

python run\_pipeline.py          # writes reports/results.md + reports/figures/\*

python -m pytest                # optional: runs the tests

```

A Kaggle-ready notebook version is in `notebooks/financial\_survival\_case\_study.ipynb`.



\## Repo layout

```

data/            README with download steps (raw CSV is git-ignored)

src/             config, cleaning, analysis, demo-data generator

notebooks/       self-contained notebook for Kaggle

reports/         results.md + figures (generated)

tests/           small tests for the cleaning step

run\_pipeline.py  one command to run everything

```

