Guess the Person Game
=====================

"""
인물 맞추기 게임은 랜덤으로 표시되는 이미지를 보고 사용자가 정답을 입력하는 게임입니다. 
사용자는 정답을 맞추면 점수를 얻고, 틀리면 오답을 표시해줍니다.
"""

게임 특징:
---------
- 게임은 이미지가 랜덤으로 표시되며, 그에 해당하는 정답을 입력해야 합니다.
- 사용자가 입력한 정답이 맞는지 확인하고 결과를 출력합니다.

게임 진행:
----------
1. 화면에 랜덤 이미지가 표시됩니다.
2. 사용자는 이미지를 보고 그에 해당하는 이름을 입력합니다.
3. 정답이 맞으면 "정답입니다!"를, 틀리면 "오답입니다!"가 표시됩니다.

코드:
-----
```python
# 인물 맞추기 게임 코드 설명
def GuessPersonGame(self, images):
    random.shuffle(images)
    # 코드를 실행시키고 이미지를 랜덤으로 섞는 함수
    # ... 코드 생략 ...
    
def check_answer(self):
    # 사용자의 답을 확인하는 함수
    # ... 코드 생략 ...
    
def load_image(self):
    # 이미지를 불러오는 함수
    # ... 코드 생략 ...

# 인물 맞추기 게임 코드 사용방법
tg = total_game()
images = [
    {"image": "path_to_image_1.jpg", "answer": "Person 1"},
    {"image": "path_to_image_2.jpg", "answer": "Person 2"}
]
tg.GuesseGameApp(images)