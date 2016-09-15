# import the necessary packages
from PIL import Image
import imagehash
import argparse
import shelve

# construct the argument parse and parse the arguments
ap = argument.ArgumentParser()
ap.add_argument("-d","--dataset",required = True,help="path to input dadaset of images" )
ap.add_argument("-s","--shelve", required = True, help ="output shelve database")
ap.add_argument("-q", "--query", required = True,
help = "path to the query image")
args = vars(ap.parse_args())
