import csv	# Comma Separated File Processing Library
import re	# Regular Expressions Library
import sys	# System Services (to pick up Command Line File Spec)

# Pick up the CSV filename from the command line

f = open(sys.argv[1], 'rt')

# Specify what a SKU and Values look like in the Materials Field,
# grouping the SKU value and values list (in brackets) so we can 
# extract them. This will all look a bit bizarre, but this is 
# UNIX standard Regular Expressions syntax.

regexp = '\.*sku: ([A-Za-z0-9_]*.?)\s.*?\svalues: ([0-9,]*.?)\s.*?'

# That says: examine materials, find 'sku: ', capture the next word
# containing characters A-Z, a-Z, 0-9 or underscore, then any number
# of characters until you hit space or newline, then pickup anything 
# between values: and the next space or newline (this may be one 
# number or several with commas between each. We'll use a Python
# trick with .split later down to peel of the numbers one by one.

try:
	# Pick up the field names from the first row

	reader = csv.DictReader(f)

	# Output the Column Headers

	print '"Pattern","Yarn","Balls"'

	# Now iterate through every row in the CSV file

	for row in reader:

		# Pick out the CSV file Columns that interest us

		pattern_sku = row['sku']
		pattern_name = row['name']
		materials = row['materials']

		# Now go iterate over any Yarn SKUs and Qtys found
		# within materials;
		# re.DOTALL forces '.' to match any char inc NewLine

#		/Debug Lines
#
#                print "SKU =", pattern_sku
#                print "Pattern = ", pattern_name
#                print "Materials contains:"
#                print materials

		for parts in re.finditer(regexp, materials, re.DOTALL):
			yarnsku = parts.group(1)
			yarnvalues = parts.group(2)
			for balls in yarnvalues.split(","):
				print '"'+pattern_sku.strip()+'","'+yarnsku.strip()+'",'+balls.strip()
#
#				/Debug Lines
#
#				print "pattern_sku =",pattern_sku
#				print "yarnsku =", yarnsku
#				print "yarnvalues = ", yarnvalues
#				print "balls = ", balls
#		x = raw_input('Press return for next:')

# All done now

finally:
	f.close()
