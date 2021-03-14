f = open("file.txt", "r")
f_text = f.readlines()
f_mod_text = []
for line in f_text:
    f_mod_text.append(line[:len(line)-1])
new_text = ""
for line in f_mod_text:
    for character in line:
        if character.isalpha() or character.isspace() or character == "'":
            new_text += character
    new_text += " "
new_text = new_text.lower()
words_list = new_text.split(" ")
for word in words_list:
    if "n't" in word:
        words_list.append(word[:len(word)-3])
        words_list.append("not")
        words_list.remove(word)
    elif "'s" in word:
        words_list.append(word[:len(word)-2])
        words_list.append("is")
        words_list.remove(word)
words_dict = {}
for word in words_list:
    if word in words_dict.keys():
        words_dict[word] += 1
    else:
        words_dict.update({word:1})
words_dict.pop("")
words_tuple_list = list(words_dict.items())
def bubble_sort(words_dict, words_tuple_list):
    n = len(words_dict)
    array = list(words_dict.values())
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                words_tuple_list[j], words_tuple_list[j+1] = words_tuple_list[j+1], words_tuple_list[j]
                already_sorted = False
        if already_sorted:
            break

    return words_tuple_list

words_tuple_list = bubble_sort(words_dict, words_tuple_list)
words_tuple_list = words_tuple_list[::-1]
for tuple in words_tuple_list:
    print(tuple)





