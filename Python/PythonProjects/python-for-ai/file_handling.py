# File Handling

# Reading a File
file=open('file_handling_test.txt','r')
print(file.read())
# OR
file=open('file_handling_test.txt','r')
for line in file:
    print(line)

# return 50 characters
file=open('file_handling_test.txt','r')
print(file.read(50))   

# returns the first line
file=open('file_handling_test.txt','r')
print(file.readline()) 

# returns the first 2 characters from the first line
file=open('file_handling_test.txt','r')
print(file.readline(2)) 

# returns only characters from the first line
file=open('file_handling_test.txt','r')
print(file.readline(50)) 



  

