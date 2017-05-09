class Stack(object):
    def __init__(self):
        self.__data = []

    def push(self, x):
        self.__data.append(x)

    def pop(self):
        if self.__data:
            return self.__data.pop()

    def size(self):
        return len(self.__data)

    def peek(self):
        return self.__data[self.size()-1]

class MyQueue(object):
    def __init__(self):
        self.__queue = Stack()
        self.__stack = Stack()

    def peek(self):
        ret = None
        if not self.__stack.size():
            while self.__queue.size():
                self.__stack.push(self.__queue.pop())
        ret = self.__stack.peek()
        return ret

    def pop(self):
        ret = None
        if not self.__stack.size():
            while self.__queue.size():
                self.__stack.push(self.__queue.pop())
        ret = self.__stack.pop()
        return ret


    def put(self, value):
        self.__queue.push(value)


queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())

