#!/usr/bin/python3
import sys, math
from RobotLocalization import RobotLocalization
from collections import namedtuple

Position = namedtuple('Position', 'x y')

def main(argv):
  if len(argv) != 6:
    print('Usage: python3 RobotLocalization <top post x> <top post y> <bottom post x> <bottom post y> <real x> <real y>')
    return
  top_post_position = Position(float(argv[0]), float(argv[1]))
  bottom_post_position = Position(float(argv[2]), float(argv[3]))
  real_position = Position(float(argv[4]), float(argv[5]))
  localizer = RobotLocalization(top_post_position, bottom_post_position)
  top_distance = math.sqrt(pow(top_post_position.x - real_position.x, 2) + pow(top_post_position.y - real_position.y, 2))
  bottom_distance = math.sqrt(pow(bottom_post_position.x - real_position.x, 2) + pow(bottom_post_position.y - real_position.y, 2))
  found_position = localizer.find_position(top_distance, bottom_distance)
  print('Found position: {:.20f}, {:.20f}; Real position: {:.20f}, {:.20f}\n'.format(found_position.x, found_position.y, real_position.x, real_position.y))

if __name__ == "__main__":
  main(sys.argv[1:])
