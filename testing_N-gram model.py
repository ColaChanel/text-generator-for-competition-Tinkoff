import re
import numpy as np
import pickle
import generate
import train

# class Model(object):
#
#     # Обучение
#     def fit(self, input_dir="texts"):
#         name_training = str(input('Введите название файла train '))
#         f = open('{}'.format(input_dir + "/" + name_training), encoding='utf-8')
#         text = ''
#         for line in f.readlines():
#             text += str(line)
#         f.close()
#
#         # форматирование текста
#         text = text.lower()
#         text = text.strip()
#         text = re.split("[^a-zа-яё]+", text)  # удаление неалфавитных символов
#
#         # токенизация
#         dictionary = {}
#         for i in range(len(text) - 1):
#             if dictionary.get(text[i], 0):
#                 pointer = dictionary.get(text[i])
#                 pointer.append(text[i + 1])
#                 dictionary[text[i]] = pointer
#             else:
#                 dictionary[text[i]] = [text[i + 1]]
#
#         # сохранeние модели
#         name_file = str(input('введите название модели сохранения '))
#         with open("models/" + name_file + '.pkl', 'wb') as f:
#             pickle.dump(dictionary, f)
#         # pickle.dump('{}'.format("models/"+name_file), dictionary)
#         # np.save('{}'.format("models/"+name_file), dictionary)
#
#     # Генерация
#     def generate(self):
#         # загрузка модели
#         name_file = str(input('введите название модели загрузки '))
#         with open("models/" + name_file + '.pkl', 'rb') as db_file:
#             read_dictionary = pickle.load(db_file)
#         # read_dictionary = np.load('{}.pkl'.format("models/"+name_file), allow_pickle=True).item()
#
#         # генерация последовательности
#         sequence = ''
#         length_text = int(input('Введите длину генерируемой последовательности '))
#         for i in range(length_text):
#             if i == 0:
#                 elem_ahead = np.random.choice(list(read_dictionary.keys()))
#                 sequence += elem_ahead
#                 sequence += ' '
#             else:
#                 elem_now = np.random.choice(read_dictionary.setdefault(elem_ahead))
#                 sequence += elem_now
#                 sequence += ' '
#                 elem_ahead = elem_now
#         return sequence


def main():
    while True:
        print('1. Обучать модель')
        print('2. Генерировать результат')
        print('3.Выйти')
        start = str(input('Что вы хотите делать введите цифру: '))
        if start =='3':
            break
        if start == '1':
            answer = str(input("Хотити ли вы прописать путь до папки? Да или Нет. "))
            if answer == "Да":
                path = str(input('Введите путь используя слеши (/) до папки кроме последнего: '))
                train.LearningModel().fit(input_dir=path)
            else:
                train.LearningModel().fit()
        elif start == '2':
            print(generate.CreateResult().generate())
        else:
            print('Вы ввели неверно команду, вводите число')


if __name__ == "__main__":
    main()
