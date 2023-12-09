def double_decker():
    print("you are doing great")
    def inner_func():
        print("Greetings,from inner func")
        return 300
    return inner_func
print(double_decker()())


def do_something(work):
    print("Hi,I'm Niahd Hossain")
    work()
    print("Happy ending")
def coding():
    print("Happy! conding")
do_something(coding)
