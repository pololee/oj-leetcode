class Solution:
    def __init__(self):
        self.pathMap = dict()
        self.callbackMap = dict()
        self.pathMap[''] = 0
    
    def create(self, path, value):
        if path in self.pathMap:
            return False
        
        lastSlashIdx = path.rfind('/')
        if path[:lastSlashIdx] not in self.pathMap:
            return False
        
        self.pathMap[path] = value
        return True
    
    def get(self, path):
        if path not in self.pathMap:
            raise Exception('path not exist')
        
        return self.pathMap[path]
    
    def watch(self, path, callback):
        if path not in self.pathMap:
            raise Exception('path not exist')
        self.callbackMap[path] = callback
    
    def createWithCallback(self, path, value):
        if path in self.pathMap:
            return False
        lastSlashIdx = path.rfind('/')
        if path[:lastSlashIdx] not in self.pathMap:
            return False
        
        self.pathMap[path] = value

        curr = path
        while len(curr) > 0:
            if curr in self.callbackMap:
                self.callbackMap[curr]()
            lastSlashIdx = curr.rfind('/')
            curr = curr[:lastSlashIdx]

        return True

class TrieNode:
    def __init__(self, val):
        self.table = dict()
        self.callback = None
        self.value = val

class FileSystem:
    def __init__(self):
        self.root = TrieNode(0)
    
    def create(self, path, value):
        dirs = self.splitDirs(path)
        node = self.root

        for dirName in dirs[:-1]:
            if dirName not in node.table:
                return False
            node = node.table[dirName]
            if node.callback:
                node.callback()
        
        node.table[dirs[-1]] = TrieNode(value)
        return True
    
    def get(self, path):
        dirs = self.splitDirs(path)
        node = self.root

        for dirName in dirs:
            if dirName not in node.table:
                raise Exception('path not exist')
            node = node.table[dirName]
        
        return node.value
    
    def watch(self, path, callback):
        dirs = self.splitDirs(path)
        node = self.root

        for dirName in dirs:
            if dirName not in node.table:
                raise Exception('path not exist')
            node = node.table[dirName]
        node.callback = callback

    def splitDirs(self, path):
        if not path:
            return []
        return path.split('/')[1:]

def testSolution():
    sol = Solution()
    print(sol.create('/a', 1))
    print(sol.get('/a'))
    print(sol.create('/a/b', 2))
    print(sol.get('/a/b'))
    sol.watch('/a', lambda: print('Wathing /a'))
    sol.watch('/a/b', lambda: print('Wathing /a/b'))
    print(sol.createWithCallback('/a/b/c', 3))

def testFileSystem():
    sol = FileSystem()
    print(sol.create('/a', 1))
    print(sol.get('/a'))
    sol.watch('/a', lambda : print('watching /a'))
    # print(sol.create('/n/bbbbb', 2))
    # print(sol.get('/b'))
    print(sol.create('/a/b', 2))
    print(sol.get('/a/b'))
    sol.watch('/a/b', lambda : print('watching /a/b'))
    print(sol.create('/a/b/c', 3))

if __name__=='__main__':
    testFileSystem()


