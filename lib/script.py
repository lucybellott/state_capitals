from capitals import states
import random

def play_game():
    print("Greetings! How well do you know the geography of the United States?\nGuess the capitals of each state and test your knowledge!")
    random.shuffle(states)
    correct_answer_score = 0
    incorrect_answer_score = 0
    for state in states:
        capital_guess = input(f"What is the capital of {state['name']}?: ")
        # allows for more flexibility in the answers
        formatted_guess = capital_guess.lower().replace(".", "")
        formatted_answer = state['capital'].lower().replace(".", "")
        if formatted_guess == formatted_answer:
            correct_answer_score += 1
            print(f"Correct: {correct_answer_score} Incorrect: {incorrect_answer_score}")
        else:
            incorrect_answer_score += 1
            print(f"Incorrect. The capital of {state['name']} is actually {state['capital']}.\nCorrect: {correct_answer_score} Incorrect: {incorrect_answer_score}")
    print(f"Your final score is {correct_answer_score}!")
    play_again = input("Would you like to play again? (y or n)?: ")
    if play_again == "y":
        play_game()
    else:
        print("Thanks for playing! Come back soon!")


play_game()