class Phone:
    def call(self):
        print("you can call")

    def message(self):
        print("You can message")


# here Phone -> super class/parent class/ base class and Apple -> child class/sub class/ Derived class
class Apple(Phone):

    '''def call(self):
        print("you can call")

    def message(self):
        print("You can message")'''

    def photo(self):
        print("You can take photo")


'''p = Phone()
p.call()
p.message()'''

a = Apple()
a.call()
a.message()
a.photo()
