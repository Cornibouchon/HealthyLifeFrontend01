import streamlit as st

from config import TEAM_2md23_COL, TEAM_Arbs_COL, TEAM_2md23, TEAM_Arbs, TEAM_2md23, TEAM_Arbs, TEAM_MinhKhaZen


def display_ranking(sorted_scores):
    for i, row in sorted_scores.iterrows():
        # Determine team icon based on ranking
        if i == 0:
            team_icon = "🥇"  # Gold trophy
        elif i == 1:
            team_icon = "🥈"  # Silver trophy
        elif i == 2:
            team_icon = "🥉"  # Bronze trophy
        else:
            team_icon = "🏆"  # Default trophy for others

        # Determine CSS class for top 3
        rank_class = f"top-{i + 1}" if i < 3 else ""

        # HTML for each participant row with team icon
        st.markdown(f"""
            <div class="participant-ranking {rank_class}">
                <div class="participant-name">{team_icon} {row['Participant']}</div>
                <div class="participant-score">{row['Total Score']:.1f}</div>
            </div>
        """, unsafe_allow_html=True)


def display_ranking_chase(sorted_scores, Score1, Score2):
    for i, row in sorted_scores.iterrows():
        # Determine CSS class for top 3 or if the score is higher or equal to Score1 or Score2
        rank_class = f"top-1" if row['Total Score'] >= Score1 and row['Total Score'] >= Score2 else ""

        # HTML for each participant row with dynamic styling
        st.markdown(f"""
            <div class="participant-ranking {rank_class}">
                <div class="participant-name">{row['Participant']}</div>
                <div class="participant-score">{row['Total Score']:.1f}</div>
            </div>
        """, unsafe_allow_html=True)


def display_Teamscore(filtered_data, team01_col, team02_col, team03_col):
    # Calculate the sum for Bonjour, Muchachos and the third team
    total_score_team01 = filtered_data[TEAM_2md23_COL].sum()
    total_score_team02 = filtered_data[TEAM_Arbs_COL].sum()
    total_score_team03 = filtered_data["Minh-Kha-Zen"].sum()
    # Display team names and total scores in three columns
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"<h2 style='text-align: center;'>{team01_col}</h2>", unsafe_allow_html=True)
        st.markdown(f"""
                    <div class='total-score'>
                        <h2>Total Score</h2>
                        <h1>{total_score_team01:.1f}</h1> 
                    </div>
                """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"<h2 style='text-align: center;'>{team02_col}</h2>", unsafe_allow_html=True)
        st.markdown(f"""
                    <div class='total-score'>
                        <h2>Total Score</h2>
                        <h1>{total_score_team02:.1f}</h1> 
                    </div>
                """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"<h2 style='text-align: center;'>{team03_col}</h2>", unsafe_allow_html=True)
        st.markdown(f"""
                    <div class='total-score'>
                        <h2>Total Score</h2>
                        <h1>{total_score_team03:.1f}</h1> 
                    </div>
                """, unsafe_allow_html=True)
