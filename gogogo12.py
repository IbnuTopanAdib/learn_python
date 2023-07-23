def mutate_string(string, position, character):
    string_list = list(string)
    string_list[position] = character
    result = "".join(string_list)
    return result
def mutate_string1(string, position, character):
    result = string[:position] + character +string[position+1:]
    return result
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    s_new1 = mutate_string1(s, int(i), c)
    print(s_new)
    print(s_new1)