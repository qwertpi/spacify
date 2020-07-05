import re
import string

#splitlines instead of readlines as splitlines removes newline chars
#all printable charcters are added to prevent the code from getting stuck if no words exist
with open("words.txt", "r") as f:
    words = f.read().splitlines() + list(string.printable)

try:
    #loads from file
    #merges onto one line
    with open("input.txt", "r") as f:
        inp = "".join(f.read().splitlines())
#unless no files exist
except FileNotFoundError:
    #in which case loads from input
    inp = input(">  ")

#removes all characters from input that aren't letters, or certain punctuation
#change depending on whether spaces in the input should preserved
ignore_spaces = False
if ignore_spaces:
    banned_chars = "".join(list(set(string.printable) - set(string.ascii_letters) - set([",", "!", ".", "?", "-"])))
else:
    banned_chars = "".join(list(set(string.printable) - set(string.ascii_letters) - set([",", "!", ".", "?", "-", " "])))
for char in banned_chars:
    inp = inp.replace(char, "")    

char = ""
prev_char = ""
out = ""

#rule based spacification to speed up the main brute force spacification
for char in inp:
    #if the current character is uppercase and the previous character wasn't uppercase
    #as captials require spaces with the exception of acronyms
    #or if the character is punctuation
    if (char in string.ascii_uppercase and prev_char not in string.ascii_uppercase) or char not in list(string.ascii_letters):
        #adds a space before the next character
        out += " "
    out += char
    #pucntuation isn't included in prev_char
    if char in string.ascii_letters:
        prev_char = char

print(out)

longest_word = ""
word_segment = ""
inp = out
out = ""

def possible_words(string, words):
    '''
    Tells you whether any words begin with a certain string
    :param string: str, the string you want to check for words begining with
    :param words: list, the words you want to check for matches in
    :returns: bool, whether 
    '''
    #cehcks every word
    for word in words:
        regex = re.compile("^" + string)
        #if the word starts with with string
        if bool(regex.search(word)):
            #return causes the function to quit
            return True
    #this will only be ran if we get to the end of the for loop without having returned True
    return False

#respects the word bounadries created by the rules
for word in inp.split(" "):
    #bool(list) is equal to False when the list is empty
    while bool(word) != False:
        for char in word:
            word_segment += char.lower()
            #if no words start with the word segment
            if not possible_words(word_segment, words):
                #we've already found the longest possible word so breaks out of the for char loop
                break
            #if word_segment is a word
            try:
                words.index(word_segment)
                longest_word = word_segment
            #else do nothing
            except ValueError:
                pass
        #once we've either reached the end of the for char loop or (more likely) no words starting with word_segment exist
        #adds the longest word we found to the output string followed by a space
        out += longest_word + " "
        #remove the word we found from the input
        #else the while len() > 0 will never end
        word = word[len(longest_word):]
        #resets relevant variables ready to find the next word
        longest_word = ""
        word_segment = ""
        #very basic progress indicator
        #without flush=True the output won't be shown until a new line occurs
        print("_", end="", flush=True)

print("")
print(out)

inp = out
out = ""

prev_char = ""
for char in inp:
    #strips spaces from before punctuation
    if char not in string.punctuation or prev_char != " ":
        out += prev_char
    prev_char = char

#provides final output
print(out)
#also sticks it in a text file for increased conveinece
with open("out.txt", "w") as f:
    f.write(out) 
