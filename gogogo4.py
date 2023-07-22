if __name__ == '__main__':
    N = int(input("masukan jumlah: "))
    arr = []
    
    for _ in range(N):
        operation_index_elemen = input('masukan operasi, index, elemen : ')
        parts = operation_index_elemen.split()
        operation = parts[0]
        
        if operation == 'insert':
            index = int(parts[1])
            elemen = int(parts[2])  # Assuming you are working with integers in the list
            arr.insert(index, elemen)
        elif operation == 'append':
            elemen = int(parts[1])
            arr.append(elemen)
        elif operation == 'remove':
            elemen = int(parts[1])
            arr.remove(elemen)
        elif operation == 'pop':
            arr.pop()
        elif operation == 'sort':
            arr.sort()
        elif operation == 'reverse':
            arr.reverse()
        elif operation == 'print':
            print(arr)
