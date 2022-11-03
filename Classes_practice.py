from typing import List
import math


class CountVectorizer():
    '''Создали класс'''

    def __init__(self):
        pass

    def fit_transform(self, raw_documents: List[str]) -> List[List[int]]:
        '''Возвращает терм-документную матрицу https://ru.wikipedia.org/wiki/Терм-документная_матрица '''
        words = set()
        for sentence in raw_documents:
            sentence_words = sentence.split()
            for word in sentence_words:
                words.add(word.lower())
        self.words = list(words)  # self.words - это атрибут

        index_words = {}
        for index in range(len(self.words)):
            index_words[self.words[index]] = index  # дикт из ключей-слов и валью-индексов

        count_matrix = []
        for sentence in raw_documents:
            sentence_words = sentence.split()
            count_vector = [0] * len(self.words)
            for word in sentence_words:
                word = word.lower()
                index = index_words[word]
                count_vector[index] += 1
            count_matrix.append(count_vector)
        return count_matrix

    def get_feature_names(self) -> List[str]:
        '''Возвращет все уникальные слова'''
        return self.words


# Task 1
def tf_transform(matr: List[List[int]]) -> List[List[float]]:
    freq_list = []
    sum_word = 0
    for one_list in matr:
        sum_word = sum(one_list)
        sentence_tf = []
        for number in one_list:
            freq = number/sum_word
            sentence_tf.append(freq)
        freq_list.append(sentence_tf)
    return freq_list


# Task 2 (var 1)
def idf_transform_1(matr: List[List[int]]) -> List[float]:
    len_matr = len(matr)
    idf = []
    colm_len = len(matr[0])
    for i in range(colm_len):  # i - index of word
        counter = 0
        for doc in matr:
            if doc[i] != 0:
                counter += 1
        idf.append(math.log((len_matr + 1) / (counter + 1)) + 1)
    return idf


# Task 2 (var 2)
def idf_transform_2(matr: List[List[int]]) -> List[float]:
    result = []
    docs_num = len(matr)
    for row in zip(*matr):
        result.append(math.log((docs_num + 1) / (sum([int(num > 0) for num in row]) + 1)) + 1)
    return result


# Task 2.1 (как коротка записать цикл: comprehension и lambda)
def count_pos(matr: List[int]) -> int:
    counter = 0

    #  for elem in matr:
    #    if elem > 0 :
    #        counter += 1

    #  counter = sum([(elem > 0) for elem in matr])

    #  counter = sum(filter(lambda x: x > 0, matr))

    counter = sum(list(filter(bool, matr)))
    return counter


# Task 3
class TfidfTransformer:

    def tf_transform(self, matr: List[List[int]]) -> List[List[float]]:
        freq_list = []
        sum_word = 0
        for one_list in matr:
            sum_word = sum(one_list)
            sentence_tf = []
            for number in one_list:
                freq = number/sum_word
                sentence_tf.append(freq)
            freq_list.append(sentence_tf)
        return freq_list

    @staticmethod #  статику не нужен self
    def idf_transform(matr: List[List[int]]) -> List[float]:
        result = []
        docs_num = len(matr)
        for row in zip(*matr):
            result.append(math.log((docs_num + 1) / (sum([int(num > 0) for num in row]) + 1)) + 1)
        return result

    def fit_transform(self, matr: List[List[int]]) -> List[List[float]]:
        tf = self.tf_transform(matr)
        idf = self.idf_transform(matr)
        tf_idf = [[x * y for x, y in zip(row, idf)] for row in tf]
        return tf_idf


# Task 5 (наследование или композиция(?)) Композиция - это когда в классе использвуем объект другого класса
class TfidfVectorizer(CountVectorizer):  # наследуемся от CountVectorizerа
    def __init__(self):
        super().__init__()  #  вызывает родительский init
        self.transformer = TfidfTransformer()

    def fit_transform(self, raw_documents: List[str]):
        matrix = super().fit_transform(raw_documents)  # super получает объект родительского класса
        return self.transformer.fit_transform(matrix)


# Task 5.1 Попробуем то же, но без наследования
class TfidfVectorizerV2:
    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.transform = TfidfTransformer()

    def fit_transform(self, raw_documents: List[str]):
        matrix = self.vectorizer.fit_transform(raw_documents)  # super получает объект родительского класса
        return self.transform.fit_transform(matrix)

    def get_feature_names(self):
        return self.vectorizer.get_feature_names()


def main():
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()  # инициализируем объект
    count_matrix = vectorizer.fit_transform(corpus)  # метод fit transform вернул count matrix
    matrix = [1, 0, 1, 0, 1, 1, 1, 0]
    print(vectorizer.get_feature_names())
    # : ['crock', 'pot', 'pasta', 'never', 'boil', 'again', 'pomodoro',
    #       'fresh', 'ingredients', 'parmesan', 'to', 'taste']
    print(count_matrix)
    count_matrix = [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]

    # print('\n tf_transform result:')
    # print(tf_transform(count_matrix))

    # print('\n idf_transform_1 result:')
    # print(idf_transform_1(count_matrix))

    # print('\n idf_transform_2 result:')
    # print(idf_transform_2(count_matrix))

    # print('\n count_pos result:')
    # print(count_pos(matrix))

    # transformer = TfidfTransformer()
    # tf_idf = transformer.fit_transform_new(count_matrix)
    # print(tf_idf)

    # idf_1 = transformer.idf_transform(count_matrix)
    # idf_2 = TfidfTransformer.idf_transform(count_matrix)
    # print('\n tf_idf result:')
    # print(tf_idf)

    tf_idvectorizer = TfidfVectorizer()  # тут вызывается init
    print('\n Tfidf_class result:')
    print(tf_idvectorizer.fit_transform(corpus))
    # print(tf_idvectorizer.get_feature_names(corpus))

    tf_idvectorizer = TfidfVectorizerV2()  # тут вызывается init
    print('\n TfidfV2_class result:')
    print(tf_idvectorizer.fit_transform(corpus))
    # print(tf_idvectorizer.get_feature_names(corpus))


if __name__ == '__main__':
    main()
