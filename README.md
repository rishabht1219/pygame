# Asteroids (Pygame)

A simple **Asteroids-style arcade game** built with **Python and Pygame**.  
Control a ship, shoot asteroids, and avoid collisions. Asteroids spawn over time and split into smaller pieces when destroyed.

## Controls
- **W / S** – Move forward / backward  
- **A / D** – Rotate left / right  
- **Space** – Shoot  

## Features
- Frame-rate independent movement using delta time (`dt`)
- Player shooting with cooldown
- Asteroid spawning and splitting
- Collision detection (player–asteroid, shot–asteroid)
- Event and state logging
- Sprite groups for clean update and draw handling

## Requirements
- Python 3.13
- `pygame`

Install dependencies:
```bash
pip install pygame
```

Run the game:
```bash
python main.py

