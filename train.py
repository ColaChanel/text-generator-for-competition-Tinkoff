import re
import pickle


# Обучение
class LearningModel(object):
    def fit(self, input_dir="texts"):
        name_training = str(input('Введите название файла train '))
        f = open('{}'.format(input_dir + "/" + name_training), encoding='utf-8')
        text = ''
        for line in f.readlines():
            text += str(line)
        f.close()

        # форматирование текста
        text = text.lower()
        text = text.strip()
        text = re.split("[^a-zа-яё]+", text)  # удаление неалфавитных символов

        # токенизация
        dictionary = {}
        for i in range(len(text) - 1):
            if dictionary.get(text[i], 0):
                pointer = dictionary.get(text[i])
                pointer.append(text[i + 1])
                dictionary[text[i]] = pointer
            else:
                dictionary[text[i]] = [text[i + 1]]

        # сохранeние модели
        name_file = str(input('введите название модели сохранения '))
        with open("models/" + name_file + '.pkl', 'wb') as f:
            pickle.dump(dictionary, f)
        # pickle.dump('{}'.format("models/"+name_file), dictionary)
        # np.save('{}'.format("models/"+name_file), dictionary)


obj = LearningModel()
answer = str(input("Хотити ли вы прописать путь до папки? Да или Нет. "))
if answer == "Да":
    path = str(input('Введите путь используя слеши (/) до папки кроме последнего: '))
    obj.fit(input_dir=path)
else:
    obj.fit()
