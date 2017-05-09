#!/usr/bin/python3
import sys
import math
from Localization import Localization
from LeddarInterface import LeddarInterface
from LeddarPositionInterface import LeddarPositionInterface
from Position import Position

leddar1_com_port = '/dev/ttyUSB0'
leddar1_address = 1
leddar2_com_port = '/dev/ttyUSB1'
leddar2_address = 1


def main(argv):
  top_post_position = Position(float(argv[0]), float(argv[1]))
  bottom_post_position = Position(float(argv[2]), float(argv[3]))
  positioner = LeddarPositionInterface(leddar1_com_port, leddar1_address,
                                      leddar2_com_port, leddar2_address,
                                      top_post_position, bottom_post_position)

  for i in range(0, 1000):
    print("At {0}".format(positioner.get_position()))


if __name__ == "__main__":
  main(sys.argv[1:])
