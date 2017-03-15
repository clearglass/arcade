import simplegui, time, random

class Constants:
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = WINDOW_WIDTH
    GLOBAL_CIRCLE_DIAMETER = 25

    GRID_WIDTH = WINDOW_WIDTH / 25
    GRID_HEIGHT = GRID_WIDTH
class Circle:

    DEFAULT_CIRCLE_DRAW_ATTRIBUTES = {
        "line_width": 2,
        "line_color": 'Blue',
        "fill_color": 'Aqua'
    }    
    
    DIAMETER = Constants.GLOBAL_CIRCLE_DIAMETER
    RADIUS = DIAMETER / 2
    SHAPE_ATTRIBUTES = DEFAULT_CIRCLE_DRAW_ATTRIBUTES

    def __init__(self, center, radius=RADIUS, shape_attributes=SHAPE_ATTRIBUTES):
        self.radius = radius
        self.center_point = (center[0]*self.DIAMETER + self.RADIUS, center[1]*self.DIAMETER + self.RADIUS)
        self.shape_attributes = shape_attributes

    def draw_me(self, canvas):
        canvas.draw_circle(
            self.center_point,
            self.radius,
            self.shape_attributes["line_width"],
            self.shape_attributes["fill_color"],
            self.shape_attributes["fill_color"]   
        )

circ_list = []
for i in range(Constants.GRID_WIDTH):
    for j in range(Constants.GRID_WIDTH):
        circ_list.append(Circle((i,j)))
                               
def draw(canvas):
    for circ in circ_list:
        circ.draw_me(canvas)

class Graphics:
    WINDOW_WIDTH = Constants.WINDOW_WIDTH
    WINDOW_HEIGHT = Constants.WINDOW_HEIGHT
    
    def __init__(self, width=WINDOW_WIDTH, height=WINDOW_HEIGHT):
        frame = simplegui.create_frame("Home", width, height)
        frame.set_canvas_background("Silver")
        frame.set_draw_handler(draw)
        frame.start()                     
Graphics()
