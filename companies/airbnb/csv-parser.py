import unittest


class Solution:
    def parseLine(self, line):
        size = len(line)

        result = []
        inQuote = False
        buffer = []

        i = 0
        while i < size:
            if inQuote:
                if line[i] == '"':
                    # inQuote
                    # if double "" => " else inQuote finish
                    if i + 1 < size and line[i+1] == '"':
                        buffer.append('"')
                        i += 1
                    else:
                        inQuote = False
                else:
                    buffer.append(line[i])
            else:
                if line[i] == '"':
                    inQuote = True
                elif line[i] == ',':
                    result.append(''.join(buffer))
                    buffer = []
                else:
                    buffer.append(line[i])

            i += 1

        if len(buffer) > 0:
            result.append(''.join(buffer))

        return '|'.join(result)


class TestParser(unittest.TestCase):
    parser = Solution()

    def testParseLineSimple(self):
        test = "John,Smith,john.smith@gmail.com,Los Angeles,1"
        expected = "John|Smith|john.smith@gmail.com|Los Angeles|1"
        self.assertEqual(expected, self.parser.parseLine(test))

    def testParseLineWithQuote(self):
        test = "Jane,Roberts,janer@msn.com,\"San Francisco, CA\",0"
        expected = "Jane|Roberts|janer@msn.com|San Francisco, CA|0"
        self.assertEqual(expected, self.parser.parseLine(test))
    
    def testParseLineWithDoubleQuotes(self):
        test = "\"Alexandra \"\"Alex\"\"\",Menendez,alex.menendez@gmail.com,Miami,1"
        expected = "Alexandra \"Alex\"|Menendez|alex.menendez@gmail.com|Miami|1"
        self.assertEqual(expected, self.parser.parseLine(test))
    
    def testParseLineWithStupidQuotes(self):
        test = "\"\"\"Alexandra Alex\"\"\""
        expected = "\"Alexandra Alex\""
        self.assertEqual(expected, self.parser.parseLine(test))


if __name__ == '__main__':
    unittest.main()
