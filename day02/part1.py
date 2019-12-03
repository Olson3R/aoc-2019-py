import numpy as np

def load_data():
  data = np.loadtxt('input.csv', dtype='int32', delimiter=',')
  return data

def main():
  data = load_data()
  data[1] = 12
  data[2] = 2
  index = 0
  while(True):
    cmd = data[index * 4]
    if cmd == 99:
      break
    else:
      in1 = data[index*4 + 1]
      val1 = data[in1]
      in2 = data[index*4 + 2]
      val2 = data[in2]
      out = data[index*4 + 3]
      if cmd == 1:
        data[out] = val1 + val2
      elif cmd == 2:
        data[out] = val1 * val2
    index += 1

  print(data)
  print(data[0])


if __name__ == "__main__":
  main()
