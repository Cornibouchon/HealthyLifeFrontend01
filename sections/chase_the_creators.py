import streamlit as st
import pandas as pd

from config import TEAM_RESTFUL_GAINZ_COL, TEAM_FINAL_BOSSES_COL, CREATOR_ONE, CREATOR_TWO
from widgets.ranking import display_ranking, display_Teamscore, display_ranking_chase
from widgets.slider import daterange_slider
from utils.data_manipulation import calculate_total_team_scores_by_type, \
    calculate_average_score_per_particpant_and_type, calculate_abs_sport_score_per_particpant, \
    calculate_total_abs_activity


def display_chase_the_creators(full_data, chase_data):
    creators_data_sum1 = calculate_average_score_per_particpant_and_type(chase_data, ["abs_activity", "abs_sleep"])

    creators_data_sum1 = creators_data_sum1[
        (creators_data_sum1['Date'] >= '2024-11-07') & (creators_data_sum1['Date'] <= '2024-11-10')]

    # Create two columns for Team Bonjour and Team Muchachos
    col1, col2 = st.columns(2)
    total_friss_mi_stoub = creators_data_sum1["Friss mi Stoub"].sum()  # Use the rounded scores
    total_smaesh_di_waeg = creators_data_sum1["Smash di weg"].sum()  # Use the rounded scores

    with col1:
        st.markdown(f"<h2 style='text-align: center;'>{CREATOR_ONE}</h2>",
                    unsafe_allow_html=True)  # Centered heading
        st.markdown(f"""
                <div class='total-score' style="text-align: center;">
                    <h2>iEvent Score</h2>
                    <h1>{total_friss_mi_stoub.__round__(2)}</h1>
                </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"<h2 style='text-align: center;'>{CREATOR_TWO}</h2>",
                    unsafe_allow_html=True)  # Centered heading
        st.markdown(f"""
                <div class='total-score' style="text-align: center;">
                    <h2>iEvent Score</h2>
                    <h1>{total_smaesh_di_waeg.__round__(2)}</h1>
                </div>
            """, unsafe_allow_html=True)

    # Get the total scores
    average_sport_scores_per_participant = calculate_abs_sport_score_per_particpant(full_data)

    # Filter the data between February 6 and February 10
    selected_participant_data = average_sport_scores_per_participant[
        (average_sport_scores_per_participant['Date'] >= '2024-11-07') &
        (average_sport_scores_per_participant['Date'] <= '2024-11-10')
        ]

    # Calculate total scores for each participant based on the filtered data
    total_participant_scores = selected_participant_data.iloc[:, 1:].sum()

    # Create DataFrame for sorted scores
    sorted_scores = pd.DataFrame({
        'Participant': selected_participant_data.columns[1:],
        'Total Score': total_participant_scores.values
    })

    # Sort participants by total score in descending order
    sorted_scores = sorted_scores.sort_values(by='Total Score', ascending=False).reset_index(drop=True)

    # Display the sorted participant rankings with custom styling
    st.subheader("Participant Ranking")

    display_ranking_chase(sorted_scores, total_friss_mi_stoub, total_smaesh_di_waeg)
