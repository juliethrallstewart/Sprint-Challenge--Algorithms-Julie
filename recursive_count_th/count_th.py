'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if len(word) == 0:
        return 0
    th = 'th'
    count = 0
    if th in word:
        count+=1
        new_word = word.replace(th,'',1)
        word = new_word
       
        return 1 + count_th(word[0:])
    return count
  
    
    
print(count_th('therethere'),2)
print(count_th('there'),1)
print(count_th('abcThthde'),1)
print(count_th('thththth'),4)


