import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import random

def add_word():
    word = entry_word.get()
    meaning = entry_meaning.get()
    if word and meaning:
        words[word] = meaning
        entry_word.delete(0, tk.END)
        entry_meaning.delete(0, tk.END)
        save_data(words)
        update_word_list()
    else:
        messagebox.showwarning("경고", "영단어와 뜻을 모두 입력하세요.")

def show_words():
    update_word_list()

def quiz():
    if words:
        word = random.choice(list(words.keys()))
        answer = simpledialog.askstring("퀴즈", f"{word}의 뜻은 무엇일까요?")
        if answer == words[word]:
            messagebox.showinfo("정답", "정답입니다!")
            stats['correct'] += 1
        else:
            messagebox.showinfo("오답", f"오답입니다. 정답은 {words[word]}입니다.")
            stats['incorrect'] += 1
        update_stats()
        save_stats()
    else:
        messagebox.showwarning("경고", "저장된 단어가 없습니다.")

def delete_word():
    selected_word = listbox_words.get(tk.ACTIVE).split(":")[0].strip()
    if selected_word in words:
        del words[selected_word]
        save_data(words)
        update_word_list()
    else:
        messagebox.showwarning("경고", "삭제할 단어를 선택하세요.")

def edit_word():
    selected_word = listbox_words.get(tk.ACTIVE).split(":")[0].strip()
    if selected_word in words:
        new_word = simpledialog.askstring("단어 편집", "새로운 단어를 입력하세요:", initialvalue=selected_word)
        new_meaning = simpledialog.askstring("뜻 편집", "새로운 뜻을 입력하세요:", initialvalue=words[selected_word])
        if new_word and new_meaning:
            del words[selected_word]
            words[new_word] = new_meaning
            save_data(words)
            update_word_list()
    else:
        messagebox.showwarning("경고", "편집할 단어를 선택하세요.")

def save_data(words):
    with open("words_data.json", "w") as f:
        json.dump(words, f)

def load_data():
    try:
        with open("words_data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_stats():
    with open("stats_data.json", "w") as f:
        json.dump(stats, f)

def load_stats():
    try:
        with open("stats_data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {'correct': 0, 'incorrect': 0}

def update_word_list():
    listbox_words.delete(0, tk.END)
    for word, meaning in words.items():
        listbox_words.insert(tk.END, f"{word}: {meaning}")

def update_stats():
    label_stats.config(text=f"정답: {stats['correct']} 오답: {stats['incorrect']}")

root = tk.Tk()
root.title("영단어 복습 프로그램")

words = load_data()
stats = load_stats()

frame_input = tk.Frame(root)
frame_input.pack(pady=10)

tk.Label(frame_input, text="영단어:").grid(row=0, column=0, padx=5, pady=5)
entry_word = tk.Entry(frame_input)
entry_word.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_input, text="뜻:").grid(row=1, column=0, padx=5, pady=5)
entry_meaning = tk.Entry(frame_input)
entry_meaning.grid(row=1, column=1, padx=5, pady=5)

button_add = tk.Button(frame_input, text="추가", command=add_word)
button_add.grid(row=2, columnspan=2, pady=10)

frame_list = tk.Frame(root)
frame_list.pack(pady=10)

listbox_words = tk.Listbox(frame_list, width=50, height=10)
listbox_words.pack(padx=10)

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

button_show = tk.Button(frame_buttons, text="영단어 목록 보기", command=show_words)
button_show.pack(side=tk.LEFT, padx=5)

button_quiz = tk.Button(frame_buttons, text="퀴즈", command=quiz)
button_quiz.pack(side=tk.LEFT, padx=5)

button_delete = tk.Button(frame_buttons, text="삭제", command=delete_word)
button_delete.pack(side=tk.LEFT, padx=5)

button_edit = tk.Button(frame_buttons, text="편집", command=edit_word)
button_edit.pack(side=tk.LEFT, padx=5)

label_stats = tk.Label(root, text="")
label_stats.pack(pady=10)

update_word_list()
update_stats()

root.mainloop()
