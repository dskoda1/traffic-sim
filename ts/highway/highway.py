import pygame

from ts.highway import config

WHITE = (255, 255, 255)
YELLOW = (243, 211, 0)

class HighwayDrawer(object):

    MAX_LANE = config.LANE_EDGES - 1

    def __init__(self, screen):
        self.screen = screen

    def draw(self):
        height = self.screen.get_height()
        width = self.screen.get_width()
        dash_segment = int(width / config.SEGMENT_WIDTH)
        lanes = []
        # Get the top edge of the highway, roughly halfway on the screen
        current_edge = height / 2 - 10
        self.top_edge = current_edge

        for x in range(config.LANE_EDGES):
            # Set the color of the lane, also the dashed-ness
            if x == 0 or x == config.LANE_EDGES - 1:
                color = YELLOW
                dashed = False
            else:
                color = WHITE
                dashed = True
            if dashed:
                for y in range(config.SEGMENT_WIDTH):
                    if y % 2 == 0:
                        start = y * dash_segment
                        # Create two points - one at start/height
                        # Another at start+segment/height
                        lanes.append((start, current_edge))
                        lanes.append((start + dash_segment, current_edge))
                        pygame.draw.lines(self.screen, color, False, lanes, 1)
                        lanes = []
            else:
                lanes.append((0, current_edge))
                lanes.append((width, current_edge))
                pygame.draw.lines(self.screen, color, False, lanes, 1)
                lanes = []
            # Dashed or not, add to the edge
            current_edge += config.LANE_HEIGHT

    def lane(self, height):
        lane_top = self.top_edge
        for i, x in enumerate(range(config.LANE_EDGES)):
            if height > lane_top and height < lane_top + config.LANE_HEIGHT:
                return i
            else:
                lane_top += config.LANE_HEIGHT
