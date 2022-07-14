import textwrap

def wrap(string, max_width):
    wraper = textwrap.TextWrapper(width = max_width)
    phrase = textwrap.dedent(text = string)
    result = wraper.fill(text = phrase)
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
