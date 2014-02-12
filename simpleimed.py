from graphics import *
from random import *
from math import *
from time import sleep

# Begin by setting up the edit and view windows.
editor_bkg = color_rgb(40,40,40)
editor = GraphWin("Edit Image",500,400)
editor.setCoords(0,0,50,40)
editor.setBackground(editor_bkg)

img = Image(Point(0,0), "bilde.gif")
width = img.getWidth()
height = img.getHeight()
img.anchor = Point(width / 2, height / 2) # centres the image
win = GraphWin("Image Display", width, height)
img.draw(win)

# Two methods for the editor: one to draw, the other to operate buttons.

def draw_controls(window):
    """Draws control buttons and their names in a 50x40 input window.
    Returns a list of rectangles (buttons.)"""

    lft_mgn  = 5  # left and right margin values (mgn2 for +/- buttons)
    lft_mgn2 = 15 
    rht_mgn  = 45
    rht_mgn2 = 30
    shrt_bt  = 5  # length of short and long buttons
    long_bt  = 15
    bt_hght  = 4  # values for height and "bottom" of buttons
    bt_btom  = 4.9

    # left panel commands in the editor
    bright_lobox = Rectangle(Point(lft_mgn2,7*bt_btom+1),
                             Point(lft_mgn2+5,7*bt_btom+1+bt_hght))
    
    contra_lobox = Rectangle(Point(lft_mgn2,6*bt_btom+1),
                             Point(lft_mgn2+5,6*bt_btom+1+bt_hght))
    
    vtflip_box = Rectangle(Point(lft_mgn,5*bt_btom+1),
                           Point(lft_mgn+long_bt,5*bt_btom+1+bt_hght))
    
    mirror_box = Rectangle(Point(lft_mgn,4*bt_btom+1),
                           Point(lft_mgn+long_bt,4*bt_btom+1+bt_hght))
    
    greysc_box = Rectangle(Point(lft_mgn,3*bt_btom+1),
                           Point(lft_mgn+long_bt,3*bt_btom+1+bt_hght))
    
    sepia_box  = Rectangle(Point(lft_mgn,2*bt_btom+1),
                           Point(lft_mgn+long_bt,2*bt_btom+1+bt_hght))

    pixela_box = Rectangle(Point(lft_mgn,bt_btom+1),
                           Point(lft_mgn+long_bt,bt_btom+1+bt_hght))

    popart_box = Rectangle(Point(lft_mgn,1),
                           Point(lft_mgn+long_bt,1+bt_hght))

    # right panel commands
    bright_hibox = Rectangle(Point(rht_mgn2,7*bt_btom+1),
                         Point(rht_mgn2+5,7*bt_btom+1+bt_hght))

    contra_hibox = Rectangle(Point(rht_mgn2,6*bt_btom+1),
                         Point(rht_mgn2+5,6*bt_btom+1+bt_hght))

    rounds_box = Rectangle(Point(rht_mgn-long_bt,5*bt_btom+1),
                         Point(rht_mgn,5*bt_btom+1+bt_hght))
    
    newspp_box = Rectangle(Point(rht_mgn-long_bt,4*bt_btom+1),
                         Point(rht_mgn,4*bt_btom+1+bt_hght))

    raingl_box = Rectangle(Point(rht_mgn-long_bt,3*bt_btom+1),
                         Point(rht_mgn,3*bt_btom+1+bt_hght))

    vignet_box = Rectangle(Point(rht_mgn-long_bt,2*bt_btom+1),
                         Point(rht_mgn,2*bt_btom+1+bt_hght))

    framer_box = Rectangle(Point(rht_mgn-long_bt,bt_btom+1),
                         Point(rht_mgn,bt_btom+1+bt_hght))

    tiny_moth_box = Rectangle(Point(rht_mgn-long_bt,1),
                         Point(rht_mgn,1+bt_hght))

    # centre panel commands
    u_p1_y = greysc_box.getP1().getY()
    u_p1_x = sepia_box.getP2().getX()+1
    u_p2_y = vtflip_box.getP2().getY()
    u_p2_x = rounds_box.getP1().getX()-1
    undo_box = Rectangle(Point(u_p1_x,u_p1_y),Point(u_p2_x,u_p2_y))

    s_p1_y = popart_box.getP1().getY()
    s_p1_x = popart_box.getP2().getX()+1
    s_p2_y = vignet_box.getP2().getY()
    s_p2_x = vignet_box.getP1().getX()-1    
    save_box = Rectangle(Point(s_p1_x,s_p1_y),Point(s_p2_x,s_p2_y))

    # exit button, bottom right
    exit_box = Rectangle(Point(rht_mgn+1,1),
                         Point(rht_mgn+4.4,1+bt_hght))

    # list of all buttons 
    button_list = [bright_lobox,contra_lobox,vtflip_box,mirror_box,
                   greysc_box,sepia_box,pixela_box,popart_box,
                   tiny_moth_box,framer_box,vignet_box,raingl_box,
                   newspp_box,rounds_box,contra_hibox,bright_hibox,
                   undo_box,save_box,exit_box]

    # buttons for features (apart from exit), not effects:
    feature_list = [tiny_moth_box,undo_box,save_box]
    

    # produces text for buttons
    bright_minus = bright_lobox.getCenter()
    bright_centr = bright_minus.getY()
    contra_minus = contra_lobox.getCenter()
    contra_centr = contra_minus.getY()
    vtflip_centr = vtflip_box.getCenter()
    mirror_centr = mirror_box.getCenter()
    greysc_centr = greysc_box.getCenter()
    sepia_centr  = sepia_box.getCenter()
    pixela_centr = pixela_box.getCenter()
    popart_centr = popart_box.getCenter()
    bright_plus  = bright_hibox.getCenter()
    contra_plus  = contra_hibox.getCenter()
    rounds_centr = rounds_box.getCenter()
    newspp_centr = newspp_box.getCenter()
    raingl_centr = raingl_box.getCenter()
    vignet_centr = vignet_box.getCenter()
    tiny_moth_centr = tiny_moth_box.getCenter()
    framer_centr = framer_box.getCenter()
    undo_centr = undo_box.getCenter()
    save_centr = save_box.getCenter()
    exit_centr = exit_box.getCenter()
    
    bright_lo = Text(bright_minus,"-")
    contra_lo = Text(contra_minus,"-")
    flip = Text(vtflip_centr,"flip")
    mirror = Text(mirror_centr,"mirror")
    greyscale = Text(greysc_centr,"greyscale")
    sepia  = Text(sepia_centr,"sepia")
    pixelate = Text(pixela_centr,"pixelate")
    popart = Text(popart_centr,"pop-art")

    brightness = Text(Point(25,bright_centr),"brightness")
    contrast = Text(Point(25,contra_centr),"contrast")

    bright_hi = Text(bright_plus,"+")
    contra_hi = Text(contra_plus,"+")
    rounds = Text(rounds_centr,"rounds")
    newspaper = Text(newspp_centr,"newspaper")
    rainglow  = Text(raingl_centr,"rainglow")
    vignette  = Text(vignet_centr,"vignette")
    tiny_moth = Text(tiny_moth_centr,"tiny moth")
    framer = Text(framer_centr,"choose frame")

    undo = Text(undo_centr,"undo\nor\nredo")
    save = Text(save_centr,"save")
    ext = Text(exit_centr,"exit")

    # list of names (text for buttons)
    name_list = [bright_lo,bright_hi,contra_lo,contra_hi,flip,
                 mirror,greyscale,sepia,pixelate,popart,brightness,
                 contrast,rounds,newspaper,rainglow,vignette,tiny_moth,
                 framer,undo,save,ext]

    # finally draws buttons, then draws text
    button_outline = color_rgb(30,30,30)
    for button in button_list:
        button.setOutline(button_outline)
        if button in feature_list:
            button.setFill(color_rgb(60,60,60))
        if button == exit_box:
            button.setFill(color_rgb(150,0,0))
        button.draw(window)

    for name in name_list:
        name.setFill("AliceBlue")
        name.setFace("helvetica")
        name.setSize(16)
        if name == ext:
            name.setSize(12)
        name.draw(window)

    return button_list

