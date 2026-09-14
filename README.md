# 📊 A/B Test Analysis

## Project Overview

This project performs an A/B test analysis to determine whether a Treatment version produces a statistically significant improvement compared with a Control version.

The analysis uses session duration as the primary continuous metric.

## Objective

The objective is to:

- Compare Control and Treatment groups
- Calculate descriptive statistics
- Visualize the distributions
- Perform hypothesis testing
- Calculate statistical significance
- Measure effect size
- Calculate a 95% confidence interval
- Provide an evidence-based recommendation

## Dataset

The dataset contains 1,000 observations:

- 500 Control users
- 500 Treatment users
- Session duration measured in minutes

### Variables

| Variable | Description |
|---|---|
| user_id | Unique user identifier |
| group | Control or Treatment |
| session_duration_min | Session duration in minutes |

## Hypotheses

### Null Hypothesis (H₀)

There is no difference in mean session duration between Control and Treatment.

### Alternative Hypothesis (H₁)

There is a difference in mean session duration between Control and Treatment.

Significance level:

**α = 0.05**

## Methodology

The following steps were performed:

1. Data loading
2. Data quality checks
3. Descriptive statistics
4. Distribution visualization
5. Hypothesis formulation
6. Assumption checking
7. Welch's independent two-sample t-test
8. Effect size calculation using Cohen's d
9. 95% confidence interval
10. Final recommendation

## Results

| Metric | Result |
|---|---:|
| Control Mean | 49.87 min |
| Treatment Mean | 52.55 min |
| Absolute Difference | 2.68 min |
| Percentage Lift | 5.38% |
| t-statistic | -4.2891 |
| p-value | 0.0000197 |
| Cohen's d | 0.2713 |
| 95% CI | 1.46 to 3.91 min |

## Statistical Conclusion

Since the p-value is below 0.05, the null hypothesis is rejected.

Therefore, there is statistically significant evidence of a difference between the Control and Treatment groups.

## Business Recommendation

The Treatment version is recommended for further consideration because it produced a statistically significant increase in average session duration.

However, Cohen's d is approximately 0.27, indicating a relatively small standardized effect.

Therefore, statistical significance should be considered together with practical/business significance, implementation cost, user experience, and other guardrail metrics.

## Technologies Used

- Python
- Pandas
- NumPy
- SciPy
- Matplotlib
- Jupyter Notebook
- Google Colab

## Project Structure

```text
AB_Test_Analysis_Project/
│
├── AB_Test_Analysis.ipynb
├── ab_test_analysis_dataset.csv
└── README.md
How to Run

Open the notebook using Google Colab or Jupyter Notebook.

Install required libraries:

pip install pandas numpy scipy matplotlib

Then run all notebook cells.

Key Learning

This project demonstrates that statistical significance alone is not sufficient for a business decision. Effect size and practical impact must also be considered.

## Live Demo

[[View the live A/B Testing Dashboard](YOUR_STREAMLIT_URL](https://ab-test-analysis-3fxdvag3xo8tgxuxdn5x7x.streamlit.app/))
