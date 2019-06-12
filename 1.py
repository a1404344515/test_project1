# i=0
# r = 0
# while i<=10:
#     if i%2==0:
#         print(i)
#     i+=1
# print('循环结束后,i=%d' %i)
# print('0-100之间数值和为%d'%r)
# a = "*"
# print(a)
# print(a*2)
# print(a*3)
# print(a*4)
# print(a*5)
#
# b = 1
# while b<=9:
#     print('*'*b)
#     b+=1
a = 1#行号
while a<=9:
    b=1#列号

    while b<=a:

        print('%d*%d=%d' %(b,a,b*a),end=' ')
        b+=1
    print('')

    a+=1
