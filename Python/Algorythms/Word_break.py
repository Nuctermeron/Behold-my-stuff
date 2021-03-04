class Solution:
    def wordBreak(self, s, wordDict):
        if not wordDict: return False
        intervals = []
        
        for w in wordDict:
            startIndex = 0
            while True:
                try:
                    index = s.index(w, startIndex)
                except ValueError:
                    break
                intervals.append([index, index+len(w)-1])
                startIndex = index + 1
        
        intervals.sort()
        
        searching = {0}
        for interval in intervals:
            start, end = interval
            if start in searching:
                if end == len(s)-1:
                    return True
                else:
                    searching.add(end+1)
        
        return False
    
s = "leetcode"
wordDict = ["leet","code"]
result = Solution()
print(result.wordBreak(s,wordDict))
