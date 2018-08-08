class ServerManager:
    def __init__(self):
        self.table = dict()

    def allocate(self, string):
        answer = ''
        if string in self.table:
            size = len(self.table[string])
            answer = '{}{}'.format(string, size + 1)
            self.table[string].append(answer)
        else:
            answer = '{}{}'.format(string, 1)
            self.table[string] = [answer]

        return answer

    def deallocate(self, string):
        if string in self.table:
            self.table[string].pop()


def main():
    manager = ServerManager()
    print(manager.allocate('apibox'))
    print(manager.allocate('apibox'))
    manager.deallocate('apibox')
    print(manager.allocate('apibox'))

if __name__ == '__main__':
    main()
