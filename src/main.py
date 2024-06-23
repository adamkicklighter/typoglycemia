from fetcher import fetch_article
from splitter import split_sentences
from scrambler import typoglycemia
from prompter import get_user_input, validate_input
from scorer import score_guess
import random

def main():
    """
    Execute the main function of the Wikipedia sentence scrambler game.
    
    Steps:
    1. Fetch a random Wikipedia article using `fetch_article`.
    2. Extract sentences from the article content using `split_sentences`.
    3. Select one random sentence and scramble it using `typoglycemia`.
    4. Display the scrambled sentence and prompt the user to guess its unscrambled form.
    5. Score the user's guess against the original sentence and provide feedback.
    
    Outputs feedback based on the accuracy of the user's guess and handles cases where no valid article or sentences are found.
    """
    article = fetch_article()
    if article:
        print(f"Title: {article['title']}\n")
        punkt_path = './assets/punkt tokenizers/punkt'
        sentences = split_sentences(article['content'], punkt_path)

        if sentences:
            selected_sentence = random.choice(sentences)
            scrambled_sentence = typoglycemia(selected_sentence)
            print("Scrambled Sentence:", scrambled_sentence)

            user_input = get_user_input("Guess the unscrambled sentence: ")
            score = score_guess(selected_sentence, user_input)
            print(f"Your score: {score:.2f}%")

            if score > 90:  # You can adjust this threshold
                print("Correct! Well done.")
            else:
                print(f"Incorrect. The correct sentence was: {selected_sentence}")
        else:
            print("No sentences extracted.")
    else:
        print("Failed to fetch a random Wikipedia article")

if __name__ == '__main__':
    main()
