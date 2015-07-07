__author__ = 'Nikhil'

result = str(raw_input("Enter string:"))

reversed = result[::-1]
if reversed == result:
    print "The entered string is a palindrome"
else:
    print "The entered string is not a palindrome"

total = 0
for x in result:
    if x in "AEIOUaeiou":
        total += 1
if total>0:
    print "There are %d vowels in the input" % total
else:
    print "there are no vowels"
