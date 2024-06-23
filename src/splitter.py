import re

def split_sentences(text):
    """
    Splits the given text into sentences based on punctuation marks followed by spaces or the end of the string.

    Args:
        text (str): A string containing the text to be split into sentences.

    Returns:
        list: A list of sentences extracted from the text.
    """
    
    # Regular expression pattern to split the text where a period is followed by space(s) or it is the end of the string.
    # This will capture scenarios where sentences end with a period followed by whitespace or directly at the end of the text.
    sentences = re.split(r'\.\s+|\.$', text)
    return sentences

# Example document string
document = "Hello world. This is a test document. It contains several sentences."

# Call the function to split the document into sentences
sentences = split_sentences(document)

# Print the list of sentences
print(sentences)
