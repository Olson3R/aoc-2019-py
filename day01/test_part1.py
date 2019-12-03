from part1 import calculate_fuel

def test_calculate_fuel():
  assert calculate_fuel(12) == 2, "Invalid value for mass 12, should be 2"
  assert calculate_fuel(14) == 2, "Invalid value for mass 14, should be 2"
  assert calculate_fuel(1969) == 654, "Invalid value for mass 1969, should be 654"
  assert calculate_fuel(100756) == 33583, "Invalid value for mass 100756, should be 33583"
  print("Passed!")

if __name__ == "__main__":
  test_calculate_fuel()
