import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer


def clean_string(s: str) -> str:
    """
    Cleans string by converting to lowercase, striping whitespace, and removing periods and quotation marks.

    Args:
        s: The string to clean

    Returns:
        str: The cleaned string
    """

    trans = str.maketrans('', '', '."') 
    return s.strip().lower().translate(trans)



misconceptions = pd.read_csv('../eedi-mining-misconceptions-in-mathematics/misconception_mapping.csv')
misconception_list = list(misconceptions['MisconceptionName'])

model = SentenceTransformer('all-MiniLM-L6-v2')
misconception_embeddings = model.encode(misconception_list, convert_to_tensor=True)


# def match_misconception(response: str, subject: str) -> str:
#     """
#     Matches response to a misconception from the misconception list. 
#     If no match is found, returns a string indicating no match.

#     Args:
#         response: The text to match against misconceptions
#         subject: The subject area for context

#     Returns:
#         str: Either the matched misconception or a no-match message
#     """

#     misconception_list_formatted = "\n".join([f"- {item}" for item in misconception_list])
#     prompt = f"""Match the following input to a misconception from the following list. Your answer should be the exact text of the misconception. The subject is included as additional context.
# For example:
# - user: "Believes that the sum of the interior angles of a triangle is 360 degrees. (Subject: geometry)"
# - assistant: "Does not know that angles in a triangle sum to 180 degrees".
# Input: {response} (Subject: {subject})
# List: 
# {misconception_list_formatted}
# """
#     from .api import get_completion
#     response = get_completion(prompt, max_tokens=100)
#     if clean_string(response) in [clean_string(m) for m in misconception_list]:
#         return response
#     else:
#         return f"No match, response: {response}"
    
# TODO test this
def match_misconception(response: str, subject: str) -> str:
    """
    Matches response to a misconception from the misconception list using word embeddings.
    If no match exceeds the similarity threshold, returns a string indicating no match.

    Args:
        response: The text to match against misconceptions
        subject: The subject area for context

    Returns:
        str: Either the matched misconception or a no-match message
    """
    # Combine response with subject for context
    contextual_response = f"{response} (Subject: {subject})"
    
    # Compute embedding for the response
    response_embedding = model.encode([contextual_response], convert_to_tensor=True)
    
    # Calculate cosine similarities between the response and all misconceptions
    similarities = cosine_similarity(response_embedding, misconception_embeddings)[0]
    
    # Identify the best match
    best_idx = similarities.argmax()
    best_score = similarities[best_idx]
    
    # Define a similarity threshold
    threshold = 0.7  # Adjust based on desired sensitivity
    
    if best_score >= threshold:
        return misconception_list[best_idx]
    else:
        return f"No match, response: {response}"