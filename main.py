from sense_hat import SenseHat
from random import randint
import time

sense = SenseHat()
sense.clear()
sense.low_light = True  # set False if you want it brighter

W, H = 8, 8

# Speed Configuration
BASE_STEP_DELAY = 0.35
BASE_MIN_DELAY = 0.10
BASE_SPEEDUP_EVERY = 4

# Colors (R, G, B)
C_BG = (0, 0, 0)
C_SNAKE = (0, 255, 0)
C_HEAD = (0, 160, 255)
C_FOOD = (255, 0, 0)
C_TEXT = (255, 255, 255)
C_FLASH = (255, 255, 0)

# Directions as (dx, dy)
DIRS = {
    "up": (0, -1),
    "down": (0, 1),
    "left": (-1, 0),
    "right": (1, 0),
}


def wrap(x, y):
    """Wrap coordinates to the grid"""
    return x % W, y % H


def place_food(snake):
    """Place food at a random location that is not occupied by the snake"""
    snake_set = set(snake)
    while True:
        p = (randint(0, W - 1), randint(0, H - 1))
        if p not in snake_set:
            return p


def draw(snake, food):
    """Draw the snake and food on the Sense HAT"""
    sense.clear(C_BG)
    # Food
    sense.set_pixel(food[0], food[1], C_FOOD)
    # Snake
    for i, (x, y) in enumerate(snake):
        sense.set_pixel(x, y, C_HEAD if i == 0 else C_SNAKE)


def game_over(score):
    """Display game over message"""
    for _ in range(3):
        sense.clear(C_FLASH)
        time.sleep(0.12)
        sense.clear(C_BG)
        time.sleep(0.12)
    sense.show_message('Score ' + score, text_colour=C_TEXT, back_colour=C_BG, scroll_speed=0.06)
    sense.clear()


def read_direction(current_dir):
    """Read direction from joystick"""
    opposite = {"up": "down", "down": "up", "left": "right", "right": "left"}

    events = sense.stick.get_events()
    new_dir = current_dir
    for e in events:
        if e.action != "pressed":
            continue
        if e.direction in ("up", "down", "left", "right"):
            if e.direction != opposite[current_dir]:
                new_dir = e.direction
    return new_dir


def main():
    """Main game loop"""

    snake = [(4, 4), (3, 4), (2, 4)]
    direction = "right"
    food = place_food(snake)
    score = 0

    step_delay = BASE_STEP_DELAY
    min_delay = BASE_MIN_DELAY
    speedup_every = BASE_SPEEDUP_EVERY

    last_step = time.time()

    while True:
        direction = read_direction(direction)

        now = time.time()
        if now - last_step < step_delay:
            time.sleep(0.01)
            continue
        last_step = now

        dx, dy = DIRS[direction]
        head_x, head_y = snake[0]
        new_head = wrap(head_x + dx, head_y + dy)

        # Collision with self -> game over
        if new_head in snake:
            game_over(score)
            return

        snake.insert(0, new_head)

        if new_head == food:
            score += 1
            food = place_food(snake)

            # Increase speed.
            if score % speedup_every == 0:
                step_delay = max(min_delay, step_delay - 0.03)
        else:
            snake.pop()

        draw(snake, food)


if __name__ == "__main__":
    try:
        main()
    finally:
        sense.clear()
