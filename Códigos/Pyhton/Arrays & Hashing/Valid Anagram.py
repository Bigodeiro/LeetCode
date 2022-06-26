#https://leetcode.com/problems/valid-anagram/

#* Comparação por remoção: remover os caracteres de um string na outra, se não sobrar nada elas são anagramas
class Solution:
    def isAnagram(s: str, t: str) -> bool:

        s = list(s)
        t = list(t)

        for i in range(len(s)):
            if(s[i] in t):
                t.remove(s[i])
            else: return False
        if len(t) == 0:
            return True
        else: return False

#* Sorting: Organizar as strings e comparara-las
class Solution1:
    def isAnagram(s: str, t: str) -> bool:

        s = list(s)
        t = list(t)

        s.sort()
        t.sort()
        
        s = str(s)
        t = str(t)

        if s == t: return True
        else: return False
