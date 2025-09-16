

#my_string="I am writing java program"
# my_string="  hello   world  "
#
# my_list=my_string.split(" ")
# my_list.reverse()
# print(my_list)
#
# rev_word_string=""
# for word in my_list:
#     rev_word_string=rev_word_string+" "+word
#
# print(rev_word_string.strip())

#another way to reverse word
my_string="I am writing java program"
word=""
words=[]

for char in my_string:
    if char !=' ':
        word= word+char
    else:
        words.append(word)
        word=""
# add last word
if word:
    words.append(word)

print(words)
rev_word_sent=""
for i in range(len(words)-1,-1,-1):
    rev_word_sent=rev_word_sent+" "+words[i]
print(rev_word_sent.strip())

