class RecursiveSolution:
    # This is to figure out how to convert the front part
    # and then we deal with the last char
    def min_edit_distance(self, x, y):
        if x == "":
            return len(y)
        if y == "":
            return len(x)
        
        add_dist = self.min_edit_distance(x, y[:-1]) + 1
        remove_dist = self.min_edit_distance(x[:-1], y) + 1
        change_dist = self.min_edit_distance(x[:-1], y[:-1])
        if x[-1] != y[-1]:
            change_dist += 1
        
        return min(add_dist, remove_dist, change_dist)
    
    # This is to figure out the how to convert the trailing part
    # then we deal with the first char
    def min_edit_distance_2(self, x, y):
        if x == "":
            return len(y)
        if y == "":
            return len(x)
        
        add_dist = self.min_edit_distance_2(x, y[1:]) + 1
        remove_dist = self.min_edit_distance_2(x[1:], y) + 1
        change_dist = self.min_edit_distance(x[1:], y[1:])
        if x[0] != y[0]:
            change_dist += 1
        
        return min(add_dist, remove_dist, change_dist)
