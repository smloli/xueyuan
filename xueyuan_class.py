import pickle

class Manager_System():
    def __init__(self):
        self.fg = '-' * 35
        self.student = self._RW_Data('rb')
        self.info = ['姓名','年龄','性别']

    def _add(self,**kwargs):
        self.student.append(kwargs)
        self._print_all()

    def _del(self):
        Name = input('姓名:')
        for i in self.student:
            if i['Name'] == Name:
                self.student.remove(i)
        self._print_all()

    def _Inquire(self):
        Name = input('姓名:')
        for i in self.student:
            if i['Name'] == Name:
                print(self.fg)
                for c in self.info:
                    print(f'{c.center(10)}',end='')
                print(f'\n{self.fg}')
                for j in i.values():
                    print(f'{j.center(10)}',end='')
                print()

    def _modify(self):
        c = 0
        Name = input('姓名:')
        for i in self.student:
            if i['Name'] == Name:
                Name = input('姓名:')
                Age = input('年龄:')
                Gender = input('性别:')
                tmp = [Name,Age,Gender]
                for j,k in i.items():
                    i[j] = tmp[c]
                    c+=1
        self._print_all()

    def _print_all(self):
        print(self.fg)
        for i in self.info:
            print(f'{i.center(10)}',end='')
        print(f'\n{self.fg}')
        for c in self.student:
            for j in c.values():
                print(f'{j.center(10)}',end='')
            print()

    def _RW_Data(self,mode):
        try:
            with open('student.txt',mode) as f:
                if mode == 'wb':
                    pickle.dump(self.student,f)
                else:
                    return pickle.load(f)
        except FileNotFoundError:
            return []

    def run(self):
        while True:
            print(f'{self.fg}\n1.添加学员\n2.删除学员\n3.查询学员\n4.修改学员\n5.显示学员信息\n6.保存学员信息\n7.退出系统\n{self.fg}')
            num = input('num:')
            if num == '1':
                Name = input('姓名:')
                Age = input('年龄:')
                Gender = input('性别:')
                self._add(Name=Name,Age=Age,Gender=Gender)
            elif num == '2':
                self._del()
            elif num == '3':
                self._Inquire()
            elif num == '4':
                self._modify()
            elif num == '5':
                self._print_all()
            elif num == '6':
                self._RW_Data('wb')
            elif num == '7' or num == '':
                break
            else:
                print('似不似傻!!!')

if __name__ == '__main__':
    Loli = Manager_System()
    Loli.run()
