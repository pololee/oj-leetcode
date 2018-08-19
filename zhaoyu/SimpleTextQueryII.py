import sys
import collections


class SimpleTextQueryII:
    def textQueirs(self, sentences, phrases):
        """
        :type sentences: list[str]
        :type phrases: list[list[str]]
        :rtype list[int]
        """
        table = self.wordAppearence(sentences)
        for p_ph in phrases:
            query_result = self.query(p_ph, table)
            if query_result:
                print(' '.join([str(i) for i in query_result]))
            else:
                print('-1')


    def wordAppearence(self, sentences):
        # return a map
        # key: string
        # value: sentence idx which contains this string
        table = collections.defaultdict(list)
        size = len(sentences)
        for i in range(size):
            for word in sentences[i].split(' '):
                table[word].append(i)
        return table
    
    def query(self, phrase, table):
        result = None
        for word in phrase.split(' '):
            if word in table:
                if result is None:
                    result = list(table[word])
                else:
                    result = self.retain_all(result, table[word])
            else:
                return []
        
        return result
    
    def retain_all(self, retain, other):
        other = set(other)
        result = []
        for x in retain:
            if x in other:
                result.append(x)
        return result

def main():
    sentences = ['bob and alice like to text each other',
                 'bob does not like to ski',
                 'alice likes to ski']
    phrases = ['bob alice',
               'alice',
               'like']
    query = SimpleTextQueryII()
    query.textQueirs(sentences, phrases)

    sentences = ['it go will away', 'go do art', 'what to will east']
    phrases = ['it will', 'go east will', 'will']
    query.textQueirs(sentences, phrases)

if __name__ == '__main__':
    main()
