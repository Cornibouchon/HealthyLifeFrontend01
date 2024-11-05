# sections/overview_newData.py
import streamlit as st
import plotly.express as px
import pandas as pd
from utils.data_manipulation import calculate_average_score_per_particpant_and_type, calculate_total_team_scores
from config import TEAM_BONJOUR_COL, TEAM_MUCHACHOS_COL


def display_overview_new(data):
    # Calculate scores
    results_data = calculate_total_team_scores(data)

    # Create a long-format DataFrame for plotting
    data_long = results_data.melt(id_vars=['Date'], value_vars=[TEAM_BONJOUR_COL, TEAM_MUCHACHOS_COL],
                                  var_name='Team', value_name='Score')

    fig_bonjour = plot_total_team_score(data_long, TEAM_BONJOUR_COL)
    fig_muchachos = plot_total_team_score(data_long, TEAM_MUCHACHOS_COL)

    # Create two columns for Team Bonjour and Team Muchachos
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"<h2 style='text-align: center;'>{TEAM_BONJOUR_COL}</h2>",
                    unsafe_allow_html=True)  # Centered heading
        total_bonjour = results_data[TEAM_BONJOUR_COL].sum()  # Use the rounded scores
        st.markdown(f"""
            <div class='total-score' style="text-align: center;">
                <h2>Team Score</h2>
                <h1>{total_bonjour}</h1>
            </div>
        """, unsafe_allow_html=True)
        st.plotly_chart(fig_bonjour, use_container_width=True, key='fig_bonjour')  # Plot for Team Bonjour

    with col2:
        st.markdown(f"<h2 style='text-align: center;'>{TEAM_MUCHACHOS_COL}</h2>",
                    unsafe_allow_html=True)  # Centered heading
        total_muchachos = results_data[TEAM_MUCHACHOS_COL].sum()  # Use the rounded scores
        st.markdown(f"""
            <div class='total-score' style="text-align: center;">
                <h2>Team Score</h2>
                <h1>{total_muchachos}</h1>
            </div>
        """, unsafe_allow_html=True)
        st.plotly_chart(fig_muchachos, use_container_width=True, key='fig_muchachos')  # Plot for Team Muchachos


def plot_total_team_score(data_long, team_name):
    # Plotly Bar Chart for Team Bonjour
    fig_bonjour = px.bar(data_long[data_long['Team'] == team_name], x='Date', y='Score', barmode='group',
                         title="Daily Scores",
                         labels={"Score": "Points", "Date": "Date"})
    fig_bonjour.update_layout(title_x=0.5)
    fig_bonjour.update_yaxes(range=[0, 50])
    fig_bonjour.update_xaxes(tickformat="%Y-%m-%d", tickvals=data_long['Date'].unique())
    return fig_bonjour
