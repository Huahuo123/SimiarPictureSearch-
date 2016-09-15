# before index of images,please install PIL. 
# import the necessary packages
from PIL import Image 
import imagehash
import argparse 
import shelve 
import glob

# construct the argument parse and parse the arguments
ap = argument.ArgumentParser()
ap.add_argument("-d","--dataset",required = True,help="path to input dadaset of images" )
ap.add_argument("-s","--shelve", required = True, help ="output shelve database")
args = vars(ap.parse_args())

# open the shelve datebase
db = shelve.open(args["shelve"],writeback = True)

# loop over the image dataset
for imagePath in glob.glob(args["dataset"] + "/*.jpg"):
# load the image and compute the difference hash
image = Image.open(imagePath)
# Understand:h = str(imagehash.dhash())
h = str(imagehash.dhash(image))
# extract the filename from the path and update the database
# using the hash as the key and the filename append to the list of the values
filename = imagePath[imagePath.rfind("/") + 1:]
db[h] = db.get(h,[]) + [filename]
# close the shelve database
db.close()