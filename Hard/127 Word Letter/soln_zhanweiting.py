"""
Community answer from Zhan Wei Ting, dated 30 Jul 2019
"""
from collections import deque
from collections import defaultdict

def ladderLength(beginWord: str, endWord: str, wordList: list[str]) -> int:
    if endWord not in wordList or not endWord or not beginWord or not wordList:
        return 0

    L = len(beginWord)
    all_combo_dict = defaultdict(list)
    for word in wordList:
        for i in range(L):
            all_combo_dict[word[:i] + "*" + word[i + 1 :]].append(word)

    queue = deque([(beginWord, 1)])
    visited = set()
    visited.add(beginWord)
    while queue:
        current_word, level = queue.popleft()
        for i in range(L):
            intermediate_word = current_word[:i] + "*" + current_word[i + 1 :]
            for word in all_combo_dict[intermediate_word]:
                if word == endWord:
                    return level + 1
                if word not in visited:
                    visited.add(word)
                    queue.append((word, level + 1))

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
