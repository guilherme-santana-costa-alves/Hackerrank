def average(array):
    soma = sum(set(arr))
    tamanho = len(set(arr))
    media = soma / tamanho
    return media

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
