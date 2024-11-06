import streamlit as st
import pandas as pd

from config import TEAM_RESTFUL_GAINZ_COL, TEAM_FINAL_BOSSES_COL
from widgets.ranking import display_ranking, display_Teamscore
from widgets.slider import daterange_slider
from utils.data_manipulation import calculate_total_team_scores_by_type, calculate_average_score_per_particpant_and_type


def display_sport(full_data):
    # Set the column names for the new DataFrame

    sport_team_data = calculate_total_team_scores_by_type(full_data,
                                                          ['abs_activity', 'rel_activity'])  # Get the total scores
    average_sport_scores_per_participant = calculate_average_score_per_particpant_and_type(full_data, ['abs_activity',
                                                                                                       'rel_activity'])

    date_labels, selected_dates_adjusted = daterange_slider(average_sport_scores_per_participant)

    # Display the selected date range with formatting
    st.markdown(
        f"**Selected Dates:** {date_labels[selected_dates_adjusted[0]]} to {date_labels[selected_dates_adjusted[1]]}")

    # Get the selected dates for summing scores
    selected_date_range = sport_team_data['Date'][selected_dates_adjusted[0]:selected_dates_adjusted[1] + 1]

    # Filter sport_team_data based on the selected date range
    filtered_data = sport_team_data[sport_team_data['Date'].isin(selected_date_range)]

    display_Teamscore(filtered_data, TEAM_RESTFUL_GAINZ_COL, TEAM_FINAL_BOSSES_COL)

    # Filter average_sport_scores_per_participant based on the selected date range
    selected_participant_data = average_sport_scores_per_participant[
        average_sport_scores_per_participant['Date'].isin(selected_date_range)
    ]

    # Calculate total scores for each participant based on the filtered data
    total_participant_scores = selected_participant_data.iloc[:, 1:].sum()  # Sum across participants

    # Create DataFrame for sorted scores
    sorted_scores = pd.DataFrame({
        'Participant': selected_participant_data.columns[1:],
        'Total Score': total_participant_scores.values
    })

    # Sort participants by total score in descending order
    sorted_scores = sorted_scores.sort_values(by='Total Score', ascending=False).reset_index(drop=True)

    # Display the sorted participant rankings with custom styling
    st.subheader("Participant Ranking")

    display_ranking(sorted_scores)
