import sys
try:
    f = open(sys.argv[1], "r")
except IndexError:
    print "python "+sys.argv[0]+" <file> <input>"
    sys.exit()
except IOError:
    print "cannot open file: " + sys.argv[0]
    sys.exit()
user_input = []

try:
    user_input = [ord(x) for x in sys.argv[2][::-1]]
except IndexError:
    pass

code = [x for x in f.read()]
space = [0 for x in range(30000)]
pointer = 0
stack = []
string_builder = ""

i = 0
while i < len(code):
    if code[i] == '[':
        stack.append(i)
    elif code[i] == ']':
        if space[pointer] != 0:
            i = stack.pop() -1
    elif code[i] == '+':
        space[pointer] += 1
    elif code[i] == '-':
        space[pointer] -= 1
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
        pointer = max(0, pointer)

    elif code[i] == '@':
        print "pointer: " + str(pointer)
        print "memory:  " + str(space[:10])
    i +=1

if string_builder != "":
    print string_builder
