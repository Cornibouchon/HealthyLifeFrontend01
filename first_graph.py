import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from sections.overview_newData import display_overview_new
from sections.sleep_newData import display_sleep
from sections.sport_newData import display_sport

# Set page configuration
st.set_page_config(page_title="HealthyLife November Dashboard", layout="wide")

# Load CSS from styles.css
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sidebar content
with st.sidebar:
    choose = option_menu(
        "Navigation",
        ["Overview", "Sport", "Sleep", ],
        icons=["house", "activity", "moon", ],
    )

# Load the data from the Excel file
file_path = "data/Daily_Scores.xlsx"

data = pd.read_excel(file_path)
# Renaming the Total Score names
data = data.rename(columns={'Muchachos': 'Final Bosses', 'Bonjour': 'Muchachos'})


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
            HealthyLife November: Overview
        </h1>
        """,
        unsafe_allow_html=True
    )
    display_overview_new(data)
elif choose == "Sport":
    st.markdown(
        """
        <h1 style='text-align: center;'>
            HealthyLife November: Sport
        </h1>
        """,
        unsafe_allow_html=True
    )
    display_sport(data)
elif choose == "Sleep":
    st.markdown(
        """
        <h1 style='text-align: center;'>
            HealthyLife November: Sleep
        </h1>
        """,
        unsafe_allow_html=True
    )
    display_sleep(data)
