def sum_of_nested_arrays(arrys):
    if not arrys:
        return 0

    if isinstance(arrys[0], list):
        return sum_of_nested_arrays(arrys[0]) + sum_of_nested_arrays(arrys[1:])

    return arrys[0] + sum_of_nested_arrays(arrys[1:])

if __name__ == '__main__':
    input_arrys = [1, 2, [1, 2], 3, [5]]
    print(sum_of_nested_arrays(input_arrys))
