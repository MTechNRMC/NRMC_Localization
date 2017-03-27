#!/usr/bin/python3
import sys, math
from RobotLocalization import RobotLocalization
from LeddarInfoGetter import get_distance
from Position import Position

leddar_com_port = '/dev/ttyUSB0'
leddar_address = 1

def main(argv):
  top_post_position = Position(float(argv[0]), float(argv[1]))
  bottom_post_position = Position(float(argv[2]), float(argv[3]))
  localizer = RobotLocalization(top_post_position, bottom_post_position)
  
  distance = get_distance(leddar_com_port, leddar_address)
  print(distance)
  input('Hit enter to continue')
  # Clear current reading so the distance is correct
  get_distance(leddar_com_port, leddar_address)
  distance2 = get_distance(leddar_com_port, leddar_address)
  print(distance2)
  
  found_position = localizer.find_position(distance, distance2)
  print(found_position)

if __name__ == "__main__":
  main(sys.argv[1:])
