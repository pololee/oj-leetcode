def generate_binary_strings(n):
    if n == 0:
        return []

    if n == 1:
        return ['0', '1']

    answer = []
    for item in generate_binary_strings(n - 1):
        answer.append('0' + item)
        answer.append('1' + item)
    return answer

if __name__ == '__main__':
    print(generate_binary_strings(2))
