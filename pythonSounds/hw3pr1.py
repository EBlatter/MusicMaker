#
# hw3pr1.py - Lab 3 problem, "Sounds Good!"
#
# Name(s):
#
#

import time
import random
import math
import csaudio
from csaudio import *

# a function to get started with a reminder 
# about list comprehensions...
def three_ize( L ):
    """ three_ize is the motto of the green CS 5 alien.
        It's also a function that takes in a list and
        returns a list of elements each three times as large.
    """
    # this is an example of a list comprehension
    LC = [ 3*x for x in L ]
    return LC



# Function to write #1:  scale







# here is an example of a different method
# for writing the three_ize function:
def three_ize_by_index( L ):
    """ three_ize_by_index has the same I/O behavior as three_ize
        but it uses the INDEX of each element, instead of
        using the elements themselves -- this is much more flexible!
    """
    # we get the length of L first, in order to use it in range:
    N = len(L)
    LC = [ 3*L[i] for i in range(N) ]
    return LC



# an example of shifting elements
def wrap1( L ):
    """ What does this do -- and why?!
    """
    N = len(L)
    LC = [ L[i-1] for i in range(N) ]
    return LC

# write a 1-sentence summary/comment
# describing what wrap1 does, and how:





# Function to write #2:  wrapN






# Function to write #3:  add_2






# Function to write #4:  add_scale_2








# Helper function:  randomize

def randomize( x, chance_of_replacing ):
    """ randomize takes in an original value, x
        and a fraction named chance_of_replacing.

        With the "chance_of_replacing" chance, it
        should return a random float from -32767 to 32767.

        Otherwise, it should return x (not replacing it).
    """
    r = random.uniform(0,1)
    if r < chance_of_replacing:
        return random.uniform(-32768,32767)
    else:
        return x
    





# Function to write #5:  replace_some











#
# below are functions that relate to sound-processing ...
#


# a function to make sure everything is working
def test():
    """ a test function that plays swfaith.wav
        You'll need swfailt.wav in this folder.
    """
    play( 'swfaith.wav' )

    
# The example changeSpeed function
def changeSpeed(filename, newsr):
    """ changeSpeed allows the user to change an audio file's speed
        input: filename, the name of the original file
               newsr, the *new* sampling rate in samples per second
        output: no return value; creates and plays the file 'out.wav'
    """
    samps, sr = readwav(filename)

    print "The first 10 sound-pressure samples are\n", samps[:10]
    print "The original number of samples per second is", sr
    
    newsamps = samps                        # no change to the sound
    writewav( newsamps, newsr, "out.wav" )  # write data to out.wav
    print "\nPlaying new sound..."
    play( 'out.wav' )   # play the new file, 'out.wav'
    


def flipflop(filename):
    """ flipflop swaps the halves of an audio file
        input: filename, the name of the original file
        output: no return value, but
                this creates the sound file 'out.wav'
                and plays it
    """
    print "Playing the original sound..."
    play(filename)
    
    print "Reading in the sound data..."
    samps, sr = readwav(filename)
    
    print "Computing new sound..."
    # this gets the midpoint and calls it x
    x = len(samps)/2
    newsamps = samps[x:] + samps[:x] # flip flop
    newsr = sr                       # no change to the sr
    
    writewav( newsamps, newsr, "out.wav" )
    print "Playing new sound..."
    play( 'out.wav' )




# Sound function to write #1:  reverse







# Sound function to write #2:  volume







# Sound function to write #3:  static







# Sound function to write #4:  overlay







# Sound function to write #5:  echo








# Helper function for generating pure tones
def gen_pure_tone(freq, seconds):
    """ pure_tone returns the y-values of a cosine wave
        whose frequency is freq Hertz.
        It returns nsamples values, taken once every 1/44100 of a second;
        thus, the sampling rate is 44100 Hertz.
        0.5 second (22050 samples) is probably enough.
    """
    sr = 44100
    # how many data samples to create
    nsamples = int(seconds*sr) # rounds down
    # our frequency-scaling coefficient, f
    f = 2*math.pi/sr           # converts from samples to Hz
    # our amplitude-scaling coefficient, a
    a = 32767.0
    # the sound's air-pressure samples
    samps = [ a*math.sin(f*n*freq) for n in range(nsamples) ]
    # return both...
    return samps, sr


def pure_tone(freq, time_in_seconds):
    """ plays a pure tone of frequence freq for time_in_seconds seconds """
    print "Generating tone..."
    samps, sr = gen_pure_tone(freq, time_in_seconds)
    print "Writing out the sound data..."
    writewav( samps, sr, "out.wav" )
    print "Playing new sound..."
    play( 'out.wav' )




# Sound function to write #6:  chord








