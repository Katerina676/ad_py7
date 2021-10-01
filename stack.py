class Stack:
    def __init__(self, lst):
        self.lst = []

    def isEmpty(self):
        return len(self.lst) == 0

    def push(self, item):
        self.lst.append(item)

    def pop(self):
        return self.lst.pop()

    def peek(self):
        return self.lst[-1]

    def size(self):
        return len(self.lst)


def check_balanced(string):
    stack = Stack(string)
    opening = ['(', '{', '[']
    closing = [')', '}', ']']

    if len(string) % 2 > 0:
        return 'Несбалансированно'

    for i in string:
        if i in opening:
            stack.push(i)
        if i in closing:
            if len(stack.lst) == 0:
                return 'Небалансированно'
            index = closing.index(i)
            opens = opening[index]
            if stack.lst[-1] == opens:
                stack.pop()
            else:
                return 'Небалансированно'
    return 'Сбалансированно'


if __name__ == "__main__":
    print(check_balanced('(((([{}]))))'))
    print(check_balanced('[([])((([[[]]])))]{()}'))
    print(check_balanced('{{[()]}}'))
    print(check_balanced('}{}'))
    print(check_balanced('{{[(])]}}'))
    print(check_balanced('[[{())}]'))

