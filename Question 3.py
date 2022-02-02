
# Program to check if two given strings are anagrams

def check_anagram(str1,str2):
    if set(str1.lower())==set(str2.lower()):
        print("Yes,Given two strings are anagrams")
    else:
        print("No,Given two strings are not anagrams")

check_anagram("Mary","Army")
