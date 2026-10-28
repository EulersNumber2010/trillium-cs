"""A tiny Pygame game that also runs in the browser.

Run it in the browser (this is the normal way in a codespace):
    pygbag --port 3000 pygame-starter
then open the forwarded port 3000 when the notification appears.

The only rule for browser-friendly Pygame: the game loop is `async` and
calls `await asyncio.sleep(0)` once per frame. Everything else is ordinary
Pygame. On a real desktop the same file runs with `python main.py`.
"""
import asyncio
import pygame
import random

WIDTH, HEIGHT = 640, 400
#WIDTH, HEIGHT = 480, 360
CELL_SIZE = 3
COLS, ROWS = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE
BRUSH_RADIUS = 3


async def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Powder")
    clock = pygame.time.Clock()

    # A true cell holds one grain of powder.
    grid = [[False for _ in range(COLS)] for _ in range(ROWS)]
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if pygame.mouse.get_pressed()[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            cx, cy = mouse_x // CELL_SIZE, mouse_y // CELL_SIZE
            for dy in range(-BRUSH_RADIUS, BRUSH_RADIUS + 1):
                for dx in range(-BRUSH_RADIUS, BRUSH_RADIUS + 1):
                    if dx * dx + dy * dy > BRUSH_RADIUS * BRUSH_RADIUS:
                        continue
                    x, y = cx + dx, cy + dy
                    if 0 <= x < COLS and 0 <= y < ROWS:
                        grid[y][x] = True

        # Process from the bottom upward so grains fall one cell per frame.
        for y in range(ROWS - 2, -1, -1):
            xs = range(COLS) if random.getrandbits(1) else range(COLS - 1, -1, -1)
            for x in xs:
                if not grid[y][x]:
                    continue
                if not grid[y + 1][x]:
                    grid[y][x], grid[y + 1][x] = False, True
                    continue

                sides = (-1, 1) if random.getrandbits(1) else (1, -1)
                for dx in sides:
                    nx = x + dx
                    if 0 <= nx < COLS and not grid[y + 1][nx]:
                        grid[y][x], grid[y + 1][nx] = False, True
                        break

        screen.fill((24, 27, 35))
        for y, row in enumerate(grid):
            for x, occupied in enumerate(row):
                if occupied:
                    pygame.draw.rect(
                        screen,
                        (235, 190, 90),
                        (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE),
                    )

        pygame.display.flip()
        clock.tick(60)
        await asyncio.sleep(0)  # hands control to the browser once per frame

asyncio.run(main())
