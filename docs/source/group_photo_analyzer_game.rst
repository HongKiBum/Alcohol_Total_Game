Group Photo Analyzer Game
=========================

"""
그룹 사진에서 사람의 손 모양을 분석하여 랜덤으로 벌칙 대상을 선택하는 프로그램입니다.
YOLO를 이용하여 사람을 감지하고, 손 모양에 따라 특징을 분석합니다.
"""

게임 특징:
---------
- YOLO 모델을 사용하여 그룹 사진에서 사람을 감지합니다.
- 사람의 손 모양을 분석하여 랜덤으로 벌칙 대상을 선택합니다.

게임 진행:
----------

1. 사용자가 이미지를 업로드합니다.
2. YOLO 모델이 이미지를 분석하고 사람을 감지합니다.
3. 감지된 사람의 손 모양에 따라 특징을 분석하고 랜덤으로 벌칙을 부여합니다.

코드:
-----

```python
# 그룹 사진 분석 게임 코드 설명
def analyze_group_photo(self, state, image_path, mission, confidence_threshold=0.5):
    # 그룹 사진을 분석하는 함수
    # ... 코드 생략 ...

def select_image(self, state):
    # 이미지를 선택하는 함수
    # ... 코드 생략 ...
    
def start_analysis(self, state):
    # 분석을 시작하는 함수
    # ... 코드 생략 ...


# 그룹 사진 분석 게임 코드 사용방법
tg = total_game()
tg.GroupPhotoAnalyzerApp()