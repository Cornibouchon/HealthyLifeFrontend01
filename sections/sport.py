# sections/sport.py
import streamlit as st
import plotly.express as px


def display_sport(fulldata):
    # Exclude the first two rows
    sportData = fulldata.iloc[2:]

    team_names = fulldata['Team'].tolist()
    total_scores = fulldata["Total Score"].tolist()

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

    # Add content to the second column (Team Muchachos)
    with col2:
        st.markdown(f"<h2 style='text-align: center;'>{team_names[1]}</h2>", unsafe_allow_html=True)  # Centered heading
        st.markdown(f"""
                <div class='total-score'>
                    <h2>Total Score</h2>
                    <h1>{total_scores[1]}</h1>
                </div>
            """, unsafe_allow_html=True)

        # Calculate Total Scores for each team member
    sportData['Total Score'] = sportData.iloc[:, 1:].sum(axis=1)

    # Sort the data by Total Score in descending order
    sorted_data = sportData.sort_values(by='Total Score', ascending=False)

    # Display the sorted team members and their total scores
    st.subheader("Participant ranking ")
    for index, row in sorted_data.iterrows():
        st.write(f"{row['Team']}: {row['Total Score']}")
