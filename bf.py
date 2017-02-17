import sys

try:
    f = open(sys.argv[1], "r")
except IndexError:
    print "python "+sys.argv[0]+" <file> <input>"
    sys.exit()
except IOError:
    print "cannot open file: " + sys.argv[0]
    sys.exit()

try:
    user_input = [ord(x) for x in sys.argv[2][::-1]]
except IndexError:
    user_input = []

commands = "+-,.[]<>@"
code = [x for x in f.read() if x in commands]
space = [0 for x in range(30000)]
pointer = 0
loop = []
stack = []
string_builder = ""

for i in range(len(code)):
    if code[i] == '[':
        stack.append(i)
        loop.append(i)
    if code[i] == ']':
        loop.insert(loop.index(stack.pop()) + 1, i)
i = 0

while i < len(code):
    if code[i] == '[':
        if space[pointer] == 0:
            i = loop[loop.index(i) + 1]
    elif code[i] == ']':
        if space[pointer] != 0:
            i = loop[loop.index(i) - 1]
    elif code[i] == '+':
        space[pointer] += 1
        if space[pointer] > 255:
            space[pointer] = 0
    elif code[i] == '-':
        space[pointer] -= 1
        if space[pointer] < 0:
            space[pointer] = 255
    elif code[i] == '.':
        string_builder += chr(space[pointer])
    elif code[i] == ',':
        try:
            space[pointer] = user_input.pop()
        except:
            pass
    elif code[i] == '>':
        pointer += 1
    elif code[i] == '<':
        pointer -= 1

    elif code[i] == '@':
        print "pointer: " + str(pointer)
        print space[:10]
        print " " + "   "*pointer + "^"
    # print i, "'"+code[i]+"'", pointer, space[:10]
    i += 1

if string_builder != "":
    print string_builder