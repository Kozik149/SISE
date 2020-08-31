from helper import Helper
from program import WorkWithFile
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
            current_vertex = self.to_search.popleft()
            self.searched.append(current_vertex)
            if (current_vertex.goalCheck()):
                self.solved = True
                self.solution = Helper().track(current_vertex)
                break
            current_vertex.make_children(self.order)
            for i in range(len(current_vertex.children)): #TODO
                if (current_vertex.children[i] not in self.to_search and current_vertex.children[i] not in self.searched):
                    self.to_search.append(current_vertex.children[i])

        WorkWithFile.visited = len(self.searched)
        WorkWithFile.processed = len(self.searched) + len(self.to_search)
        WorkWithFile.deepest = self.solution[0].depth
        return self.solution