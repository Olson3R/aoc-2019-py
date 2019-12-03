import numpy as np

def load_data():
  data = np.loadtxt('input.csv', dtype='int32', delimiter=',')
  return data

def find_noun_verb(data):
  for noun in range(0, 100):
    for verb in range(0, 100):
      d = np.array(data, copy=True)
      d[1] = noun
      d[2] = verb
      index = 0
      while(True):
        cmd = d[index * 4]
        if cmd == 99:
          break
        else:
          try:
            in1 = d[index*4 + 1]
            val1 = d[in1]
            in2 = d[index*4 + 2]
            val2 = d[in2]
            out = d[index*4 + 3]
            if cmd == 1:
              d[out] = val1 + val2
            elif cmd == 2:
              d[out] = val1 * val2
          except:
            break
        index += 1

      print(f'noun={noun}, verb={verb}, total={d[0]}')
      if d[0] == 19690720:
        return noun, verb

def main():
  data = load_data()

  noun, verb = find_noun_verb(data)
  print(f'noun={noun}, verb={verb}, total={100*noun + verb}')


if __name__ == "__main__":
  main()
