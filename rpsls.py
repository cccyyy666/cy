"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者:陈洋
日期:2021.11.29
"""
import random
def name_to_number(name):
    if name=="石头":
        a=0
    elif name=="史波克":
        a=1
    elif name=="布":
        a=2
    elif name=="蜥蜴":
        a=3
    elif name=="剪刀":
        a=4
    else:a=5
    return a
def number_to_name(number):
    if number==0:
        comp_name="石头"
    elif number==1:
        comp_name="史波克"
    elif number==2:
        comp_name="布"
    elif number==3:
        comp_name="蜥蜴"
    elif number==4:
        comp_name="剪刀"
    return comp_name
def rpsls(player_choice):
    number=random.randint(0,4)
    print("----------------")
    print("你的选择为"+player_choice)
    print("计算机的选择为"+number_to_name(number))
    a=name_to_number(player_choice)
    if a==5:
       print("Error: No Correct Name")
    elif a==number:
       print("平局")
    elif a==0 and number==3:
       print("您赢了")
    elif a==1 and number==0:
       print("您赢了")
    elif a==2 and number==0:
       print("您赢了")
    elif a==3 and number==1:
       print("您赢了")
    elif a==4 and number==2:
       print("您赢了")
    elif a==0 and number==1:
       print("机器赢了")
    elif a==1 and number==2:
       print("机器赢了")
    elif a==2 and number==3:
       print("机器赢了")
    elif a==3 and number==0:
       print("机器赢了")
    elif a==4 and number==0:
       print("机器赢了")
    elif a == 0 and number==4:
       print("您赢了")
    elif a == 1 and number==4:
        print("您赢了")
    elif a == 2 and number==1:
        print("您赢了")
    elif a == 3 and number==2:
        print("您赢了")
    elif a == 4 and number==3:
        print("您赢了")
    elif a == 0 and number==2:
        print("机器赢了")
    elif a == 1 and number==3:
        print("机器赢了")
    elif a == 2 and number==4:
        print("机器赢了")
    elif a == 3 and number==4:
        print("机器赢了")
    elif a == 4 and number==1:
        print("机器赢了")
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
rpsls(choice_name)
input()
