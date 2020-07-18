'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # print(word)
    # if len(word) < 2:
    #     return 0
    # if word[:3] != 'th':
    #     count_th(word[2:])
    # if word[:3] == 'th':
    #     return 1
    # count = count_th(word[2:])
    # return count
    print(word)
    if word.find('th') < 0:
        return 0
    if word.find('th') >=0:
        return 1

    position = word.find('th')
    count = count_th(word[position+2:])
    return count

print(count_th('abcthefthghith'))