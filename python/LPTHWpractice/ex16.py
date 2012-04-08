from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "if you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file.  Goodbye!"
target.truncate()

print "What day do you want to remember four things to do?"
date = raw_input("Date: ")

print "Now I'm going to ask you for four lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
line4 = raw_input("line 4: ")

print "I'm going to write these to the file."

target.write(date), 
target.write(line1)
target.write("\n")
target.write(date),
target.write(line2)
target.write("\n")
target.write(date),
target.write(line3)
target.write("\n")
target.write(date)
target.write(line4)
target.write("\n")

print "And finally, we close it."
target.close()
