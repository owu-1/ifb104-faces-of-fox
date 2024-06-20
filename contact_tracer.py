
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item for QUT's teaching unit
#  IFB104, "Building IT Systems", Semester 1, 2021.  By submitting
#  this code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
student_number = 0 # put your student number here as an integer
student_name   = "" # put your name here as a character string
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  CONTACT TRACER
#
#  This assessment item tests your skills at processing data stored in
#  lists, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function, "visualise".  You are required to
#  complete this function so that when the program runs it fills
#  a grid with various symbols, using data stored in a list to
#  determine which symbols to draw and where.  See the various
#  "client requirements" in Blackboard for full details.
#
#  Note that this assessable assignment is in multiple parts,
#  simulating incremental release of instructions by the client.
#  This single template file will be used for all parts and you will
#  submit your final solution as a single Python 3 file only, whether
#  or not you complete all requirements for the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should NOT change
# any of the code in this section.
#

# Import standard Python modules needed to complete this assignment.
# You should not need to use any other modules for your solution.
# In particular, your solution must NOT rely on any non-standard
# Python modules that need to be downloaded and installed separately,
# because the markers will not have access to such modules.
from turtle import *
from math import *
from random import *
from sys import exit as abort
from os.path import isfile

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values unless
# instructed.
cell_size = 100 # pixels (default is 100)
grid_width = 9 # squares (default is 9)
grid_height = 7 # squares (default is 7)
x_margin = cell_size * 2.75 # pixels, the size of the margin left/right of the grid
y_margin = cell_size // 2 # pixels, the size of the margin below/above the grid
window_height = grid_height * cell_size + y_margin * 2
window_width = grid_width * cell_size + x_margin * 2
small_font = ('Arial', cell_size // 5, 'normal') # font for the coords
big_font = ('Arial', cell_size // 4, 'normal') # font for any other text

# Validity checks on grid size - do not change this code
assert cell_size >= 80, 'Cells must be at least 80x80 pixels in size'
assert grid_width >= 8, 'Grid must be at least 8 squares wide'
assert grid_height >= 6, 'Grid must be at least 6 squares high'

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  Do NOT change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas(bg_colour = 'light grey',
                          line_colour = 'slate grey',
                          draw_grid = True,
                          label_spaces = True): # NO! DON'T TOUCH THIS!
    
    # Set up the drawing canvas with enough space for the grid and
    # spaces on either side
    setup(window_width, window_height)
    bgcolor(bg_colour)

    # Draw as quickly as possible
    tracer(False)

    # Get ready to draw the grid
    penup()
    color(line_colour)
    width(2)

    # Determine the left-bottom coords of the grid
    left_edge = -(grid_width * cell_size) // 2 
    bottom_edge = -(grid_height * cell_size) // 2

    # Optionally draw the grid
    if draw_grid:

        # Draw the horizontal grid lines
        setheading(0) # face east
        for line_no in range(0, grid_height + 1):
            penup()
            goto(left_edge, bottom_edge + line_no * cell_size)
            pendown()
            forward(grid_width * cell_size)
            
        # Draw the vertical grid lines
        setheading(90) # face north
        for line_no in range(0, grid_width + 1):
            penup()
            goto(left_edge + line_no * cell_size, bottom_edge)
            pendown()
            forward(grid_height * cell_size)

        # Draw each of the labels on the x axis
        penup()
        y_offset = cell_size // 3 # pixels
        for x_label in range(0, grid_width):
            goto(left_edge + (x_label * cell_size) + (cell_size // 2), bottom_edge - y_offset)
            write(chr(x_label + ord('a')), align = 'center', font = small_font)

        # Draw each of the labels on the y axis
        penup()
        x_offset, y_offset = cell_size // 10, cell_size // 10 # pixels
        for y_label in range(0, grid_height):
            goto(left_edge - x_offset, bottom_edge + (y_label * cell_size) + (cell_size // 2) - y_offset)
            write(str(y_label + 1), align = 'right', font = small_font)

        # Mark centre coordinate (0, 0)
        home()
        dot(cell_size // 6)

    # Optionally mark the blank spaces ... NO! YOU CAN'T CHANGE ANY OF THIS CODE!
    if label_spaces:
        # Left side
        goto(-((grid_width + 1.5) * cell_size) // 2, -(cell_size // 3))
        write('This space\nintentionally\nleft blank', align = 'right', font = big_font)    
        # Right side
        goto(((grid_width + 1.5) * cell_size) // 2, -(cell_size // 3))
        write('This space\nintentionally\nleft blank', align = 'left', font = big_font)    

    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas to the operating
# system.  By default the cursor (turtle) is hidden when the
# program ends.  Call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    tracer(True) # ensure any drawing still in progress is displayed
    if hide_cursor:
        hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "visualise" function.  ALL of your solution code
#  must appear in this area.  Do NOT put any of your code in other
#  parts of the program and do NOT change any of the provided code
#  except as allowed in the main program below.
#

from abc import ABC, abstractmethod


def offset_y(offset):
    # Set turtle y-axis to an offset from the turtle's current y-axis position
    sety(ycor() + offset)


def offset_x(offset):
    # Set turtle x-axis to an offset from the turtle's current x-axis position
    setx(xcor() + offset)


def offset_cord(x_base, y_base, x_offset, y_offset):
    # Set turtle to offsets from the supplied position
    goto(
        x_base + x_offset,
        y_base + y_offset
    )


class Draw:
    # Draw context manager to ease the process of drawing and filling
    def __init__(self, fill_colour=None, pen_colour="black", pen_size=1):
        self.fill_colour = fill_colour
        if self.fill_colour:
            fillcolor(fill_colour)
        pencolor(pen_colour)
        pensize(pen_size)

    def __enter__(self):
        pendown()
        if self.fill_colour:
            begin_fill()

    def __exit__(self, exc_type, exc_value, traceback):
        if self.fill_colour:
            end_fill()
        penup()


class Drawing(ABC):
    # Template class for drawings
    SIZE = 100  # Square length
    BACKGROUND_COLOUR = "#bcd3f6"

    # Retrive the drawing functions via a method
    @abstractmethod
    def get_layer_functions(self):
        pass

    def __init__(self, variations):
        self.variations = variations
        self.layer_functions = self.get_layer_functions()

    # Draw the drawing's variation
    def draw(self, variation_index, grid_coordinate=None):
        # If no grid coordinate suppplied, use current turtle position
        # x, y refers to the bottom left of the box
        if grid_coordinate:
            (x, y) = grid_coordinate.to_turtle_coordinate()
        else:
            (x, y) = position()
        self.x = x
        self.y = y
        # Draw box
        goto(self.x, self.y)
        with Draw(fill_colour=self.BACKGROUND_COLOUR):
            setheading(0)
            for i in range(4):
                forward(Drawing.SIZE)
                left(90)
        # Draw drawing
        variation = self.variations[variation_index]
        for layer_name, layer_function_data in self.layer_functions.items():
            # Function data is a dict if there are multiple variations of layer
            if isinstance(layer_function_data, dict):
                # Retrive wanted variation
                layer_variation_name = variation[layer_name]
                if layer_variation_name is False:
                    continue  # Skip drawing variation
                layer_draw_function = layer_function_data[layer_variation_name]
            else:
                # Default layer function
                layer_draw_function = layer_function_data

            layer_draw_function()  # Call the layer draw function

        goto(x, y)  # Go back to bottom left corner

    def goto(self, x, y):
        # Sets x, y based from the bottom left corner of the cell
        # 0, 0 refers to the bottom left
        offset_cord(
            x_base=self.x,
            y_base=self.y,
            x_offset=x,
            y_offset=y
        )


class Write:
    # Allow consistent font type and size
    TITLE_FONT_SIZE = 20
    DESCRIPTION_FONT_SIZE = 10

    @staticmethod
    def write(text, font_size):
        write(text, font=("Arial", font_size, "normal"))


class Legend:
    DESCRIPTION_GAP = 20

    def __init__(self, title, x, y, length):
        self.title = title
        # x, y refers to the top left of the first (top) legend box
        self.x = x
        self.y = y
        self.length = length  # Length does not encapsulate the title

    # Draws a legend of drawing variations
    def draw(self, drawing):
        # Setup for amount of drawing variations
        drawing_variations = drawing.variations
        drawing_variation_count = len(drawing_variations)
        space_used_for_drawings = drawing_variation_count * Drawing.SIZE
        if self.length < space_used_for_drawings:
            print("Legend length of", self.length, "is too small")
            return

        gap_between_drawings = \
            (self.length - space_used_for_drawings) // drawing_variation_count
        gap_between_description_and_next_drawing = \
            (gap_between_drawings - self.DESCRIPTION_GAP) + Drawing.SIZE

        # Drawing legend
        goto(self.x, self.y)
        Write.write(self.title, Write.TITLE_FONT_SIZE)  # Write title
        # Draw the drawings
        offset_y(-Drawing.SIZE)  # Go to the bottom left to draw
        for (variation_index, variation_data) in drawing_variations.items():
            drawing.draw(variation_index)  # Draw drawing
            offset_y(-self.DESCRIPTION_GAP)  # Go to below drawing
            description = f"{variation_index}. {variation_data['name']}"
            # Write description
            Write.write(description, Write.DESCRIPTION_FONT_SIZE)
            # Go to start of next drawing
            offset_y(-gap_between_description_and_next_drawing)    


class Grid:
    def __init__(self):
        # Record what variations were drawn onto the grid
        # A cell has None representing an empty cell
        # or a variation index e.g. 'A' representing a drawn cell
        self.cells = [
            [None for number in Grid_Coordinate.LETTERS]
            for letter in range(Grid_Coordinate.NUMBERS)
        ]

    # Draws drawing variations onto a grid based on supplied data
    def draw(self, drawing, action_data):
        # Handle start action
        start_data = action_data.pop(0)  # Start action is always at index 0
        self.current_cord = Grid_Coordinate(
            letter=start_data[1],
            number=start_data[2]
        )
        self.current_variation = start_data[3]
        self.fill_cell(drawing)
        # Handle Change/Move actions
        for action_text, action_value in action_data:
            if action_text == "Change":
                self.current_variation = action_value
                self.fill_cell(drawing)
            # Action must be a move action
            elif action_value == 0:
                # Client demo does not redraw a cell when no movement occurs
                continue
            else:
                orientation = action_text
                move_count = action_value
                for i in range(move_count):
                    self.current_cord.move(orientation)
                    self.fill_cell(drawing)
        return self.current_variation

    # Fills a cell with the current drawing variation
    def fill_cell(self, drawing):
        drawing.draw(self.current_variation, self.current_cord)
        letter = self.current_cord.letter
        number = self.current_cord.number
        self.cells[number][letter] = self.current_variation


class Grid_Coordinate:
    # Simplifies the use of grid coordinates
    LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']  # X axis
    NUMBERS = 7  # Y axis
    # Minimum coordinate refers to A1 (bottom left coordinate)
    MIN_X = -(len(LETTERS) * Drawing.SIZE) // 2
    MIN_Y = -(NUMBERS * Drawing.SIZE) // 2

    def __init__(self, letter, number):
        # Letter and number are stored as integers
        # where A1 represents the letter 0 and number 0
        self.letter = self.LETTERS.index(letter)
        self.number = number - 1

    # Converts grid coordinate to turtle coordinate
    def to_turtle_coordinate(self):
        x = Grid_Coordinate.MIN_X + (self.letter * Drawing.SIZE)
        y = Grid_Coordinate.MIN_Y + (self.number * Drawing.SIZE)
        return (x, y)

    # Move the coordinate by one cell based on the orientation
    def move(self, orientation):
        if orientation == "North":
            self.number += 1
        elif orientation == "East":
            self.letter += 1
        elif orientation == "South":
            self.number -= 1
        elif orientation == "West":
            self.letter -= 1


class Fox(Drawing):
    # A drawing of the character Fox, a dog from the Housepets comic
    HEAD_RADIUS = 30  # DO NOT MODIFY - Layers are hardcoded to the head
    INNER_FUR_COLOUR = "#ebe7fe"
    OUTER_FUR_COLOUR = "#bfc2d3"
    OUTER_EYE_COLOUR = "#ada3fc"

    def get_layer_functions(self):
        # Map option names to functions and define the layer draw order
        LAYER_FUNCTIONS = {
            "right_ear": self.right_ear,
            "neck_and_shoulders": self.neck_and_shoulders,
            "neck_wear": {
                "neckerchief": self.neckerchief,
                "bow_tie": self.bow_tie,
                "collar": self.collar,
            },
            "head": self.head,
            "left_ear": self.left_ear,
            "hair": self.hair,
            "snout": self.snout,
            "eyes": {
                "open": self.eyes_open,
                "slightly_closed": self.eyes_slightly_closed,
                "angry_for_eye_patch": self.eyes_angry_for_eye_patch,
            },
            "mouth": {
                "smile": self.mouth_smile,
                "panting": self.mouth_panting,
                "unsure": self.mouth_unsure,
                "pain": self.mouth_pain,
            },
            "nose": self.nose,
            "extra": {
                "butterfly": self.butterfly,
                "book": self.book,
                "microphone_on_table": self.microphone_on_table,
                "eye_patch": self.eye_patch,
            },
        }

        return LAYER_FUNCTIONS

    # Traverse head anti-clockwise
    def traverse_head(self, extent):
        self.goto(
            Drawing.SIZE / 2,
            Drawing.SIZE - ((Drawing.SIZE / 2) - self.HEAD_RADIUS)
        )
        setheading(180)  # Point east
        circle(self.HEAD_RADIUS, extent=extent)

    # Body part definitions
    def head(self):
        self.goto(
            Drawing.SIZE / 2,
            (Drawing.SIZE / 2) - self.HEAD_RADIUS
        )
        with Draw(fill_colour=self.INNER_FUR_COLOUR):
            setheading(0)
            circle(self.HEAD_RADIUS)
        # Draw face fur lines
        self.traverse_head(360 - 70)  # Wrap around head for fill
        with Draw(fill_colour=self.OUTER_FUR_COLOUR):
            circle(self.HEAD_RADIUS, extent=180 + 35)
            # To left eye
            setheading(90 + 45)
            circle(-10, extent=100)
            setheading(180 + 10)
            forward(5)
            setheading(70)
            circle(-10, extent=60)
            setheading(180 - 10)
            forward(5)
            setheading(40)
            circle(-10, extent=50)
            # To right eye
            setheading(30)
            forward(23)  # Through left eye
            for i in range(2):
                setheading(270 + 25)
                forward(5)
                setheading(90 - 25)
                forward(5)
            setheading(270 + 25)
            forward(5)
            # Close fur line to head
            setheading(0)
            forward(7)

    def left_ear(self):
        self.traverse_head(90)  # Goto the middle left of head
        setheading(90 + 45)
        with Draw(fill_colour=self.OUTER_FUR_COLOUR):
            circle(-60, extent=40)  # Draw left line
            setheading(270 + 80)
            circle(-70, extent=27)  # Draw right line

    def right_ear(self):
        self.traverse_head(360 - 23)  # Shuffle right a bit across head
        setheading(45)
        with Draw(fill_colour=self.OUTER_FUR_COLOUR):
            circle(-50, extent=25)  # Draw left line
            setheading(270 + 30)
            circle(-30, extent=66)  # Draw right line

    def hair(self):
        self.traverse_head(15)  # Go left a bit across head
        setheading(60)
        with Draw(fill_colour=self.OUTER_FUR_COLOUR):
            # Draw first strand
            circle(-35, extent=60)
            setheading(180 + 65)
            circle(-70, extent=10)
            # Draw second strand
            setheading(10)
            circle(-40, extent=40)
            setheading(180 + 30)
            circle(-70, extent=23)
            # Draw third strand
            setheading(0)
            circle(-50, extent=15)
            setheading(180 + 30)
            circle(-100, extent=5)

    def snout(self):
        self.traverse_head(180 + 92)
        setheading(180)
        forward(10)  # Go inwards a bit
        circle(15, extent=150)
        with Draw(fill_colour=self.INNER_FUR_COLOUR):
            circle(15, extent=170)

    def nose(self):
        COLOUR = "#464646"
        self.traverse_head(180 + 92)
        x = xcor() - 6
        y = ycor() - 5
        goto(x, y)
        setheading(180)
        with Draw(fill_colour=COLOUR):
            circle(5)

    def neck_and_shoulders(self):
        self.traverse_head(180 - 20)
        # Left side
        with Draw(fill_colour=Fox.OUTER_FUR_COLOUR):
            setheading(270)  # Left line
            forward(10)
            # Shoulder
            setheading(180 + 20)
            circle(20, extent=50)
            setheading(0)
            # Base
            setheading(0)
            forward(15)
            # Connect
            setheading(90)
            circle(-15, extent=60)
            setheading(90)
            forward(8)
        # Right Side
        self.traverse_head(180 + 25)  # Reposition
        with Draw(fill_colour=self.INNER_FUR_COLOUR):
            # Right line
            setheading(270)
            forward(10)
            # Shoulder
            setheading(360 - 20)
            circle(-50, extent=27)
            # Connect
            setheading(180)
            forward(39.5)  # Stop bolding with floating point
            # Reline left side connection
            setheading(90)
            circle(-15, extent=60)
            setheading(90)
            forward(8)

    # Mouth definitions
    def mouth_smile(self):
        self.traverse_head(180)
        y = ycor() + 10
        sety(y)
        with Draw():
            setheading(360 - 15)  # Down
            forward(15)
            setheading(20)  # Up
            forward(11)
            setheading(90)  # Straight up to nose
            forward(5)
            setheading(270)  # Back down
            forward(5)
            setheading(360 - 15)  # Down
            forward(7)

    def mouth_panting(self):
        MOUTH_COLOUR = "#d280a4"
        TOOTH_COLOUR = "#e0eaf3"
        self.traverse_head(200)
        y = ycor() + 5
        sety(y)
        # Mouth
        with Draw(fill_colour=MOUTH_COLOUR):
            setheading(180 + 60)
            forward(3)
            setheading(360 - 20)
            circle(-20, extent=45)
            circle(7, extent=180)
            setheading(90)
            circle(15, extent=40)
            setheading(180 + 30)
            circle(-23, extent=47)
        # Edge of mouth
        setheading(heading() + 180)  # Go back
        with Draw():
            circle(23, extent=51)
        # Tooth
        setheading(heading() + 180)  # Go back
        circle(-23, extent=46)
        with Draw(fill_colour=TOOTH_COLOUR):
            setheading(270)
            circle(3.5, extent=150)
        # Line on mouth
        x = xcor() + 3
        y = ycor() - 3
        goto(x, y)
        with Draw():
            setheading(0)
            circle(-4, extent=80)

    def mouth_unsure(self):
        self.traverse_head(185)
        y = ycor() + 7
        sety(y)
        with Draw():
            for i in range(3):
                setheading(45)
                forward(6)
                setheading(360 - 45)
                forward(6)
            setheading(40)
            forward(7)

    def mouth_pain(self):
        self.traverse_head(163)
        y = ycor() + 6
        sety(y)
        # Draw the mouth arch
        with Draw(fill_colour="white"):
            setheading(90)  # Left line start
            forward(3)
            circle(-8, extent=160)
            circle(11, extent=40)
            setheading(180)  # Connect arch
            forward(20)
        setheading(0)  # Go back
        forward(20)
        # Draw the rest of the mouth
        with Draw():
            setheading(330)
            circle(11, extent=75)
            setheading(90)  # Connect to the nose
            forward(6)
            # Go back down
            setheading(270)
            forward(6)
            # Right part of mouth
            setheading(360 - 30)
            forward(7)
        # Draw mouth features
        self.traverse_head(163)  # Go back to left corner of mouth
        y = ycor() + 10
        sety(y)
        with Draw():
            # Draw teeth
            setheading(30)
            forward(5)
            setheading(360 - 30)
            forward(5)
            setheading(30)
            forward(3)

    # Eye definitions
    def left_eye(self, eye_height):
        start_position = (41, 43)
        self.goto(*start_position)
        with Draw(fill_colour="white"):
            setheading(90)  # Left line
            forward(eye_height)
            circle(-7.5, extent=180)  # Top
            forward(eye_height)  # Right line
            self.goto(*start_position)  # Base

    def right_eye(self, eye_height):
        start_position = (72, 45)
        self.goto(*start_position)
        with Draw(fill_colour="white"):
            setheading(90)  # Left line
            forward(eye_height)
            circle(-4, extent=180)  # Top
            forward(eye_height)  # Right line
            self.goto(*start_position)  # Base

    def normal_pupils(self):
        # Left eye pupil
        start_position = (56, 56)  # Top of pupil
        # Outer
        self.goto(*start_position)
        with Draw(fill_colour=self.OUTER_EYE_COLOUR):
            setheading(180)
            circle(5, extent=180)
        # Inner
        self.goto(
            x=start_position[0],
            y=start_position[1] - 1.5
        )
        with Draw(fill_colour="black"):
            setheading(180)
            circle(3, extent=180)

        # Right eye pupil
        start_position = (73, 47)  # Bottom of pupil
        # Outer
        self.goto(*start_position)
        with Draw(fill_colour=self.OUTER_EYE_COLOUR):
            setheading(0)
            circle(5, extent=180)
        # Inner
        self.goto(
            start_position[0],
            start_position[1] + 1.7
        )
        with Draw(fill_colour="black"):
            setheading(0)
            circle(3, extent=180)

    def eyes_open(self):
        eye_height = 13
        self.left_eye(eye_height=eye_height)
        self.right_eye(eye_height=eye_height)
        self.normal_pupils()

    def eyes_angry_for_eye_patch(self):
        # Does not draw left eye
        self.right_eye(eye_height=11)
        self.normal_pupils()

    def eyes_slightly_closed(self):
        eye_height = 2
        self.left_eye(eye_height=eye_height)
        self.right_eye(eye_height=eye_height + 2)  # Add 2 to normalise eye

        # Left eye pupil
        start_position = (53, 51)
        # Outer
        self.goto(*start_position)
        with Draw(fill_colour=self.OUTER_EYE_COLOUR):
            setheading(180)
            circle(4, extent=155)
            offset_x(5)  # Go along base to connect fill
        # Inner
        self.goto(
            start_position[0] + 1,
            start_position[1] - 6
        )
        dot(4)

        # Left eye pupil
        start_position = (73, 43)
        # Outer
        self.goto(*start_position)
        with Draw(fill_colour=self.OUTER_EYE_COLOUR):
            setheading(0)
            circle(4.5, extent=180)
        # Inner
        self.goto(
            start_position[0],
            start_position[1] + 4
        )
        dot(3)

    # Neck wear definitions
    def neckerchief(self):
        NECK_LINE_HEADING = 180 - 5  # Neck and bandana need coordination
        COLOUR = "#f3d422"
        self.traverse_head(90 + 55)
        with Draw(fill_colour=COLOUR):
            # Left side
            setheading(180 + 30)
            forward(8)
            setheading(270 + 60)
            forward(8)
            setheading(180 + 30)
            forward(8)
            setheading(0)
            circle(-50, extent=43)
            # Base
            setheading(0)
            forward(23)
            # Right side
            setheading(45)
            circle(10, extent=110)
            setheading(50)
            forward(8)
            setheading(90 + 80)
            forward(10)
        setheading(270)  # Go down
        forward(10)
        with Draw():
            # Neck line
            setheading(NECK_LINE_HEADING)
            forward(40)
        # Insert neck ontop of neckerchief
        self.traverse_head(180 - 20)
        # Left side
        with Draw(fill_colour=self.OUTER_FUR_COLOUR):
            setheading(270)  # Left line
            forward(5)
            setheading(180 + NECK_LINE_HEADING)  # Base
            forward(10)
            setheading(90)  # Right line
            forward(10)
        # Right side
        with Draw(fill_colour=self.INNER_FUR_COLOUR):
            setheading(270)  # Go back
            forward(10)
            setheading(180 + NECK_LINE_HEADING)  # Base
            forward(15)
            setheading(90)
            forward(10)

    def bow_tie(self):
        COLOUR = "red"
        self.traverse_head(180 + 15)
        y = ycor() - 7
        sety(y)
        # Right side
        with Draw(fill_colour=COLOUR):
            setheading(360 - 20)
            circle(20, extent=40)
            setheading(90)
            forward(6)
            setheading(180 - 20)
            circle(20, extent=50)
        # Reset
        self.traverse_head(180 + 15)
        y = ycor() - 7
        sety(y)
        # Left side
        with Draw(fill_colour=COLOUR):
            setheading(180 + 30)
            circle(-20, extent=35)
            setheading(180 - 45)
            circle(-5, extent=100)
            circle(-10, extent=60)
        # Reset
        self.traverse_head(180 + 15)
        y = ycor() - 7
        sety(y)
        # Middle circle
        with Draw(fill_colour=COLOUR):
            setheading(0)
            circle(3)

    def collar(self):
        LEATHER_COLOUR = "#cead7f"
        METAL_COLOUR = "#bcbcbc"
        self.traverse_head(220)
        y = ycor() - 9
        sety(y)
        # Leather
        with Draw(fill_colour=LEATHER_COLOUR):
            setheading(180 - 3)
            forward(33)
            setheading(270)
            forward(8)
            setheading(360 - 3)
            forward(33)
            # Connect
            setheading(90)
            forward(8)
        # Reset
        self.traverse_head(220)
        y = ycor() - 9
        sety(y)
        # Metal bit
        with Draw(fill_colour=METAL_COLOUR):
            # Inner
            setheading(180)
            forward(10)
            setheading(270)
            forward(10)
            setheading(10)
            forward(10)
            # Outer
            setheading(270)
            forward(2)
            setheading(180 + 10)
            forward(13)
            setheading(90)
            forward(16)
            setheading(0)
            forward(13)
            setheading(270)
            forward(5)

    # Extra defintions
    def butterfly(self):
        COLOUR = "pink"
        self.traverse_head(360 - 20)
        x = round(xcor())  # Fix lines
        y = ycor() + 5
        goto(x, y)
        # Body
        circle(3, extent=120)  # Go around butterfuly head
        with Draw(fill_colour=COLOUR):
            setheading(180 + 45)
            forward(15)
            circle(2, extent=180)
            forward(15)
        # Head
        forward(5)  # Go up a bit
        setheading(180 - 45)
        forward(2)
        with Draw(fill_colour=COLOUR):
            circle(3)
        # Go back
        setheading(360 - 45)
        forward(2)
        setheading(180 + 45)
        forward(5)
        # Right wing - top
        with Draw(fill_colour=COLOUR):
            setheading(10)
            circle(-20, extent=60)
            setheading(270 - 20)
            circle(-20, extent=40)
            setheading(180)
            circle(-20, extent=60)
            # Connect
            setheading(45)
            forward(15)
        # Go back
        setheading(180 + 45)
        forward(15)
        # Right wing - bottom
        with Draw(fill_colour=COLOUR):
            setheading(270 + 45)
            circle(-30, extent=25)
            circle(-5, extent=180)
            circle(-20, extent=30)
            # Connect
            setheading(45)
            forward(1)
        # Go back
        x = xcor() + 7
        y = ycor() + 13
        goto(x, y)
        # Left wing - top
        with Draw(fill_colour=COLOUR):
            setheading(90 + 10)
            circle(20, extent=60)
            setheading(270 - 45)
            circle(20, extent=40)
            setheading(270 + 20)
            circle(20, extent=44.6)
            # Connect
            setheading(45)
            forward(15)
        # Go back
        setheading(180 + 45)
        forward(15)
        # Left wing - bottom
        with Draw(fill_colour=COLOUR):
            setheading(270 + 45 + 180)
            circle(30, extent=25)
            circle(5, extent=180)
            circle(20, extent=32)
            # Connect
            setheading(45)
            forward(1)

    def book(self):
        COVER_COLOUR = "#b81c1f"
        PAGES_COLOUR = "#cad0c4"
        # Go to bottom right of cell
        self.goto(
            Drawing.SIZE - 13,
            30
        )
        # Book pages
        with Draw(fill_colour=PAGES_COLOUR):
            setheading(30)
            forward(8)
            setheading(360 - 30)
            forward(7)
            # Connect
            setheading(270)
            forward(20)
        # Reset
        self.goto(
            Drawing.SIZE - 18,
            0
        )
        # Book cover
        with Draw(fill_colour=COVER_COLOUR):
            setheading(90)
            forward(33)
            setheading(360 - 30)
            forward(21)
            # Connect
            setheading(270)
            forward(20)
        # Reset
        self.goto(
            Drawing.SIZE,
            3
        )
        # Hand
        with Draw(fill_colour=self.OUTER_FUR_COLOUR):
            setheading(180)
            circle(-25, extent=55)
            setheading(180 + 10)
            forward(10)
            setheading(270 - 10)
            forward(12)
            # Connect
            setheading(0)
            forward(31)

    def microphone_on_table(self):
        TABLE_COLOUR = "#cea54b"
        PAPER_COLOUR = "white"
        # Go to bottom right of cell
        self.goto(
            Drawing.SIZE - 35,
            0
        )
        # Table
        with Draw(fill_colour=TABLE_COLOUR):
            setheading(30)
            forward(40)
            # Connect
            setheading(270)
            forward(20)
        # Reset
        self.goto(
            Drawing.SIZE - 25,
            0
        )
        # Paper
        with Draw(fill_colour=PAPER_COLOUR):
            setheading(30)
            forward(29)
            # Connect
            setheading(270)
            forward(13)
        # Reset
        self.goto(
            Drawing.SIZE - 15,
            0
        )
        # Writing
        with Draw():
            for i in range(3):
                setheading(90 - 20)
                forward(3)
                setheading(270 + 75)
                forward(3)
            # Last line needs modification
            setheading(90 - 20)
            forward(3)
            setheading(270 + 75)
            forward(2)  # Modified 3 to 2
        # Reset
        self.goto(
            Drawing.SIZE - 2,
            10
        )
        # Microphone
        with Draw(pen_size=5):
            setheading(90 + 20)
            circle(30, extent=32)
        dot(10)

    def eye_patch(self):
        self.traverse_head(90)
        # Left line
        with Draw(pen_size=4):
            setheading(0)
            forward(27)
        # Eye patch
        dot(20)
        # Right line
        with Draw(pen_size=4):
            setheading(25)
            forward(30)


FOX_VARIATIONS = {
    'A': {
        "name": "Happy",
        "mouth": "smile",
        "eyes": "open",
        "neck_wear": "neckerchief",
        "extra": "butterfly",
    },
    'B': {
        "name": "Reading while tired",
        "mouth": "panting",
        "eyes": "slightly_closed",
        "neck_wear": False,
        "extra": "book",
    },
    'C': {
        "name": "Presenting a speech",
        "mouth": "unsure",
        "eyes": "open",
        "neck_wear": "bow_tie",
        "extra": "microphone_on_table",
    },
    'D': {
        "name": "Angry new Fox style",
        "mouth": "pain",
        "eyes": "angry_for_eye_patch",
        "neck_wear": "collar",
        "extra": "eye_patch",
    }
}


def visualise(action_data):
    fox = Fox(FOX_VARIATIONS)

    legend = Legend(
        title="Faces of Fox",
        x=500,
        y=250,
        length=500
    )
    legend.draw(fox)

    grid = Grid()
    last_variation = grid.draw(fox, action_data)

    # Draw the final variant to the left of the grid
    goto(-650, 55)
    Write.write("Final variant:", Write.DESCRIPTION_FONT_SIZE)
    offset_y(-Drawing.SIZE - 5)  # Extra 5 pixels between looks neater
    fox.draw(last_variation)

#
#--------------------------------------------------------------------#



#-----Initialisation Steps-------------------------------------------#
#
# This code checks that the programmer's identity has been provided
# and whether or not the data generation function is available.  You
# should NOT change any of the code in this section.
#

# Confirm that the student has declared their authorship
if not isinstance(student_number, int):
    print('\nUnable to run: No student number supplied',
          '(must be an integer)\n')
    abort()
if not isinstance(student_name, str):
    print('\nUnable to run: No student name supplied',
          '(must be a character string)\n')
    abort()

### Define the function for generating data sets, using the
### client's "raw data" function if available, but otherwise
### creating a dummy function that returns an empty list
if isfile('data_generator.py'):
    print('\nNote: Data module found\n')
    from data_generator import raw_data
    def data_set(new_seed = None):
        seed(new_seed)
        return raw_data(grid_width, grid_height)
else:
    print('\nNote: No data module available\n')
    def data_set(dummy_parameter = None):
        return []

#
#--------------------------------------------------------------------#



#-----Main Program to Create Drawing Canvas--------------------------#
#
# This main program sets up the canvas, ready for you to start
# drawing your solution.  Do NOT change any of this code except
# as indicated by the comments marked '*****'.  Do NOT put any of
# your solution code in this area.
#

# Set up the drawing canvas
# ***** You can change the background and line colours, and choose
# ***** whether or not to draw the grid and other elements, by
# ***** providing arguments to this function call
create_drawing_canvas(label_spaces = False)

# Control the drawing speed
# ***** Change the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** forever while the cursor moves slooooowly around the screen
tracer(False)

# Give the drawing canvas a title
# ***** Replace this title with a description of your solution's
# ***** overall theme
title("Faces of Fox, From the Housepets comic")

### Call the student's function to process the data set
### ***** While developing your program you can call the
### ***** "data_set" function with a fixed seed for the
### ***** random number generator, but your final solution must
### ***** work with "data_set()" as the argument to "visualise",
### ***** i.e., for any data set that can be returned by
### ***** calling function "data_set" with no seed.
visualise(data_set()) # <-- no argument for "data_set" when assessed

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas()

#
#--------------------------------------------------------------------#
