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
