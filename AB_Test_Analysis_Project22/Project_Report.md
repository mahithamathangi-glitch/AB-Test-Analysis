# A/B Test Analysis — Project Report

## 1. Introduction

A/B testing is a controlled experimentation technique used to compare two versions of a product, feature, webpage, or campaign.

This project compares a Control group with a Treatment group using session duration as the primary performance metric.

## 2. Objective

The objective is to determine whether the Treatment version significantly changes average session duration compared with the Control version.

## 3. Dataset

The dataset contains 1,000 users:

- 500 Control
- 500 Treatment

The primary metric is session duration in minutes.

## 4. Hypotheses

### Null Hypothesis

There is no difference between the mean session duration of Control and Treatment.

### Alternative Hypothesis

There is a difference between the mean session duration of Control and Treatment.

Significance level: 0.05.

## 5. Statistical Method

Welch's independent two-sample t-test was used because the metric is continuous and the two groups contain independent observations.

Cohen's d was used to measure the standardized effect size.

A 95% confidence interval was calculated for the difference between Treatment and Control.

## 6. Results

Control mean:

**49.87 minutes**

Treatment mean:

**52.55 minutes**

Absolute improvement:

**2.68 minutes**

Percentage lift:

**5.38%**

Welch's t-statistic:

**-4.2891**

p-value:

**0.0000197**

Cohen's d:

**0.2713**

95% confidence interval:

**1.46 to 3.91 minutes**

## 7. Interpretation

The p-value is substantially below the significance threshold of 0.05.

Therefore, the null hypothesis is rejected.

The Treatment group has a higher average session duration.

However, Cohen's d of approximately 0.27 indicates a relatively small standardized effect.

## 8. Recommendation

The Treatment version can be recommended for further consideration because the observed improvement is statistically significant.

However, before full rollout, the business should evaluate:

- Implementation cost
- User experience
- Revenue impact
- Conversion rate
- Retention
- Other guardrail metrics

## 9. Limitations

The dataset used in this project is a reproducible practice dataset.

Real-world A/B testing should additionally consider:

- Randomization quality
- Sample ratio mismatch
- Experiment duration
- Statistical power
- Multiple testing
- Business guardrail metrics
- Pre-defined stopping criteria

## 10. Conclusion

The analysis demonstrates the complete A/B testing workflow from data preparation through statistical testing and business recommendation.

The Treatment group produced a 5.38% improvement in average session duration, and the difference was statistically significant.
