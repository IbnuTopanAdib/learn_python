def count_substring(string, sub_string):
    jumlah_kesamaan = 0
    sub_len = len(sub_string)
    for i in range(len(string) - sub_len + 1):
        if string[i:i+sub_len] == sub_string:
            jumlah_kesamaan += 1
    return jumlah_kesamaan

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)