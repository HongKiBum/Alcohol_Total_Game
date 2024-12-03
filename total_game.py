import pygame
import math
import random

class total_game:
    def __init__(self):
        pass

    def initialize_pygame(self, width, height):
        pygame.init()
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Roulette")
        clock = pygame.time.Clock()
        return screen, clock

    def draw_roulette(self, screen, font, values, angle, width, height):
        screen.fill((60, 0, 0))  # Background color (brown)
        radius = min(width, height) // 2 - 40
        triangle_size = 15
        center = (width // 2, height // 2)

        colors = [(255, 0, 0), (0, 0, 0)]  # Red and Black for segments

        for i, value in enumerate(values):
            start_angle = math.radians(360 / len(values) * i + angle)
            end_angle = math.radians(360 / len(values) * (i + 1) + angle)
            color = colors[i % len(colors)]

            points = [center]
            num_points = 50
            for j in range(num_points + 1):
                t = j / num_points
                angle_step = start_angle + (end_angle - start_angle) * t
                x = center[0] + radius * math.cos(angle_step)
                y = center[1] + radius * math.sin(angle_step)
                points.append((x, y))
            pygame.draw.polygon(screen, color, points)

            text_angle = (start_angle + end_angle) / 2
            text_x = center[0] + radius * 0.7 * math.cos(text_angle)
            text_y = center[1] + radius * 0.7 * math.sin(text_angle)
            text_surface = font.render(value, True, (255, 255, 255))
            screen.blit(text_surface, (text_x - text_surface.get_width() // 2,
                                       text_y - text_surface.get_height() // 2))

        pygame.draw.circle(screen, (60, 0, 0), center, 10)

        pygame.draw.polygon(screen, (255, 255, 255), [
            (center[0], center[1] - radius + triangle_size),
            (center[0] - triangle_size, center[1] - radius),
            (center[0] + triangle_size, center[1] - radius)
        ])

    def get_result(self, values, angle):
        arrow_angle = (270 - angle) % 360
        index = int(arrow_angle // (360 / len(values)))
        return values[index]

    def roulette_game(self, values):
        width, height = 500, 500
        # Use self to call the initialize_pygame method
        screen, clock = self.initialize_pygame(width, height)
        font = pygame.font.SysFont("malgungothic", 20)

        angle = 0
        speed = 0
        is_spinning = False
        is_stopping = False

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if not is_spinning:
                        speed = random.uniform(10, 15)
                        is_spinning = True
                    elif not is_stopping:
                        is_stopping = True

            if is_spinning:
                angle += speed
                if is_stopping:
                    speed *= 0.98
                    if speed < 0.1:
                        speed = 0
                        is_spinning = False
                        is_stopping = False
                        result = self.get_result(values, angle)  # Use self
                        print(f"Selected value: {result}")

            self.draw_roulette(screen, font, values, angle, width, height)  # Use self
            pygame.display.flip()
            clock.tick(60)

        pygame.quit()
