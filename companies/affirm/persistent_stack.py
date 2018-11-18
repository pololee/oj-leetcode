import unittest


class PStack:
    def __init__(self, prev=None, value=None, size=0):
        self.prev = prev
        self.value = value
        self.size = size

    def push(self, x):
        return PStack(self, x, self.size + 1)

    def pop(self):
        return self.prev

    def peek(self):
        return self.value

    def getSize(self):
        return self.size


class PStackTest(unittest.TestCase):
    def testPstack(self):
        pstack = PStack()

        s1 = pstack.push(1)
        s2 = pstack.push(2)
        s3 = s2.push(3)
        tmp = s3.pop()

        self.assertEqual(0, pstack.getSize())
        self.assertEqual(1, s1.getSize())
        self.assertEqual(1, s1.peek())
        self.assertEqual(1, s2.getSize())
        self.assertEqual(2, s2.peek())
        self.assertEqual(3, s3.peek())
        self.assertEqual(2, s3.getSize())
        self.assertEqual(tmp, s2)


if __name__ == "__main__":
    unittest.main()
