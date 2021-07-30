def clamp(num, min, max):
    if num < min:
        return min
    elif num > max:
        return max
    else:
        return num

def infinityFlow(num, min, max):
    if num < min:
        return infinityFlow(max - abs(min - num), min, max)
    elif num > max:
        return infinityFlow(min + abs(max - num), min, max)
    else:
        return num

def findSegment(str, opener, closer):
    start = 0
    end = len(str)
    level = 0
    for i in range(len(str)):
        c = str[i]
        if c == opener:
            if level == 0:
                start = i
            level += 1
        elif c == closer:
            level -= 1
            if level <= 0:
                end = i
                break

    return [start, end]
        

class Pointer:
    MAX_VALUE = 256
    position = 0

    def __init__(self, array_size=30000):
        array_size = array_size
        self.array_size = array_size
        self.array = [0] * (array_size - 1)

    def getValue(self):
        return self.array[self.position]

    def setValue(self, value):
        self.array[self.position] = clamp(value, 0, self.MAX_VALUE)

    def getPosition(self):
        return self.position

    def setPosition(self, position):
        self.position = clamp(position, 0, self.array_size - 1)
    
    def left(self):
        self.setPosition(infinityFlow(self.getPosition() - 1, 0, self.array_size - 1))

    def right(self):
        self.setPosition(infinityFlow(self.getPosition() + 1, 0, self.array_size - 1))

    def increment(self):
        self.setValue(infinityFlow(self.getValue() + 1, 0, self.MAX_VALUE))
    
    def decrement(self):
        self.setValue(infinityFlow(self.getValue() - 1, 0, self.MAX_VALUE))

    def output(self):
        cell_value = self.getValue()
        print(chr(cell_value), end="")
    
    def input(self):
        while True:
            try:
                user_input = input("input: ")[0]
                self.setValue(ord(user_input))
                break
            except:
                continue

    def execute(self, code):
        i = 0
        while i < len(code):
            instruction = code[i]
            if instruction == ">":
                self.right()
            elif instruction == "<":
                self.left()
            elif instruction == "+":
                self.increment()
            elif instruction == "-":
                self.decrement()
            elif instruction == ",":
                self.input()
            elif instruction == ".":
                self.output()
            elif instruction == "[":
                segment_data = findSegment(code[i:], "[", "]")
                start = i + segment_data[0]
                end = i + segment_data[1]
                content = code[(start + 1):end]
                while self.getValue() != 0:
                    self.execute(content)

                i = end
            
            i += 1

def brainfuck(code, array_size=30000, pointer=None):
    pointer = Pointer(array_size)
    pointer.execute(code)


hello_program = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."

brainfuck(hello_program)