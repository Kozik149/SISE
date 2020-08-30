from helper import Helper
from queue import Queue

class Bfs:
    def __init__(self, order = ()):
        self.order = order
        self.to_search = Queue().queue
        self.searched = Queue().queue
        self.solution = []
        self.solved = False

    def steps(self, root):
        self.to_search.append(root)
        while (len(self.to_search) > 0 and self.solved is False):
            current_vert = self.to_search.popleft()
            self.searched.append(current_vert)
            if (current_vert.goalCheck()):
                self.solved = True
                self.solution = Helper().track(current_vert)
                break
            current_vert.make_children(self.order)
            for i in range(len(current_vert.children)): #TODO
                if (current_vert.children[i] not in self.to_search and current_vert.children[i] not in self.searched):
                    self.to_search.append(current_vert.children[i])

        visited = len(self.searched)
        processed = len(self.searched) + len(self.to_search)
        deepest = self.solution[0].depth
        return self.solution