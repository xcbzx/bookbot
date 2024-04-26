def file_to_string(book_path):
    with open(book_path, 'r') as file:
        file_string = file.read()
    words = file_string.split()
    return words


def total_words():
    word_count = file_to_string(book_path)
    return len(word_count)


char_count = {}
def count_characters(book_path):
    list_of_words = file_to_string(book_path)
    for word in list_of_words:
        chars = list(word)
        for char in chars:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    return char_count
        


def main():
    book_path = "books/Frankenstein.txt"
    print("---Begin report of books/Frankenstein.txt ---")
    print(f"Words in book: {total_words()}")

    # sort logic here. ie: sort(count_chars)
    sorted_char_count = sorted(count_characters(book_path).items(), key=lambda x: x[1], reverse=True)
    for char, count in sorted_char_count:
        print(f"{char} was found {count} times")



if __name__ == "__main__":
    main()