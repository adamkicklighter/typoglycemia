import nltk
from nltk.tokenize import sent_tokenize

def split_sentences(text, punkt_path):
    """
    Splits the given text into sentences using the nltk library and a pre-downloaded punkt tokenizer model.
    
    Args:
        text (str): A string containing the text to be split into sentences.
        punkt_path (str): The path to the directory containing the punkt files.
        
    Returns:
        list: A list of sentences extracted from the text.
    """
    
    # Set the tokenizer to the provided punkt path
    nltk.data.path.append(punkt_path)
    
    # Tokenize the text into sentences using nltk's sent_tokenize
    sentences = sent_tokenize(text)
    return sentences

# Example document string
document = "Hello world. I am Dr. Spock. This is a test document! It contains several sentences."

# Specify the path to the punkt tokenizer files
punkt_path = './assets/punkt tokenizers/punkt' # Run a terminal command to install the punkt files to a local direcotry path

# Call the function to split the document into sentences
sentences = split_sentences(document, punkt_path)

# Print the list of sentences
print(sentences)