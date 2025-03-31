# sections/overview_newData.py
import streamlit as st
import plotly.express as px
import pandas as pd
from utils.data_manipulation import calculate_total_team_scores
from config import TEAM_2md23, TEAM_Arbs, TEAM_MinhKhaZen, TEAM_2md23_COL, TEAM_Arbs_COL, TEAM_MinhKhaZen_COL


def display_overview_new(data):
    # Calculate scores
    results_data = calculate_total_team_scores(data)

    # Create a long-format DataFrame for plotting
    data_long = results_data.melt(id_vars=['Date'], value_vars=[TEAM_2md23_COL, TEAM_Arbs_COL, TEAM_MinhKhaZen_COL],
                                  var_name='Team', value_name='Score')

    fig_team01 = plot_total_team_score(data_long, TEAM_2md23_COL)
    fig_team02 = plot_total_team_score(data_long, TEAM_Arbs_COL)
    fig_team03 = plot_total_team_score(data_long, TEAM_MinhKhaZen_COL)

    # Create two columns for Team Bonjour and Team Muchachos
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"<h2 style='text-align: center;'>{TEAM_2md23_COL}</h2>",
                    unsafe_allow_html=True)  # Centered heading
        total_bonjour = results_data[TEAM_2md23_COL].sum().__round__(2)  # Use the rounded scores
        st.markdown(f"""
            <div class='total-score' style="text-align: center;">
                <h2>Team Score</h2>
                <h1>{total_bonjour}</h1>
            </div>
        """, unsafe_allow_html=True)
        st.plotly_chart(fig_team01, use_container_width=True, key='fig_team01')  # Plot for Team Bonjour

    with col2:
        st.markdown(f"<h2 style='text-align: center;'>{TEAM_Arbs_COL}</h2>",
                    unsafe_allow_html=True)  # Centered heading
        total_muchachos = results_data[TEAM_Arbs_COL].sum().__round__(2)  # Use the rounded scores
        st.markdown(f"""
            <div class='total-score' style="text-align: center;">
                <h2>Team Score</h2>
                <h1>{total_muchachos}</h1>
            </div>
        """, unsafe_allow_html=True)
        st.plotly_chart(fig_team02, use_container_width=True, key='fig_team02')  # Plot for Team Muchachos

    with col3:
        st.markdown(f"<h2 style='text-align: center;'>{TEAM_MinhKhaZen_COL}</h2>",
                    unsafe_allow_html=True)  # Centered heading
        total_minhkha = results_data[TEAM_MinhKhaZen_COL].sum().__round__(2)  # Use the rounded scores
        st.markdown(f"""
            <div class='total-score' style="text-align: center;">
                <h2>Team Score</h2>
                <h1>{total_minhkha}</h1>
            </div>
        """, unsafe_allow_html=True)
        st.plotly_chart(fig_team03, use_container_width=True, key='fig_team03')  # Plot for Team MinhKhaZen


def plot_total_team_score(data_long, team_name):
    # Plotly Bar Chart for Team Bonjour
    fig_bonjour = px.bar(data_long[data_long['Team'] == team_name], x='Date', y='Score', barmode='group',
                         title="Daily Scores",
                         labels={"Score": "Points", "Date": "Date"})
    fig_bonjour.update_layout(title_x=0.5)
    fig_bonjour.update_yaxes(range=[0, 50])
    fig_bonjour.update_xaxes(tickformat="%Y-%m-%d", tickvals=data_long['Date'].unique())
    return fig_bonjour
