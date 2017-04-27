import pygame

WHITE = (255, 255, 255)
YELLOW = (243, 211, 0)
LANES = 8

class HighwayDrawer(object):

    def __init__(self, screen):
        self.screen = screen

    def draw(self):
        height = self.screen.get_height()
        width = self.screen.get_width()
        dash_segment = int(width / 40)
        lanes = []
        lane_height = height / 2 + 10
        for x in range(LANES):
            # Set the color of the lane, also the dashed-ness
            if x == 0 or x == LANES - 1:
                color = YELLOW
                dashed = False
            else:
                color = WHITE
                dashed = True
            if dashed:
                for y in range(40):
                    if y % 2 == 0:
                        start = y * dash_segment
                        # Create two points - one at start/height
                        # Another at start+segment/height
                        lanes.append((start, lane_height))
                        lanes.append((start + dash_segment, lane_height))
                        pygame.draw.lines(self.screen, color, False, lanes, 1)
                        lanes = []
                lane_height += 20
            else:
                lanes.append((0, lane_height))
                lanes.append((width, lane_height))
                pygame.draw.lines(self.screen, color, False, lanes, 1)
                lanes = []
                lane_height += 20
