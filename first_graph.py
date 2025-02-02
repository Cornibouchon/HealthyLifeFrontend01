import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

from sections.chase_the_creators import display_chase_the_creators
from sections.overview_newData import display_overview_new
from sections.sleep_newData import display_sleep
from sections.sport_newData import display_sport
from sections.goals_page import display_goals_page

# Set page configuration
st.set_page_config(page_title="HealthyLife February Dashboard", layout="wide")

# Load CSS from styles.css
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sidebar content
with st.sidebar:
    choose = option_menu(
        "Navigation",
        ["Sport", "Sleep", "Overview", "Goals"],
        #["Sport", "Sleep","Overview", "Goals", "Chase The Creators"],
        icons=["house", "activity", "moon", "dash", "dash"],
    )

# Load the data from the Excel file
file_path = "data/Firmen/ipt/2025-02-01/Daily_Scores.xlsx"
# file_path_chase = "data/Daily_Scores_all.xlsx"
file_path_goals="data/Firmen/ipt/2025-02-01/Daily_Motivations.xlsx"

data = pd.read_excel(file_path)
# data_chase = pd.read_excel(file_path_chase)
data_goals = pd.read_excel(file_path_goals)

def test_muchacho_columns_sum_equals_muchachos(df):
    # Filter columns containing "Muchacho"
    muchacho_columns = [col for col in df.columns[:-2] if "Muchacho" in col]

    # Iterate through each row
    for index, row in df.iterrows():
        # Calculate the sum of all "Muchacho" columns for the current row
        muchacho_sum = row[muchacho_columns].sum()

        # Assert that this sum equals the value in the "Muchachos" column
        assert muchacho_sum == row["Final Bosses"], f"Sum mismatch in row {index}: {muchacho_sum} != {row['Muchachos']}"


if choose == "Overview":

    st.markdown(
        """
        <h1 style='text-align: center;'>
            HealthyLife February: Overview
        </h1>
        """,
        unsafe_allow_html=True
    )
    display_overview_new(data)
elif choose == "Sport":
    st.markdown(
        """
        <h1 style='text-align: center;'>
            HealthyLife February: Sport
        </h1>
        """,
        unsafe_allow_html=True
    )
    display_sport(data)
elif choose == "Sleep":
    st.markdown(
        """
        <h1 style='text-align: center;'>
            HealthyLife February: Sleep
        </h1>
        """,
        unsafe_allow_html=True
    )
    display_sleep(data)
elif choose == "Goals":
    st.markdown(
        """
        <h1 style='text-align: center;'>
            Reach your Goals
        </h1>

        """,
        unsafe_allow_html=True
    )
    display_goals_page(data_goals)

# elif choose == "Chase The Creators":
#     st.markdown(
#         """
#         <h1 style='text-align: center;'>
#             Chase the Creators:
#         </h1>
#         <h1 style='text-align: center;'>
#             (Absolute Sport + Absolute Sleep) / 2
#         </h1>
#         """,
#         unsafe_allow_html=True
#     )
#     display_chase_the_creators(data, data_chase)
