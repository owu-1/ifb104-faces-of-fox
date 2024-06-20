
from random import randint, choice

#-----Data Set Function for Assessing Your Solution------------------#
#
# The function in this module generates the data sets that will be
# used to assess your solution.
#
# Do NOT change any of the code in this module.  Do NOT submit a copy
# of this module with your solution - we will use our own copy to
# assess your code.
#
# The following function creates a random data set defining the
# overall image to draw.  Your program must work for any data set that
# can be produced by this function.  The results returned by calling
# this function will be used as the argument to your data visualisation
# function during marking.  For convenience during code development
# and marking this function also prints the data set generated to the
# shell window.  NB: Your solution should not print anything else to
# the shell.  Make sure any debugging calls to the "print" function
# are disabled before you submit your solution.
#
def raw_data(width = 1, height = 1):
    
    # Define the variants
    variants = ['A', 'B', 'C', 'D']
    # Define the directions we can move
    directions = ['North', 'South', 'East', 'West']
    # Choose the total number of data items
    # (in addition to the 'start' item)
    num_data = randint(0, 100)
    # Define the likelihood of mutating
    mutation_probability = 20 # percent 

    # Choose the starting point
    x_start = randint(0, width - 1)
    y_start = randint(0, height - 1)
    # Choose the first variant
    variant = choice(variants)
    # Initialise the data set with the first location and variant
    location = [x_start, y_start]
    data_items = [['Start', chr(ord('a') + x_start), y_start + 1, variant]]

    # Add the individual data items
    for datum in range(0, num_data):
        if randint(1, 100) <= mutation_probability:
            # Choose a new variant (remembering that Python lists
            # are mutable and changes are done in-place)
            other_variants = variants.copy()
            other_variants.remove(variant)
            variant = choice(other_variants)
            # Add the mutation to the data set
            data_items.append(['Change', variant])
        else:
            # Choose direction to move
            direction = choice(directions)
            # Choose number of steps (always staying within the grid)
            if direction == 'North':
                num_steps = randint(0, height - location[1] - 1)
                location[1] = location[1] + num_steps
            elif direction == 'South':
                num_steps = randint(0, location[1])
                location[1] = location[1] - num_steps
            elif direction == 'East':
                num_steps = randint(0, width - location[0] - 1)
                location[0] = location[0] + num_steps
            else:
                num_steps = randint(0, location[0])
                location[0] = location[0] - num_steps
            # Add the move to the data set
            data_items.append([direction, num_steps])

    # Print the whole data set to the shell window, nicely laid out
    print('The data set to visualise is as follows:\n')
    print(str(data_items).replace('],', '],\n'))
    if len(data_items) == 1:
        print('\nThere was one step only\n')
    else:
        print('\nThere were', len(data_items), 'steps in total\n')
    # Return the data set to the caller
    return data_items

#
#--------------------------------------------------------------------#



#--------------------------------------------------------------------#
#
# Some "fixed" data sets
#
# Developing code when the underlying data set changes randomly can
# be difficult.  To help you develop your code you can temporarily
# provide the call to the "data_set" function defined in the
# assignment template file with a "seed" value which will force it to
# produce a known data set.
#
# To use them, just put the seed value in the call to "data_set" as
# its argument.  Of course, having completed your solution, your
# program must work for any list that can be returned by calling
# "data_set" with no argument.
#
# Note that the following descriptions all assume that the grid has
# its default width and height (9 x 7 cells).
#
# Some examples of useful seeds follow.  Each of these seed values
# produces a short sequence of steps only, which makes it easier to
# see whether or not your program is following them correctly.
#
#    seed 2: 8 steps with variants C and B all on the first row
#    seed 31: 2 steps with no "moves"
#    seed 32: 10 steps with variants C and A visible at the end
#    seed 43: 5 steps with only variant D visible at the end
#    seed 49: 9 steps with variant A only (no changes)
#    seed 57: 6 steps with variants A and D
#    seed 104: 3 steps with only 'zero moves'
#    seed 113: 4 steps with variants D and B
#    seed 123: 7 steps with variants D, B and C visible at the end
#    seed 139: 1 step with variant C only
#    seed 162: 7 steps with variants B and A
#    seed 165: 3 steps with only variant B visible at the end
#    seed 174: 1 step with variant D only
#    seed 176: 4 steps with variants B and A
#    seed 190: 10 steps with variants C and A
#    seed 198: 7 steps with variant D only
#
# At the other extreme, here are some seeds that produce very long
# lists of steps.  You can use them to test the robustness of your
# final solution.
#
#    seed 23: 100 steps
#    seed 26: 96 steps
#    seed 68: 95 steps
#    seed 86: 100 steps
#    seed 140: 99 steps
#    seed 191: 98 steps
#
#--------------------------------------------------------------------#
