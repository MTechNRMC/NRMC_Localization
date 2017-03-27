import math
from Position import Position

class RobotLocalization:
  def __init__(self, top_post_position, bottom_post_position):
    self.top_post_position = top_post_position
    self.bottom_post_position = bottom_post_position

  def find_position(self, top_distance, bottom_distance):
    separation = self.top_post_position.y - self.bottom_post_position.y
    vertical_offset = ((bottom_distance-top_distance)*(bottom_distance+top_distance)+pow(separation, 2))/(2*separation)
    return Position(math.sqrt(pow(bottom_distance, 2) - pow(vertical_offset, 2)), self.bottom_post_position.y + vertical_offset)
