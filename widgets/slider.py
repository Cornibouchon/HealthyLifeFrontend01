import streamlit as st
import pandas as pd


def daterange_slider(average_sport_scores_per_participant):
    # Extract date columns and convert them to datetime
    date_columns = pd.to_datetime(average_sport_scores_per_participant['Date'],
                                  errors='coerce')  # Handle invalid parsing
    # Create formatted date labels
    date_labels = [date.strftime('%-d. %B') for date in date_columns if date is not pd.NaT]  # Filter out NaT values
    # Create a slider using the range of indices
    selected_dates = st.slider(
        "Select Date Range",
        min_value=1,  # Start from 1
        max_value=len(date_labels),  # Max value corresponds to the number of dates
        value=(1, len(date_labels)),  # Default to show all dates starting from 1
        step=1
    )
    # Adjust the selected_dates to zero-based indexing for DataFrame operations
    selected_dates_adjusted = (selected_dates[0] - 1, selected_dates[1] - 1)
    return date_labels, selected_dates_adjusted
