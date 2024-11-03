import streamlit as st
import pandas as pd
import plotly.express as px


def calculate_total_team_scores_sleep(data):
    # Create a new DataFrame to store results
    result_data = {
        'Date': [],
        'Bonjour': [],
        'Muchachos': []
    }

    # Iterate through each unique date in the original DataFrame
    for date in data['Date'].unique():
        # Filter the rows for the current date and only keep rows with 'abs_sleep' or 'rel_sleep'
        date_data = data[(data['Date'] == date) & (data['Score_typ'].isin(['abs_sleep', 'rel_sleep']))]

        # Calculate total scores for 'Bonjour' and 'Muchachos' by summing the relevant entries
        total_score_bonjour = date_data['Bonjour'].sum() / 2  # Sum and divide by 2
        total_score_muchachos = date_data['Muchachos'].sum() / 2  # Sum and divide by 2

        # Round to one decimal place
        total_score_bonjour = round(total_score_bonjour, 1)
        total_score_muchachos = round(total_score_muchachos, 1)

        # Append the results to the result_data dictionary
        result_data['Date'].append(date)
        result_data['Bonjour'].append(total_score_bonjour)
        result_data['Muchachos'].append(total_score_muchachos)

    # Convert the result_data dictionary into a new DataFrame
    result_df = pd.DataFrame(result_data)
    return result_df


def calculate_average_scores(fulldata):
    # Filter the relevant rows for abs_sleep and rel_sleep
    activity_data = fulldata[fulldata['Score_typ'].isin(['abs_sleep', 'rel_sleep'])]

    # Select participant columns (assuming they are HL1, HL2, ..., HLN)
    participant_columns = fulldata.columns[2:-2]  # Adjust indices based on your DataFrame

    # Create an empty DataFrame to store results
    result_data = {'Date': [], **{col: [] for col in participant_columns}}

    # Group by date
    for date, group in activity_data.groupby('Date'):
        # Calculate the average score for each participant
        average_scores = {}
        for col in participant_columns:
            abs_score = group.loc[group['Score_typ'] == 'abs_sleep', col].sum()
            rel_score = group.loc[group['Score_typ'] == 'rel_sleep', col].sum()
            average_score = (abs_score + rel_score) / 2
            average_scores[col] = average_score

        # Append the results to the result_data dictionary
        result_data['Date'].append(date)
        for col in participant_columns:
            result_data[col].append(average_scores[col])

    # Convert the result_data dictionary into a new DataFrame
    result_df = pd.DataFrame(result_data)
    return result_df


def display_sleep(full_data):
    # Set the column names for the new DataFrame
    team_bonjour_col = 'Bonjour'
    team_muchachos_col = 'Muchachos'

    sleep_team_data = calculate_total_team_scores_sleep(full_data)  # Get the total scores
    average_sleep_scores_per_participant = calculate_average_scores(full_data)

    # Extract date columns and convert them to datetime
    date_columns = pd.to_datetime(average_sleep_scores_per_participant['Date'],
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

    # Display the selected date range with formatting
    st.markdown(
        f"**Selected Dates:** {date_labels[selected_dates_adjusted[0]]} to {date_labels[selected_dates_adjusted[1]]}")

    # Get the selected dates for summing scores
    selected_date_range = sleep_team_data['Date'][selected_dates_adjusted[0]:selected_dates_adjusted[1] + 1]

    # Filter sleep_team_data based on the selected date range
    filtered_data = sleep_team_data[sleep_team_data['Date'].isin(selected_date_range)]

    # Calculate the sum for Bonjour and Muchachos
    total_score_bonjour = filtered_data['Bonjour'].sum()
    total_score_muchachos = filtered_data['Muchachos'].sum()

    # Display team names and total scores in two columns
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"<h2 style='text-align: center;'>{team_bonjour_col}</h2>", unsafe_allow_html=True)
        st.markdown(f"""
                    <div class='total-score'>
                        <h2>Total Score</h2>
                        <h1>{total_score_bonjour:.1f}</h1> 
                    </div>
                """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"<h2 style='text-align: center;'>{team_muchachos_col}</h2>", unsafe_allow_html=True)
        st.markdown(f"""
                    <div class='total-score'>
                        <h2>Total Score</h2>
                        <h1>{total_score_muchachos:.1f}</h1> 
                    </div>
                """, unsafe_allow_html=True)

    # Filter average_sleep_scores_per_participant based on the selected date range
    selected_participant_data = average_sleep_scores_per_participant[
        average_sleep_scores_per_participant['Date'].isin(selected_date_range)
    ]

    # Calculate total scores for each participant based on the filtered data
    total_participant_scores = selected_participant_data.iloc[:, 1:].sum()  # Sum across participants

    # Create DataFrame for sorted scores
    sorted_scores = pd.DataFrame({'Participant': selected_participant_data.columns[1:],
                                  'Total Score': total_participant_scores.values})

    sorted_scores = sorted_scores.sort_values(by='Total Score', ascending=False)

    # Display the sorted participant rankings
    st.subheader("Participant Ranking")
    for index, row in sorted_scores.iterrows():
        st.write(f"{row['Participant']}: {row['Total Score']:.1f}")  # Rounded score display