def is_inside(point,button):
    """Takes in a point (click) and a button and returns True iff the
    point is inside the given button."""
    x_pt = point.getX()
    y_pt = point.getY()
    x_lo = button.getP1().getX()
    y_lo = button.getP1().getY()
    x_hi = button.getP2().getX()
    y_hi = button.getP2().getY()
    return (x_lo < x_pt < x_hi) and (y_lo < y_pt < y_hi)


# Next: effect methods (general helpers, then more central methods.)
def fix_rgb(r,g,b):
    """Makes sure r,g,b is in [0,255] range."""
    if r < 0:
        r = 0
    elif r > 255:
        r = 255
    if g < 0:
        g = 0
    elif g > 255:
        g = 255
    if b < 0:
        b = 0
    elif b > 255:
        b = 255
        
    return r,g,b

def create_matrix(img):
    """Creates a two-dimensional array (matrix) with the r,g,b values
    for img."""
    width  = img.getWidth()
    height = img.getHeight()
    matrix = [[0,0,0]*height for x in range(width)] #what?
    for x in range(width):
        for y in range(height):
            matrix[x][y] = img.getPixel(x,y)
    return matrix

def matrix_to_img(matrix,img):
    """Updates img to reflect the r,g,b values of the given matrix."""
    width  = img.getWidth()
    height = img.getHeight()
    for x in range(width):
        for y in range(height):
            r,g,b = matrix[x][y]
            img.setPixel(x, y, color_rgb(r,g,b))

