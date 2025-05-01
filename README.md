# Labyrinth

## Game Description

Labyrinth is a game where you play as an adventurer exploring a dungeon filled with dragons. Your goal is to find and defeat the dragons while navigating through a maze of rotating rooms.

## Game Objective

The main objective of the game is to find and defeat all the dragons present in the dungeon. To do this, you must navigate through the maze, using the rotating rooms to create paths and access the dragons.

## How to Play

1. Launch the game by following the installation and execution instructions below.
2. Use the arrow keys to move your adventurer through the maze.
3. Use the spacebar to rotate the rooms and create new paths.
4. Find and defeat all the dragons to win the game.

## Installation and Execution

### Prerequisites

- Python 3.x
- `fltk` library

### Instructions

1. Clone the GitHub repository:
   ```bash
   git clone https://github.com/yacine20005/Labyrinth.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Labyrinth
   ```
3. Run the game:
   ```bash
   python main.py
   ```

## Game Controls and Mechanics

- Use the arrow keys to move your adventurer.
- Press the spacebar to rotate the rooms.
- Rotating rooms can be used to create new paths and access the dragons.

### Detailed Explanation of Game Mechanics

- **Movement**: Use the arrow keys to move your adventurer one tile at a time in the maze.
- **Room Rotation**: Press the spacebar to rotate the room your adventurer is currently in. This can open up new paths or close existing ones.
- **Dragon Encounter**: When you move into a tile with a dragon, you will engage in a battle. The outcome of the battle depends on your adventurer's level and the dragon's level.
- **Leveling Up**: Defeating dragons will increase your adventurer's level, making it easier to defeat stronger dragons.

## Game Structure

The game is composed of several main elements:

- **Main Menu**: Allows you to start a new game or access the options.
- **Options Menu**: Allows you to choose the map and game settings.
- **Game Board**: Represented as a grid with different tiles representing the rooms of the dungeon.
- **Adventurer**: The character controlled by the player, represented by an image on the game board.
- **Dragons**: Enemies to defeat, represented by images on the game board.

## Game Maps

The game includes several maps stored in the `resources/maps` directory. Each map is represented by a text file containing the layout of the rooms and the positions of the dragons.

### Adding a New Map

To add a new map, follow these steps:

1. Create a new text file in the `resources/maps` directory.
2. Define the layout of the rooms using the appropriate characters (see `resources/tiles.txt` for available symbols).
3. Add the positions of the adventurer and dragons at the end of the file, using the following format:
   ```
   A x y
   D x y level
   ```
   Where `x` and `y` are the coordinates of the position, and `level` is the level of the dragon.
