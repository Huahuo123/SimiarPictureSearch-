# open the shelve database
db = shelve.open(args["shelve"])
 
# load the query image, compute the difference image hash, and
# and grab the images from the database that have the same hash
# value
query = Image.open(args["query"])
h = str(imagehash.dhash(query))
filenames = db[h]
print "Found %d images" % (len(filenames))
 
# loop over the images
for filename in filenames:
image = Image.open(args["dataset"] + "/" + filename)
image.show()
 
# close the shelve database
db.close()