def to_grey(r,g,b):
    """Calculates effective luminance."""
    luminance = (r * 0.3) + (g * 0.59) + (b * 0.11)
    return luminance

# Central image effect methods.
def increase_brightness(img):
    """Increases the image's brightness by one step."""
    step = 10
    width = img.getWidth()
    height = img.getHeight()
    for x in range(width):
        for y in range(height):
            r,g,b = img.getPixel(x,y)
            r_new = (r + step)
            g_new = (g + step)
            b_new = (b + step)
            r2,g2,b2 = fix_rgb(r_new,g_new,b_new)
            img.setPixel(x,y,color_rgb(r2,g2,b2))

def decrease_brightness(img):
    """Decreases the image's brightness by one step."""
    step = 10
    width = img.getWidth()
    height = img.getHeight()
    for x in range(width):
        for y in range(height):
            r,g,b = img.getPixel(x,y)
            r_new = (r - step)
            g_new = (g - step)
            b_new = (b - step)
            r2,g2,b2 = fix_rgb(r_new,g_new,b_new)
            img.setPixel(x,y,color_rgb(r2,g2,b2))

def increase_contrast(img):
    """Increases the image's contrast by one step."""
    step = 20
    width = img.getWidth()
    height = img.getHeight()
    for x in range(width):
        for y in range(height):
            r,g,b = img.getPixel(x,y)
            if r <= 127:
                r_new = r - step + (r*step/127)
            else:
                r_new = r + step*(abs(b-128) / 127)
            if g <= 127:
                g_new = g - step + (g*step/127)
            else:
                g_new = g + step*(abs(b-128) / 127)
            if b <= 127:
                b_new = b - step + (b*step/127)
            else:
                b_new = b + step*(abs(b-128) / 127)

            r2,g2,b2 = fix_rgb(r_new,g_new,b_new)
            img.setPixel(x,y,color_rgb(r2,g2,b2))

def decrease_contrast(img):
    """Decreases the image's contrast by one step."""
    step = 20
    width = img.getWidth()
    height = img.getHeight()
    for x in range(width):
        for y in range(height):
            r,g,b = img.getPixel(x,y)
            if r <= 127:
                r_new = r + step - (r*step/127)
            else:
                r_new = r - step*(abs(b-128) / 127)
            if g <= 127:
                g_new = g + step - (g*step/127)
            else:
                g_new = g - step*(abs(b-128) / 127)
            if b <= 127:
                b_new = b + step - (b*step/127)
            else:
                b_new = b - step*(abs(b-128) / 127)

            r2,g2,b2 = fix_rgb(r_new,g_new,b_new)
            img.setPixel(x,y,color_rgb(r2,g2,b2))

