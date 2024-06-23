import random

def typoglycemia(text):
    """
    Process the input text into its typoglycemic form by scrambling the middle letters of each word.
    Words shorter than four letters are left unchanged.

    Parameters:
    text (str): The sentence provided by the user to be scrambled.

    Returns:
    str: The typoglycemic version of the input sentence.
    """
    def scramble(word):
        """
        Scramble the middle letters of a word while keeping the first and last letter intact.
        Words with three letters or fewer are returned unchanged.

        Parameters:
        word (str): A single word to potentially scramble.

        Returns:
        str: The scrambled word, if applicable.
        """
        if len(word) > 3:  # Only scramble if word length is greater than 3
            middle = list(word[1:-1])
            random.shuffle(middle)
            return word[0] + ''.join(middle) + word[-1]
        return word
    
    return ' '.join(scramble(word) for word in text.split())

def main():
    """
    Main function to get user input and display the typoglycemic version of the input text.
    """
    user_input = input('Enter a sentence to typoglycemize: ')
    scrambled_sentence = typoglycemia(user_input)
    print("Typoglycemic output:", scrambled_sentence)

if __name__ == "__main__":
    main()