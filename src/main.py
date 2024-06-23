from fetcher import fetch_article
from splitter import split_sentences
from scrambler import typoglycemia
from prompter import get_user_input, validate_input
from scorer import score_guess
from controller import handle_game_control
import random

def play_round():
    """
    Plays a round of the Wikipedia sentence scrambler game.

    Fetches a random Wikipedia article, selects a sentence, scrambles it, and prompts the user to guess the original sentence. The user's guess is then scored based on accuracy, and feedback is provided.

    Steps:
    1. Fetch an article using `fetch_article`.
    2. Split the article into sentences using `split_sentences`.
    3. Randomly select one sentence and scramble it.
    4. Display the scrambled sentence and prompt the user for a guess.
    5. Score the user's guess against the original sentence using `score_guess`.
    6. Provide feedback based on the score.
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

            guess = get_user_input("Guess the unscrambled sentence: ")
            score = score_guess(selected_sentence, guess)
            print(f"Your score: {score:.2f}%")

            if score > 95:
                print("Correct! Well done.")
            else:
                print(f"Incorrect. The correct sentence was: {selected_sentence}")
        else:
            print("No sentences extracted.")
    else:
        print("Failed to fetch a random Wikipedia article")

if __name__ == '__main__':
    while True:
        print("Type 'stop' to quit or press enter to play:")
        user_input = get_user_input("")

        if user_input.lower() == 'stop':
            break
        else:
            play_round()
