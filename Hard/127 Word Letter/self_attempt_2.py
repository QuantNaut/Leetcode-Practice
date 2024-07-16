"""
Passed: 29/51 testcases
"""
from collections import deque

def ladderLength(beginWord, endWord, wordList):
    if beginWord == endWord:
        return 0
    if endWord not in wordList:
        return 0
    
    # Return 2 if strings are only 1 character in size
    if len(beginWord) == 1 and len(endWord) == 1:
        return 2
    
    used_words = list()
    word_queue = deque([beginWord])
    used_words.append(beginWord) # Remove starting word
    used_words.append(endWord) # Remove ending word
    curr_word = beginWord
    sequence_length = 1 # Start at 1 - includes starting word
    arrived_at_end = False
    
    while len(word_queue) > 0:
        curr_word = word_queue.popleft()
        remaining_words = list(set(wordList).difference(set(used_words))) # Filter out previously read words
        remaining_words.sort() # Sort the list
        remaining_words.insert(0, endWord) # Insert the ending word at front of list
        
        if len(remaining_words) > 0:
            for word in remaining_words:
                diff_count = 0
                for char_1, char_2 in zip(curr_word, word): # Pair the 2 words and loop through their characters
                    if char_1 != char_2:
                        diff_count += 1
                if diff_count == 1: # Difference of only a single letter - Adjacent word found
                    sequence_length += 1
                    used_words.append(word)
                    if word != endWord: # Only append to word queue if not the ending word
                        word_queue.append(word)
                    else:
                        arrived_at_end = True
                    break
    
    # Return the length
    if arrived_at_end:
        return sequence_length
    else:
        return 0

def main():
    # Open and read from input file
    file = open('input.txt', 'r') # Swap out name of the different input files as you like here
    beginWord = file.readline().strip() # Read the beginning word
    endWord = file.readline().strip() # Read the ending word
    wordList = file.readline().split(' ') # Read the word list
    print(ladderLength(beginWord, endWord, wordList))
    
# Run the program
if __name__ == '__main__':
    main()
