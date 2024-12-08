# Zero Kata (Tic Tac Toe) 🎮

**Zero Kata** is a Python-based implementation of the classic Tic Tac Toe game with a challenging twist! The computer utilizes an advanced **minimax algorithm** to ensure optimal play, making it tough for players to outsmart it.

---

## 🎯 Features
- **Single Player Mode**: Play against the computer with an advanced AI.
- **Minimax Algorithm**: The AI calculates the best possible move to maximize its winning chances.
- **Interactive Gameplay**: Player-friendly interface with ASCII art.
- **Replay Option**: Play multiple games without restarting the program.
- **Draw Handling**: The game handles tied scenarios gracefully.

---

## 🚀 How to Run the Project

### Prerequisites
- Python 3.6 or later installed on your system.

### Steps to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/aditya-kr86/zero-kata-tic-tac-toe.git
   ```
2. Navigate to the project directory:
   ```bash
   cd zero-kata-tic-tac-toe
   ```
3. Run the script:
   ```bash
   python zero_kata_pro.py
   ```

---

## 🎮 Gameplay Instructions
1. The game starts with the player (O) going first.
2. Input the number corresponding to the position where you want to place your mark (O):
   ```
    1 | 2 | 3
   ---|---|---
    4 | 5 | 6
   ---|---|---
    7 | 8 | 9
   ```
3. The computer (X) will make its move based on the minimax algorithm.
4. The game continues until:
   - A player wins (O or X), or
   - The board is full (draw).
5. After the game ends, you can choose to replay or exit.

---

## 💡 Minimax Algorithm
The **minimax algorithm** used in this project ensures that the computer:
1. Always plays optimally to win or prevent a loss.
2. Simulates all possible moves and selects the best outcome for itself.
3. Makes Zero Kata highly challenging for players!

---

## 📂 Project Structure
```
zero-kata-tic-tac-toe/
├── zero_kata.py     # Main game script
├── README.md        # Project documentation
└── LICENSE          # License file (optional)
```

---

## 🎨 ASCII Art Preview
Here’s how the board looks during gameplay:
```
 X | O | 3
---|---|---
 4 | 5 | X
---|---|---
 O | 8 | 9
```

---

## 🤝 Contribution Guidelines
Want to enhance Zero Kata? Contributions are welcome! Here's how you can help:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature description"
   ```
4. Push the changes to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## 📜 License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

---

## 🧑‍💻 Author
- **Aditya Kumar**  
  - [GitHub](https://github.com/aditya-kr86)  
  - [Email](mailto:adityakumargupta082003@gmail.com)  

---

## 🌟 Acknowledgments
- **ASCII Art**: Enhances the user experience with a visual representation of the board.
- **Minimax Algorithm**: Makes the AI unbeatable for most players.
- Inspired by the timeless game of Tic Tac Toe.
