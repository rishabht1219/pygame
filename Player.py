import pygame
from constants import (
    PLAYER_RADIUS,
    LINE_WIDTH,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    PLAYER_SHOOT_SPEED,
    PLAYER_SHOOT_COOLDOWN_SECONDS,
)
from shot import Shot
from CircleShape import CircleShape


class Player(CircleShape):
    def __init__(self, x: int, y: int):
        # Call parent constructor with x, y, and radius
        super().__init__(x, y, PLAYER_RADIUS)

        # Rotation angle in degrees
        self.rotation = 0
        self.shoot_timer = 0.0

    
    def triangle(self):
        # Returns the 3 points of the triangle representing the player
        # Forward vector
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        right = forward.rotate(120)
        left = forward.rotate(-120)

        tip = self.position + forward * self.radius
        right_point = self.position + right * self.radius
        left_point = self.position + left * self.radius

        return [tip, right_point, left_point]

    def draw(self, surface):
        pygame.draw.polygon(
            surface,
            "white",
            self.triangle(),
            LINE_WIDTH
        )

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += direction * PLAYER_SPEED * dt

    def update(self, dt):
        if self.shoot_timer > 0:
            self.shoot_timer -= dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()



    def shoot(self):
        if self.shoot_timer > 0:
            return

        shot = Shot(self.position.x, self.position.y)

        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity = direction * PLAYER_SHOOT_SPEED

        self.shoot_timer = PLAYER_SHOOT_COOLDOWN_SECONDS



