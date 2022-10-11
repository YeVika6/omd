from typing import List


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


def main():
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()  # инициализируем объект
    count_matrix = vectorizer.fit_transform(corpus)  # метод fit transform вернул count matrix
    print(vectorizer.get_feature_names())
    # Out: ['crock', 'pot', 'pasta', 'never', 'boil', 'again', 'pomodoro',
    #       'fresh', 'ingredients', 'parmesan', 'to', 'taste']
    print(count_matrix)
    # Out: [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]


if __name__ == '__main__':
    main()
