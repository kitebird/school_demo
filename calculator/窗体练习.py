import tkinter

# 窗体设置
calculator = tkinter.Tk()
calculator.title("计算器")
calculator.minsize(300, 510)
calculator.maxsize(300, 510)

# 全局变量
his_val = ''
ans_val = ''
ans_temp_num = ''
ans_temp_sign = ''
flag_point = True

# 历史纪录
display_his = tkinter.StringVar()
display_his.set(his_val)

# 结果显示
display_ans = tkinter.StringVar()
display_ans.set(0)

# 显示历史纪录
laber_1 = tkinter.Label(calculator, font=('微软雅黑', 20), bg='#EEE9E9', bd='9', fg='#828282', anchor='se',
                        textvariable=display_his)
laber_1.place(x=0, y=0, width=300, height=60)

# 显示答案
label_2 = tkinter.Label(calculator, font=('微软雅黑', 30), bg='#EEE9E9', bd='9', fg='black', anchor='se',
                        textvariable=display_ans)
label_2.place(x=0, y=60, width=300, height=60)

# 按钮集合
btn_his = tkinter.Button(calculator, text='---', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5)
btn_his.place(x=0, y=120, width=300, height=15)

btn_c = tkinter.Button(calculator, text='C', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda: pressC())
btn_c.place(x=0, y=135, width=150, height=75)

btn_remove = tkinter.Button(calculator, text='←', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda: pressRM())
btn_remove.place(x=150, y=135, width=75, height=75)

btn_chu = tkinter.Button(calculator, text='÷', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5,
                         command=lambda: pressCompute('/'))
btn_chu.place(x=225, y=135, width=75, height=75)

btn_7 = tkinter.Button(calculator, text='7', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda: pressNum('7'))
btn_7.place(x=0, y=210, width=75, height=75)

btn_8 = tkinter.Button(calculator, text='8', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda: pressNum('8'))
btn_8.place(x=75, y=210, width=75, height=75)

btn_9 = tkinter.Button(calculator, text='9', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda: pressNum('9'))
btn_9.place(x=150, y=210, width=75, height=75)

btn_che = tkinter.Button(calculator, text='*', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5,
                         command=lambda: pressCompute('*'))
btn_che.place(x=225, y=210, width=75, height=75)

btn_4 = tkinter.Button(calculator, text='4', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda: pressNum('4'))
btn_4.place(x=0, y=285, width=75, height=75)

btn_5 = tkinter.Button(calculator, text='5', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda: pressNum('5'))
btn_5.place(x=75, y=285, width=75, height=75)

btn_6 = tkinter.Button(calculator, text='6', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda: pressNum('6'))
btn_6.place(x=150, y=285, width=75, height=75)

btn_jian = tkinter.Button(calculator, text='-', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5,
                          command=lambda: pressCompute('-'))
btn_jian.place(x=225, y=285, width=75, height=75)

btn_1 = tkinter.Button(calculator, text='1', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda: pressNum('1'))
btn_1.place(x=0, y=360, width=75, height=75)

btn_2 = tkinter.Button(calculator, text='2', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda: pressNum('2'))
btn_2.place(x=75, y=360, width=75, height=75)

btn_3 = tkinter.Button(calculator, text='3', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda: pressNum('3'))
btn_3.place(x=150, y=360, width=75, height=75)

btn_jia = tkinter.Button(calculator, text='+', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5,
                         command=lambda: pressCompute('+'))
btn_jia.place(x=225, y=360, width=75, height=75)

btn_0 = tkinter.Button(calculator, text='0', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda: pressNum('0'))
btn_0.place(x=0, y=435, width=150, height=75)

btn_point = tkinter.Button(calculator, text='.', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5,
                           command=lambda: pressPoint())
btn_point.place(x=150, y=435, width=75, height=75)

btn_dy = tkinter.Button(calculator, text='=', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda: pressAns())
btn_dy.place(x=225, y=435, width=75, height=75)


# 左移
def pressRM():
    global ans_val
    global ans_temp_num
    global ans_temp_sign
    global flag_point

    ans_val = ans_val + ans_temp_sign + ans_temp_num
    ans_temp_num = ''
    ans_temp_sign = ''
    flag_point = True

    ans_val = str(ans_val)
    if len(ans_val) > 0:
        ans_val = ans_val[0:-1]
    else:
        return
    display_ans.set(ans_val)

    for i in range(len(ans_val) - 1, -1, -1):
        if ans_val[i] == '.':
            flag_point = False
        if ans_val[i] == '+' or ans_val[i] == '-' or ans_val[i] == '*' or ans_val[i] == '/':
            break

    # flag = True
    #
    # if ans_val[-1] == '+' or ans_val[-1] == '*' or ans_val[-1] == '/' or ans_val[-1] == '-':
    #     ans_temp_sign = ans_val[-1]
    #     ans_val = ans_val[0:-1]
    # elif ans_val[-1] == '.':
    #     flag_point = False

