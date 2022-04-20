def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    arr = sentence.split(" ")
    arr = reversed(arr)
    new_sentence =""
    for i in arr:
        word =""
        for j in i:
            if j.islower():
                word+=j.upper()
            elif j.isupper():
                word+=j.lower()
        new_sentence+=word+" "
    print(new_sentence)

reverse_words_order_and_swap_cases("rUns dOg")