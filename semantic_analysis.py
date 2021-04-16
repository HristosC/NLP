import re


####function####
def myfunction(list):
    string = ""
    for i in list:

        if (  # Intransitive Verbs (iv) with s
                i.__eq__("runs") or
                i.__eq__("hurts") or
                i.__eq__("walks") or
                i.__eq__("jumps") or
                i.__eq__("shoots")
        ):
            string += ("iv:s" + i + ",")

        if (  # Intransitive Verbs (iv) with q
                i.__eq__("running") or
                i.__eq__("hurting") or
                i.__eq__("walking") or
                i.__eq__("jumping") or
                i.__eq__("shooting")
        ):
            string += ("iv:q" + i + ",")

        if (  # Auxiliary Verbs (av)
                i.__eq__("is") or i.__eq__("does") or i.__eq__("are") or i.__eq__("do") or i.__eq__("did")
        ):
            string += ("av" + i + ",")

        if (  # Transitive Verbs (tv) with s
                i.__eq__("gives") or i.__eq__("gave:s")
        ):
            string += ("tv:s" + i + ",")

        if (  # Transitive Verbs (tv) with q
                i.__eq__("give") or i.__eq__("giving:q")
        ):
            string += ("tv:q" + i + ",")

        if (  # Verbs (v) with s
                i.__eq__("needs") or i.__eq__("jumps") or
                i.__eq__("hates") or i.__eq__("has") or
                i.__eq__("loves") or i.__eq__("kicks") or
                i.__eq__("chase") or i.__eq__("chased")
        ):
            string += ("v:s" + i + ",")

        if (  # Verbs (v) with q
                i.__eq__("need") or i.__eq__("hate") or i.__eq__("have") or
                i.__eq__("love") or i.__eq__("kick") or i.__eq__("jump")
        ):
            string += ("v:q" + i + ",")

        if (  # Adjectives (adj)
                i.__eq__("scary") or i.__eq__("tall") or
                i.__eq__("short") or i.__eq__("blonde") or
                i.__eq__("slim") or i.__eq__("fat")
        ):
            string += ("adj" + i + ",")

        if (  # Adverb (adv)
                i.__eq__("quickly") or
                i.__eq__("slowly") or
                i.__eq__("independently")
        ):
            string += ("adv" + i + ",")

        if ( # Noun (n)
                i.__eq__("food") or i.__eq__("cat") or i.__eq__("cats") or i.__eq__("dog") or
                i.__eq__("dogs") or i.__eq__("book") or i.__eq__("books") or i.__eq__("feather") or
                i.__eq__("feathers") or i.__eq__("baby") or i.__eq__("babies") or i.__eq__("boy") or
                i.__eq__("boys") or i.__eq__("girl") or i.__eq__("girls") or i.__eq__("icecream") or
                i.__eq__("icecreams")
        ):
            string += ("n" + i + ",")

        if (  # Proper Nouns (pn)
                i.__eq__("mary")
                or i.__eq__("john")
                or i.__eq__("tomy")
        ):
            string += ("pn" + i + ",")

        if (  # Determiner (det)
                i.__eq__("the")
                or i.__eq__("a")
                or i.__eq__("an")
        ):
            string += ("det" + i + ",")

    string = string[:-1]  # edw diagrafoyme to teleytaio komma

    string = string.split(",")  # edw xwrizioyme tis le3eis me ta kommata
    i = 0

    while i < len(string):

        # Noun Phrase (np)
        if (  # sem_np(N) 	--> sem_det(_), sem_n(N).
                string[i][0:3] == "det" and
                string[i + 1][0] == "n"
        ):
            string[i] = "np" + string[i + 1][1:]
            del string[i + 1]
            i += 1

        elif (  # sem_np(N)	--> sem_pn(N).
                string[i][0:2] == "pn"
        ):
            string[i] = "np" + string[i][2:]
            i += 1

        elif (  # sem_np(N) 	--> sem_n(N).
                string[i][0] == "n"
        ):
            string[i] = "np" + string[i][1:]
            i += 1
        else:
            i += 1

    i = 0

    #  verb phrase
    while i < len(string):

        if (  # sem(1,Sem) --> sem_np(N), sem_vp(1,V,N1),  	{Sem=..[V,N,N1]}.
                string[i][0:2] == "np" and string[i + 1][0:3] == "v:s" and string[i + 2][0:2] == "np"
        ):

            string[i] = string[i+1][3:] + "(" + string[i][2:] + "," + string[i+2][2:] + ")"
            del string[(i + 1):(i + 3)]
            i += 1

        elif (  # sem(2,Sem) --> sem_np(N), sem_vp(2,_,A),  	{Sem=..[A,N]}.
                string[i][0:2] == "np" and string[i + 1][0:4] == "avis" and string[i + 2][0:3] == "adj"
        ):

            string[i] = string[i + 2][3:] + "(" + string[i][2:] + ")"
            del string[(i + 1):(i + 3)]
            i += 1

        elif (  # sem(4,Sem) --> sem_np(N), sem_iv(V,s), sem_adv(A),	{Sem=..[V,N,A]}.
                string[i][0:2] == "np" and
                string[i + 1][0:4] == "iv:s" and
                string[i + 2][0:3] == "adv"
        ):

            string[i] = string[i + 1][4:] + "(" + string[i][2:] + "," + string[i+2][3:] + ")"
            del string[(i + 1):(i + 3)]
            i += 1

        elif (  # sem(3,Sem) --> sem_np(N), sem_iv(V,s),       	{Sem=..[V,N]}.
                string[i][0:2] == "np" and
                string[i + 1][0:4] == "iv:s"
        ):

            string[i] = string[i+1][4:] + "(" + string[i][2:] + ")"
            del string[(i + 1):(i + 2)]
            i += 1
        elif (  # sem(5,Sem) -->sem_np(N), sem_tv(V,s), sem_np(N1), sem_np(N2), {Sem=..[V,N,N1,N2]}.
                string[i][0:2] == "np" and
                string[i + 1][0:4] == "tv:s" and
                string[i + 2][0:2] == "np" and
                string[i + 3][0:2] == "np"
        ):

            string[i] = string[i + 1][4:] + "(" + string[i][2:] + "," + string[i + 2][2:] + "," + string[i+3][2:] + ")"
            del string[(i + 1):(i + 4)]
            i += 1
        else:
            i += 1

    string = "".join(string)
    print(string)

