# sections/overview_newData.py
import streamlit as st
import plotly.express as px
import pandas as pd


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


def display_overview_new(data):
    # Set the column names for the new DataFrame
    team_bonjour_col = 'Bonjour'
    team_muchachos_col = 'Muchachos'

    # Calculate scores
    results_data = calculate_total_team_scores(data)

    # Create a long-format DataFrame for plotting
    data_long = results_data.melt(id_vars=['Date'], value_vars=[team_bonjour_col, team_muchachos_col],
                                  var_name='Team', value_name='Score')

    # Plotly Bar Chart for Team Bonjour
    fig_bonjour = px.bar(data_long[data_long['Team'] == team_bonjour_col], x='Date', y='Score', barmode='group',
                         title="Daily Scores",
                         labels={"Score": "Points", "Date": "Date"})
    fig_bonjour.update_layout(title_x=0.5)
    fig_bonjour.update_yaxes(range=[0, 200])
    fig_bonjour.update_xaxes(tickformat="%Y-%m-%d", tickvals=data_long['Date'].unique())

    # Plotly Bar Chart for Team Muchachos
    fig_muchachos = px.bar(data_long[data_long['Team'] == team_muchachos_col], x='Date', y='Score', barmode='group',
                           title="Daily Scores",
                           labels={"Score": "Points", "Date": "Date"})
    fig_muchachos.update_layout(title_x=0.5)
    fig_muchachos.update_yaxes(range=[0, 200])
    fig_muchachos.update_xaxes(tickformat="%Y-%m-%d", tickvals=data_long['Date'].unique())

    # Create two columns for Team Bonjour and Team Muchachos
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"<h2 style='text-align: center;'>{team_bonjour_col}</h2>",
                    unsafe_allow_html=True)  # Centered heading
        total_bonjour = results_data[team_bonjour_col].sum()  # Use the rounded scores
        st.markdown(f"""
            <div class='total-score' style="text-align: center;">
                <h2>Team Score</h2>
                <h1>{total_bonjour}</h1>
            </div>
        """, unsafe_allow_html=True)
        st.plotly_chart(fig_bonjour, use_container_width=True, key='fig_bonjour')  # Plot for Team Bonjour

    with col2:
        st.markdown(f"<h2 style='text-align: center;'>{team_muchachos_col}</h2>",
                    unsafe_allow_html=True)  # Centered heading
        total_muchachos = results_data[team_muchachos_col].sum()  # Use the rounded scores
        st.markdown(f"""
            <div class='total-score' style="text-align: center;">
                <h2>Team Score</h2>
                <h1>{total_muchachos}</h1>
            </div>
        """, unsafe_allow_html=True)
        st.plotly_chart(fig_muchachos, use_container_width=True, key='fig_muchachos')  # Plot for Team Muchachos
