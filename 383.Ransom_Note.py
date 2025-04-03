class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_hash_table = {}
        for char in magazine:
            magazine_hash_table[char] = magazine_hash_table.get(char, 0) + 1
        for char in ransomNote:
            if char in magazine_hash_table:
                if magazine_hash_table[char] > 0:
                    magazine_hash_table[char] -= 1
                    continue
                return False
            else:
                return False
        return True 
