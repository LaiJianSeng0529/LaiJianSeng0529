n = int(input('Selection:'))
dic = {}
def op(dic, n):
    if n == 1:

        print('请输入账号密码:')
        name = input('账号:')
        password = input('密码:')
        dic[name] = password
        if dic[name] in dic:
            print('登录成功')
        else:
            print('密码不存在，输⼊q回到⾸⻚选择注册功能')
            if 'q' == input('输入q:'):
                res()
    if n == 2:
        print('请输入账号密码:')
        name = input('账号:')
        password = input('密码')
        dic[name] = password
        if dic[name] in dic:
            print('已注册，输⼊q回到⾸⻚选择登录功能')
            if 'q' == input('输入q：'):
                res()
        else:
            print('注册成功')
        if n == 3:
            print('欢迎下次使⽤ ')
            exit(0)

def res():
    print('''
=======登⼊系统======= 
1.登⼊ 
2.注册
3.退出
''')
    n = int(input('请选择操作：'))
    op(dic, n)
res()