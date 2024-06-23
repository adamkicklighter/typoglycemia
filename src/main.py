from fetcher import fetch_article
from splitter import split_sentences
from scrambler import typoglycemia  # Import the typoglycemia function to scramble sentences
import random

def main():
    """
    Main execution function that fetches a random Wikipedia article, extracts sentences,
    randomly selects one sentence, and scrambles it using the typoglycemia method from scrambler.py.
    """
    article = fetch_article()
    if article:
        print(f"Title: {article['title']}\n")
        punkt_path = './assets/punkt tokenizers/punkt'
        sentences = split_sentences(article['content'], punkt_path)

        if sentences:
            selected_sentence = random.choice(sentences)  # Randomly select one sentence
            scrambled_sentence = typoglycemia(selected_sentence)  # Scramble the selected sentence
            print("Selected Sentence:", selected_sentence)
            print("Scrambled Sentence:", scrambled_sentence)
        else:
            print("No sentences extracted.")
    else:
        print("Failed to fetch a random Wikipedia article")

if __name__ == '__main__':
    main()