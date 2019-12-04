import re

def test_num(num):
  str_num = str(num)
  if re.search("(1{2}|2{2}|3{2}|4{2}|5{2}|6{2}|7{2}|8{2}|9{2}|0{2})", str_num) == None:
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
