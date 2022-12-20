def canConstruct(ransomNote, magazine):
    magazine = list(magazine)
    for i in ransomNote:
        if i not in magazine:
            return False
        magazine.remove(i)
    return True