* 127\. Word Letter

A **transformation sequence** from word _beginWord_ to word _endWord_ using a dictionary wordList is a sequence of words _beginWord -> s1 -> s2 -> ... -> sk_ such that:

- Every adjacent pair of words differs by a single letter.
- Every _si_ for _1 <= i <= k_ is in _wordList_. Note that _beginWord_ does not need to be in _wordList_.
- _sk == endWord_

Given two words, _beginWord_ and _endWord_, and a dictionary _wordList_, return the **number of words in the shortest transformation sequence** from _beginWord_ to _endWord_, or _0_ if no such sequence exists.

Official page: https://leetcode.com/problems/word-ladder/description/

** Example 1
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

** Example 2
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

** Constraints:
- _1 <= beginWord.length <= 10_
- _endWord.length == beginWord.length_
- _1 <= wordList.length <= 5000_
- _wordList[i].length == beginWord.length_
- _beginWord_, _endWord_, and _wordList[i]_ consist of lowercase English letters.
- _beginWord != endWord_
All the words in _wordList_ are **unique**.
