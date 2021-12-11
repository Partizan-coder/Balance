class Stack:

    def __init__(self, list=[]):
        self.stack = []
        for i in range(len(list)):
            self.stack.append(list[i])
        return

    def isEmpty(self):
        length = len(self.stack)
        if length > 0:
            return False
        else:
            return True

    def push(self, elem):
        self.stack.append(elem)
        print(self.stack)
        return

    def pop(self):
        removable_elem = self.stack[len(self.stack)-1]
        self.stack.remove(removable_elem)
        return removable_elem

    def peek(self):
        return self.stack[len(self.stack)-1]

    def size(self):
        return len(self.stack)

def balance(str):

    close_bracket = {'(':')','[':']','{':'}'}
    open_bracket = ['(','[','{']
    check_stack = Stack()
    if len(str)%2 != 0:
        print('Несбалансированная строка')
    else:
        logic = True
        for i in range(len(str)):
            if str[i] in open_bracket:
                check_stack.push(str[i])
            else:
                bracket = check_stack.pop()
                if str[i] == close_bracket.get(bracket):
                    pass
                elif str[i] != close_bracket.get(bracket):
                    logic = False
        if logic:
            print('Cбалансированная строка')
        else:
            print('Несбалансированная строка')


if __name__ == '__main__':
    var_list_1 = '[([])((([[[]]])))]{()}'
    var_list_2 = '[[{())}]'

    balance(var_list_2)




