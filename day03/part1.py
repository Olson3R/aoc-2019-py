from shapely.geometry import LineString, Point

def parse_point_instruction(point_str):
  dir = point_str[0]
  length = int(point_str[1:])
  return (dir, length)

def parse_line_instructions(line_str):
  parts = line_str.split(',')
  line_instructions = list(map(parse_point_instruction, parts))
  return line_instructions

def find_next_point(point, line_instruction):
  if line_instruction[0] == 'U':
    return (point[0], point[1] + line_instruction[1])
  elif line_instruction[0] == 'D':
    return (point[0], point[1] - line_instruction[1])
  elif line_instruction[0] == 'L':
    return (point[0] - line_instruction[1], point[1])
  elif line_instruction[0] == 'R':
    return (point[0] + line_instruction[1], point[1])

def process(file):
  f = open(file, 'r')
  line_strs = f.readlines()
  lines = []
  for line_str in line_strs:
    current_point = (0, 0)
    line_instructions = parse_line_instructions(line_str)
    line = [current_point]
    for line_instruction in line_instructions:
      current_point = find_next_point(current_point, line_instruction)
      line.append(current_point)
    lines.append(LineString(line))
  intersections = []
  for i in range(len(lines) - 1):
    for j in range(i + 1, len(lines)):
      intersections.extend(lines[i].intersection(lines[j]))
  intersections.remove(Point(0,0))
  print(f'Intersections {list(map(lambda i: i.wkt, intersections))}')
  min_distance = min(map(lambda i: abs(i.x) + abs(i.y), intersections))
  print(f'Intersections Min Distance {min_distance}')
  return min_distance

def main():
  process('input.csv')

if __name__ == "__main__":
  main()
