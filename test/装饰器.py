# def outer(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return res
#
#     return wrapper
import time


def ctrl_time(func):
    def wrapper(*args, **kwargs):
        stat_time = time.time()
        res = func(*args, **kwargs)
        time.sleep(2)
        end_time = time.time()
        print(end_time - stat_time)
        return res

    return wrapper


# def user():
#     print("hello")


# user = ctrl_time(user)


# 语法糖
@ctrl_time  # user = ctrl_time(user)
def user():
    print("hello")


user()
