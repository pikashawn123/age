car = input('你有沒有開過車?')
if car != ('有') and car != ('沒有'):
    print('              ')
    print('只能輸入有/沒有')
    print('請不要亂輸入 電腦看不懂')
    raise SystemExit
age = input('你現在幾歲？')
age = int(age)
if car == '有':
    if age <= 17:
        print('你怎麼可以開車')
    else:
        print('算你通過')
elif car == '沒有':
    if  age >= 18:
        print('你可以考駕照了，幹嘛不考勒!')
    else:
        print('很好，再過幾年，就可以考了!')