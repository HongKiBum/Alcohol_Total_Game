import os
import re
import random
from difflib import SequenceMatcher
import speech_recognition as sr
from tkinter import Tk, Label, Button, filedialog
from PIL import Image, ImageTk  # 이미지 처리를 위한 라이브러리


import pytesseract
from tkinter import messagebox
import shutil


class total_game:

    def __init__(self, root):
        self.root = root
        self.root.title("어려운 문장 발음 평가 프로그램")
        self.root.geometry("800x500")
        self.root.configure(bg="#FFFFFF")  # 배경색 설정

        # 문장 리스트
        self.sentences = [
            "도토리가 문을 도로록, 드르륵, 두루룩 열었는가?",
            "우리집 옆집 앞집 뒤창살은 홑겹창살이고 우리집 뒷집 앞집 옆창살은 겹홑창살이다.",
            "한양양장점 옆에 한영양장점 한영양장점 옆에 한양양장점",
            "청단풍잎 홍단풍잎 흑단풍잎 백단풍잎",
            "작은 토끼 토끼통 옆에는 큰 토끼 토끼 통이 있고 큰 토끼 토끼통 옆에는 작은 토끼 토끼 통이 있다.",
            "생각이란 생각하면 생각할수록 생각나는 것이 생각이므로 생각하지 않는 생각이 좋은 생각이라 생각한다.",
            "앞뜰에 있는 말뚝이 말 맬 말뚝이냐 말 못맬 말뚝이냐",
            "경찰청 쇠창살 외철창살 검찰청 쇠창살 쌍철창살",
            "간장 공장 공장장은 강 공장장이고 된장 공장 공장장은 장 공장장이다."
        ]
        self.selected_sentence = ""

        # GUI 요소
        self.label = Label(
            root, text="랜덤 문장을 읽어보세요!", font=("Arial", 18), bg="#FFFFFF", fg="#333333"
        )
        self.label.pack(pady=20)

        self.sentence_label = Label(
            root, text="", font=("Arial", 14), wraplength=700, justify="center", bg="#FFFFFF", fg="#333333"
        )
        self.sentence_label.pack(pady=20)

        self.select_button = Button(
            root,
            text="누르면 랜덤한 문장이 나와요!",
            command=self.select_sentence,
            font=("Arial", 14),
            bg="#87CEEB",
            fg="white",
            activebackground="#B0E0E6",
            relief="flat",
            width=23,
            height=2,
        )
        self.select_button.pack(pady=10)

        self.upload_button = Button(
            root,
            text="오디오 파일 업로드",
            command=self.upload_audio,
            font=("Arial", 14),
            bg="#87CEEB",
            fg="white",
            activebackground="#B0E0E6",
            relief="flat",
            width=15,
            height=2,
        )
        self.upload_button.pack(pady=10)

        self.result_label = Label(
            root, text="", font=("Arial", 14), bg="#FFFFFF", fg="#333333"
        )
        self.result_label.pack(pady=30)

    def similar_sound_correction(self, word):
        replacements = {
            "쟝": "장",  # 비슷한 발음 처리
            "깡": "강",
            "도로록": "도로룩",
            "두루룩": "두루륵",
            "홑겹": "홀겹",
            "겹홑": "겹홀",
            "창살": "창쌀",
            "단풍잎": "단퐁잎",
            "토끼통": "토끼톳",
            "쇠창살": "쇠쌍살",
            "철창살": "쓸창살",
            "공장장": "공쨍장"
        }
        for key, value in replacements.items():
            word = word.replace(key, value)
        return word

    def evaluate_pronunciation(self, correct_text, recorded_text):
        correct_words = re.findall(r'\S+', correct_text)
        recorded_words = re.findall(r'\S+', recorded_text)

        total_ratio = 0
        word_count = min(len(correct_words), len(recorded_words))
        detailed_results = []

        for correct_word, recorded_word in zip(correct_words, recorded_words):
            corrected_recorded_word = self.similar_sound_correction(recorded_word)
            ratio = SequenceMatcher(None, correct_word, corrected_recorded_word).ratio()
            detailed_results.append((correct_word, corrected_recorded_word, ratio))
            total_ratio += ratio

        avg_ratio = total_ratio / word_count if word_count > 0 else 0
        avg_percentage = avg_ratio * 100

        if avg_ratio > 0.9:
            result = "정확"
        elif avg_ratio > 0.7:
            result = "조금 틀림"
        else:
            result = "많이 틀림"

        return result, avg_percentage, detailed_results

    def recognize_audio(self, file_path):
        recognizer = sr.Recognizer()
        audio_file = sr.AudioFile(file_path)

        with audio_file as source:
            audio_data = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio_data, language='ko-KR')
            return text
        except sr.UnknownValueError:
            return "음성을 인식할 수 없습니다."
        except sr.RequestError:
            return "서비스에 접근할 수 없습니다."

    def analyze_pronunciation(self, correct_text, audio_file):
        recorded_text = self.recognize_audio(audio_file)
        print(f"녹음된 텍스트: {recorded_text}")

        result, avg_percentage, _ = self.evaluate_pronunciation(correct_text, recorded_text)
        print(f"발음 정확도: {result} (평균 유사도: {avg_percentage:.2f}%)")

        return result, avg_percentage

    def select_sentence(self):
        self.selected_sentence = random.choice(self.sentences)
        self.sentence_label.config(text=self.selected_sentence)

    def upload_audio(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav;*.mp3")])
        if file_path:
            result, avg_percentage = self.analyze_pronunciation(self.selected_sentence, file_path)
            self.result_label.config(text=f"발음 정확도: {result} ({avg_percentage:


      
    def receipt():
            """
            영수증 이미지에서 금액을 추출하고, 인원 수로 나누어 금액을 계산하는 모든 작업을 하나의 함수에서 처리하는 함수.
            """
            try:
                # Tkinter 메인 창 생성
                root = tk.Tk()
                root.title("영수증 나누기 계산기")
    
                # 이미지 경로 입력
                tk.Label(root, text="이미지 경로:").grid(row=0, column=0, padx=10, pady=10)
                image_path_entry = tk.Entry(root, width=30)
                image_path_entry.grid(row=0, column=1, padx=10, pady=10)
    
                # 인원 수 입력
                tk.Label(root, text="인원 수:").grid(row=1, column=0, padx=10, pady=10)
                num_people_entry = tk.Entry(root, width=10)
                num_people_entry.grid(row=1, column=1, padx=10, pady=10)
    
                        # Tesseract 경로 설정
                if shutil.which('tesseract'):  # 시스템 PATH에서 'tesseract' 실행 파일 찾기
                    tesseract_path = shutil.which('tesseract')
                elif os.getenv('TESSERACT_PATH'):  # 환경 변수 TESSERACT_PATH 확인
                    tesseract_path = os.getenv('TESSERACT_PATH')
                else:
                    # 운영 체제에 따라 기본 경로 설정
                    if os.name == 'nt':  # Windows
                        tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
                    elif os.name == 'posix':  # Linux 또는 macOS
                        tesseract_path = '/usr/local/bin/tesseract'  # macOS / Linux
                    else:
                        tesseract_path = None  # 경로를 찾을 수 없음
    
                if not tesseract_path or not os.path.isfile(tesseract_path):
                    messagebox.showerror("에러", "Tesseract 경로를 찾을 수 없습니다. Tesseract가 설치되었는지 확인해 주세요.")
                    return
                
                pytesseract.pytesseract.tesseract_cmd = tesseract_path
    
    
                def on_calculate_click():
                    """
                    계산 버튼 클릭 시 실행되는 함수.
                    """
                    image_path = image_path_entry.get()
                    try:
                        num_people = int(num_people_entry.get())
                        
                        if num_people <= 0:
                            messagebox.showerror("에러", "인원 수는 1명 이상이어야 합니다.")
                            return
    
                        # 이미지에서 금액을 추출
                        img = Image.open(image_path)
                        result = pytesseract.image_to_string(img)
    
                        # 쉼표가 포함된 금액 추출
                        numbers_with_commas = re.findall(r'\d{1,3}(?:,\d{3})*', result)
                        numbers = [int(num.replace(',', '')) for num in numbers_with_commas]
    
                        # 가장 큰 금액 추출
                        total_amount = max(numbers) if numbers else None
    
                        if total_amount is not None:
                            # 1인당 금액 계산
                            amount_per_person = total_amount / num_people
    
                            # 금액 포맷팅
                            formatted_total = f"{total_amount:,.2f} 원"
                            formatted_per_person = f"{amount_per_person:,.2f} 원"
    
                            # 결과 출력
                            result_text = f"총 금액: {formatted_total}\n1인당 금액: {formatted_per_person}"
                            messagebox.showinfo("계산 결과", result_text)
                        else:
                            messagebox.showerror("에러", "유효한 금액을 추출할 수 없습니다.")
                    except Exception as e:
                        messagebox.showerror("에러", f"오류 발생: {e}")
    
                # 실행 버튼
                calculate_button = tk.Button(root, text="계산하기", command=on_calculate_click)
                calculate_button.grid(row=2, column=0, columnspan=2, pady=20)
    
                root.mainloop()
            
            except Exception as e:
                messagebox.showerror("에러", f"전체 프로그램 실행 중 오류 발생: {e}")
    
  
