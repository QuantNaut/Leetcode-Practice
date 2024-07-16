"""
Passed: 4/51 testcases
"""
def ladderLength(beginWord, endWord, wordList):
    if beginWord == endWord:
        return 0
    if endWord not in wordList:
        return 0
    
    # Remove the beginning and ending word from word list
    if beginWord in wordList:
        wordList.remove(beginWord)
    wordList.remove(endWord)
    
    if len(wordList) == 0: # Nothing to compare
        return 0
    
    used_words = list() # List of used words
    used_words.append(beginWord)
    
    while beginWord != endWord:
        for i in range(len(wordList)): # Loop through the word list
            # Compare transformed beginning word with ending word
            diff_count = 0
            for char_1, char_2 in zip(beginWord, endWord): # Pair the 2 words and loop through their characters
                if char_1 != char_2:
                    diff_count += 1
            if diff_count == 1:
                used_words.append(endWord)
                beginWord = endWord # Word transformation complete
                break
            
            # Identify the adjacent word
            diff_count = 0
            for char_1, char_2 in zip(beginWord, wordList[i]): # Do the same as above
                if char_1 != char_2:
                    diff_count += 1
            if diff_count == 1: # Difference of only a single letter - Adjacent word found
                used_words.append(wordList[i])
                beginWord = wordList[i] # Transform the beginning word
                break # Break out and re-enter loop again
            
            i = 0 # Reset loop index
    
    # return transformation sequence length
    return len(used_words)

def main():
    # Open and read from input file
    file = open('input3.txt', 'r') # Swap out name of the different input files as you like here
    beginWord = file.readline().strip() # Read the beginning word
    endWord = file.readline().strip() # Read the ending word
    wordList = file.readline().split(' ') # Read the word list
    print(ladderLength(beginWord, endWord, wordList))
    
# Run the program
if __name__ == '__main__':
    main()
