s=input()
vowels,consonants=0,0
for i in range(len(s)):
    if s[i] in "aeiou":
        vowels+=1
    else:
        consonants+=1
print(f"Number of vowels:{vowels}")
print(f"Number of consonants:{consonants}")
