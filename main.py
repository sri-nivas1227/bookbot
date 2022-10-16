# from macpath import split


def count_words(content):
    word_list = content.split()
    print(type(word_list))
    # print(len(word_list))
    return len(word_list)


def count_letters(content):
    content = content.lower()
    word_list = content.split()
    letter_dict = {}
    for word in word_list:
        for i in word:
            if letter_dict.get(i) != None:
                letter_dict[i] += 1
            else:
                letter_dict[i] = 1
    # print(letter_dict)
    return letter_dict


def main():

    with open("./books/frankenstein.txt") as f:
        content = f.read()
        word_count = count_words(content)
        letters_count = count_letters(content)
        print("------ Report of books/frankenstein.txt------")
        print(f"{word_count} words found in the document")
        key_list = list(letters_count.keys())
        key_list.sort()

        for key in key_list:
            if key.isalpha():
                print(
                    f"The '{key}' character was found {letters_count[key]} times in the file")
        print("------End Report------")


main()
