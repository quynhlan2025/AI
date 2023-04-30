# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Ex8: Let user type 2 words in English as input. Print out the output
# which is the shortest chain according to the following rules:
# - Each word in the chain has at least 3 letters
# - The 2 input words from user will be used as the first and the last words of the chain
# - 2 last letters of 1 word will be the same as 2 first letters of the next word in the chain
# - All the words are from the file wordsEn.txt
# - If there are multiple shortest chains, return any of them is sufficient

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    f = open("wordsEn.txt", "r")
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    pre_word = ''
    for x in f:
        if len(x) >= 3:
            last_str = get_last_2_letter(pre_word)
            first_str = get_first_2_letter(x)
            if last_str == first_str:
                print("The shortest chain is: ")
                print("Preword:", pre_word)
                print("word",x)
            pre_word = x


def get_first_2_letter(Str):
    first_two = Str[:2]
    return first_two


def get_last_2_letter(Str):
    # get input

    N = 3

    # get length of string
    length = len(Str)

    # create a new string of last N characters
    Str2 = Str[length - N:]

    # print Last N characters

    return Str2.replace("\n", "")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # last2letter = get_last_2_letter('PyCharm');
    # print(last2letter)
    # last2letter = get_last_2_letter('PyCharm');
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
