from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring
import json
import re

root = Tk()
root.title("일정 관리 어플리케이션")

# 일정 데이터를 저장할 딕셔너리
schedule_data = {}

# 일정 데이터를 파일로 저장
def save_data():
    with open("schedule_data.json", "w") as f:
        json.dump(schedule_data, f)

# 일정 데이터를 파일에서 로드
def load_data():
    global schedule_data
    try:
        with open("schedule_data.json", "r") as f:
            schedule_data = json.load(f)
            for date, events in schedule_data.items():
                listbox_dates.insert(END, date)
    except FileNotFoundError:
        pass

# 일정을 추가하는 함수
def add_schedule():
    date = entry_date.get()
    event = entry_event.get()

    if date and event:
        if not re.match(r'\d{4}-\d{2}-\d{2}', date):
            messagebox.showwarning("경고", "날짜 형식이 올바르지 않습니다. (YYYY-MM-DD)")
            return
        if date not in schedule_data:
            schedule_data[date] = []
            listbox_dates.insert(END, date)
        schedule_data[date].append(event)
        entry_date.delete(0, END)
        entry_event.delete(0, END)
        save_data()
    else:
        messagebox.showwarning("경고", "날짜와 일정을 모두 입력하세요.")

# 선택한 날짜의 일정을 표시하는 함수
def show_schedule(event):
    selected_date = listbox_dates.get(ACTIVE)
    if selected_date in schedule_data:
        listbox_events.delete(0, END)
        for event in schedule_data[selected_date]:
            listbox_events.insert(END, event)

# 일정 삭제 함수
def delete_event():
    selected_date = listbox_dates.get(ACTIVE)
    selected_event_index = listbox_events.curselection()
    if selected_event_index:
        selected_event = listbox_events.get(selected_event_index)
        schedule_data[selected_date].remove(selected_event)
        listbox_events.delete(selected_event_index)
        save_data()
    else:
        messagebox.showwarning("경고", "삭제할 일정을 선택하세요.")

# 일정 편집 함수
def edit_event():
    selected_date = listbox_dates.get(ACTIVE)
    selected_event_index = listbox_events.curselection()
    if selected_event_index:
        selected_event = listbox_events.get(selected_event_index)
        new_event = askstring("일정 편집", "새로운 일정을 입력하세요:", initialvalue=selected_event)
        if new_event:
            schedule_data[selected_date][selected_event_index[0]] = new_event
            listbox_events.delete(selected_event_index)
            listbox_events.insert(selected_event_index, new_event)
            save_data()
    else:
        messagebox.showwarning("경고", "편집할 일정을 선택하세요.")

# UI 구성
frame_input = Frame(root)
frame_input.pack(pady=10)

Label(frame_input, text="날짜 (YYYY-MM-DD):").grid(row=0, column=0, padx=5, pady=5)
entry_date = Entry(frame_input)
entry_date.grid(row=0, column=1, padx=5, pady=5)

Label(frame_input, text="일정:").grid(row=1, column=0, padx=5, pady=5)
entry_event = Entry(frame_input)
entry_event.grid(row=1, column=1, padx=5, pady=5)

button_add = Button(frame_input, text="일정 추가", command=add_schedule)
button_add.grid(row=2, columnspan=2, pady=10)

frame_list = Frame(root)
frame_list.pack(pady=10)

listbox_dates = Listbox(frame_list, height=10)
listbox_dates.pack(side=LEFT, padx=10)

listbox_events = Listbox(frame_list, height=10)
listbox_events.pack(side=LEFT, padx=10)

frame_buttons = Frame(root)
frame_buttons.pack(pady=10)

button_edit = Button(frame_buttons, text="일정 편집", command=edit_event)
button_edit.pack(side=LEFT, padx=5)

button_delete = Button(frame_buttons, text="일정 삭제", command=delete_event)
button_delete.pack(side=LEFT, padx=5)

listbox_dates.bind("<<ListboxSelect>>", show_schedule)

# 프로그램 시작 시 데이터 로드
load_data()

root.mainloop()
