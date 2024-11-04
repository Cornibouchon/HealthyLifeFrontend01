import pandas as pd

from config import TEAM_BONJOUR_COL, TEAM_MUCHACHOS_COL


def calculate_total_team_scores(data):
    # Create a new DataFrame to store results
    result_data = {
        'Date': [],
        'Bonjour': [],
        'Muchachos': []
    }

    # Iterate through each unique date in the original DataFrame
    for date in data['Date'].unique():
        # Filter the rows for the current date
        date_data = data[data['Date'] == date]

        # Calculate total scores by summing the first four entries
        total_score_bonjour = date_data['Bonjour'].head(4).sum()
        total_score_muchachos = date_data['Muchachos'].head(4).sum()

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


def calculate_total_team_scores_by_type(data, score_types):
    # Create a new DataFrame to store results
    result_data = {
        'Date': [],
        'Bonjour': [],
        'Muchachos': []
    }

    # Iterate through each unique date in the original DataFrame
    for date in data['Date'].unique():
        # Filter the rows for the current date and only keep rows with the specified score types
        date_data = data[(data['Date'] == date) & (data['Score_typ'].isin(score_types))]

        # Calculate total scores for 'Bonjour' and 'Muchachos' by summing the relevant entries
        total_score_bonjour = date_data[TEAM_BONJOUR_COL].sum() / 2  # Sum and divide by 2
        total_score_muchachos = date_data[TEAM_MUCHACHOS_COL].sum() / 2  # Sum and divide by 2

        # Round to one decimal place
        total_score_bonjour = round(total_score_bonjour, 1)
        total_score_muchachos = round(total_score_muchachos, 1)

        # Append the results to the result_data dictionary
        result_data['Date'].append(date)
        result_data[TEAM_BONJOUR_COL].append(total_score_bonjour)
        result_data[TEAM_MUCHACHOS_COL].append(total_score_muchachos)

    # Convert the result_data dictionary into a new DataFrame
    result_df = pd.DataFrame(result_data)
    return result_df


def calculate_average_score_per_particpant_and_type(fulldata, score_types):
    # Filter the relevant rows for the specified score types
    activity_data = fulldata[fulldata['Score_typ'].isin(score_types)]

    # Select participant columns (assuming they are HL1, HL2, ..., HLN)
    participant_columns = fulldata.columns[2:-2]  # Adjust indices based on your DataFrame

    # Create an empty DataFrame to store results
    result_data = {'Date': [], **{col: [] for col in participant_columns}}

    # Group by date
    for date, group in activity_data.groupby('Date'):
        # Calculate the average score for each participant
        average_scores = {}
        for col in participant_columns:
            abs_score = group.loc[group['Score_typ'] == score_types[0], col].sum()
            rel_score = group.loc[group['Score_typ'] == score_types[0], col].sum()
            average_score = (abs_score + rel_score) / 2
            average_scores[col] = average_score

        # Append the results to the result_data dictionary
        result_data['Date'].append(date)
        for col in participant_columns:
            result_data[col].append(average_scores[col])

    # Convert the result_data dictionary into a new DataFrame
    result_df = pd.DataFrame(result_data)
    return result_df
