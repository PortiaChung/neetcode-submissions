import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        start = {beginWord}
        end = {endWord}
        if endWord not in words:
            return 0
        dist = 1
        while start and end:
            if len(start) > len(end):
                start,end = end,start
            tmp = set()
            for word in start:
                for i in range(len(word)):
                    char = word[i]
                    for c in string.ascii_lowercase:
                        if char == c:
                            continue
                        else:
                            new_word = word[:i] + c + word[i+1:]
                            if new_word in end:
                                return dist+1
                            if new_word in words:
                                tmp.add(new_word)
                                words.remove(new_word)
            dist+=1
            start = tmp
        return 0

        