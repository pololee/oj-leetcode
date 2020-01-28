class Vector2D(object):

    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        # Initialize your data structure here
        self.vec2d = vec2d
        self.row = 0
        self.col = 0

    def next(self):
        # @return {int} a next element
        # Write your code here
        if self.hasNext():
            value = self.vec2d[self.row][self.col]
            self.col += 1
            return value

    def hasNext(self):
        # @return {boolean} true if it has next element
        # or false
        # Write your code here
        while self.row < len(self.vec2d) and self.col >= len(self.vec2d[self.row]):
            self.row += 1
            self.col = 0
        
        return self.row < len(self.vec2d)

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
