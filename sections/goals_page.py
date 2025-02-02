import streamlit as st
import calendar
import pandas as pd


def display_goals_page(data_goals):
    # Convert date column to datetime
    data_goals['Date'] = pd.to_datetime(data_goals['Date'], format="mixed")
    # Get participants (column names starting from the 3rd column)
    participants = data_goals.columns[2:]

    # Dropdown for participant selection
    participant = st.selectbox("Choose a participant:", participants)

    # Generate February calendar for 2025
    year = 2025
    month = 2
    february_days = calendar.Calendar(firstweekday=0).monthdayscalendar(year, month)  # Week starts on Monday

    # Weekday names
    weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    def get_day_color(date, goal_type, participant):
        """Determine the background color for a given date and goal type for the selected participant."""
        # Filter rows for the given date and goal type
        entry = data_goals[(data_goals['Date'] == date) & (data_goals['Motivation_typ'] == goal_type)]
        if entry.empty:
            return "#f9f9f9"  # Neutral color for missing entries
        value = entry[participant].iloc[0]  # Get the value for the selected participant
        return "#d6c420" if not value and goal_type == "activity" else "#4CAF50" if value else "#9e1818"

        
    def render_calendar(title, goal_type):
        """Render a calendar with color-coded days."""
        # Display title
        st.markdown(
            f"<h2 style='text-align: center; margin-bottom: 20px;'>{title}</h2>",
            unsafe_allow_html=True,
        )
        # Display weekday headers
        cols = st.columns(7)
        for i, weekday in enumerate(weekdays):
            cols[i].markdown(
                f"<div style='text-align: center; font-weight: bold; font-size: 16px; color: #2d572c;'>{weekday}</div>",
                unsafe_allow_html=True,
            )

        # Display days of the month
        for week in february_days:
            cols = st.columns(7, gap="small")
            for i, day in enumerate(week):
                if day == 0:
                    # Empty day slots for padding in the calendar
                    cols[i].markdown("<div style='text-align: center;'> </div>", unsafe_allow_html=True)
                else:
                    date = pd.Timestamp(year, month, day)  # Create a timestamp for the current day
                    color = get_day_color(date, goal_type, participant)  # Determine the day's background color
                    cols[i].markdown(
                        f"""
                        <div style="text-align: center; 
                                    padding: 8px; 
                                    border-radius: 8px; 
                                    background-color: {color};
                                    margin: 2px 0;  /* Reduce vertical margin */
                                    font-size: 14px;">
                            {day}
                        </div>
                        """, unsafe_allow_html=True
                    )

    # Render the page with two side-by-side calendars with added gap
    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        render_calendar("Sport", "activity")

    with col2:
        render_calendar("Sleep", "sleep")


