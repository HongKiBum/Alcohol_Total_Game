import pygame
import math
import random
from tkinter import Tk, Label, Entry, Button
from PIL import Image, ImageTk


class total_game:
    def __init__(self):
        pass

  
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
    
