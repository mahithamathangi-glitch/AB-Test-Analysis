import streamlit as st
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="A/B Test Analysis",
    page_icon="📊"
)

st.title("📊 A/B Test Analysis Dashboard")

st.write(
    "Comparison of Control and Treatment groups "
    "using session duration."
)

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR.parent / "ab_test_analysis_dataset.csv"

df = pd.read_csv(DATA_FILE)

control = df[
    df["group"] == "Control"
]["session_duration_min"]

treatment = df[
    df["group"] == "Treatment"
]["session_duration_min"]

control_mean = control.mean()
treatment_mean = treatment.mean()

difference = treatment_mean - control_mean

lift = (
    difference / control_mean
) * 100

t_stat, p_value = stats.ttest_ind(
    control,
    treatment,
    equal_var=False
)

pooled_std = np.sqrt(
    (
        (len(control)-1) * control.std()**2 +
        (len(treatment)-1) * treatment.std()**2
    )
    /
    (
        len(control) +
        len(treatment) -
        2
    )
)

cohens_d = difference / pooled_std

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Control Mean",
    f"{control_mean:.2f}"
)

col2.metric(
    "Treatment Mean",
    f"{treatment_mean:.2f}"
)

col3.metric(
    "Lift",
    f"{lift:.2f}%"
)

col4.metric(
    "p-value",
    f"{p_value:.6f}"
)

st.subheader("Descriptive Statistics")

summary = pd.DataFrame({
    "Mean": [
        control_mean,
        treatment_mean
    ],
    "Median": [
        control.median(),
        treatment.median()
    ],
    "Std Dev": [
        control.std(),
        treatment.std()
    ]
}, index=["Control", "Treatment"])

st.dataframe(summary)

st.subheader("Distribution Comparison")

fig, ax = plt.subplots()

ax.boxplot(
    [control, treatment],
    tick_labels=["Control", "Treatment"]
)

ax.set_ylabel(
    "Session Duration (minutes)"
)

ax.set_title(
    "Control vs Treatment"
)

st.pyplot(fig)

st.subheader("Statistical Test")

st.write(
    f"**Welch t-statistic:** {t_stat:.4f}"
)

st.write(
    f"**p-value:** {p_value:.6f}"
)

st.write(
    f"**Cohen's d:** {cohens_d:.4f}"
)

if p_value < 0.05:

    st.success(
        "Statistically significant: Reject H₀."
    )

    st.write(
        "Treatment shows a statistically significant "
        "improvement in average session duration."
    )

else:

    st.warning(
        "Not statistically significant: Fail to reject H₀."
    )
