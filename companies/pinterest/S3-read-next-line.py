import unittest
from collections import deque


class S3Reader:
    def __init__(self, stream):
        self.stream = stream
        self.pos = 0

    def next(self):
        # read next 8 character
        if self.pos >= len(self.stream):
            return ""

        nextPos = min(self.pos + 8, len(self.stream))
        output = self.stream[self.pos:nextPos]
        self.pos = nextPos
        return output


class S3ReaderWrapper:
    def __init__(self, stream):
        self.s3Reader = S3Reader(stream)
        self.queue = deque()

    def nextLine(self):
        output = []
        newLine = False
        eof = False
        while not eof and not newLine:
            next8 = self.s3Reader.next()
            if next8:
                for ch in next8:
                    self.queue.append(ch)
                if "\n" in next8:
                    newLine = True
            else:
                eof = True
        while self.queue and self.queue[0] != "\n":
            output.append(self.queue.popleft())

        if self.queue:
            self.queue.popleft()  # \n
            output.append("\n")
        return ''.join(output)


class S3ReaderTest(unittest.TestCase):
    def testNext(self):
        reader = S3Reader("This is the first line.\nThis is the second line.")
        self.assertEqual('This is ', reader.next())
        self.assertEqual('the firs', reader.next())
        self.assertEqual('t line.\n', reader.next())
        self.assertEqual('This is ', reader.next())
        self.assertEqual('the seco', reader.next())
        self.assertEqual('nd line.', reader.next())
        self.assertEqual('', reader.next())

    def testNextLine(self):
        reader = S3ReaderWrapper(
            "This is the first line.\nThis is the second line."
        )
        self.assertEqual("This is the first line.\n", reader.nextLine())
        self.assertEqual("This is the second line.", reader.nextLine())


if __name__ == '__main__':
    unittest.main()
