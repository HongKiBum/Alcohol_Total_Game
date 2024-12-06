Pronunciation Evaluation Game
=============================

"""
사용자가 발음한 문장을 기준 문장과 비교하여 발음 정확도를 평가하는 게임입니다. 
평균 유사도를 계산하여 '정확', '조금 틀림', '많이 틀림'으로 판별합니다.
"""

게임 특징:
---------
- 사용자가 문장을 읽고, 그 발음을 기준 문장과 비교하여 정확도를 평가합니다.
- 발음 정확도는 '정확', '조금 틀림', '많이 틀림'으로 판별됩니다.

게임 진행:
----------
1. 랜덤으로 문장이 선택되어 화면에 표시됩니다.
2. 사용자가 발음한 문장을 입력하거나 음성으로 녹음합니다.
3. 기준 문장과의 비교 후 발음 정확도가 화면에 표시됩니다.

코드:
-----
```python
# 발음 평가 게임 코드 설명
def evaluate_pronunciation(self, correct_text, recorded_text):
    # 발음 정확도를 평가하는 함수
    # ... 코드 생략 ...

def recognize_audio(self, file_path):
    # 음성 파일을 텍스트로 변환하는 함수
    # ... 코드 생략 ...
    
def analyze_pronunciation(self, correct_text, audio_file, result_label):
    # 발음 분석을 실행하는 함수
    # ... 코드 생략 ...

# 발음 평가 게임 코드 사용방법
tg = total_game()
tg.PronunciationApp()