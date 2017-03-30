from LeddarInterface import LeddarInterface
from Position import Position
from Localization import Localization

class LeddarPositionInterface:

  def __init__(self, leddar1_com_port, leddar1_address, leddar2_com_port, leddar2_address, top_post_position, bottom_post_position):
    self.leddar1 = LeddarInterface(leddar1_com_port, leddar1_address)
    self.leddar2 = LeddarInterface(leddar2_com_port, leddar2_address)
    self.localizer = Localization(top_post_position, bottom_post_position)

  def get_position(self):
    dist1 = self.leddar1.get_distance()
    dist2 = self.leddar2.get_distance()
    position = self.localizer.find_position(dist1, dist2)
    return position;
