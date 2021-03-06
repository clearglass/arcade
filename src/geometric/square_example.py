import simplegui, time, random

WINDOW_WIDTH = 500
WINDOW_HEIGHT = WINDOW_WIDTH
GLOBAL_DEFAULT_SQUARE_SIZE = 25

GRID_WIDTH = WINDOW_WIDTH / GLOBAL_DEFAULT_SQUARE_SIZE
GRID_HEIGHT = GRID_WIDTH

DEFAULT_SQUARE_DRAW_ATTRIBUTES = {
    "line_width": 1,
    "line_color": 'Green',
    "fill_color": 'Orange'
}

class Rect:
    
    def rect_coords (length, height, startpos = (0, 0)) :
        x = startpos[0]
        y = startpos[1]
        return [
            (x, y),
            (x, y + height),
            (x + length, y + height),
            (x + length, y)  
        ] 

    class Square:

        SHAPE_ATTRIBUTES = DEFAULT_SQUARE_DRAW_ATTRIBUTES
        SIZE = GLOBAL_DEFAULT_SQUARE_SIZE

        def __init__(self, top_left_pt, size=SIZE, shape_attributes=SHAPE_ATTRIBUTES):
            self.top_left_point = top_left_pt
            self.shape_attributes = shape_attributes
            self.size = size

        def draw_me(self, canvas):
            size = self.size
            (x,y) = self.top_left_point
            (x,y) = x*size, y*size
            canvas.draw_polygon(Rect.rect_coords(size, size, (x,y)),
                self.shape_attributes["line_width"],
                self.shape_attributes["line_color"],
                self.shape_attributes["fill_color"]
            )

grid_list = []
for i in range(GRID_WIDTH):
    for j in range(GRID_WIDTH):
        sqr = Rect.Square((i,j))
        grid_list.append(sqr)
                               
def draw(canvas):
    for sqr in grid_list:
        sqr.draw_me(canvas)
        
frame = simplegui.create_frame("Home", WINDOW_WIDTH, WINDOW_HEIGHT)
frame.set_canvas_background("Silver")
frame.set_draw_handler(draw)
frame.start()        
              