def vertical_flip(img):
    """Flips the image vertically."""
    width = img.getWidth()
    height = img.getHeight()
    
    for x in range(width):
        point_set = []
        
        for y in range(height):
            r,g,b = img.getPixel(x,y)
            point_set.append((r,g,b))

        flipped_y = point_set[::-1]
        counter = 0

        for y in range(height):
            (r,g,b) = flipped_y[counter]
            img.setPixel(x,y,color_rgb(r,g,b))
            counter = counter + 1

def mirror(img):
    """Flips the image horizontally, producing a mirror image."""
    width = img.getWidth()
    height = img.getHeight()

    for y in range(height):
        point_set = []

        for x in range(width):
            r,g,b = img.getPixel(x,y)
            point_set.append((r,g,b))

        flipped_x = point_set[::-1]
        counter = 0

        for x in range(width):
            (r,g,b) = flipped_x[counter]
            img.setPixel(x,y,color_rgb(r,g,b))
            counter = counter + 1

def greyscale(img):
    """Converts the image to greyscale."""
    width = img.getWidth()
    height = img.getHeight()

    for x in range(width):
        for y in range(height):
            r,g,b = img.getPixel(x,y)
            lumin = to_grey(r,g,b)
            img.setPixel(x,y,color_rgb(lumin,lumin,lumin))

def sepia(img):
    """Just like a sepia print!"""
    width = img.getWidth()
    height = img.getHeight()

    sepia_value = 20

    for x in range(width):
        for y in range(height):
            r,g,b = img.getPixel(x,y)
            r_raw = g_raw = b_raw = to_grey(r,g,b)
            r_raw = r_raw + (sepia_value * 2)
            b_raw = b_raw - sepia_value
            r_new,g_new,b_new = fix_rgb(r_raw,g_raw,b_raw)
            img.setPixel(x,y,color_rgb(r_new,g_new,b_new))

def pixelate(img):
    """Pixelates the image."""
    width = img.getWidth()
    height = img.getHeight()

    pixel_size = 7

    for x in range(width):
        for y in range(height):
            if y%pixel_size == 0:
                r,g,b = img.getPixel(x,y)
            else:
                img.setPixel(x,y,color_rgb(r,g,b))

    for y in range(height):
        for x in range(width):
            if x%pixel_size == 0:
                r,g,b = img.getPixel(x,y)
            else:
                img.setPixel(x,y,color_rgb(r,g,b))

def pop_art(img):
    """Produces Warholesque colouring with four, two-tone panels."""
    tone1 = (127,255,212) # aqua
    tone2 = (255,69,0)    # orange-red
    tone3 = (255,225,0)   # yellow
    tone4 = (186,85,211)  # orchid

    width = img.getWidth()
    height = img.getHeight()
    halfx = round(width/2)
    halfy = round(height/2)

    
    for x in range(width):
        for y in range(height):
            if x <= halfx and y <= halfy:
                r,g,b = img.getPixel(x,y)
                nr,ng,nb = poptone(tone1,r,g,b)
                img.setPixel(x,y,color_rgb(nr,ng,nb))
                
            elif x > halfx and y <= halfy:
                r,g,b = img.getPixel(x,y)
                nr,ng,nb = poptone(tone2,r,g,b)
                img.setPixel(x,y,color_rgb(nr,ng,nb))                

            elif x <= halfx and y > halfy:
                r,g,b = img.getPixel(x,y)
                nr,ng,nb = poptone(tone3,r,g,b)
                img.setPixel(x,y,color_rgb(nr,ng,nb))

            elif x > halfx and y > halfy:
                r,g,b = img.getPixel(x,y)
                nr,ng,nb = poptone(tone4,r,g,b)
                img.setPixel(x,y,color_rgb(nr,ng,nb))                

def poptone(tone,r,g,b):
    """Adjust r,g,b values for a two-tone image (black and tone.)"""
    (tr,tg,tb) = tone

    lum = to_grey(r,g,b)

    new_r = lum*(tr/255)
    new_g = lum*(tg/255)
    new_b = lum*(tb/255)

    r,g,b = fix_rgb(new_r,new_g,new_b)
    return r,g,b


def choose_frame(img):
    """Gives user opportunity to choose a frame colour."""
    border_tint = input("Pick a color (e.g., MidnightBlue): ")
    draw_frame(img,border_tint)

