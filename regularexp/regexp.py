"""import re
matcher=re.finditer("ab","abababababababababababababab")
count=0
for match in matcher:
    print(match.start())#starting point
    print(match.group())#print the curresponding group
    count+=1
print(count)"""

# character setss........


"""import re
#x='[abc]'
#x='[a-z]'
#x='[0-9]'
#x='[0-9a-z]'
#x='[^a-z]'#^ use to except a-z
#x='[^a-z1-9A-Z]' #only characters
matcher=re.finditer(x,"ab_12kzl")
count=0
for match in matcher:
    print(match.start())
    print(match.group())
    count+=1
print(count)"""

##########  predefined characters ######

"""import re
#x='\s'#check for space
#x='\d'#check for digits
#x='\D'#except digits
#x='\w'#check for words(including "_")
#x='\W'#except words(can pick special characters


matcher=re.finditer(x,"ab_12 @kzl")
count=0
for match in matcher:
    print(match.group())
    print(match.start())"""

######  Quantifiers(checking quantity)
"""
import re
#x="a+" # occurance of singe a and multiple occurance of a
#x="a*" # check occurance of a and absence of a
#x='a?' # check single elements print every position
#x='aa?' # check double a s and every position
#x="a{2}" # check only two numbers of a
#x="a{2,3}" # check min 2 numbers of a and maximum 3 numbers of a"
#x="^a" # check the string stars with a
#x="a$" # check the given string ends with a

matcher=re.finditer(x,"aaaaaaaaabbbbbbbaaabbbaaaaba")
count=0
for match in matcher:
    print(match.group())
    print(match.start())"""
