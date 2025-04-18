import streamlit as st
from PIL import Image

# Page configuration
st.set_page_config(page_title="A/B Testing Project", layout="wide", initial_sidebar_state="expanded")

# Custom styling for header
st.markdown("""
    <h1 style='text-align: center; color: #2E7D32;'>📊 A/B Testing Analysis: Landing Page Experiment</h1>
""", unsafe_allow_html=True)

# Key finding at the top
st.info("""
    **Key Finding**: The new landing page does not significantly improve conversion rates over the old one. Recommendation: Retain the current landing page.
""")

# Introduction
st.markdown("""
    Welcome to the interactive report of an A/B testing experiment designed to evaluate whether a new landing page design increases user conversions compared to the existing one. This analysis provides a data-driven foundation for deciding which landing page to implement.
""")

# Sidebar navigation
with st.sidebar:
    st.markdown("### Navigation")
    selected = st.radio("Explore the Analysis:", [
        "1. Business Problem & Objective",
        "2. Dataset Details",
        "3. Visualizations",
        "4. Hypothesis Testing",
        "5. Conclusion"
    ], index=0)

# Section 1: Business Problem & Objective
if selected == "1. Business Problem & Objective":
    st.header("🎯 Objective")
    st.markdown("""
        The primary goal of this A/B testing experiment is to assess whether a newly designed landing page yields a **statistically significant** increase in conversion rates compared to the existing landing page. This evaluation aims to guide a data-driven decision on optimizing user engagement and business outcomes.
    """)

    st.header("💼 Business Problem")
    st.markdown("""
        In today's competitive online environment, even marginal improvements in conversion rates can lead to substantial revenue gains. The company has developed a redesigned landing page, hypothesizing that it enhances user experience and boosts conversions. To test this, users were randomly assigned to:

        - **Control Group**: Exposed to the existing (old) landing page.
        - **Treatment Group**: Exposed to the new landing page.

        The experiment tracked user interactions over a set period. The decision to adopt the new design hinges on **strong statistical evidence** of its superiority in driving conversions.
    """)

# Section 2: Dataset Details
elif selected == "2. Dataset Details":
    st.header("📂 Dataset Description")
    st.markdown("""
        The dataset captures user interactions during the A/B test. Below is a detailed breakdown of its structure:
    """)
    st.markdown("""
        | **Column Name**   | **Description**                              | **Data Type** |
        |-------------------|----------------------------------------------|---------------|
        | `user_id`         | Unique identifier for each user              | Int64         |
        | `time`       | Time of the user's site visit                | Datetime      |
        | `group`           | Assignment: 'control' or 'treatment'         | String        |
        | `landing_page`    | Page viewed: 'old_page' or 'new_page'        | String        |
        | `converted`       | Conversion status (1 = Yes, 0 = No)          | Int64         |
    """)
    st.markdown("""
        **Additional Notes**: 
        - The dataset includes thousands of user sessions collected over the experiment duration.
        - Random assignment ensures unbiased group comparisons.
    """)
    st.markdown("""
        **Explore the dataset on Kaggle**: [Ecommerce A/B Testing Dataset](https://www.kaggle.com/datasets/ahmedmohameddawoud/ecommerce-ab-testing)
    """)

# Section 3: Visualizations
elif selected == "3. Visualizations":
    st.header("📉 Visualizations")
    st.markdown("These visualizations provide insights into the experiment's outcomes.")

    # Two-column layout for first two plots
    col1, col2 = st.columns(2)
    with col1:
        st.image("average_conversion_by_group.png", caption="Average Conversion Rate by Group", use_container_width=True)
        st.markdown("""
            *Insight*: The control group (12.04%) slightly outperforms the treatment group (11.88%), but the difference appears minor.
        """)
    with col2:
        st.image("received_rate_control_treatment.png", caption="Received Rates for Both Groups", use_container_width=True)
        st.markdown("""
            *Insight*: The near-equal split (50.16% vs. 49.84%) confirms a balanced random assignment.
        """)

    # Remaining plots
    st.image("conversion_hist_by_group.png", caption="Conversion Distribution by Group", use_container_width=True)
    st.markdown("""
        *Insight*: Both groups show similar conversion distributions, suggesting no major behavioral shift with the new page.
    """)
    st.image("daily_rolling_avg.png", caption="Daily and 7-Day Rolling Average Conversion Rates", use_container_width=True)
    st.markdown("""
        *Insight*: Conversion trends remain stable over time, with no clear advantage for either page.
    """)
    st.image("z_test_distribution.png", caption="Z-Test Visualization with Rejection Regions", use_container_width=True)
    st.markdown("""
        *Insight*: The test statistic falls outside the rejection regions, indicating no significant difference.
    """)

