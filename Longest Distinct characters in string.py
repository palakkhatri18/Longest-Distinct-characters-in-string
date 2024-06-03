#Given a string S, find the length of the longest substring with all distinct characters. 
class Solution:

    def longestSubstrDistinctChars(self,S):
        
        ans=0
        j=[]
        k=0
        for i in range S:
            if i in j:
                j=j[j.index(i)+1:]
            j=j.append(i)
            ans=max(ans,len(j))
        return ans            
