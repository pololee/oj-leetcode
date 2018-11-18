import unittest
from expression_evaluation import ExpressionEvaluation

class ExpressionEvaluation2:
    def evaluate(self, s):
        if not s:
            return 0

class ExpressionEvaluation2Test(unittest.TestCase):
    def test_evaluate(self):
        s1 = "( let x ( add 1 2 3 ) : ( mul 4 5 ( add x 1 2 ) ) )"
