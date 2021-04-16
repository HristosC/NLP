import re

f = open('test.txt', 'r').read()  # We open the file here

pattern = re.compile(
    "[a-zA-Z0-9]+[\.!\?]+[a-zA-Z0-9]+")  # Here we create a pattern for a later check statement
# if the writer of the story made a mistake
# and didn't leave a blank space after a "."
f = f.split()  # we split the txt file into a string list ( the split happens whenever we meet a space)
list_outside = []  # we create the outside list that contains inside a list of sentences
list_inside = []  # this is the inside list that contains all the words inside a list

for x in f:  # here we create a loop so we can check every word in the text

    if x.__contains__(".") or x.__contains__("!") or x.__contains__("?"):  # if statement to check if the word is the
        # last one of the sentence ( that's why we check for the "." , "!" , "?" symbols

        if pattern.match(x):  # if the word matches the pattern that we gave above.

            x = re.sub('[.!?]', ' ', x)  # we replace every "." "!" "?" symbol with a blank space
            x = re.sub('[\'\[\],:;)(\-]', '', x)  # we delete every symbol ( the ones that are included
            # in the regex) from the word
            x = x.split()  # here we split the two words based on the blank space that we created earlier
            list_inside.append(x[0])  # we first put the first word from the split function and insert it to our list
            list_outside.append(list_inside)  # we append the list_inside to the list_outside

            list_inside = []  # we empty the list inside so that we can append the next sentence
            x = re.sub('[\'\[\],:;)(\-]', '', x[-1])  # we take the second word ( and last word ) of the split
            # and we delete every symbol that the word has.
            list_inside.append(x)  # we take the x that we modified from above and we put it as a starter to our list.

        else:  # if the word doesnt match the pattern.
            x = re.sub('[.!?]', '', x)  # we delete every "." , "!" , or "?" that exists as a symbol inside the word
            x = re.sub('[\'\[\],:;)(\-]', '', x)  # we delete every symbol ( the ones that are included
            # in the regex) from the word
            list_inside.append(x)  # we append the inside list with x
            list_outside.append(list_inside)  # we append list_inside to the list_outside

            list_inside = []  # we empty the list inside so that we can append the next sentence

    else:
        x = re.sub('[\'\[\],:;)(\-]', '', x)  # if the word is not the last word of the
        # sentence then we delete every symbol that is inside that word

        list_inside.append(x)  # we append the word to the list inside

print(list_outside)  # we print the final list that is the list outside
