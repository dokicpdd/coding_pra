from collections import Counter
from typing import List


def longestPalindrome_substring(self, s: str) -> str:
        '''
         return the longest palindrome as a substring of s
        '''
        #brute_force
        max=0
        max_str=''
        l=len(s)
        for i in range(l-1):
                for j in range(i+1,l+1):
                        cur=s[i:j]
                        if is_palindrome(cur) and len(cur)>max:
                               max=len(cur)
                               max_str=cur
        return max_str

def is_palindrome(s):
        l=len(s)-1
        i=0
        while i<l:
            if s[i]!=s[l]:
                  return False
            i+=1
            l-=1
        return True                        

def longestPalindrome(self, s: str) -> int:
        '''
         return the length of the longest palindrome
         that can be built with those letters.        
        '''
        if len(s)==1:
                return 1

        max=0
        odd=0
        s={}

        for c in s:
                if c in s:
                       s[c]+=1
                else:
                       s[c]=1
        for count in s.values():
        #char that appears for even number of times can form palindrome
        #if reminder of count%2 is 1, it means num is odd and we get rem-1 to get a even
                rem=count%2
                add=count-rem
                max+=add
                if rem==1:
                       odd=1
        return max+odd
        
def longestPalindrome(self, s: str) -> int:
        '''
        same question as the upper one,but different soultion
        '''
        check = set()
        ans = 0
        for c in s:
            if c in check:
                ans += 2
                check.remove(c)
            else:
                check.add(c)
        return ans+1 if check else ans
        
def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        find the length of the longest substring
        without duplicate characters.
        '''
        #two pointers and sliding window
        seen=set()
        l=len(s)
        max=0
        left=0

        #right is the index, and c is the current string,a char actually
        for right,c in enumerate(s):
                while c in seen:
                      seen.remove(s[left])
                      left+=1
                seen.add(c)
                diff=right-left+1
                if diff>max:
                       max=diff
        return max

def encode_decode(something):
        output=''
        def encode(strs:list[str])->str:
                result=''
                for s in strs:
                       l=len(str)
                       result+=str(l)+'#'+s
                return result
        def decode(str)->list[str]:
                result=[]
                l=len(str)
                i,j=0
                while(j<l):
                        while str[j]!='#':
                              j+=1
                        i=j+1
                        length=str[j-1]
                        cur_str=str[i,i+length]
                        result.append(cur_str)
                        j=i+length
                return result
                
        if type(something)==str:
               output=decode(something)
        if type(something)==list:
               output=encode(something)
        return output

def scramble(s1, s2):

        '''
        Complete the function scramble(str1, str2) that returns true 
        if a portion of str1 characters can be rearranged to match str2,
        otherwise returns false.
        portion does not mean substring, any char from s1
        '''

        freq_s = Counter(s1)
        
        # Now loop through unique chars in s2 (avoids checking duplicates)
        for c, count_in_t in Counter(s2).items():
                if freq_s.get(c, 0) < count_in_t:
                        return False
        return True

def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string ""
        '''
        min_s=min(strs,key=len)
        n=len(min_s)
        i=0
        for c in min_s:
                for str in strs:
                        if c!=str[i]:
                             return min_s[:i]
                i+=1
        return min_s
