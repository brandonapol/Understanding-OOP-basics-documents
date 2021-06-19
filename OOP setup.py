class Butt_sauce():

    def __init__(self):
        print('initialized!')

    def someFunc(self, ):
        user_said = input('What did you say? ')
        self.user_said = user_said
        return user_said

    def otherMethod(self):
        # print('I would like to buy an hamburgweyur and use the input from before, Inspector Closeau')
        # you have to use self here so that otherMethod knows where to look for the variable
        new_var = self.user_said
        # print(self.empty_string)
        print(new_var)

def launcher():
    launched = Butt_sauce()
    launched.otherMethod()
    launched.someFunc()

launcher()

