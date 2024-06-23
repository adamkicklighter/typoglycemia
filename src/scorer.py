from difflib import SequenceMatcher

def score_guess(original, guess):
    """
    Scores the user's guess against the original sentence.
    
    The score is calculated based on the similarity of sequences,
    considering the order of words. It uses the SequenceMatcher from
    difflib, which compares two sequences of words and computes a
    similarity ratio.
    
    Parameters:
        original (str): The original unscrambled sentence.
        guess (str): The user's guess of the unscrambled sentence.
    
    Returns:
        float: The similarity score as a percentage, where 100% is a perfect match.
    """
    # Tokenize the sentences to lists of words
    original_words = original.split()
    guess_words = guess.split()
    
    # Create a SequenceMatcher to compare the two lists of words
    matcher = SequenceMatcher(None, original_words, guess_words)
    
    # Calculate the similarity ratio and convert to percentage
    similarity_ratio = matcher.ratio() * 100
    
    return similarity_ratio