# Section 4: Hypothesis Testing
elif selected == "4. Hypothesis Testing":
    st.header("🧪 Hypothesis Testing")
    st.markdown("A two-sample z-test for proportions was conducted to compare conversion rates.")

    st.subheader("Statistical Hypotheses")
    st.markdown("""
        - **Null Hypothesis (H₀)**: Conversion rates for the old and new landing pages are equal (p₁ = p₂).
        - **Alternative Hypothesis (H₁)**: Conversion rates differ (p₁ ≠ p₂).
    """)

    st.subheader("Observed Metrics")
    st.markdown("""
        | **Metric**                    | **Value**         |
        |-------------------------------|-------------------|
        | Control Group Conversion Rate | 0.1204 (12.04%)   |
        | Treatment Group Conversion Rate | 0.1188 (11.88%) |
        | Probability of New Page       | 0.5016            |
        | Probability of Old Page       | 0.4984            |
        | Standard Error (SE)           | 0.0012            |
        | Z-Score                       | -1.3109           |
        | P-Value                       | 0.1899            |
        | Alpha (Significance Level)    | 0.05              |
        | 95% Confidence Interval       | (-0.00394, 0.00078) |
        | Minimum Detectable Effect (MDE) | 0.01            |
        | Observed Effect               | -0.00157          |
    """)
    st.markdown("""
        **Interpretation**: 
        - The p-value (0.1899) exceeds alpha (0.05), so we fail to reject H₀.
        - The confidence interval includes zero, reinforcing no significant difference.
        - The observed effect (-0.00157) is below the MDE (0.01), indicating practical insignificance.
    """)

    st.subheader("Z-Test Visualization")
    st.image("z_test_distribution.png", caption="Z-Test Normal Distribution with Rejection Regions (α = 0.05)")
    st.markdown("""
        The z-score (-1.3109) lies within the acceptance region, supporting the null hypothesis.
    """)

# Section 5: Conclusion
elif selected == "5. Conclusion":
    st.header("📌 Conclusion")
    st.markdown("""
        Based on the A/B testing analysis, the following conclusions emerge:
        
        - **Statistical Significance**: The difference in conversion rates is not significant (p-value = 0.1899 > 0.05).
        - **Practical Significance**: The observed effect (-0.00157) is smaller than the minimum detectable effect (0.01), suggesting no meaningful business impact.
        - **Decision**: We fail to reject the null hypothesis, indicating insufficient evidence to favor the new landing page.
    """)
    st.success("""
        **Business Recommendation**: Retain the existing (old) landing page, as the new design does not demonstrate a significant improvement. Consider testing alternative designs or increasing sample size for future experiments if smaller effects are of interest.
    """)

# Footer with centered content
st.markdown("---")
st.markdown("""
    <style>
    a {
        color: #2E7D32;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    </style>
    <div style="text-align: center; font-size: 0.9em;">
        Analysis conducted by Mahan on 18-04-2025<br>
        GitHub: <a href='https://github.com/Mahan1554/A-B-Testing-Analysis-of-a-New-Landing-Page/blob/main/ABTesting_Project.ipynb'>Documentary</a><br>
        Contact: <a href='mailto:mahanbhimireddy@gmail.com'>mahanbhimireddy@gmail.com</a>
    </div>
""", unsafe_allow_html=True)
