import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
        function()

    return wrapper_function


@delay_decorator
def say_hello():
    print("hello")


def say_goodbye():
    print("goodbye")


def say_greeting():
    print("greeting")


say_hello()  # This will take 2 seconds to print "hello"(because of the delay_decorator which provides a extra specification)
say_goodbye()


# @delay_decorator
# def say_greeting():
#     print("greeting")
# -------------------- equivalent to below code--------------------------------
# decorated_function = delay_decorator(say_greeting)
# decorated_function()
