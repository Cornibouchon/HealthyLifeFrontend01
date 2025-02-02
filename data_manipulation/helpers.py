import numpy as np


def calculate_personality_score(data, score_name, offset):
    # Convert input to a NumPy array if it's not already
    if not isinstance(data, np.ndarray):
        data = np.array(data)

    # Ensure that the input has at least 18 elements
    if len(data) < 18:
        raise ValueError("Input data must contain at least 18 entries.")

    # Calculate the score based on the specified offset
    score = (
            int(data[offset]) +
            int(data[offset + 4]) +
            int(data[offset + 8]) +
            int(data[offset + 12])
    )
    return score
