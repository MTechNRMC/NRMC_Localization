#!/usr/bin/python3
import sys, math
from Localization import Localization
from LeddarInterface import LeddarInterface
from Position import Position

leddar_com_port = '/dev/ttyUSB0'
leddar_address = 1

def main(argv):
  top_post_position = Position(float(argv[0]), float(argv[1]))
  bottom_post_position = Position(float(argv[2]), float(argv[3]))
  localizer = Localization(top_post_position, bottom_post_position)
  leddar_interface = LeddarInterface(leddar_com_port, leddar_address)
  distances = [None] * 10
  for i in range(0, 10):
    distances[i] = leddar_interface.get_distance()
    print(distances[i])
    print(leddar_interface.cached_read_time)
  found_position = localizer.find_position(distances[0], distances[1])
  print(found_position)

if __name__ == "__main__":
  main(sys.argv[1:])