f = open('mary.txt', 'r').read()

list_inside = []
pattern = re.compile("[a-zA-Z0-9]+[\.!\?]+[a-zA-Z0-9]+")  # Here we create a pattern for a later check statement
f = f.split()  # we split the txt file into a string list ( the split happens whenever we meet a "." symbol)

for x in f:

    if x.__contains__(".") or x.__contains__("!") or x.__contains__("?"):  # if statement to check if the word is the
        # last one of the sentence ( that's why we check for the "." , "!" , "?" symbols)

        if pattern.match(x):  # if the word matches the pattern that we gave above.

            x = re.sub('[.!?]', ' ', x)  # we replace every "." "!" "?" symbol with a blank space
            x = re.sub('[\'\[\],:;)(\-]', '', x)  # we delete every symbol ( the ones that are included
            # in the regex) from the word
            x = x.split()  # here we split the two words based on the blank space that we created earlier
            list_inside.append(x[0])  # we first put the first word from the split function and insert it to our list
            myfunction(list_inside)
            list_inside = []  # we empty the list inside so that we can append the next sentence
            x = re.sub('[\'\[\],:;)(\-]', '', x[-1])  # we take the second word ( and last word ) of the split
            # and we delete every symbol that the word has.
            list_inside.append(x)  # we take the x that we modified from above and we put it as a starter to our list.

        else:  # if the word doesnt match the pattern.

            x = re.sub('[.!?]', '', x)  # we delete every "." , "!" , or "?" that exists as a symbol inside the word

            x = re.sub('[\'\[\],:;)(\-]', '', x)  # we delete every symbol ( the ones that are included
            # in the regex) from the word

            list_inside.append(x)  # we append the inside list with x
            myfunction(list_inside)
            list_inside = []  # we empty the list inside so that we can append the next sentence

    else:

        x = re.sub('[\'\[\],:;)(\-]', '', x)  # if the word is not the last word of the
        # sentence then we delete every symbol that is inside that word
        list_inside.append(x)  # we append the word to the list inside
