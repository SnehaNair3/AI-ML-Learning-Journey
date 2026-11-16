
# open('filename',mode) 
# mode - r,a,w,x,t,b 


# Opening Files for Reading
f=open('./files/reading_file_example.txt')
print(f)
# read(): read the whole text as string
txt=f.read()
print(type(txt))
print(txt)
f.close()

# Instead of printing all the text, let us print the first 10 characters of the text file.
f = open('./files/reading_file_example.txt')
txt=f.read(10)
print(type(txt))
print(txt)
f.close()

# readline(): read only the first line
f = open('./files/reading_file_example.txt')
line=f.readline()
print(type(line))
print(line)
f.close()

# readlines(): read all the text line by line and returns a list of lines
f = open('./files/reading_file_example.txt')
lines=f.readlines()
print(type(lines))
print(lines)
f.close()

# Another way to get all the lines as a list is using splitlines():
f = open('./files/reading_file_example.txt')
lines=f.read().splitlines()
print(type(lines))
print(lines)
f.close()


# There is a new way of opening files using with - closes the files by itself. 
with open('./files/reading_file_example.txt') as f:
    lines=f.read().splitlines()
    print(type(lines))
    print(lines)

    