""" 成员可见性 """

#类变量
class Student():
    sum = 0

    #实例变量
    def __init__(self,name,age):
        
        self.name = name
        self.age = age
        self.score = 0
        self.__class__.sum += 1
    
    #实例方法
    def marking(self,score):
        if score < 0:
            return '不能够给别人打负分'
        elif score > 100:
            return '最高100分'
        self.score = score
        print(self.name + '同学本次考试成绩为：'+ str(self.score))
      
    def do_homework(self):
        self.do_english_homework()
        print('homework')

    def do_english_homework(self):
        print()

    #类方法
    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        print(cls.sum)

    #静态方法
    @staticmethod
    def add(x,y):
        print(Student.sum)
        print('this is a static method')

student1 = Student('shigandang',18)
result = student1.marking(-105)
print(result)




