sentence = input("please enter the sentence: ")

sentence_list = sentence.split()

for word in sentence_list:
    print("{} : {}".format(word, sentence_list.count(word)))


sentence2 = input("enter the sentence you want to reverse")

