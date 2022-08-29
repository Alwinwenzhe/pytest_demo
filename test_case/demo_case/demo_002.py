a = 2
b = 0

def positive_to_negative(num):
    return '-' + str(num)

c = positive_to_negative(a)

if int(c) > b:
    print('error')
else:
    print('ok')
