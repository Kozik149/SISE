from bfs import Bfs
from vertex import Vertex
from program import WorkWithFile
import time
import sys

if __name__ == '__main__':
    algorithm = sys.argv[1]
    option = sys.argv[2]
    input_file = sys.argv[3]
    solution_file = sys.argv[4]
    statistic_file = sys.argv[5]
    work_with_file = WorkWithFile()
    init_vertex = Vertex(work_with_file.readBoard(input_file))
    visited = None
    processed = None
    deepest = None

    start_time = time.process_time()

    switch = {
        'bfs': Bfs(option).steps(init_vertex)
    }

    end_time = time.process_time()

    solution = switch.get(algorithm.lower())

    to_solution_file = work_with_file.prepare_solution(solution)
    to_stats_file = work_with_file.prepareStats(solution, start_time, end_time)

    work_with_file.writeToFile(solution_file, to_solution_file)
    work_with_file.writeToFile(statistic_file, to_stats_file)