def draw_frame(img,border_tint):
    """Draws a border around the image."""
    width = img.getWidth()
    height = img.getHeight()

    border_width = 10

    for x in range(width):
        for y in range(height):
            if y < border_width or y > (height-border_width):
                img.setPixel(x,y,border_tint)
            elif x < border_width or x > (width-border_width): 
                img.setPixel(x,y,border_tint)

def rounds(img):
    """Produces a mosaic-like effect: circles on a black background."""
    width  = img.getWidth()
    height = img.getHeight()
    
    radius = 5
    diameter = 2 * radius
    bkg = color_rgb(0,0,0)

    for x in range(width):
        for y in range(height):
            near_x = diameter * round(x/diameter) 
            near_y = diameter * round(y/diameter) 
            distance = sqrt((near_x-x)**2 + (near_y-y)**2)            
            if (distance < radius and
                near_x < width and near_y < height):
                r,g,b = img.getPixel(near_x,near_y)
                img.setPixel(x,y,color_rgb(r,g,b))
            else:
                img.setPixel(x,y,bkg)

def newspaper(img):
    """Produces a halftone effect."""
    width  = img.getWidth()
    height = img.getHeight()
    centerspace = 7
    bkg  = color_rgb(240,240,240) # background colour (newspaper)
    frg = color_rgb(20,20,20)     # foreground colour (ink)
    
    for x in range(width):
        for y in range(height):
            near_x = centerspace * round(x/centerspace) 
            near_y = centerspace * round(y/centerspace)
            distance = sqrt((near_x-x)**2 + (near_y-y)**2)
            
            if near_x < width and near_y < height:
                r,g,b = img.getPixel(near_x,near_y)
                if distance < halftone(r,g,b):
                    img.setPixel(x,y,frg)
                else:
                    img.setPixel(x,y,bkg)

def halftone(r,g,b):
    """Determines the size of radius for halftone circles. For use with
    the 'newspaper' effect."""
    size = 75
    
    luminance = to_grey(r,g,b)
    radius = abs(luminance-254)/size
    return radius
   
def rainglow(img):
    """Produces glow, mostly at the top and at the right."""
    width = img.getWidth()
    height = img.getHeight()

    factor = 20
    
    glowr1 = 50
    glowg1 = 205
    glowb1 = 50
    
    glowr2 = 255
    glowg2 = 215
    glowb2 = 0

    for x in range(width):
        for y in range(height):
            r,g,b = img.getPixel(x,y)
            new_r = round((y*r + factor*glowr1)/(y+1))
            new_g = round((y*g + factor*glowg1)/(y+1))
            new_b = round((y*b + factor*glowb1)/(y+1))
            nr,ng,nb = fix_rgb(new_r,new_g,new_b)
            img.setPixel(x,y,color_rgb(nr,ng,nb))

    for y in range(height):
        for x in range(width):
            r,g,b = img.getPixel(x,y)
            new_r = round((x*r + factor*glowr2)/(x+1) + (x-y)/factor)
            new_g = round((x*g + factor*glowg2)/(x+1) + (x-y)/factor)
            new_b = round((x*b + factor*glowb2)/(x+1) +
                                                  1.8*((x-y)/factor))
            nr,ng,nb = fix_rgb(new_r,new_g,new_b)
            img.setPixel(x,y,color_rgb(nr,ng,nb))

def vignette(img):
    """Produces a vignette effect."""
    width = img.getWidth()
    height = img.getHeight()
    centre_x = round(width/2)
    centre_y = round(height/2)
    
    intensity = 100

    for x in range(width):
        n = 1
        for y in range(height):
            r,g,b = img.getPixel(x,y)
            new_r = round(r-intensity**((abs(centre_x-x)/width)+
                                        (abs(centre_y-y)/height)))
            new_g = round(g-intensity**((abs(centre_x-x)/width)+
                                        (abs(centre_y-y)/height)))
            new_b = round(b-intensity**((abs(centre_x-x)/width)+
                                        (abs(centre_y-y)/height)))
            nr,ng,nb = fix_rgb(new_r,new_g,new_b)
            img.setPixel(x,y,color_rgb(nr,ng,nb))
            n = n + 1

# Features that aren't effects (tiny moth, save, undo)

