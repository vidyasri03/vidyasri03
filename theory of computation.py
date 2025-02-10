import ssfsm #DFA
import time #run time

global COUNT #counting the number of times the substring is visible
COUNT = 0
def has_space(word):
    for char in word:
        if char.isspace():
            return True
    return False

def word_check(search_key, word):
    #A = ssfsm.Machine()
    for i in range(0, len(word)):
        flag = False #to check if the search_key is found or not
        if word[i] == search_key[0] and len(word[i:]) >= len(search_key):
            flag =fsm_word(search_key, word,i)
        if flag == True:
            print("found")
            global COUNT
            COUNT+=1
            continue
        else:
            print("not found")


def fsm(char,search_key_char):
    A = ssfsm.Machine()
    A().reset(A.One) #start state
    #print("HI")
    A().alphabet ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_()!@#%$^&*?:;1234567890.,"\/`~\''
    A.One[search_key_char] = A.Two
    A().polyfill() #assign the remaining transitions 
    A.Two = True #final state
    A(char)
    if A:
        return True
    else:
        return False


def fsm_word(search_key, word,n):
    if n+(len(search_key)) <= len(word) :
        sub_str = word[n:(n+(len(search_key)))]
        print(sub_str)
    else:
        return False
    for i in range(0, len(sub_str)):
        f = fsm(sub_str[i],search_key[i])
        if f == False:
            return False
    return True
        
#main
start = time.time() #start time of the execution
file = open('C:\\Users\\NEW\\Documents\\Python Scripts\\sample.txt', 'r')

# Read the entire contents of the file
file_contents = file.read()

# Close the file
file.close()

# Print the contents of the file
print(file_contents)
words = file_contents.split() 
while(True):
    search_key =  input("Enter the word to be searched and counted: ")
    if has_space(search_key) == False :
        break
    # Print each word
for word in words:
    print(word, end = "   ")
    word_check(search_key, word)
    print()
print("\"",search_key,"\" is found ", COUNT," number of times")
end = time.time()
print("Total time:", end-start)