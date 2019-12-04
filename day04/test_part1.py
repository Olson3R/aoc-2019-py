from part1 import test_num

def test_test_num():
  assert test_num(111111) == True, "Expected 111111 to pass"
  assert test_num(223450) == False, "Expected 223450 to fail"
  assert test_num(123789) == False, "Expected 123789 to fail"
  print("Passed!")

if __name__ == "__main__":
  test_test_num()
