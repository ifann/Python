ACCOUNT = 'qiyue'
PASSWORD = '123456'

print('please input ACCOUNT')
USER_ACCOUNT = input()

print('please input PASSWORD')
USER_PASSWORD = input()

if ACCOUNT == USER_ACCOUNT and PASSWORD == USER_PASSWORD:
    print('success')
else:
    print('fail')