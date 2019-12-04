import itertools

def test_num(num):
  str_num = str(num)
  if 2 not in list(map(lambda grp: len(grp), list("".join(g) for k, g in itertools.groupby(str_num)))):
    return False
  return list(str_num) == sorted(str_num)

def process(start, end):
  count = 0
  for num in range(start, end + 1):
    if test_num(num):
      print(f'Num passed {num}')
      count += 1
  print(f'Valid password count {count}')
  return count

def main():
  process(235741, 706948)

if __name__ == "__main__":
  main()
