import streamlit as st


def display_ranking(sorted_scores):
    for i, row in sorted_scores.iterrows():
        # Determine CSS class for top 3
        rank_class = f"top-{i + 1}" if i < 3 else ""

        # HTML for each participant row with dynamic styling for the top 3
        st.markdown(f"""
            <div class="participant-ranking {rank_class}">
                <div class="participant-name">{row['Participant']}</div>
                <div class="participant-score">{row['Total Score']:.1f}</div>
            </div>
        """, unsafe_allow_html=True)
