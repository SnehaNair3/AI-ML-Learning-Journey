
# What is the most frequent word in the following paragraph?
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

words=paragraph.replace('.','').split()

word_count={}

for word in words:
    word_count[word]=word_count.get(word,0)+1
result=sorted([(count,word) for word,count in word_count.items()],reverse=True)
print(result)
