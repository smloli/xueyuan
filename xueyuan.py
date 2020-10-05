import pickle
def print_info():
    print('1.添加学员\n2.删除学员\n3.修改学员信息\n4.查询学员信息\n5.显示所有学员\n6.保存数据\n7.退出系统')
    print(f'{a}')

def _add(**kwargs):
    student_list.append(kwargs)
    _print_all()

def _del(name):
    c = 0
    for i in student_list:
        if i['name'] == name:
            student_list.remove(i)
            _print_all()
            break
        c+=1

def _modify(name):
    for i in student_list:
        if i['name'] == name:
            age = input('年龄:')
            gender = input('性别:')
            if gender == '':
                gender = '女'
            tmp = (name,age,gender)
            k = 0
            for j in i.keys():
                i[j] = tmp[k]
                k+=1
            _print_all()

def _inquire(name):
    c = 0
    print(a)
    for i in student_list:
        if i['name'] == name:
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
    for i in student_list:
        if not c:
            for d in info_list:
                print(f'{d.center(10)}',end='')
            print(f'\n{a}')
            c = 1
        for j,k in i.items():
            print(f'{k.center(10)}',end='')
        print(f'\n{a}')

def RW_data(mode = 'ab+'):
    with open(path,mode) as f:
        if mode == 'wb':
            global student_list
            pickle.dump(student_list,f)
        else:
            try:
                f.seek(0,0)
                student_list = pickle.load(f)
            except EOFError:
                student_list = []
            return student_list

if __name__ == '__main__':
    path = '/storage/emulated/0/Download/student.txt'
    info_list = ['姓名','年龄','性别']
    student_list = RW_data()
    a = '-' * 35
    print_info()
    num = input('num:')
    while num != '7' and num != '':
        if num == '1':
            name = input('姓名:')
            age = input('年龄:')
            gender = input('性别:')
            if gender == '':
                gender = '女'
            _add(name=name,age=age,gender=gender)
        elif num == '2':
            name = input('姓名:')
            _del(name)
        elif num == '3':
            name = input('姓名:')
            _modify(name)
        elif num == '4':
            name = input('姓名:')
            _inquire(name)
        elif num == '5':
            _print_all()
        elif num == '6':
            RW_data('wb')

        print_info()
        num = input('num:')
