
""" terminal_animation (v1.0)

A text-based animation which runs on the command line.
The frames of the animation are loaded from the 'anim_frames' module.
A frame is simply a string of characters and the animation consists of a list of frames.

Author: mdq3
2012/05/16

"""

import time
import os
import animation

duration = 0.05    # The duration of time in seconds between each frame.
cycles = 100       # The number of cycles the animation plays through.

def animate():
    """Iterate through the frames, printing then clearing each one to create an animation."""
    count = 0
    while count < cycles:
        for frame in animation.frames:
            print '\033[1;34m' + frame + '\033[1;m'  # Print the frame in color blue.
            time.sleep(duration)
            print(os.system('clear'))
        count = count + 1

animate()
