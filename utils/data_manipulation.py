import pandas as pd

from config import TEAM_2md23_COL, TEAM_Arbs_COL, TEAM_MinhKhaZen_COL
import pandas as pd


def calculate_total_team_scores(data):
    # Create a new DataFrame to store results
    result_data = {
        'Date': [],
        TEAM_2md23_COL: [],
        TEAM_Arbs_COL: [],
        TEAM_MinhKhaZen_COL: []
    }

    # Iterate through each unique date in the original DataFrame
    for date in data['Date'].unique():
        # Filter the rows for the current date
        date_data = data[data['Date'] == date]

        # Calculate total scores by summing the first four entries
        total_score_team01 = date_data[TEAM_2md23_COL].head(4).sum() / 4
        total_score_team02 = date_data[TEAM_Arbs_COL].head(4).sum() / 4
        total_score_team03 = date_data[TEAM_MinhKhaZen_COL].head(4).sum() / 4
        # Round to one decimal place
        total_score_team01 = round(total_score_team01, 1)
        total_score_team02 = round(total_score_team02, 1)
        total_score_team03 = round(total_score_team03, 1)
        # Append the results to the result_data dictionary
        result_data['Date'].append(date)
        result_data[TEAM_2md23_COL].append(total_score_team01)
        result_data[TEAM_Arbs_COL].append(total_score_team02)
        result_data[TEAM_MinhKhaZen_COL].append(total_score_team03)
    # Convert the result_data dictionary into a new DataFrame
    result_df = pd.DataFrame(result_data)
    return result_df


def calculate_total_abs_activity(data):
    # Filter the data to only include dates from February 6, 2024, onward
    data = data[data['Date'] >= '2024-11-06']

    # Create a new DataFrame to store results
    result_data = {
        'Date': [],
        'Friss mi Stoub': [],
        'Smash di weg': []
    }

    # Iterate through each unique date in the filtered DataFrame
    for date in data['Date'].unique():
        # Filter the rows for the current date and for 'abs_activity'
        date_data = data[(data['Date'] == date) & (data['Score_typ'] == 'abs_activity')]

        # Sum the 'abs_activity' scores for each participant
        total_score_friss_mi_stoub = date_data['Friss mi Stoub'].sum()
        total_score_smash_di_weg = date_data['Smash di weg'].sum()

        # Append the results to the result_data dictionary
        result_data['Date'].append(date)
        result_data['Friss mi Stoub'].append(total_score_friss_mi_stoub)
        result_data['Smash di weg'].append(total_score_smash_di_weg)

    # Convert the result_data dictionary into a new DataFrame
    result_df = pd.DataFrame(result_data)
    return result_df


def calculate_total_abs_activity_and_sleep(data):
    # Filter the data to only include dates from February 6, 2024, onward
    data = data[data['Date'] >= '2024-11-06']

    # Create a new DataFrame to store results
    result_data = {
        'Date': [],
        'Friss mi Stoub': [],
        'Smash di weg': []
    }

    # Iterate through each unique date in the filtered DataFrame
    for date in data['Date'].unique():
        # Filter the rows for the current date and for 'abs_activity'
        date_data = data[(data['Date'] == date) & (data['Score_typ'] == 'abs_activity')]

        # Sum the 'abs_activity' scores for each participant
        total_score_friss_mi_stoub = date_data['Friss mi Stoub'].sum()
        total_score_smash_di_weg = date_data['Smash di weg'].sum()

        # Append the results to the result_data dictionary
        result_data['Date'].append(date)
        result_data['Friss mi Stoub'].append(total_score_friss_mi_stoub)
        result_data['Smash di weg'].append(total_score_smash_di_weg)

    # Convert the result_data dictionary into a new DataFrame
    result_df = pd.DataFrame(result_data)
    return result_df


def calculate_total_team_scores_by_type(data, score_types):
    # Create a new DataFrame to store results
    result_data = {
        'Date': [],
        TEAM_2md23_COL: [],
        TEAM_Arbs_COL: [],
        TEAM_MinhKhaZen_COL: []
    }

    # Iterate through each unique date in the original DataFrame
    for date in data['Date'].unique():
        # Filter the rows for the current date and only keep rows with the specified score types
        date_data = data[(data['Date'] == date) & (data['Score_typ'].isin(score_types))]

        # Calculate total scores for TEAM_BONJOUR_COL and TEAM_MUCHACHOS_COL by summing the relevant entries
        total_score_team1 = date_data[TEAM_2md23_COL].sum() / 2  # Sum and divide by 2
        total_score_team2 = date_data[TEAM_Arbs_COL].sum() / 2  # Sum and divide by 2
        total_score_team3 = date_data[TEAM_MinhKhaZen_COL].sum() / 2  # Sum and divide by 2
        # Round to one decimal place
        total_score_team1 = round(total_score_team1, 1)
        total_score_team2 = round(total_score_team2, 1)
        total_score_team3 = round(total_score_team3, 1)
        # Append the results to the result_data dictionary
        result_data['Date'].append(date)
        result_data[TEAM_2md23_COL].append(total_score_team1)
        result_data[TEAM_Arbs_COL].append(total_score_team2)
        result_data[TEAM_MinhKhaZen_COL].append(total_score_team3)
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
            rel_score = group.loc[group['Score_typ'] == score_types[1], col].sum()
            average_score = (abs_score + rel_score) / 2
            average_scores[col] = average_score

        # Append the results to the result_data dictionary
        result_data['Date'].append(date)
        for col in participant_columns:
            result_data[col].append(average_scores[col])

    # Convert the result_data dictionary into a new DataFrame
    result_df = pd.DataFrame(result_data)
    return result_df


def calculate_abs_sport_score_per_particpant(fulldata):
    # Filter the relevant rows for the specified score types
    activity_data = fulldata[fulldata['Score_typ'] == "abs_activity"]

    # Select participant columns (assuming they are HL1, HL2, ..., HLN)
    participant_columns = fulldata.columns[2:-2]  # Adjust indices based on your DataFrame

    # Create an empty DataFrame to store results
    result_data = {'Date': [], **{col: [] for col in participant_columns}}

    # Group by date
    for date, group in activity_data.groupby('Date'):
        # Calculate the average score for each participant
        absolute_sport_scores = {}
        for col in participant_columns:
            abs_score = group.loc[group['Score_typ'] == ["abs_activity"], col].sum()
            absolute_sport_scores[col] = abs_score

        # Append the results to the result_data dictionary
        result_data['Date'].append(date)
        for col in participant_columns:
            result_data[col].append(absolute_sport_scores[col])

    # Convert the result_data dictionary into a new DataFrame
    result_df = pd.DataFrame(result_data)

    return result_df
