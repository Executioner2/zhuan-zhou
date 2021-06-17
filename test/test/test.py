from common.result.Result import Result

class A:
    def test1(self):
        print("join test")
        return "amd yes"

    def test2(self, val):
        print(val)

if __name__ == '__main__':
    result = Result.ok("/login", "sagwrg")
    print(result)

    # while True:
    #     try:
    #
    #         a = A()
    #         # 通过字符串调用方法，实现类似java的反射调用方法（真TM牛逼）
    #         dd = getattr(a, "test1")
    #         dd(1,2)
    #     except AttributeError as e:
    #         print(e)
    #         continue
    #     except TypeError:
    #         dd()
