# Does Cash Keep Companies Alive?

### A Liquidity vs. Survival Case Study

Dataset:https://www.kaggle.com/datasets/fedesoriano/company-bankruptcy-prediction)
Tools: Python, pandas, SciPy, scikit-learn, Matplotlib


### Business Question

Do companies with stronger liquidity have a better chance of survival? And how does liquidity compare with debt and profitability in predicting bankruptcy?

### 1. Project Overview

A company can be profitable on paper but still fail because it cannot meet its short-term financial obligations.

I explored this issue using financial data from 6,819 Taiwanese companies, including 220 bankrupt companies (3.2%).

I focused on 10 financial ratios covering liquidity, debt, and profitability.

### 2. Key Findings

**Liquidity makes a difference.**

* Companies in the lowest quick ratio quartile had a 10% bankruptcy rate, compared with 0.5% in the highest quartile.
* The quick ratio showed an 83% probability of distinguishing a surviving company from a bankrupt one based on their relative scores.

**But liquidity is not the whole story.**

I compared three predictive models:

| Model                  | ROC-AUC |
| ---------------------- | ------: |
| Liquidity only         |    0.80 |
| Debt and profitability |    0.92 |
| All financial measures |    0.93 |

Debt and profitability provided more predictive information than liquidity alone.

**Profitability and debt also mattered.**

* Bankruptcy reached 10.7% among companies in the lowest profitability quartile.
* A one-standard-deviation increase in the debt ratio was associated with 3.7 times higher odds of bankruptcy, holding other variables constant.

### 3. Business Takeaways

For lenders and financial advisors:

* Use liquidity ratios as an initial financial health check.
* Assess debt and profitability alongside cash availability.
* Avoid making financial decisions based on a single ratio.

For business owners:

Maintaining cash reserves is important, but managing debt and generating sustainable profits are equally relevant to financial stability.

### 4. My Conclusion

The analysis shows that liquidity is an important warning signal, but it does not tell the whole story.

Companies need more than cash to remain financially stable. Their ability to manage debt and generate profits also matters.

### 5. Tools and Techniques Used

**Python:** pandas, SciPy, scikit-learn, Matplotlib

**Methods:** Data cleaning, quartile analysis, statistical testing, correlation analysis, logistic regression, and cross-validation.

**Limitations:** The results show associations, not causation, and are based on publicly listed Taiwanese companies rather than small businesses generally.

**Project files:** https://github.com/nesa57903-wq/financial-survival-case-study
 Kaggle Notebook : https://www.kaggle.com/datasets/fedesoriano/company-bankruptcy-prediction
