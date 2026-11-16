
import re

# Match
re.match(substring,string,re.I)

import re
txt = 'I love to teach python and javaScript'
match1=re.match('I love to teach',txt,re.I)
print(match1)
# We can get the starting and ending position of the match as tuple using span
span=match1.span()
print(span)
# Lets find the start and stop position from the span
start,end=span
print(start,end)
substring=txt[start:end]
print(substring)

import re
txt = 'I love to teach python and javaScript'
match=re.match('I like to teach',txt,re.I)
print(match)


# Search
# re.search(substring,string,re.I)
import re
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
# It returns an object with span and match
match=re.search('first',txt,re.I)
print(match)
span=match.span()
print(span)
start,end=span
substring=txt[start:end]
print(substring)
# search is much better than match because it can look for the pattern throughout the text.
# Search returns a match object with a first match that was found, otherwise it returns None.

# findall. This function checks for the pattern through the whole string and returns all the matches as a list.
# Searching for All Matches Using findall
# findall() returns all the matches as a list
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
matches=re.findall('language',txt,re.I)
print(matches)

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
matches2=re.findall('python',txt,re.I)
print(matches2)

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
matches3=re.findall('Python|python',txt)
print(matches3)

matches4=re.findall('[Pp]ython',txt)
print(matches4)


# Replacing a Substring
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match_replaced1=re.sub('Python|python','JavaScript',txt)
print(match_replaced1)

match_replaced2=re.sub('[pP]ython','C++',txt)
print(match_replaced2)


txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches=re.sub('%','',txt)
print(matches)


# Splitting Text Using RegEx Split
txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''

print(re.split('\n',txt))


# Writing RegEx Patterns
import re
regex_pattern=r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches=re.findall(regex_pattern,txt)
print(matches)
# To make case insensitive adding flag '
matches=re.findall(regex_pattern,txt,re.I)
print(matches)
# or we can use a set of characters method
reg_pattern=r'[Aa]pple'
matches=re.findall(reg_pattern,txt)
print(matches)

reg_pattern=r'[Aa]pple|[Bb]anana'
txt='Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches=re.findall(reg_pattern,txt)
print(matches )


# Escape character(\) in RegEx
reg_pattern=r'\d'  # d is a special character which means digits
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches=re.findall(reg_pattern,txt)
print(matches)


# One or more times(+)
reg_pattern=r'\d+'
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches=re.findall(reg_pattern,txt)
print(matches)

# Period(.)
