import numpy as np
import pickle


# Генерация
class CreateResult(object):
    def generate(self):
        # загрузка модели
        name_file = str(input('введите название модели загрузки '))
        with open("models/" + name_file + '.pkl', 'rb') as db_file:
            read_dictionary = pickle.load(db_file)
        # read_dictionary = np.load('{}.pkl'.format("models/"+name_file), allow_pickle=True).item()

        # генерация последовательности
        sequence = ''
        length_text = int(input('Введите длину генерируемой последовательности '))
        for i in range(length_text):
            if i == 0:
                elem_ahead = np.random.choice(list(read_dictionary.keys()))
                sequence += elem_ahead
                sequence += ' '
            else:
                elem_now = np.random.choice(read_dictionary.setdefault(elem_ahead))
                sequence += elem_now
                sequence += ' '
                elem_ahead = elem_now
        return sequence


obj = CreateResult()
print(obj.generate())