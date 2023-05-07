from capitals import states
import random

def play_game():
    print("Greetings! How well do you know the geography of the United States?\nGuess the capitals of each state and test your knowledge!")
    random.shuffle(states)
    correct_answer_score = 0
    incorrect_answer_score = 0
    for state in states:
        capital_guess = input(f"What is the capital of {state['name']}?: ")
        if capital_guess.lower() == state["capital"].lower():
            correct_answer_score += 1
            print(f"Correct: {correct_answer_score} Incorrect: {incorrect_answer_score}")
        else:
            incorrect_answer_score += 1
            print(f"Correct: {correct_answer_score} Incorrect: {incorrect_answer_score}")
    # guess = input(f"What is the capital of {state["name"]}?: ")
# print(states)

play_game()