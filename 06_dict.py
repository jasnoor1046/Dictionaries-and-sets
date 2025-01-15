def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False

    # initializing two empty dictionaries
    count1 = {}
    count2 = {}

    for char in str1:
        count1[char] = count1.get(char, 0) + 1

    for char in str2:
        count2[char] = count2.get(char, 0) + 1

    return count1 == count2


str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
# function calling
result = are_anagrams(str1, str2)
# displaying the result
if result:
    print(f"{str1} and {str2} are anagrams.")

else:
    print(f"{str1} and {str2} are not anagrams.")
