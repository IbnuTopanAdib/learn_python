sentence2 = input("enter the sentence you want to reverse: ")
def reverse_sentence(sentence):
    sentence_list = sentence.split()
    sentence_list.reverse()
    reversed_sentence =" ".join(sentence_list)
    return reversed_sentence


rs = reverse_sentence(sentence2)
print(rs)



