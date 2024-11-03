import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from sections.overview import display_overview
from sections.overview_newData import display_overview_new
from sections.sport import display_sport

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
file_path = "Daily_Scores.xlsx"

data = pd.read_excel(file_path)

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

# Output the new DataFrame
print(result_df)

if choose == "Overview":

    st.markdown(
        """
        <h1 style='text-align: center;'>
            HealthyLife November: Overview
        </h1>
        """,
        unsafe_allow_html=True
    )
    display_overview_new(result_df)
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
