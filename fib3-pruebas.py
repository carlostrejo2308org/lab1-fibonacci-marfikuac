import program

class FibUnitTest:
  def __init__(self, name, input, expectedOutput):
    self.name = name
    self.input = input
    self.expectedOutput = expectedOutput

#0 1 2 3 4 5 6  7  8  9 10 11  12  13  14
#0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
tests = [
  FibUnitTest(1, 2, "0 1 1"),
  FibUnitTest(2, 3, "0 1 1 2"),
  FibUnitTest(3, 7, "0 1 1 2 3 5 8 13"),
  FibUnitTest(4, 14, "0 1 1 2 3 5 8 13 21 34 55 89 144 233 377"),
  FibUnitTest(5, 11, "0 1 1 2 3 5 8 13 21 34 55 89"),
  FibUnitTest(7, 1, "0 1"),
  FibUnitTest(8, 0, "0"),
  # FibUnitTest(6, -1, "0 1"),
]

for test in tests:
  iterPassed = program.fib_iter(test.input) == test.expectedOutput
  recurPassed = program.fib_recur(test.input) == test.expectedOutput
  print(f"Test {test.name}: Iter. ({iterPassed}); Rec. ({recurPassed})")
