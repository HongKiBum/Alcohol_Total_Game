import pytesseract
from PIL import Image
import re
import tkinter as tk
from tkinter import messagebox
import os
import shutil

class total_game:
  
    def __init__(self):
            pass
      
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
    
  