def pressPoint():
    global ans_val
    global ans_temp_num
    global ans_temp_sign
    global flag_point

    print(flag_point)
    if flag_point == True:
        flag_point = False

        ans_val = ans_val + ans_temp_num + ans_temp_sign
        ans_temp_num = ''
        ans_temp_sign = ''
        if  ans_val =='' or ans_val[-1] == '+' or  ans_val[-1] == '-' or ans_val[-1] == '*' or  ans_val[-1] == '/' :
            ans_val = ans_val + '0.'
        else:
            ans_val = ans_val + '.'


        display_ans.set(ans_val)
    print(ans_val,ans_temp_num,flag_point)



# 数字函数 ok
def pressNum(num):  # 设置一个数字函数 判断是否按下数字 并获取数字将数字写在显示版上
    global ans_val
    global ans_temp_num
    global ans_temp_sign
    global flag_point

    # 将ans_val 和 ans_temp_sign 合并，
    if ans_temp_sign != '':
        ans_val = ans_val + ans_temp_sign
        ans_temp_sign = ''

    if ans_val == '0':
        ans_val = ''

    if ans_temp_num == '' and len(ans_val) > 0 and ans_val[-1] != '.':
        ans_temp_num = '0'

    if ans_temp_num == '0' and num == '0' and flag_point:
        ans_temp_num = '0'
    elif ans_temp_num == '0' and num != '0' and flag_point:
        ans_temp_num = num
    else:
        ans_temp_num = ans_temp_num + num

    display_ans.set(ans_val + ans_temp_num)


# 运算函数 ok
def pressCompute(sign):
    global ans_val
    global ans_temp_num
    global ans_temp_sign
    global flag_point
    flag_point = True

    # 初始前缀 -
    if ans_val == '' and sign == '-':
        ans_val = '-'
        display_ans.set(ans_val)
        return

    if ans_temp_num != '':
        ans_val = ans_val + ans_temp_num
        ans_temp_num = ''


    if ans_val == '':
        ans_val = '0'

    if sign == '+' or sign == '/' or sign == '*' or (sign == '-' and (ans_temp_sign == '' or ans_temp_sign == '+')):
        ans_temp_sign = sign
    elif sign == '-' and ans_temp_sign[-1] != '-' and ans_temp_sign[-1] != '+':
        ans_temp_sign = ans_temp_sign + sign

    #print(ans_temp_sign)

    display_ans.set(ans_val + ans_temp_sign)


# 全部清除 oK
def pressC():
    global flag_point
    global ans_val
    global ans_temp_num
    global ans_temp_sign
    global his_val
    his_val = ''
    ans_val = ''
    ans_temp_num = ''
    ans_temp_sign = ''
    flag_point = True
    # 历史纪录
    display_his.set(his_val)
    # 结果显示
    display_ans.set(0)


# 等于
def pressAns():
    global his_val
    global ans_val
    global ans_temp_num
    global ans_temp_sign
    global flag_point

    his_val = ans_val + ans_temp_num + ans_temp_sign
    if ans_val == str(ans_val + ans_temp_num + ans_temp_sign):
        return

    # if (his_val[-1] == '0' and his_val[-2] == '/') or (
    #         his_val[-1] == '0' and his_val[-2] == '-' and his_val[-3] == '/'):
    #     ans_val = ''
    #     ans_temp_num = ''
    #     ans_temp_sign = ''
    #     flag_point = True
    #     # 历史纪录
    #     display_his.set(his_val)
    #     # 结果显示
    #     display_ans.set("不能除以0")
    #     return

    try:
        ans = eval(str(ans_val + ans_temp_num))
    except ZeroDivisionError:
        ans_val = ''
        ans_temp_num = ''
        ans_temp_sign = ''
        flag_point = True
        # 历史纪录
        display_his.set(his_val)
        # 结果显示
        display_ans.set("不能除以0")
        return


        print("yes")
    else:
        ans = round(ans, 2)

        ans_temp_sign = ''
        ans_temp_num = ''
        ans_val = str(ans)

        display_his.set(his_val)
        display_ans.set(str('=' + ans_val))

        for i in range(len(ans_val) - 1, -1, -1):
            if ans_val[i] == '.':
                flag_point = False
            if ans_val[i] == '+' or ans_val[i] == '-' or ans_val[i] == '*' or ans_val[i] == '/':
                break


if __name__ == '__main__':
    calculator.mainloop()
