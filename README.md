# Hardware Group Snake Game Project

A classic Snake game built for the Raspberry Pi Sense HAT using the 8×8 LED matrix and the joystick.

---

## Requirements

### Hardware
- Raspberry Pi (any model that supports Sense HAT well; Pi 3/4/5 are common)
- Sense HAT
- MicroSD card + power supply
- Optional: case/spacers to prevent shorts

### Software
- Python 3
- Raspberry Pi OS
- Mu Editor

---

## How the Game Works (High-Level)

The game is basically a repeated cycle:

- Read input (joystick)
- Update state (move snake, grow if food eaten)
- Check rules (collision / game over)
- Render output (draw pixels on LED matrix)
- Wait a short time so it’s playable

This is the same core structure used in lots of systems: robotics, dashboards, controllers, and real games.

## Lesson Pieces

### Lesson 1 — The LED Grid as Coordinates

Concepts: 2D coordinates, mapping, constraints

- The LED matrix is 8×8
- Valid coordinates are x=0..7, y=0..7
- Drawing is just: set_pixel(x, y, (r,g,b))

Mini-task: light up corners, draw a diagonal line.

Real-world tie: coordinate grids show up in:

- robotics localization
- camera pixels / image processing
- CNC/3D printer toolpaths
- UI layout and game design

### Lesson 2 — Game State (Data Structures)

Concepts: lists/tuples, state representation

Snake is stored as a list of (x, y) positions:
- Head at index 0
- Tail at the end

Example:

```python
snake = [(4,4), (3,4), (2,4)]
```

Mini-task: print snake positions, move it one step.

Real-world tie: state modeling is used in:

- tracking inventory across warehouses
- GPS breadcrumb trails
- modeling a robot arm’s joint positions
- representing network nodes in a route

### Lesson 3 — Input as Events (Joystick)

Concepts: event handling, debouncing, valid transitions
Joystick produces events (pressed/released/held).
You only want to react to the pressed event and ignore invalid reversals.

Mini-task: display joystick direction as text.

Real-world tie: event-driven systems are everywhere:

- keyboards/mice/touch screens
- button panels on machines
- industrial safety switches
- web apps (clicks, taps, notifications)

### Lesson 4 — The Update Loop (The “Engine”)

Concepts: loops, timing, “tick rate”
The game loop is a controlled repeating process.
You control speed by waiting between moves (delay).

Mini-task: change speed after every food.

Real-world tie: “control loops” are the basis of:

- thermostats (read temp → adjust heat)
- cruise control
- factory automation PLC cycles
- live monitoring dashboards

### Lesson 5 — Collision Detection and Rules

Concepts: conditionals, sets, logic
Collision is “head is already in snake body”.

Mini-task: add wall collisions (game over if x<0 or x>7).

Real-world tie: rule checks mirror:

- access control rules (is user allowed?)
- fraud detection triggers
- quality control pass/fail logic
- safety interlocks in machinery

### Lesson 6 — Randomness and Fair Spawning

Concepts: randomness, constraints, loops
Food must spawn not on the snake, so you try random positions until valid.

Mini-task: spawn “gold food” worth 3 points sometimes.

Real-world tie: constrained randomness shows up in:

- load balancing
- testing (randomized tests with rules)
- procedural generation in games
- simulation modeling

## Suggested Extensions (Pick One)

- Hard mode: walls kill you (no wrap)
- Pause/Resume: middle click toggles paused state
- High score: save to a text file
- Power-ups: fast/slow, double score, shrink tail
- AI snake: simple “greedy” path to food (teaches algorithms)

## Learning Goals Checklist

By the end, you should be able to:

- Represent a game world as data
- Use an input device as events
- Build a loop with timing control
- Apply collision/rule logic
- Debug using prints/logging
- Connect code structure to real systems