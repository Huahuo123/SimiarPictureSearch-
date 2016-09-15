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
