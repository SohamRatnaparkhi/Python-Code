
def subsrting_count(word, string):
    c = 0
    for i in range(len(string)):
        for j in range(len(string) + 1):
            if i != j:
                w = string[i:j]
                if w == word:
                    c += 1
    return c

def minion_game(string):
    # your code goes here
    stuart = 0
    stuart_word = []
    kevin = 0
    kevin_words = []
    vovels = ['A', 'E', 'I', 'O', 'U']
    for i in range(len(string)):
        c = string[i]
        for j in range(i + 1, len(string) + 1):
            #if i != j:
                #c = string[i]
                w = string[i: j]
                #if w == '':
                   # continue
                if w in kevin_words or w in stuart_word:
                    continue
                if c in vovels:
                    #if w != '':
                        kevin_words.append(w)
                        kevin += subsrting_count(w, string)
                        #stuart += subsrting_count(w, string)
                else:
                    #if w != '':
                        stuart_word.append(w)
                       # kevin += subsrting_count(w, string)
                        stuart += subsrting_count(w, string)
    '''for word in stuart_word:
        stuart += subsrting_count(word, string)
    for word in kevin_words:
        kevin += subsrting_count(word, string)
    '''
    

    if kevin > stuart:
        print (f"Kevin {kevin}")
    elif stuart > kevin:
        print (f"Stuart {stuart}")
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)