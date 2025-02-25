import streamlit as st

from config import TEAM_RESTFUL_GAINZ_COL, TEAM_FINAL_BOSSES_COL, TEAM_RESTFUL_GAINZ_MEMBERS, TEAM_FINAL_BOSSES_MEMBERS


def display_ranking(sorted_scores):
    for i, row in sorted_scores.iterrows():
        # Determine team icon
        team_icon = "🥩" if row['Participant'] in TEAM_RESTFUL_GAINZ_MEMBERS else "💪🏼" if row['Participant'] in TEAM_FINAL_BOSSES_MEMBERS else "⚪"
        
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


def display_Teamscore(filtered_data, team_bonjour_col, team_muchachos_col):
    # Calculate the sum for Bonjour and Muchachos
    total_score_bonjour = filtered_data[TEAM_RESTFUL_GAINZ_COL].sum()
    total_score_muchachos = filtered_data[TEAM_FINAL_BOSSES_COL].sum()
    # Display team names and total scores in two columns
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"<h2 style='text-align: center;'>{team_bonjour_col} 🥩</h2>", unsafe_allow_html=True)
        st.markdown(f"""
                    <div class='total-score'>
                        <h2>Total Score</h2>
                        <h1>{total_score_bonjour:.1f}</h1> 
                    </div>
                """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"<h2 style='text-align: center;'>{team_muchachos_col} 💪🏼</h2>", unsafe_allow_html=True)
        st.markdown(f"""
                    <div class='total-score'>
                        <h2>Total Score</h2>
                        <h1>{total_score_muchachos:.1f}</h1> 
                    </div>
                """, unsafe_allow_html=True)
