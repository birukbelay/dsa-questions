"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number 
could represent. Return the answer in any order.
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]


no of output string =4^n
time complexity O(n*4^n)
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
        "2": 'abc', "3":"def", "4":"ghi", "5":"jkl", "6":"mno",
        "7":'pqrs', "8":'tuv', "9":'wxyz'        
       
        }
        res =[]

        
        def backtrack(i, curStr):
            if len(curStr) ==len(digits):
                res.append(curStr)
                return
            for c in d[digits[i]]:
                backtrack(i +1, curStr + c)
        if digits:
            backtrack(0, '')
        return res

