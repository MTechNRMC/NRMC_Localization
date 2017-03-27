import minimalmodbus
import time

# Returns distance in meters to whatever the leddar at
# leddar_address with leddar_id is looking at
def get_distance(leddar_com_port, leddar_address):
  minimalmodbus.BAUDRATE=115200
  # Might fix communication errors?
  minimalmodbus.TIMEOUT = 1.0
  
  leddar = minimalmodbus.Instrument(leddar_com_port, leddar_address)
  return leddar.read_register(24, 0, 4)/1000
