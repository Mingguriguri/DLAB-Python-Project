import json
import random


def add_word(words, word, meaning):
    words[word] = meaning


def show_words(words):
    for word, meaning in words.items():
        print(f"{word}: {meaning}")


def quiz(words):
    if words:
        word = random.choice(list(words.keys()))
        print(f"단어: {word}")
        answer = input("이 단어의 뜻은 무엇일까요? ")
        if answer == words[word]:
            print("정답입니다!")
        else:
            print(f"오답입니다. 정답은 {words[word]}입니다.")
    else:
        print("저장된 단어가 없습니다.")


def save_data(words):
    with open("words_data.json", "w") as f:
        json.dump(words, f)


def load_data():
    try:
        with open("words_data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


words = load_data()

while True:
    print("\n1. 영단어 추가")
    print("2. 영단어 목록 보기")
    print("3. 랜덤 영단어 퀴즈")
    print("4. 종료")

    action = input("원하는 작업을 선택하세요: ")

    if action == '1':
        word = input("영단어를 입력하세요: ")
        meaning = input("뜻을 입력하세요: ")
        add_word(words, word, meaning)
        save_data(words)
    elif action == '2':
        show_words(words)
    elif action == '3':
        quiz(words)
    elif action == '4':
        break
    else:
        print("잘못된 선택입니다. 다시 시도하세요.")
