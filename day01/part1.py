import math

def calculate_fuel(mass):
  return math.floor(mass / 3) - 2

def main():
  f = open("input.txt", "r")
  lines = f.readlines()
  total_fuel = 0
  for line in lines:
    mass = int(line)
    fuel = calculate_fuel(mass)
    print("{mass} = {fuel}".format(mass=mass, fuel=fuel))
    total_fuel += fuel
  print("Total fuel = {total_fuel}".format(total_fuel=total_fuel))


if __name__ == "__main__":
  main()
