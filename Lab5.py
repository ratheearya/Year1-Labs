def isVowel(s): #Checks one character to see if it is a vowel
    s = s.lower() #set string to lower case so I don't have to check for uppercase vowels
    if(s == 'a' or s == 'e' or s =='i' or s =='o' or s == 'u'):
        return True
    else:
        return False

def countVowels(s): #Counts the number of vowels in a string
    count = 0
    for i in range(len(s)):
        if (isVowel(s[i])):
            count += 1
    return count

def isStable(s): #Checks whether or not two halfs of a string have the same number of vowels
    index_half = int(len(s) / 2) #splits string to two halfs
    if(len(s) % 2 == 0): #Checks to see if there are an even number of characters in the string.
        if(countVowels(s[index_half:]) == countVowels(s[:index_half])): # checks if both sides are equal to each other
            return True
        else:
            return False
    else:
        if(countVowels(s[:index_half]) == countVowels(s[index_half + 1:])): #added one to the second half index in order to skip the middle value
            return True
        else:
            return False

def hasDoubleLetters(s): #Checks to see if a string has two same letters next to each other
    s = s.lower() #set entire string to lowercase to easily compare without worrying about caps
    for i in range(len(s)-1): #subract one from the left because when you get to the last charcacter and add one to the index you will get an error because there is no character there
        if (s[i] == s[i+1]): # checks if the 1st character is equal to the 2nd character
            return True
    return False

def interleave(word1, word2): #Alternate characters of a string and mix them together ("123","456") --> "142536"
    s = ""
    if(len(word1) != len(word2)): #checks to see if the len are equal to each other.
        if(len(word1) < len(word2)): #If there are less letters in word 1, after that string ends we add the rest of word2
            for i in range(len(word1)):
                s+= word1[i] #next two lines alternate their letters and add them to string s
                s+= word2[i]
            s+= word2[len(word1):] #add the rest of word2 since it is longer
        else:
            for i in range(len(word2)): # same code as above but this time word2 length < word1 length
                s+= word1[i]
                s+= word2[i]
            s+= word1[len(word2):]
    else:
        for i in range(len(word1)): #if the words have the same length it is much simpler
            s += word1[i]
            s += word2[i]
    return s

def lcp(s1, s2): #Find the longest prefix before the letters start differing("hello","hector") --> "he"
    s1.lower() #set s1 and s2 to all lowercase to avoid error with caps
    s2.lower()
    s = ""
    i = 0
    while(s1[i] == s2[i]):
        s += s1[i]
        if(s1[i] == s1[len(s1)-1] or s2[i] == s2[len(s2)-1]):
            break
        i += 1
    return s
    
def extractLastName(full_name,email): #Find the last name from the given input
    last_name = email[1 : email.find('@')] #start from the 2nd index to the @ to get the last name
    full_name_short = ''
    n2 = ''

    for i in range(len(last_name)): 
        if(last_name[i] == '0' or last_name[i] == '1' or last_name[i] == '2' or last_name[i] == '3' or last_name[i] == '4' or last_name[i] == '5' or last_name[i] == '6' or last_name[i] == '7' or last_name[i] == '8' or last_name[i] == '9'):
            last_name = last_name[:i-1] #remove all letters from the end of the email to get the true last name

    for i in range(len(full_name)):
        if(full_name[i] != ' '):
            full_name_short += full_name[i] # delete all of the spaces from the full name in order to compare them later

    x = -1
    full_name_short = full_name_short.lower() #make the extracted last name and the full name compareable
    last_name = last_name.lower()

    for i in range(len(last_name)):
        if(last_name[x] == full_name_short[x]): #getting the index where the last name starts
            x -= 1
    
    n2 = full_name[x:] #returning the full_name starting from the index from previous for loop

    if(n2[0] == ' '): #fixing error where space is added to the front of the last name
        n2 = n2[1:]

    return n2

def capitalize_letter(s, n):
    return s[:n] + s[n:].capitalize()

if __name__ == "__main__":
    print ("countVowels: " , countVowels("Hello"))
    print ("isStable: " , isStable("jtbsaasEsialltQ"))
    print ("hasDoubleLetters: " , hasDoubleLetters("jello") , hasDoubleLetters("ironic"))
    print (extractLastName("John Smith Clyde Alpha", "jclydealpha234@gmail.com"))