def tiny_moth(img):
    """tiny_moth: it's not a bug, it's a feature! Draws a 'moth' which
    moves around the screen randomly. Since it is attracted to light, it
    will flutter around until it finds a bright spot. Note that the moth
    is NOT part of the image, so it will not appear in saved copies of
    img and it cannot be removed using the UNDO function."""

    moth = Polygon(Point(10,20),Point(15,5),Point(25,15))
    moth.setFill("RosyBrown")
    moth_x = moth_y = 15 # more or less the centre of the moth.
    
    print("Click anywhere on the image to place the bug.")
    click = win.getMouse()
    click_x = click.getX()
    click_y = click.getY()
    go_x = click_x - moth_x # dist. between click and moth's location 
    go_y = click_y - moth_y

    moth.move(go_x,go_y)
    moth.draw(win)

    current_location = click

    while bright_spot(current_location) == False:
        moth.undraw()
        moth_x = current_location.getX()
        moth_y = current_location.getY()
                
        x = randint(0,width-1)
        y = randint(0,height-1)

        go_x = x - moth_x
        go_y = y - moth_y

        moth.move(go_x,go_y)
        moth.draw(win)

        current_location = Point(x,y)
        sleep(0.5)

def bright_spot(location):
    """Returns True iff the location (a Point) is brightly lit.
    For use with tiny moth."""
    bright_value = 210
    
    x = location.getX()
    y = location.getY()
    r,g,b = img.getPixel(x,y)
    return to_grey(r,g,b) > bright_value

def save(img):
    """Saves a copy of the image as a .ppm file with a name of your
    choice."""
    filename = input("Pick a filename (without extension): ")
    filename = filename + ".ppm"
    img.save(filename)

def undo(img,backups):
    """Always brings img back to its last state: using once undoes, and
    using twice redoes."""
    width  = img.getWidth()
    height = img.getHeight()

    previous_version = backups[-2]
    matrix_backup = create_matrix(previous_version)

    matrix_to_img(matrix_backup,img)

# Main mathod.
def main():
    """Image editor: allows the user to use a variety of effects to
    modify img. Has fifteen image-editing effects and four non-effect
    features (tiny moth,undo,save,exit)."""
    
    welcome_message = "Welcome to the image editor! \n\
Click buttons in the 'Edit Image' window to effect modifications \n\
to the displayed image. Note that some effects and features ('tiny \n\
moth', 'save', 'undo', and 'choose frame') make use of this shell."
    print(welcome_message)
    
    editor_buttons = draw_controls(editor)
    
    original = img.clone()
    backups = [original]
    exiting = False    
    
    while exiting == False:
        point = editor.getMouse()
        
        if is_inside(point,editor_buttons[0]):
            decrease_brightness(img)
        elif is_inside(point,editor_buttons[1]):
            decrease_contrast(img)
        elif is_inside(point,editor_buttons[2]):
            vertical_flip(img)
        elif is_inside(point,editor_buttons[3]):
            mirror(img)
        elif is_inside(point,editor_buttons[4]):
            greyscale(img)
        elif is_inside(point,editor_buttons[5]):
            sepia(img)
        elif is_inside(point,editor_buttons[6]):
            pixelate(img)
        elif is_inside(point,editor_buttons[7]):
            pop_art(img)
        elif is_inside(point,editor_buttons[8]):
            tiny_moth(img)
        elif is_inside(point,editor_buttons[9]):
            choose_frame(img)
        elif is_inside(point,editor_buttons[10]):
            vignette(img)
        elif is_inside(point,editor_buttons[11]):
            rainglow(img)
        elif is_inside(point,editor_buttons[12]):
            newspaper(img)
        elif is_inside(point,editor_buttons[13]):
            rounds(img)
        elif is_inside(point,editor_buttons[14]):
            increase_contrast(img)
        elif is_inside(point,editor_buttons[15]):
            increase_brightness(img)
        elif is_inside(point,editor_buttons[16]):
            undo(img,backups)
        elif is_inside(point,editor_buttons[17]):
            save(img)
        elif is_inside(point,editor_buttons[18]):
            exiting = True

        new_copy = img.clone()
        backups.append(new_copy)
        win.update()
        
    win.close()
    editor.close()

# runs the editor.
main()
