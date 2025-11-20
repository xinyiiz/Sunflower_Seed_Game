# 🌾 Sundrop Farm – Python Farming Simulation Game  
**PRG1 Assignment** 
**Author:** Tan Xin Yi (S10267655E)

Sundrop Farm is a strategy-based farming simulation game built entirely in Python.  
The goal: survive 20 in-game days, manage your energy, grow crops, harvest efficiently, and earn at least **$100** to pay off your farm loan.

This project demonstrates fundamental programming skills including **functions**, **data validation**, **grid-based movement**, **game state management**, **file handling**, and **modular problem solving**.

---

## 🎮 Game Concept

You begin with:

- **$20**
- **10 energy per day**
- **a 5×5 piece of land**
- **a debt of $100 to repay in 20 days**

Each day, you can buy seeds, walk around your farm, plant crops, harvest, and manage your resources.  
Every action (moving, planting, harvesting) consumes **1 energy**, so planning is essential.

If you reach **Day 21** with **$100 or more**, you win.

---

## 🧱 Features Implemented

### ✔️ 1. Main Menu System (Start / Load / Exit)  
A navigation system that lets players:

- Start a new game  
- Load from a save file  
- Quit the application  

(Designed according to the structure in the assignment brief, page 3.) :contentReference[oaicite:1]{index=1}

---

### ✔️ 2. Game Loop & Day Progression  
- Time advances one day at a time  
- Energy resets to 10 each morning  
- Crops mature automatically as days pass  
- Game ends after Day 20  

Maturation logic follows assignment rules (page 11). :contentReference[oaicite:2]{index=2}

---

### ✔️ 3. Albatross Town Navigation  
From the town menu, players can:

- 🔹 Visit the Seed Shop  
- 🔹 Visit the Farm  
- 🔹 End the Day  
- 🔹 Save Game  
- 🔹 Exit  

(Menu structure from page 3.) :contentReference[oaicite:3]{index=3}

---

### ✔️ 4. Pierce’s Seed Shop  
Implements:

| Seed        | Price | Days to Grow | Crop Price |
|-------------|--------|----------------|--------------|
| Lettuce (LET) | $2     | 2 days         | $3           |
| Potato (POT)  | $3     | 3 days         | $6           |
| Cauliflower (CAU) | $5 | 6 days         | $14          |

Players can:

- Buy seeds  
- See updated money  
- Receive validation if they can’t afford purchase  

(Follows diagrams on page 4–5.) :contentReference[oaicite:4]{index=4}

---

### ✔️ 5. 5×5 Farm Grid  
The farm map displays:

- A 5×5 grid  
- Player position marked with `X`  
- House at center `HSE`  
- Planted crops displayed with days left to grow  

Movement supports `W`, `A`, `S`, `D` (case-insensitive).  
Prevents the player from walking off the grid.

(Farm grid and movement rules: page 6.) :contentReference[oaicite:5]{index=5}

---

### ✔️ 6. Planting Crops  
When on an empty square:

- Player may plant seeds they own  
- Days-to-mature counter is displayed on the tile  
- Planting consumes 1 energy  

(Planting menu and rules: page 7.) :contentReference[oaicite:6]{index=6}

---

### ✔️ 7. Harvesting Crops  
A crop that has **0 days left** can be harvested:

- Adds money based on crop’s sell price  
- Tile resets to empty  
- Consumes 1 energy  

(Harvest example shown on page 8.) :contentReference[oaicite:7]{index=7}

---

### ✔️ 8. Save & Load System  
Implemented according to assignment requirements (page 11–12):

- Saves all game attributes:  
  - Day  
  - Energy  
  - Money  
  - Seed inventory  
  - Farm grid (crops + remaining grow time)  
  - Player’s position  
- Loading restores the game state exactly  

---

## 🧪 Additional Logic & Validation

- Invalid input handling for every menu  
- Boundaries for farm movement  
- Checks for empty inventory when planting  
- Preventing actions when energy is 0 (page 10–11) :contentReference[oaicite:8]{index=8}  
- Correct formatting of statistics box  
- All work organized into functions to meet assignment rubric (page 13–14) :contentReference[oaicite:9]{index=9}  

---

## 📂 Project Structure

SundropFarm/
│── S10267655E_Assignment.py # Main game file
│── savegame.txt # Auto-generated when saving
│── README.md # Project documentation


---

## 🛠️ Technologies Used

- Python (Functions, loops, conditionals, validation)
- File I/O (Reading & writing save files)
- Nested lists for grid management
- Procedural programming following PRG1 standards

---

## 🧑‍🏫 Learning Outcomes

Through this project, I demonstrated:

- Designing a complete program from a detailed problem statement  
- Managing complex game logic using functions  
- Effective use of loops, conditionals, and nested data structures  
- Building a save/load feature with file handling  
- Ensuring program reliability with tight validation  
- Applying modular programming and clean code practices  

---

## 🎯 Conclusion

This project reflects my ability to design and build a full working application based on formal requirements.  
It showcases skills in **programming logic**, **problem solving**, and **game system design**—all core to my growth as a developer.

