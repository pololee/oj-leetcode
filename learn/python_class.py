class TestClass(object):
    def sayYes(self):
        return "Yes"

    def sayNo(self):
        return "No"

    def saySth(self):
        print(self.sayYes())
        print(self.sayNo())

if __name__ == "__main__":
    test = TestClass()
    test.saySth()

