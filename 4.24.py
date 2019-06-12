# 1 定义一个函数sum_num,函数能够实现 两个数字的求和 功能
def sum_num(a,b):
    c=a+b
    print(c)
sum_num(10,20)
# 2  定义一个函数 money, 传递三个实参 基本工资，奖金 ，绩效, 求总的工资，并且将总工资返回
#    根据总工资进行判断，如果大于6000 就上10%的税，求实发工资
def money(salary,jj,jx):
    z = salary + jj + jx
    return z
b = money(4000,3000,2000)
if b>6000:
    print(b*0.9)
# 3  打印分隔线
def fgx(char,time):
    print(char*time)
fgx('-',10)
# 4 定义以列表  my_list = [10, 30, 40, 50]
# 添加  数据 60, 70,90
# 在 10 和30 之间添加 数据100
#  删除 数据 90
#  修改数据30 改成 300
my_list = [10, 30, 40, 50]
my_list.extend([60,70,90])
my_list.insert(1,100)
my_list.remove(90)
my_list[2] = 300
print(my_list)
# 5遍历my_list = [“zhang”, ”wang”, ”li”]
my_list = ['zhang','wang','li']
for bl in my_list:
    print(bl)
# 6  定义一个元组  里面放6个数据
yz = (1,2,3,4,5,6)
# 7  遍历元组
for bl_yz in yz:
    print(bl_yz)
# 8  my_list= [7, 8, 9, 10]  转换为元组
my_list= [7, 8, 9, 10]
lx =tuple(my_list)
print(type(lx))
# 9   my_tuple = (3, 5 ,6,7) 转换为列表
my_tuple = (3, 5 ,6,7)
lxzh = list(my_tuple)
print(type(lxzh))