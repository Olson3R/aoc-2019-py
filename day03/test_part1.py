from part1 import process

def test_process():
  assert process("input-test1.csv") == 6.0, "Invalid value for test1, should be 6"
  assert process("input-test2.csv") == 159.0, "Invalid value for test2, should be 159"
  assert process("input-test3.csv") == 135.0, "Invalid value for test3, should be 135"
  print("Passed!")

if __name__ == "__main__":
  test_process()
