def main():
    book_path = "books/frankenstein.txt"
    content = get_file_content(book_path)
    num_words = count_words(content)
    char_dict = get_char_dict(content)
    chars_sorted_list = char_dict_to_sorted_list(char_dict)

    print(f"--- Begin report of {book_path} ---\n\n")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    print(f"--- End of report ---")

def count_words(content):
    words = content.split()
    return len(words)


def get_file_content(path):
    with open(path) as f:
        return f.read()

def get_char_dict(content):
    letters = {}
    content = content.lower()
    for letter in content:
        if letter not in letters:
            letters[letter] = 1
        else:
            letters[letter] += 1
    return letters

def sort_on(d):
    return d["num"]
    
def char_dict_to_sorted_list(char_dict):
    sorted_list = []
    for char in char_dict:
        sorted_list.append({"char": char, "num": char_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()