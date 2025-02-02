import gspread
import pandas as pd
from PIL.ImageChops import screen
from oauth2client.service_account import ServiceAccountCredentials
import numpy as np
from helpers import *

# Define the scope and authorize with credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("key.json", scope)
client = gspread.authorize(creds)

try:
    spreadsheet_list = client.openall()
    print("Available spreadsheets:")
    for sheet in spreadsheet_list:
        print(f"- {sheet.title}")
except Exception as e:
    print(f"An error occurred: {e}")

try:
    sheet = client.open(
        "HealthyLifeEveryDay: Startumfrage (Responses)").sheet1  # or use .worksheet("Your Worksheet Name")

    response_data = sheet.get_all_values()
    np_data = np.array(response_data)

    # Initialize a list to store scores
    personality_scores = []

    # Calculate scores for each entry
    for response in response_data[1:]:  # Skip the header row
        scores = [
            response[1], calculate_personality_score(response, "PersonalityScore1", 2),  # offset 0 for index 2
            calculate_personality_score(response, "PersonalityScore2", 3),  # offset 1 for index 3
            calculate_personality_score(response, "PersonalityScore3", 4),  # offset 2 for index 4
            calculate_personality_score(response, "PersonalityScore4", 5)  # offset 3 for index 5
        ]
        personality_scores.append(scores)

        print(scores)
        # Convert scores to a NumPy array
    scores_array = np.array(personality_scores)

    # Print the scores array
    print("Personality Scores Array:")
    print(scores_array)
    df = pd.DataFrame(scores_array[1:], columns=scores_array[0])  # Skip the header row if not needed

    # Save DataFrame to Excel
    df.to_excel('output.xlsx', index=False)
    # Print the NumPy array content
    # print(np_data)
except gspread.exceptions.SpreadsheetNotFound:
    print("Spreadsheet not found. Please check the name and sharing permissions.")
except Exception as e:
    print(f"An error occurred: {e}")
# Fetch all values from the sheet and convert to numpy array
