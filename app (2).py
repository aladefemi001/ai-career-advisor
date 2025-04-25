!pip install streamlit 
!pip install plotly 
!pip install pandas 
!pip install pyngrok
# AI Career Path Advisor - Streamlit App with Interactive Dashboard

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="AI Career Path Advisor", layout="wide")
st.title("🧠 AI Career Path Advisor")

# Sample dataset (can be replaced with actual CSV input or quiz output)
data = pd.read_csv("career_matches.csv")  # Assuming the file exists in your directory

# Sidebar - Weight sliders
st.sidebar.header("🎚️ Customize Weightings")
skill_weight = st.sidebar.slider("Skills Weight", 0, 10, 5)
interest_weight = st.sidebar.slider("Interests Weight", 0, 10, 5)
personality_weight = st.sidebar.slider("Personality Weight", 0, 10, 5)
workstyle_weight = st.sidebar.slider("Work Style Weight", 0, 10, 5)
goal_weight = st.sidebar.slider("Career Goals Weight", 0, 10, 5)

# Apply weights to scores (mock logic for demo purposes)
data["Weighted Score"] = (
    data["skills"] * skill_weight +
    data["interests"] * interest_weight +
    data["personality"] * personality_weight +
    data["work_style"] * workstyle_weight +
    data["goals"] * goal_weight
)
data["Weighted Score"] = data["Weighted Score"] / (skill_weight + interest_weight + personality_weight + workstyle_weight + goal_weight)

# Sort top matches
top_matches = data.sort_values(by="Weighted Score", ascending=False).head(5)

# Dashboard Charts
st.subheader("📊 Career Match Insights")
col1, col2 = st.columns(2)

# Bar chart of top careers
with col1:
    fig_bar = px.bar(top_matches, x="career", y="Weighted Score", title="Top Career Matches", color="career")
    st.plotly_chart(fig_bar, use_container_width=True)

# Radar chart of user profile breakdown
with col2:
    categories = ['Skills', 'Interests', 'Personality', 'Work Style', 'Goals']
    values = [skill_weight, interest_weight, personality_weight, workstyle_weight, goal_weight]

    fig_radar = go.Figure()
    fig_radar.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='User Preferences'
    ))
    fig_radar.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0,10])),
        showlegend=False,
        title="User Preference Profile"
    )
    st.plotly_chart(fig_radar, use_container_width=True)

# Display top matches in a table
st.subheader("🏆 Recommended Careers")
st.dataframe(top_matches[['career', 'Weighted Score']])
