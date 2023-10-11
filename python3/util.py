import time


class Problem:
    def __init__(self):
        self.problem_id = None

    def solve(self):
        pass

    def run(self):
        start = time.time_ns()
        answer = self.solve()
        end = time.time_ns()

        print(f"Problem {self.problem_id}\n - Returned: {answer}\n - Time Elapsed: {(end-start)/1000000:6f}ms")








