#
# def factor():
#     i=1
#     num=10
#     print('%d的因数是'%(num))
#     while i<=num:
#         if num%i==0:
#             print('%d'%i)
#         i+=1
# # factor()

# def factor(num):
#     i=1
#     str1=''
#     print('%d的因数是'%(num))
#
#     while i<=num:
#         if num%i==0:
#             str1=str1+' '+str(i)
#         i+=1
#     print(str1)
#
# num=[10,25,30,40]
# i=0
# len_=len(num)
# while i<len_:
#     factor(num[i])
#     i+=1

def factor(num):
    i=1
    str1=''
    while i<=num:
        if num%i==0:
            str1=str1+' '+str(i)
        i+=1
    return str1

num=[10,25,30,40]
i=0
len_=len(num)

return_str=''
while i<len_:
    return_str=factor(num[i])
    print('%d的因数是：%s'%(num[i],return_str))
    i+=1