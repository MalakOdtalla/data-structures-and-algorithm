
from stack_and_queue.stack_and_queue.Stack import Stack

open = ["[","{","("]
close = ["]","}",")"]

class validation:
    def __init__(self):
        self.stack = Stack()

    def validate_brackets(self, string):
        for i in string:
            if i in open:
                self.stack.push(i)
            elif i in close:
                if self.stack.is_empty():
                    return "FALSE"
                brackets= self.stack.pop()
                if not self.Compare(brackets, i):
                    return False
        if self.stack.is_empty():
            return "False"
        else:
            return "TRUE"

    def Compare(self,opening, closing):
            if opening == '(' and closing == ')':
                return True
            if opening == '[' and closing == ']':
                return True
            if opening == '{' and closing == '}':
                return True
            return False


if __name__ == "__main__":
    stack=validation()
    string1 = "{(})"
    string2 = "{()[]}"
    print(string1,"\t", stack.validate_brackets(string1))
    print(string2, "\t", stack.validate_brackets(string2))