# import ipdb
'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    # ipdb.set_trace()
    # print("This the current word value:", word)
    counter=0

    if word == "":
        print(counter)
        return counter
    if word[0:1] == 'th' and len(word)>=1:
        counter=counter+1
        count_th(word[2:])
    else:
        count_th(word[1:])

count_th("testth")