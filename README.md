## **Scrabble Score Game**

### **Overview**

The **Scrabble Score Game** is a Python-based application that calculates the Scrabble score for words entered by users. The game prompts players to enter words of a specific length (randomly generated), checks if the word is valid according to a predefined dictionary, and then computes the Scrabble score. The game also features a 15-second timer to encourage quick responses, awarding bonus points for faster inputs.

This project follows the principles of **Test-Driven Development (TDD)**, ensuring that all functionality is validated using Python’s **`unittest` framework**.

### **Features**

- Random word length generation (3–10 letters).
- Accurate Scrabble score calculation based on official Scrabble letter values.
- Validates words against a dictionary to ensure correctness.
- 15-second timer for bonus points on faster inputs.
- Game continues for up to 10 rounds or until the player chooses to quit.
- Full test coverage using Python's `unittest`.

### **Requirements**

- Python 3.6 or higher
- `unittest` (comes pre-installed with Python)

### **Setup Instructions**

1. **Clone the Repository**:
   ```bash
     git clone https://github.com/username/scrabble-score-project.git
   cd scrabble-score-project](https://github.com/anjanshrestha622/Scrabble_Score_Game.git)
   ```

2. **Install Python (if not already installed)**:
   - Download and install Python 3 from the official [Python website](https://www.python.org/).

3. **Run the Game**:
   ```bash
   python scrabble_score.py
   ```

4. **Run Unit Tests**:
   To verify that the code is working correctly and all test cases are passing, run:
   ```bash
   python -m unittest test_scrabble_game.py
   ```

### **Game Instructions**

1. Upon starting the game, you will be asked to enter a word that matches a randomly generated word length.
2. You have **15 seconds** to input a word. Entering the word quickly will reward you with bonus points.
3. The game will run for **10 rounds** or until you type `quit` to exit early.
4. At the end of the game, your total score will be displayed.

### **How It Works**

The program calculates the Scrabble score based on the following letter values:

| Letters        | Points  |
|----------------|---------|
| A, E, I, O, U, L, N, R, S, T  | 1  |
| D, G          | 2  |
| B, C, M, P    | 3  |
| F, H, V, W, Y | 4  |
| K             | 5  |
| J, X          | 8  |
| Q, Z          | 10 |
| * (Wildcard)  | 0  |

### **Project Structure**

```
scrabble-score-project/
│
├── scrabble_score.py            # Main game logic
├── test_scrabble_game.py        # Unit tests for the game

README.md                    # Project documentation
```

### **Testing**

This project follows **Test-Driven Development (TDD)**, and all key functionalities are covered by unit tests. The tests validate:
1. **Word scoring**: Ensuring the program calculates Scrabble scores correctly.
2. **Invalid word handling**: Ensuring invalid or special characters are handled appropriately.
3. **Word length selection**: Verifying the random word selection process for different word lengths.

Run the tests using the command:
```bash
python -m unittest test_scrabble_game.py
```

### **Future Improvements**

- Expand the word dictionary to include more words.
- Add a graphical user interface (GUI) for a more interactive user experience.
- Allow users to play against an AI or another player.

### **Contributing**

Contributions are welcome! Feel free to open issues, submit pull requests, or suggest improvements. Please follow the standard Git workflow for contributions.


**Happy Playing!**  
Developed with ❤️ by Anjan shrestha
