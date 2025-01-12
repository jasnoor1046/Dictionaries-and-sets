# this program will count the frequency of the every word in the form of dictionary.
def word_frequency():
    text = input("Enter a text: ")
    words = text.split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1

        else:
            frequency[word] = 1

    return frequency


result = word_frequency()  # function calling
print("Word Frequency: ", result)
