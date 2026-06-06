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

# Writing  a file
file=open('file_handling_test.txt','w')
file.write("Iam from Kerala and i live in Bangalore now.")
file.write("I love reading books, solving puzzles,studying etc")
file.write("I wanna learn tennis, dance, badminton, swimming, content creation.")
file.close()
file=open('file_handling_test.txt','r')
print(file.read())


# Append operation
with open('file_handling_test.txt','a') as file:
    file.write("I work in the computer science domain specifically focusing on ai-ml and data science.")
file=open('file_handling_test.txt','r')
for line in file:
    print(line)

# \n operation
file=open('file_handling_test.txt','w')
file.write("\n")    
file.write("My family consists of four members.")    
file.write("\n")    
file.write("I love my family.")    
file.close()
file=open('file_handling_test.txt','r')
print(file.read())


with open('file_handling_test.txt','a+') as file:
    file.write("\n")
    file.write("I love Kerala, its such a beautiful place.")
file=open('file_handling_test.txt','r')
for line in file:
    print(line)   
  

  

