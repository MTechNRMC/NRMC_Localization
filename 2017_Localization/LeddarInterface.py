import minimalmodbus
import time

class LeddarInterface:
  # 8.8 Hz
  LEDDAR_FREQUENCY = 1/8.8
  cached_read_time = 0
  cached_distance = -1

  def __init__(self, leddar_com_port, leddar_address):
    minimalmodbus.BAUDRATE=115200
    self.leddar = minimalmodbus.Instrument(leddar_com_port, leddar_address)

  def read_distance(self):
    try:
      distance = self.leddar.read_register(24, 0, 4)/1000
      time = ((self.leddar.read_register(21, 0, 4) << 16) + self.leddar.read_register(20, 0, 4))/1000
      if time == self.cached_read_time:
        return False
      self.cached_distance = distance
      self.cached_read_time = time
      return True
    except OSError:
      return False

  # Returns distance in meters to whatever the leddar is looking at
  def get_distance(self):
    while not self.read_distance():
      time.sleep(self.LEDDAR_FREQUENCY)
    return self.cached_distance
