"""
Author: Rainwangpupil
Project Name: 二分法
Data: 2022.08.21

You can use 'https://Rainwangpupil.github.io/Program/2022-08-21-Two-Fen.py' to download this file
"""

num = eval(input('猜数字：'))

# 一般方法猜
count = 0

while count != num:
    print('count = "{}"'.format(count))
    count += 1

print('普通方法猜了{}次'.format(count))


# 二分法猜
min_num = 0
max_num = 100
mid = (min_num + max_num) // 2 # 二分，取中间值
Two_fen_count = 0

while mid != num:
    if mid > num:
        # 猜小了
        print('猜小了,max_num={}, mid={}'.format(max_num,mid))
        max_num = mid
        Two_fen_count += 1 # 记录次数
    

    elif mid < num:
        # 猜大了
        print('猜大了,min_num={}, mid={}'.format(min_num,mid))

        min_num = mid
        Two_fen_count += 1 # 记录次数

    
    mid = (min_num + max_num) // 2 # 再次二分

print('二分法猜了{}次'.format(Two_fen_count))
