# import ipdb
'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
counter=0
def count_th(word):

    # ipdb.set_trace()
    # print("This the current word value:", word)
    global counter
    print("This the is the current value of word:", word)
    # print("This the is the current value of word[]:", word[:2])


    if word == "":
        print(counter)
        return counter
    elif word[:2] == 'th':
        counter=counter+1
        count_th(word[2:])
    else:
        count_th(word[1:])

    return counter