import sys


class SimpleTextQuery:
    def textQueirs(self, sentences, phrases):
        """
        :type sentences: list[str]
        :type phrases: list[list[str]]
        :rtype list[int]
        """
        tables = []
        for s_sent in sentences:
            tables.append(self.sentence_to_word_count(s_sent))

        for p_phrase in phrases:
            result = []

            for i in range(len(tables)):
                occurence = self.phrase_occurence(p_phrase, tables[i])
                for _ in range(occurence):
                    result.append(str(i))
            if not result:
                print('-1')
            else:
                print(' '.join(result))

    def sentence_to_word_count(self, sentence):
        words = sentence.split(' ')
        table = dict()

        for word in words:
            if word in table:
                table[word] += 1
            else:
                table[word] = 1

        return table

    def phrase_occurence(self, phrase, table):
        occurence = sys.maxsize

        for word in phrase:
            if word not in table:
                return 0
            else:
                occurence = min(occurence, table[word])

        return occurence


def main():
    sentences = ['bob and alice like to text each other',
                 'bob does not like to ski',
                 'alice likes to ski']
    phrases = [['bob', 'alice'],
               ['alice'],
               ['like']]
    query = SimpleTextQuery()
    query.textQueirs(sentences, phrases)

    sentences = ['it go will away', 'go do art', 'what to will east']
    phrases = [['it', 'will'], ['go', 'east', 'will'], ['will']]
    query.textQueirs(sentences, phrases)


if __name__ == '__main__':
    main()
