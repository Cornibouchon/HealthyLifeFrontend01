# sections/overview.py
import streamlit as st
import plotly.express as px


def display_overview(data):
    # Get team names
    team_names = data['Team'].tolist()
    total_scores = data["Total Score"].tolist()

    # Create separate long-format DataFrames for each team
    data_bonjour = data[data['Team'] == "Bonjour"].melt(id_vars=["Team"], var_name="Date", value_name="Score")
    data_muchachos = data[data['Team'] == "Muchachos"].melt(id_vars=["Team"], var_name="Date", value_name="Score")

    # Plotly Bar Chart for Team Bonjour
    fig_bonjour = px.bar(data_bonjour, x="Date", y="Score", title=f"Daily Scores Team {team_names[0]}",
                         labels={"Score": "Points", "Date": "Date"})
    fig_bonjour.update_layout(title_x=0.35)

    # Plotly Bar Chart for Team Muchachos
    fig_muchachos = px.bar(data_muchachos, x="Date", y="Score", title=f"Daily Scores Team  {team_names[1]}",
                           labels={"Score": "Points", "Date": "Date"})
    fig_muchachos.update_layout(title_x=0.4)

    # Set the y-axis range for both figures
    for fig in [fig_bonjour, fig_muchachos]:
        fig.update_yaxes(range=[0, 10])  # Set y-axis range from 0 to 10

    # Create two columns for Team Bonjour and Team Muchachos
    col1, col2 = st.columns(2)

    # Add content to the first column (Team Bonjour)
    with col1:
        st.markdown(f"<h2 style='text-align: center;'>{team_names[0]}</h2>", unsafe_allow_html=True)  # Centered heading
        st.markdown(f"""
            <div class='total-score'>
                <h2>Total Score</h2>
                <h1>{total_scores[0]}</h1>
            </div>
        """, unsafe_allow_html=True)
        st.plotly_chart(fig_bonjour, use_container_width=True)  # Plot for Team Bonjour

    # Add content to the second column (Team Muchachos)
    with col2:
        st.markdown(f"<h2 style='text-align: center;'>{team_names[1]}</h2>", unsafe_allow_html=True)  # Centered heading
        st.markdown(f"""
            <div class='total-score'>
                <h2>Total Score</h2>
                <h1>{total_scores[1]}</h1>
            </div>
        """, unsafe_allow_html=True)
        st.plotly_chart(fig_muchachos, use_container_width=True)  # Plot for Team Muchachos
