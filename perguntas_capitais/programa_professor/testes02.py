import csv
import random
import time
import os
from datetime import datetime

def read_questions_and_answers(file_name):
    questions = []
    with open(file_name, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            question = row[0]
            options = [row[1], row[2], row[3], row[4]]
            correct_answer = row[5]
            questions.append((question, options, correct_answer))
    return questions

def select_n_questions(questions, n):
    selected_questions = random.sample(questions, n)
    return selected_questions

def ask_question(question, options, correct_answer, time_limit):
    print(f"Pergunta: {question}")
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    start_time = time.time()
    user_answer = input(f"Digite a letra da resposta correta (tempo limite {time_limit} segundos): ")
    end_time = time.time()
    elapsed_time = end_time - start_time
    if user_answer.lower() == correct_answer.lower():
        return True, elapsed_time
    else:
        return False, elapsed_time

def quiz(questions, n, time_limit):
    selected_questions = select_n_questions(questions, n)
    correct_answers = 0
    incorrect_answers = 0
    time_correct_answers = 0
    time_incorrect_answers = 0
    for question in selected_questions:
        correct, elapsed_time = ask_question(*question, time_limit)
        if correct:
            correct_answers += 1
            time_correct_answers += elapsed_time
        else:
            incorrect_answers += 1
            time_incorrect_answers += elapsed_time
    return correct_answers, incorrect_answers, time_correct_answers, time_incorrect_answers

def save_results(file_name, user_name, correct_answers, incorrect_answers, time_correct_answers, time_incorrect_answers):
    with open(file_name, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([user_name, correct_answers, incorrect_answers, time_correct_answers, time_incorrect_answers])

def main():
    questions = read_questions_and_answers('paises_geonames.com.txt.csv')
    n = int(input("Digite o número de questões: "))
    time_limit = int(input("Digite o tempo limite em segundos: "))
    user_name = input("Digite o seu nome: ")
    correct_answers, incorrect_answers, time_correct_answers, time_incorrect_answers = quiz(questions, n, time_limit)
    file_name = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{user_name}.csv"
    save_results(file_name, user_name, correct_answers, incorrect_answers, time_correct_answers, time_incorrect_answers)
    print(f"Resultados salvos em {file_name}")
    print(f"Respostas corretas: {correct_answers}")
    print(f"Respostas erradas: {incorrect_answers}")
    print(f"Tempo médio das respostas corretas: {time_correct_answers / correct_answers if correct_answers > 0 else 0} segundos")
    print(f"Tempo médio das respostas erradas: {time_incorrect_answers / incorrect_answers if incorrect_answers > 0 else 0} segundos")

if __name__ == "__main__":
    main()