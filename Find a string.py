def count_substring(string, sub_string):
    str_size = len(string)
    sub_size = len(sub_string)
    count = 0
    for i in range(0, str_size - sub_size + 1):
        if string [i:i + sub_size] == sub_string:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
