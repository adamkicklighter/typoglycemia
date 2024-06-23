def get_user_input(prompt):
    """
    Prompts the user for input and returns the user's response.
    """
    return input(prompt)

def validate_input(user_input, correct_answer):
    """
    Compares the user input to the correct answer and returns whether they match.
    """
    return user_input.strip() == correct_answer