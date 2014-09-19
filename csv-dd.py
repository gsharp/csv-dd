# import sys library so we can do system level stuff like args and exits
import sys

# check for incoming file params...must have 2, 0 = script itself
if len(sys.argv) != 3:
	sys.exit("usage: python path/to/csv-dd.py input.csv output.csv")

# get the command line arguments and stuff them into variables
thisFile, inFile, outFile = sys.argv
print "Thanks for running", thisFile,"!!"
print "inFile: ", inFile
print "outFile: ", outFile
print "\n"

# setup our working data object, using a python dictionary list
# note: python dictionaries support duplicate keys :(
dict = {}

# parse the incoming file and populate the dict
print "Duplicate records:"
with open(inFile) as f:
	for line in f:
		value, key = line.replace("\n", "").split(',')
		if key not in dict:
			dict[key] = [value]
		else:
			if value not in dict[key]:
				print "appending", value, "to ", key
				dict[key].append(value)

print "\n:: example output ::"

# make a new file for output
file = open(outFile, "w")
# now read the dict object and spit out the formatted contents to a new file
for key in dict:
	out = key + "," + ";".join(dict[key])
	print out
	file.write(out+"\n")
file.close()
