# This file is part of Pixy CMUcam5 or "Pixy" for short
#
# All Pixy source code is provided under the terms of the
# GNU General Public License v2 (http://www.gnu.org/licenses/gpl-2.0.html).
# Those wishing to use Pixy source code, software and/or
# technologies under different licensing terms should contact us at
# cmucam@cs.cmu.edu. Such licensing terms are available for
# all portions of the Pixy codebase presented here.
#
# Original author: Leimon (2015)

# System imports
import sys
import signal
import time

# SWIG imports
from pixy import *

# Application imports
from Gimbal import Gimbal
from Blocks import Blocks
from pixy_constants import *


def handle_SIGINT(signal, frame):
  sys.exit(0)

def main():
  print('Pixy target tracking started')

  # Initialize Pixy Interpreter thread #
  pixy_init_status = pixy_init()
  if pixy_init_status != 0:
    pixy_error(pixy_init_status)
    sys.exit(2)

  # Initialize gimbals
  pan_gimbal  = Gimbal(PIXY_RCS_CENTER_POS, PAN_PROPORTIONAL_GAIN, PAN_DERIVATIVE_GAIN)
  tilt_gimbal = Gimbal(PIXY_RCS_CENTER_POS, TILT_PROPORTIONAL_GAIN, TILT_DERIVATIVE_GAIN)

  # Initialize block
  block       = Block()

  signal.signal(signal.SIGINT, handle_SIGINT)
  while True:
    # Get a block
    count = pixy_get_blocks(BLOCK_BUFFER_SIZE, block)
    print("Looking for target...")
    while count == 0:
      pan_gimbal.scan()
      tilt_gimbal.scan()
      
      pixy_rcs_set_position(PIXY_RCS_PAN_CHANNEL, pan_gimbal.position)
      pixy_rcs_set_position(PIXY_RCS_TILT_CHANNEL, tilt_gimbal.position)
      time.sleep(.05)
      count = pixy_get_blocks(BLOCK_BUFFER_SIZE, block)
    print("Position at {}, {}; block seen at {}, {}".format(
           tilt_gimbal.position, pan_gimbal.position,
           block.x, block.y))

    # Calculate the difference between Pixy's center of view and target
    pan_error  = PIXY_Y_CENTER - block.y
    tilt_error = PIXY_X_CENTER - block.x

    # Apply correction to try to center on target
    pan_gimbal.update(pan_error)
    tilt_gimbal.update(tilt_error)
    set_position_result = pixy_rcs_set_position(PIXY_RCS_PAN_CHANNEL, pan_gimbal.position)
    set_position_result = pixy_rcs_set_position(PIXY_RCS_TILT_CHANNEL, tilt_gimbal.position)

    if set_position_result < 0:
      pixy_error(set_position_result)
      sys.exit(2)

    # Limit speed a bit
    time.sleep(.05)
  pixy_close()

if __name__ == "__main__":
  main()
