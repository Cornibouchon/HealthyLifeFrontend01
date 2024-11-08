# sections/overview_newData.py
import streamlit as st
import plotly.express as px
import pandas as pd
from utils.data_manipulation import calculate_total_team_scores
from config import TEAM_RESTFUL_GAINZ_COL, TEAM_FINAL_BOSSES_COL


def display_overview_new(data):
    # Calculate scores
    results_data = calculate_total_team_scores(data)

    # Create a long-format DataFrame for plotting
    data_long = results_data.melt(id_vars=['Date'], value_vars=[TEAM_RESTFUL_GAINZ_COL, TEAM_FINAL_BOSSES_COL],
                                  var_name='Team', value_name='Score')

    fig_bonjour = plot_total_team_score(data_long, TEAM_RESTFUL_GAINZ_COL)
    fig_muchachos = plot_total_team_score(data_long, TEAM_FINAL_BOSSES_COL)

    # Create two columns for Team Bonjour and Team Muchachos
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"<h2 style='text-align: center;'>{TEAM_RESTFUL_GAINZ_COL}</h2>",
                    unsafe_allow_html=True)  # Centered heading
        total_bonjour = results_data[TEAM_RESTFUL_GAINZ_COL].sum().__round__(2)  # Use the rounded scores
        st.markdown(f"""
            <div class='total-score' style="text-align: center;">
                <h2>Team Score</h2>
                <h1>{total_bonjour}</h1>
            </div>
        """, unsafe_allow_html=True)
        st.plotly_chart(fig_bonjour, use_container_width=True, key='fig_bonjour')  # Plot for Team Bonjour

    with col2:
        st.markdown(f"<h2 style='text-align: center;'>{TEAM_FINAL_BOSSES_COL}</h2>",
                    unsafe_allow_html=True)  # Centered heading
        total_muchachos = results_data[TEAM_FINAL_BOSSES_COL].sum()  # Use the rounded scores
        st.markdown(f"""
            <div class='total-score' style="text-align: center;">
                <h2>Team Score</h2>
                <h1>{total_muchachos.__round__(2)}</h1>
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
