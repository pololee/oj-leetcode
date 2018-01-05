class RecursiveSolution:
    def add_binary(self, a, b):
        if len(a) == 0:
            return b
        if len(b) == 0:
            return a

        if a[-1] == '1' and b[-1] == '1':
            return self.add_binary(self.add_binary(a[:-1], b[:-1]), '1') + '0'

        if a[-1] == '0' and b[-1] == '0':
            return self.add_binary(a[:-1], b[:-1]) + '0'
        else:
            return self.add_binary(a[:-1], b[:-1]) + '1'

def main():
    sol = RecursiveSolution()
    print(sol.add_binary('11', '1'))

if __name__ == '__main__':
    main()

