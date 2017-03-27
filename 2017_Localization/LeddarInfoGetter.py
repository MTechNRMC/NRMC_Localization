import minimalmodbus
import time

# Returns distance in meters to whatever the leddar at
# leddar_address with leddar_id is looking at
def get_distance(leddar_address, leddar_id):
  minimalmodbus.BAUDRATE=115200
  leddar = minimalmodbus.Instrument(leddar_address, leddar_id)
  #print(testLeddar.read_register(22, 0, 4)/256)
  measurement = leddar.read_register(24, 0, 4)/1000
