from part2 import test_num

def test_test_num():
  assert test_num(112233) == True, "Expected 112233 to pass"
  assert test_num(123444) == False, "Expected 123444 to fail"
  assert test_num(111133) == True, "Expected 111133 to pass"
  print("Passed!")

if __name__ == "__main__":
  test_test_num()
