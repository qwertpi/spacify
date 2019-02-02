import re

print("Loading")
#load all the words in from the text file
#splitlines instead of readlines as splitlines removes newline chars
words=open("words_alpha.txt","r").read().splitlines()
#gets the text to be spaced removes any existing spaces and makes it all lower case
text=input("    ").replace(" ","").lower()
#strips characters that aren't a-z commas full stops exclemation marks or question marksfrom the text
text=re.sub("[^.,!a-zA-Z]","",text)

spaced_text=""
current_attempt=""
previous_attempt=""
#change this to make the code print every word it considers
debug=False

#while there is any unspaced text
while len(text)!=0:
    for char in text:
        #add to the current attempt one char at a time
        current_attempt+=char
        #makes a list of all words starting with the text in current attempt
        regex = re.compile(current_attempt)
        matches = [word for word in words if regex.match(word)]
        #if there are no matching words end the loop
        if len(matches)==0:
            break

        try:
            #check if the current attempt is an actual word
            #if it isn't we won't get anyfurther with the text in this try block
            words.index(current_attempt)
            #debug infp
            if debug:
                print("Trying",current_attempt)
            #set previous attempt to the current_attempt
            previous_attempt=current_attempt
        #prevents the program from stopping execution due to an Index "Error" if the current attempt isn't a word
        except ValueError:
            pass
        #if we have built up the entire of the text as current attempt
        if len(current_attempt)==len(text):
            #break as we can't go anyfurther
            break
    #add the previous_attempt (the last attempt to be an actual word) to spaced text with a space after it
    spaced_text+=previous_attempt+" "
    #remove the spaces that are added before punctuation
    spaced_text=spaced_text.replace(" ,",",")
    spaced_text=spaced_text.replace(" .",".")
    spaced_text=spaced_text.replace(" !","!")
    spaced_text=spaced_text.replace(" ?","?")
    #remove the text we just added to spaced_text from text
    text=text[len(previous_attempt):]
    
    #resets current_attempt and previous_attempt
    current_attempt=""
    previous_attempt=""
    #print the spaced text so far
    print(spaced_text)
print(spaced_text)
