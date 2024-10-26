class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        count=1
        for c in range(1,len(word)):
            if word[c]==word[c-1]:
                count+=1

        return count

    