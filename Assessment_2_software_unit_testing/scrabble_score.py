import time
import random

# Scrabble letter values with wildcard (wildcard scores 0 points)
letter_values = {
    'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1,
    'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
    'D': 2, 'G': 2,
    'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'K': 5,
    'J': 8, 'X': 8,
    'Q': 10, 'Z': 10,
    '*': 0  # Wildcard can be used for any letter, but gives 0 points
}

# Word lists for dictionary validation (example dictionary)
dictionary = [
    "cat", "dog", "ball", "bat", "rat", "apple", "zebra", "mouse", "plane",
    "dance", "pneumonia", "quiz", "xylophone", "rhythms", "jazz", "kite",
    "jump", "dogma", "balloon", "robot", "cabbage", "letter", "skipping"
]


def is_valid_word(word):
    """
    Checks if the given word is valid (exists in the dictionary).
    """
    return word.lower() in dictionary


def compute_score(word):
    """
    Calculate the Scrabble score for a given word based on letter values.
    :param word: str, the input word to calculate score for.
    :return: int, the score for the word.
    """
    score = 0
    word = word.upper()  # Convert word to uppercase for case insensitivity
    for letter in word:
        if letter in letter_values:
            score += letter_values[letter]
    return score


def choose_random_word_of_length(word_length):
    """
    Select a random word of a given length from the dictionary.
    :param word_length: int, the required length of the word.
    :return: str, the selected random word of the given length.
    """
    valid_words = [word for word in dictionary if len(word) == word_length]
    if valid_words:
        return random.choice(valid_words)
    return None


def play_scrabble_game():
    """
    Main function to play the Scrabble game. Player is prompted
    to enter words of a randomly generated length, and scores
    are calculated based on correctness and time taken.
    Game continues until player quits or after 10 rounds.
    """
    total_score = 0
    round_number = 0
    max_rounds = 10

    print("Welcome to the Scrabble Challenge!")
    print("Random words will be selected in each round based on a randomly "
          "generated length.")
    print("You can type 'quit' at any time to end the game early.\n")

    while round_number < max_rounds:
        round_number += 1
        print(f"\n--- Round {round_number} ---")

        # Randomly generate a required word length between 3 and 10
        required_length = random.randint(3, 10)
        print(f"Enter a word with exactly {required_length} letters.")

        # Get a random word of the specified length
        word = choose_random_word_of_length(required_length)
        if not word:
            print(f"No words available with {required_length} letters. "
                  "Skipping round.")
            round_number -= 1  # Don't count this round if no word is available
            continue

        print(f"A valid word must have {required_length} letters.")

        # 15-second timer
        start_time = time.time()

        # Get the player's input (word guess)
        while True:
            guess = input(
                f"Enter a word with {required_length} letters or type 'quit' "
                "to exit: "
            ).strip().lower()

            if guess == 'quit':
                print("You chose to quit.")
                break

            # Check if the word contains only alphabets and matches the length
            if not guess.isalpha():
                print("Invalid input! Please enter only alphabets.")
                continue
            if len(guess) != required_length:
                print(f"Invalid input! Please enter a word with exactly "
                      f"{required_length} letters.")
                continue
            if not is_valid_word(guess):
                print(f"Invalid word! '{guess}' is not a valid word in the "
                      "dictionary.")
                continue

            break

        # If player quits, stop the game
        if guess == 'quit':
            break

        # Record the end time and calculate the time taken
        end_time = time.time()
        time_taken = end_time - start_time
        print(f"Time taken: {time_taken:.2f} seconds")

        # Check if the guess is correct and calculate the score
        score = compute_score(guess)
        time_bonus = max(0, 15 - int(time_taken))
        # Time bonus: max of 15 points if entered quickly
        total_score += score + time_bonus
        print(f"Correct! Your score for this round: {score} + {time_bonus} "
              f"(time bonus) = {score + time_bonus}")

    # Display the final total score after the game ends
    print(f"\nGame Over! Your total score after {round_number} rounds: "
          f"{total_score}")
    print("Thanks for playing! Goodbye!")


# Run the Scrabble game if the script is executed directly
if __name__ == "__main__":
    play_scrabble_game()
