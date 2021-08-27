v = [
    [0, 0, 0, 0],
    [1.45, 1.81, 2.36, 1.79],
    [2.64, 3.16, 3.79, 2.51],
    [3.61, 4.15, 4.66, 2.81],
    [4.41, 4.89, 5.19, 2.93],
    [5.06, 5.44, 5.51, 2.97]
]

result_list = [0, 0, 0, 0]


def calculate(k, sk):
    if k == 1:
        return v[sk][0]
    result = 0
    for i in range(0, sk + 1):
        tem_result = v[i][k - 1] + calculate(k - 1, sk - i)
        if (tem_result > result):
            result_list[k - 1] = i
            result = tem_result
    calculate(k - 1, sk - result_list[k - 1])
    tem_num = 5
    for index in range(1, 4):
        tem_num = tem_num - result_list[index]
    result_list[0] = tem_num
    return result


if __name__ == '__main__':
    result = calculate(4, 5)
    for item in result_list:
        print(item, end="  ")
    print("\n%.2f" % result)
