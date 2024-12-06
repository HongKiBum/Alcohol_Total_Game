Roulette Game
=============

""" 
룰렛 게임은 pygame을 사용하여 구현된 간단한 룰렛 게임입니다. 사용자는 마우스를 클릭하여 룰렛을 돌리고, 룰렛이 멈춘 후 선택된 값이 화면에 표시됩니다.
"""

게임 특징:
---------
- 룰렛에는 여러 가지 값과 색상이 표시됩니다.
- 사용자는 마우스 클릭으로 룰렛을 돌릴 수 있습니다.
- 룰렛이 멈추면 선택된 값이 화면에 표시됩니다.

게임 진행:
----------
1. 사용자가 마우스를 클릭하여 룰렛을 돌립니다.
2. 룰렛이 회전하고 점차적으로 속도를 줄입니다.
3. 룰렛이 멈추면, 선택된 값이 화면에 표시됩니다.

코드:
-----
```python
# 룰렛 게임 코드 설명

def initialize_pygame(self, width, height):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Roulette")
    clock = pygame.time.Clock()
    return screen, clock
    #Pygame 초기화하는 함수, 화면 크기, 게임 제목, 초 표시 해준주는 함수


def draw_roulette(self, screen, font, values, angle, width, height):
    # 룰렛을 그리는 함수
    # ... 코드 생략 ...
    
def get_result(self, values, angle):
    # 룰렛에서 결과를 얻는 함수
    # ... 코드 생략 ...

def RouletteGame(self, values):
    # 룰렛 게임을 실행하는 메인 함수
    # ... 코드 생략 ...

#룰렛 벌칙 게임 코드 사용방법
tg = total_game()
tg.RoulettGame(['벌칙1','벌칙2','벌칙3'])