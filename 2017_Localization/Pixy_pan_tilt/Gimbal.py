from ctypes import *

from pixy_constants import *

class Gimbal ():
  _fields_ = [ ("position", c_uint),
               ("first_update", bool),
               ("previous_error", c_uint),
               ("proportional_gain", c_uint),
               ("derivative_gain", c_uint) ]

  def __init__(self, start_position, proportional_gain, derivative_gain):
    self.position          = start_position
    self.proportional_gain = proportional_gain
    self.derivative_gain   = derivative_gain
    self.previous_error    = 0
    self.first_update      = True
    self.scan_direction    = 1

  def limit_position(self):
    if self.position > PIXY_RCS_MAX_POS:
      self.position = PIXY_RCS_MAX_POS
      return True
    elif self.position < PIXY_RCS_MIN_POS:
      self.position = PIXY_RCS_MIN_POS
      return True
    return False
      
  def scan(self):
    self.position += 25 * self.scan_direction
    if self.limit_position():
      self.scan_direction *= -1

  def update(self, error):
    if not self.first_update:
      error_delta = error - self.previous_error
      P_gain      = self.proportional_gain;
      D_gain      = self.derivative_gain;

      # Using the proportional and derivative gain for the gimbal
      # calculate the change to the position
      velocity = (error * P_gain + error_delta * D_gain) / 1024;
      self.position += velocity;
      self.limit_position()
    else:
      self.first_update = False

    self.previous_error = error
