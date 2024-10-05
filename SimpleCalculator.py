import tkinter as tk

calc = tk.Tk() # 창 생성
calc.title("Calculator") # 타이틀
calc.geometry("300x300") # 크기

def calculate(event):
    value = tk.Entry.get(display)
    if value != '':
        result = eval(value) # eval() 함수로 계산
        print(result)
        display.delete(0,tk.END)  # 0번째 자리부터 내용 삭제
        display.insert(0,result)  # 0번째 자리부터 새 값 입력
        
def clear(event):             # C 버튼과 Esc 키를 위한 함수 입니다.
    display.delete(0,tk.END)  # 내용 삭제

display = tk.Entry(calc, width = 20) # 출력창
display.pack() # 위젯을 배치할 수 있음

button_e = tk.Button(calc, text='=', width=5)  # = 버튼 추가
button_e.bind('<Button-1>',calculate)          # 버튼에 클릭 이벤트 추가
button_e.pack()
 
button_c = tk.Button(calc, text='c', width=5)  # C버튼추가. text속성은 버튼에 표시할 문자입니다.
button_c.bind('<Button-1>',clear)           # <Button-1> 이벤트는 마우스 왼쪽클릭 이벤트입니다.
button_c.pack()
 
calc.bind('<Return>', calculate) # 엔터키(이벤트)를 func 함수로 연결.
calc.bind('Escape', clear)

calc.mainloop() # 창 종료될 때 까지 실행