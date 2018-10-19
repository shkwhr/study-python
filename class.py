# coding: utf-8

class SampleClass:
    exclamation = '!'

    def __init__(self, name):
        self.__name = name  # private変数

    def hello(self, keyword):
        print('hello ' + self.__name + ' and ' + keyword + SampleClass.exclamation)

    @classmethod
    def show(self):
        print(self.exclamation)

class SubClass(SampleClass):
    def __init__(self, name):
        super(SubClass, self).__init__(name)

    def hello(self, keyword):
        print('hello subclass' + keyword + self.exclamation)

test = SampleClass('Apple')
# キーワード引数
test.hello(keyword = 'Orange')

test2 = SubClass('Tree')
test.hello('Forest')

SampleClass.show()
SubClass.show()