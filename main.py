import os
def main():
    book_path = ("github.com/taranpitman/bookbot/books/f.txt")
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    let_dict = get_letter_count(text)
    let_sorted_dict = sort_letters(let_dict)
    print("----------Start of report----------")
    print(f"{num_words} words found in the document")
    print("count of all letters in the text:")
    for i in let_sorted_dict:
        if not i["char"].isalpha():
            continue
        print(f"The '{i['char']}' character was found {i['num']} times") 
    print("----------End of report----------")
 

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_letter_count(text):
    full_letter_count = {}
    text = text.lower()
    for l in text:
        if l in full_letter_count:
            full_letter_count[l] += 1
        else:
            full_letter_count[l] = 1
    #print(full_letter_count)
    return full_letter_count

def sort_on(a):
    return ["num"]

def sort_letters(ldict):
    sorted_list = []
    for c in ldict:
        sorted_list.append({"char": c, "num": ldict[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
  

main()