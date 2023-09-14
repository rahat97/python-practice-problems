class Phone:
    def call(self):
        print("you can call")

    def message(self):
        print("You can message")


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
