from part2 import calculate_fuel

def test_calculate_fuel():
  assert calculate_fuel(12) == 2, "Invalid value for mass 12, should be 2"
  assert calculate_fuel(14) == 2, "Invalid value for mass 14, should be 2"
  assert calculate_fuel(1969) == 966, "Invalid value for mass 1969, should be 966"
  assert calculate_fuel(100756) == 50346, "Invalid value for mass 100756, should be 50346"
  print("Passed!")

if __name__ == "__main__":
  test_calculate_fuel()
