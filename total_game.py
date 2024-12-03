import pygame
import math
import random
from tkinter import Tk, Label, Entry, Button
from PIL import Image, ImageTk


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
  
    def guesse_game_app(self,images):
    """
    인물 맞추기 게임을 실행합니다. 이미지가 랜덤 순서로 표시됩니다.

    Args:
        images (list): 각 항목이 {"image": "이미지 경로", "answer": "정답"} 형태의 딕셔너리로 이루어진 리스트.
    """
    # 이미지 랜덤 섞기
    random.shuffle(images)

    # 초기 변수 설정
    current_index = [0]  # 리스트로 선언하여 내부 함수에서 변경 가능
    score = [0]          # 리스트로 선언하여 내부 함수에서 변경 가능

        def check_answer():
            user_input = entry.get().strip()
            correct_answer = images[current_index[0]]["answer"]

            if user_input == correct_answer:
                result_label.config(text="정답입니다!", fg="green")
                score[0] += 1
            else:
                result_label.config(text=f"오답입니다! 정답은 '{correct_answer}'였습니다.", fg="red")

            # 일정 시간 후 다음 문제로 이동
            root.after(2000, next_question)

        def next_question():
            current_index[0] += 1
            if current_index[0] < len(images):
                load_image()
            else:
                result_label.config(text=f"게임 종료! 점수: {score[0]}/{len(images)}")
                entry.config(state="disabled")
                submit_button.config(state="disabled")

            entry.delete(0, "end")

        def load_image():
            img = Image.open(images[current_index[0]]["image"])
            img = img.resize((400, 400))
            photo = ImageTk.PhotoImage(img)
            image_label.config(image=photo)
            image_label.photo = photo
            result_label.config(text="")  # 결과 초기화

        # Tkinter GUI 초기화
        root = Tk()
        root.title("인물 맞추기 게임")

        # 이미지 표시
        image_label = Label(root)
        image_label.pack()

        # 입력 창
        entry = Entry(root, font=("Arial", 16))
        entry.pack(pady=10)

        # 제출 버튼
        submit_button = Button(root, text="제출", command=check_answer)
        submit_button.pack(pady=5)

        # 결과 표시
        result_label = Label(root, text="", font=("Arial", 14))
        result_label.pack(pady=10)

        # 첫 번째 이미지 로드
        load_image()

        # Tkinter 루프 시작
        root.mainloop()
    
