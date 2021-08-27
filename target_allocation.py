import numpy as np
from itertools import permutations

values = [[0, 0, 0, 0],
          [1.45, 1.81, 2.36, 1.79],
          [2.64, 3.16, 3.79, 2.51],
          [3.61, 4.15, 4.66, 2.81],
          [4.41, 4.89, 5.19, 2.93],
          [5.06, 5.44, 5.51, 2.97]]


def permute(number, target):
    # 排列所有可能性
    num = []
    for i in range(number + 1):
        num.append(i)
    num = num * target
    combination_list = list(permutations(num, target))  # 对num进行组合，便于穷举
    finalist = []
    for i in combination_list:
        if np.array(i).sum() == number:
            finalist.append(i)  # 将和为5的组合加到列表
    finalist = list(set(finalist))  # 去除重复的元素,把set格式转成list
    # print(finalist)
    return finalist


def main_enumeration():
    final_list = permute(5, 4)
    value_list = []
    for table in final_list:
        value1 = values[table[0]][0]  # value1 = 8 * (1 - np.exp(-0.2 * table[0]))
        value2 = values[table[1]][1]  # value2 = 7 * (1 - np.exp(-0.3 * table[1]))
        value3 = values[table[2]][2]  # value3 = 6 * (1 - np.exp(-0.5 * table[2]))
        value4 = values[table[3]][3]  # value4 = 3 * (1 - np.exp(-0.9 * table[3]))
        value = value1 + value2 + value3 + value4
        value_list.append(value)

    max_value = np.max(np.array(value_list))  # 最大值
    max_value_index = np.argmax(value_list)
    max_value_num = np.array(final_list)[max_value_index]  # 最大值的组合
    return max_value, max_value_num


def main_dynamic(v):
    target_num = len(v)   # 目标个数
    missile_num = len(v[0])   # 导弹数量
    max_v = [0 for _ in range(missile_num)]
    s = [[0] for _ in range(missile_num)]
    # print(target_num, missile_num, max_v, s)
    for i in range(target_num):
        for j in range(missile_num - 1, -1, -1):
            if i == 0:
                max_v[j] = v[i][j]
                s[j] = [j]
            else:
                f = 0
                for k in range(j, 0, -1):
                    if max_v[j] < max_v[j - k] + v[i][k]:
                        f += 1
                        max_v[j] = max_v[j - k] + v[i][k]
                        s[j - k].append(k)
                        s[j] = s[j - k].copy()
                        s[j - k].pop()
                if f == 0:
                    s[j].append(0)
    return max_v[-1], s[-1]


def select(ways):
    if ways == 'dynamic':
        max_value, s_final = main_dynamic(np.array(values).transpose())
        # print(np.array(s_final))
        print('------------动态规划------------')
        print('最佳火力分配方案是：\n对目标1,2,3,4发射的导弹数量分别为：%d, %d, %d, %d' %
              (s_final[0], s_final[1], s_final[2], s_final[3]))
        print('最大价值为：', max_value)
    else:
        max_value, max_value_num = main_enumeration()
        # print(max_value_num)
        print('------------穷举法------------')
        print('最佳火力分配方案是：\n对目标1,2,3,4发射的导弹数量分别为：%d, %d, %d, %d' %
              (max_value_num[0], max_value_num[1], max_value_num[2], max_value_num[3]))
        print('最大价值为：', max_value)


if __name__ == '__main__':
    # way = 'dynamic'
    way = 'enumeration'
    select(way)
