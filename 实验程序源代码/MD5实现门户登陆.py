import hashlib
import re

USER_LIST = []

# 生成MD5摘要
def pwd_Md5(password):
    password = password + 'hello python'    # 字符串混淆加长，增加复杂性
    return hashlib.md5(password.encode('utf-8')).hexdigest()

# 注册处理
def register():
    print('**********用户注册**********')
    username_pattern = r'^[a-zA-Z0-9_]+$'
    while True:
        user = input ('请输入用户名：')
        # 允许输入字母、数字和下划线
        if re.match(username_pattern, user):
           break
        print('用户名只能包含字母、数字和下划线，请重新输入。')
        # 只允许输入字母
        '''
        if user.isalpha():
            break
        '''
    while True:
        password1 = input ('请输入密码>>> : ').strip()
        password2 = input ('请再次输入密码>>> : ').strip()
        if password1 == password2:
            password = pwd_Md5(password1)   # 将密码进行Md5加密
            break
        else:
            print('密码错误！请重新输入！')
    temp = {'username':user,'password':password}
    USER_LIST.append(temp)

# 登陆处理
def login():
    print('**********用户登陆**********')
    user = input ('请输入用户名：')
    pwd = input ('请输入密码：')
    
    for item in USER_LIST:
        if item['username'] == user and item['password'] == pwd_Md5(pwd):
            return True
if __name__ == '__main__':
    
    register()
    if login():
        print('登陆成功')
    else:
        print('登陆失败')    
 