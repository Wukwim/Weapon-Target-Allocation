import numpy as np


const_a = [0.2,0.3,0.5,0.9]
kill_value = [8,7,6,3]

def Plan(object_number,resourse_number,value_list):
    gain_list=[]  #最大价值下各目标中弹数
    f=[]   #当前价值
    temp=[] #计算中的价值
    # 前i个目标打j弹获得最大利益时，打第i个目标几颗弹，因以0开始，即i=0时即为前1个目标，以此类推，弹是从0开始
    a=np.zeros((object_number,resourse_number+1))
    # 第一阶段，只有第一个目标中弹
    for j in range(resourse_number+1):
        f.append(value_list[0][j])
        temp.append(value_list[0][j])
        a[0][j] = j


    for k in range(1,object_number):
        for j in range(resourse_number+1):           # 初始化
            #f[j] = 0
            a[k][j] = 0
        for j in range(resourse_number+1):           # j为该阶段可使用的资源总数
            for i in range(j+1):                     # i为分配给下一个目标的弹量
                if temp[j-i] + value_list[k][i] > f[j]:
                    f[j] = temp[j-i] + value_list[k][i]
                    a[k][j] = i

        for j in range(resourse_number+1):
            temp[j] = f[j]                           # 更新每阶段不同弹量的最大价值


    c= resourse_number
    b= object_number-1
    d=0

    while b>=0:
        # print(a[b][c])
        gain_list.append(int(a[b][c]))
        print("第{}个目标打{}颗弹".format(b+1, gain_list[d]))
        c -= gain_list[d]
        d+=1
        b-=1


    print("最大价值：{}".format(f[resource_number]))


def kill_probability(a,x):
    return 1-np.e**(-a*x)

if __name__ == "__main__":
    # object_number = int(input("工程数:"))
    # resource_number = int(input("资源数："))
    object_number = 4
    resource_number = 5
    value_list =np.zeros((object_number,resource_number+1))
    for i in range(object_number):
        for j in range(resource_number+1):
            value_list[i][j] = kill_value[i]*kill_probability(const_a[i],j)
    Plan(object_number,resource_number,value_list)


