# sections/overview.py
import streamlit as st
import plotly.express as px


def display_overview_new(data):
    # Set the column names for the new DataFrame
    team_bonjour_col = 'Bonjour'
    team_muchachos_col = 'Muchachos'

    # Create a long-format DataFrame for plotting
    data_long = data.melt(id_vars=['Date'], value_vars=[team_bonjour_col, team_muchachos_col],
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

    # Add content to the first column (Team Bonjour)
    with col1:
        st.markdown(f"<h2 style='text-align: center;'>{team_bonjour_col}</h2>",
                    unsafe_allow_html=True)  # Centered heading
        total_bonjour = data[team_bonjour_col].sum()  # Total score for Bonjour
        st.markdown(f"""
            <div class='total-score' style="text-align: center;">
                <h2>Team Score</h2>
                <h1>{total_bonjour}</h1>
            </div>
        """, unsafe_allow_html=True)
        st.plotly_chart(fig_bonjour, use_container_width=True, key='fig_bonjour')  # Plot for Team Bonjour

    # Add content to the second column (Team Muchachos)
    with col2:
        st.markdown(f"<h2 style='text-align: center;'>{team_muchachos_col}</h2>",
                    unsafe_allow_html=True)  # Centered heading
        total_muchachos = data[team_muchachos_col].sum()  # Total score for Muchachos
        st.markdown(f"""
            <div class='total-score' style="text-align: center;">
                <h2>Team Score</h2>
                <h1>{total_muchachos}</h1>
            </div>
        """, unsafe_allow_html=True)
        st.plotly_chart(fig_muchachos, use_container_width=True, key='fig_muchachos')  # Plot for Team Muchachos

# Usage: Call this function with your new DataFrame
# display_overview_new(result_df)
