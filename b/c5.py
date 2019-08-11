
# 模板
# 类 和 对象

class Student():
    sum = 0
    # name = 'qiyue'
    # age = 0
    #类变量 实例变量
    def __init__(self,name,age):
        # 构造函数
        # 初始化对象属性
        self.name = name
        self.age = age
        self.__class__.sum += 1
        print('当前班级学生总数：' + str(self.__class__.sum))
        # print(self.name)
        # print(name)
        # print('student')
        

        # 行为与特征
    # def do_homework(self):
    #     print('homework')

    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        print(cls.sum)


    @staticmethod
    def add(x,y):
        print(Student.sum)
        print('this is a static method')

        

student1 = Student('shigandang',18)
Student.add(1,2)
student1.add(1,2)
# Student.plus_sum()
# student2 = 
# Student.plus_sum()
# student1 = Student('shigandang',18)
# Student.plus_sum()
# student1 = Student('shigandang',18)
# Student.plus_sum()
# print(student1.__dict__)


# student2 = Student('xixiaole',19)
# print(student1.name,student1.age)
# print(student2.name,student2.age)
# print(Student.name)




