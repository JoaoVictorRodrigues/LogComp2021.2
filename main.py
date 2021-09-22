import sys
import re

arg = sys.argv[1]
arg = re.sub("[/][*]\s*(.*?)\s*[*][/]", "", arg)
class Token:
    def __init__(self,Type,Value):
        self.type = Type
        self.value = Value 

class Parser:
    def __init__(self, origin):
        self.origin   = origin
        self.index = 0
        self.char     = self.getNextToken()

    def getNextToken(self):
        
        ch      = 0
        index   = 0
        number  = 0

        lenArg    = len(self.origin)
        operables = []
        

        while self.index < lenArg and self.origin[self.index].isspace():
            self.index += 1

        if self.index == lenArg:
            self.char = Token('EOF', 'end')

        elif self.origin[self.index].isdigit():
            while self.index < lenArg and self.origin[self.index].isdigit():
                operables.append(int(self.origin[self.index]))
                self.index += 1
            for ch in operables:
                number += int(ch)*10**(len(operables) - index - 1)
                index += 1
            self.char = Token('INT', number)

        elif self.index < lenArg:
            if self.origin[self.index] == '+':
                self.char = (Token('SUM', '+'))
                self.index += 1
            elif self.origin[self.index] == '-':
                self.char = (Token('SUB', '-'))
                self.index += 1
            elif self.origin[self.index] == '*':
                self.char = (Token('MUL', '*'))
                self.index += 1
            elif self.origin[self.index] == '/':
                self.char = (Token('DIV', '/'))
                self.index += 1
            else:
                self.index += 1 
        return self.char

class Calculator:
    
    def Term(): 
        if Calculator.tk.char.type == 'INT':
            out = Calculator.tk.char.value
            Calculator.tk.getNextToken()
            
            while Calculator.tk.char.type == 'MUL'  :
                if Calculator.tk.char.type =='MUL':
                    Calculator.tk.getNextToken()
                    if Calculator.tk.char.type == 'INT':
                        out *= Calculator.tk.char.value
                    else:
                        raise NameError('Err: MUL')
                Calculator.tk.getNextToken()
                        
            while Calculator.tk.char.type == 'DIV':
                if Calculator.tk.char.type == 'DIV':
                    Calculator.tk.getNextToken()
                    if Calculator.tk.char.type == 'INT':
                        out = out // Calculator.tk.char.value
                    else:
                        raise NameError('Err: DIV')
                Calculator.tk.getNextToken()
        else:
            raise NameError('Err: TERM')
        return out

    def Expression():
            out = Calculator.Term()            
            while Calculator.tk.char.type == 'SUM' or Calculator.tk.char.type == 'SUB' or Calculator.tk.char.type == 'MUL' or Calculator.tk.char.type == 'DIV':
                if Calculator.tk.char.type =='SUM':
                    Calculator.tk.getNextToken()
                    if Calculator.tk.char.type == 'INT':
                        out += Calculator.Term()
                    else:
                        raise NameError('Err: SUM')
                elif Calculator.tk.char.type == 'SUB':
                    Calculator.tk.getNextToken()
                    if Calculator.tk.char.type == 'INT':
                        out -= Calculator.Term()
                    else:
                        raise NameError('Err: SUB')
            return out
              

    def run(code):
        Calculator.tk = Parser(code)
        out = Calculator.Expression()
        if Calculator.tk.char.type != 'EOF':
            raise NameError('Err: EOF')
        else:
            return out

print(Calculator.run(arg))      