"""Line Segment"""
def make_segment(x,y):
    return (x,y)

def start_segment(a,b):
    return a

def end_segment(a,b):
    return b

def mid_point(x,y):
    start=start_segment(x,y)
    end=end_segment(x,y)
    x_new=(start[0]+end[0])/2
    y_new=(start[1]+end[1])/2
    return make_segment(x_new,y_new)
    

