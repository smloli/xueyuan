import pickle

def print_info():
    print('1.添加学员\n2.删除学员\n3.修改学员信息\n4.查询学员信息\n5.显示所有学员\n6.保存数据\n7.退出系统')
    print(f'{a}')

def _add(**kwargs):
    student_list.append(kwargs)
    _print_all()

def _del(Name):
    c = 0
    for i in student_list:
        if i['Name'] == Name:
            student_list.remove(i)
            _print_all()
        c+=1

def _modify(Name):
    for i in student_list:
        if i['Name'] == Name:
            Age = input('年龄:')
            Gender = input('性别:')
            if Gender == '':
                Gender = '女'
            tmp = [Name,Age,Gender]
            k = 0
            for j in i.keys():
                i[j] = tmp[k]
                k+=1
            _print_all()

def _inquire(Name):
    c = 0
    print(a)
    for i in student_list:
        if i['Name'] == Name:
            if not c:
                for d in info_list:
                    print(f'{d.center(10)}',end='')
                print(f'\n{a}')
                c = 1
            for j,k in i.items():
                print(f'{k.center(10)}',end='')
            print(f'\n{a}')

def _print_all():
    c = 0
    print(a)
    for d in info_list:
        print(f'{d.center(10)}', end='')
    print(f'\n{a}')
    for i in student_list:
        for k in i.values():
            print(f'{k.center(10)}',end='')
        print(f'\n{a}')

def RW_data(mode = 'rb'):
    global student_list
    try:
        with open('student.txt',mode) as f:
            if mode == 'wb':
                pickle.dump(student_list,f)
            else:
                return pickle.load(f)
    except FileNotFoundError:
        return []

if __name__ == '__main__':
    info_list = ['姓名','年龄','性别']
    student_list = RW_data()
    a = '-' * 35
    print_info()
    num = input('num:')
    while True:
        if num == '1':
            Name = input('姓名:')
            Age = input('年龄:')
            Gender = input('性别:')
            if Gender == '':
                Gender = '女'
            _add(Name=Name,Age=Age,Gender=Gender)
        elif num == '2':
            Name = input('姓名:')
            _del(Name)
        elif num == '3':
            Name = input('姓名:')
            _modify(Name)
        elif num == '4':
            Name = input('姓名:')
            _inquire(Name)
        elif num == '5':
            _print_all()
        elif num == '6':
            RW_data('wb')
        elif num == '7' or num == '':
            break
        print_info()
        num = input('num:')
