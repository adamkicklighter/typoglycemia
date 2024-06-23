import nltk
from nltk.tokenize import sent_tokenize

def split_sentences(text, punkt_path):
    """
    Splits the provided text into sentences using the nltk library and a pre-downloaded
    punkt tokenizer model.

    Args:
        text (str): The text to be split into sentences.
        punkt_path (str): The path to the directory containing the punkt tokenizer files.

    Returns:
        list: A list of sentences extracted from the text.
    """
    nltk.data.path.append(punkt_path)
    sentences = sent_tokenize(text)
    return sentences
