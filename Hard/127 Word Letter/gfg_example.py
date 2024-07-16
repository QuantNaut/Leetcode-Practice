"""
Passed: 34/51 testcases
Source: https://www.geeksforgeeks.org/word-ladder-length-of-shortest-chain-to-reach-a-target-word/
"""
from collections import deque

# Returns length of shortest chain
# to reach 'target' from 'start'
# using minimum number of adjacent moves
def ladderLength(beginWord, endWord, wordList):
    if beginWord == endWord:
        return 0
    if endWord not in wordList:
        return 0
    
    # To store the current chain length
    # and the length of the words
    level, wordlength = 0, len(beginWord)
    
    # Push the starting word into the queue
    Q = deque()
    Q.append(beginWord)
    
    # While the queue is non-empty
    while (len(Q) > 0):
        # Increment the chain length
        level += 1
        
        # Current size of the queue
        sizeofQ = len(Q)
        # Since the queue is being updated while
        # it is being traversed so only the
        # elements which were already present
        # in the queue before the start of this
        # loop will be traversed for now
        for i in range(sizeofQ):
            # Remove the first word from the queue
            word = [j for j in Q.popleft()]
            
            # For every character of the word
            for pos in range(wordlength):
                # Retain the original character
                # at the current position
                orig_char = word[pos]
                
                # Replace the current character with
                # every possible lowercase alphabet
                for c in range(ord('a'), ord('z')+1):
                    word[pos] = chr(c)

                    # If the new word is equal
                    # to the target word
                    if ("".join(word) == endWord):
                        return level + 1
                    
                    # Remove the word from the set
                    # if it is found in it
                    if ("".join(word) not in wordList):
                        continue
                    
                    wordList.remove("".join(word))
                    
                    # And push the newly generated word
                    # which will be a part of the chain
                    Q.append("".join(word))
                    
                # Restore the original character
                # at the current position
                word[pos] = orig_char
    
    # Return the length
    return 0

def main():
    # Open and read from input file
    file = open('input8.txt', 'r') # Swap out name of the different input files as you like here
    beginWord = file.readline().strip() # Read the beginning word
    endWord = file.readline().strip() # Read the ending word
    wordList = file.readline().split(' ') # Read the word list
    print(ladderLength(beginWord, endWord, wordList))
    
# Run the program
if __name__ == '__main__':
    main()
