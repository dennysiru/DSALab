class ArrayStack:
    def __init__(self):
        self.size = 0
        self.data = list()

    def push(self, input_data):
        """Stack"""
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError, IndexError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1

    def pop(self):
        try:
            remove = self.data.pop()
            self.size -= 1
            return remove
        except(TypeError, ValueError, ArithmeticError, AttributeError, IndexError):
                print("Underflow: Cannot pop data from an empty list")
                return None
            
    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False
        
    def get_stack_top(self):
        try:
            top = self.data.pop()
            self.data.append(top)
            return top
        except(TypeError, ValueError, ArithmeticError, AttributeError, IndexError):
                print("Underflow: Cannot get stack top from an empty list")
                return None

    def get_size(self):
        return self.size

    def print_stack(self):
        print(self.data)

def is_parentheses_matching(expression):
    stack = ArrayStack()
    status = True

    for char in expression:
        if char == '(':
            stack.push(char)
        elif char == ')':
            x = stack.pop()
            if not x:
                status = False
                
    if not stack.is_empty():
        status = False            
    return status

def main():
    expression = input()
    if is_parentheses_matching(expression):
        print(f"Parentheses in {expression} are matched")
        print(True)
    else:
        print(f"Parentheses in {expression} are unmatched")
        print(False)
    
main()
