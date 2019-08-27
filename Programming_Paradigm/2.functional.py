"""
Functional Programming
函数式编程

对于函数式编程来说，它只关心定义输入数据和输出数据相关的关系，数学表达式里面其实是在做一种映射 (mapping)，输入的数据和输出的数据关系是怎么样的，是用函数来定义的。

特点：

- stateless: 函数不维护任何状态。函数式编程的核心精神是 stateless，简而言之就是它不能存在状态，打个比方，你给我数据我处理完扔出来。里面的数据是不变的。
- immutable: 输入数据是不能动的，动了输入数据就有危险，所以要返回新的数据集。

下面是函数式编程用到的一些技术：

- first class function（头等函数）
- tail recursion optimization（尾递归优化）
- map & reduce
- pipeline（管道）
- recursing（递归）
- currying（柯里化）
- higher order function（高阶函数）
"""


class Pipe:
    def __init__(self, func):
        self.func = func

    def __ror__(self, other):
        def generator():
            for obj in other:
                if obj is not None:
                    yield self.func(obj)

        return generator()


@Pipe
def even_filter(num):
    return num if num % 2 == 0 else None


@Pipe
def multiply_by_three(num):
    return num * 3


@Pipe
def convert_to_string(num):
    return f"The Number: {num}"


@Pipe
def echo(item):
    print(item)
    return item


def force(sqs):
    for item in sqs:
        pass


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

force(nums | even_filter | multiply_by_three | convert_to_string | echo)
