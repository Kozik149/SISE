
class WorkWithFile:
    visited = None
    processed = None
    deepest = None

    def prepare_solution(self, solution):
        to_solution_file = []
        if (len(solution) == 0):
            to_solution_file.append("-1")
        else:
            first_line_solution = len(solution) - 1
            second_line_solution = []
            to_solution_file.append(first_line_solution)
            for i in range(len(solution) - 2, -1, -1):
                second_line_solution.append(solution[i].moveLetter)
            to_solution_file.append(second_line_solution)
            print(to_solution_file)
        return to_solution_file

    def prepare_stats(self, solution, startTime, endTime):
        to_stats_file = []
        if (len(solution) == 0):
            first_line_stats = -1
        else:
            first_line_stats = len(solution) - 1
            to_stats_file.append(first_line_stats)
            to_stats_file.append(self.visited)
            to_stats_file.append(self.processed)
            to_stats_file.append(self.deepest)
            to_stats_file.append(endTime - startTime)
            return to_stats_file

    def read_board(self, inputFile):
        try:
            with open(inputFile) as file:
                read_data = file.read()
                return list(map(int, read_data.split())) # or do it by list comprehension
        except FileExistsError as fee_error:
            return fee_error

    def write_to_file(self, filename, finishedBoard):
        try:
            with open(filename, 'w') as file:
                write_data = file.write(str(finishedBoard))
                return True
        except FileExistsError as fee_error:
            return fee_error
