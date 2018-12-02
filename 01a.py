def process_sample(seq):
    val = 0
    operand = ''
    add = False

    for i in seq:
        if i == '+':
            add = True
        elif i == '-':
            add = False
        elif i in "1234567890":
            operand += i
        elif i == '\n':
            if add:
                val += int(operand)
            else:
                val -= int(operand)

            operand = ''

    return val

sample = open("01-sample.txt", "r")

print(process_sample(sample.read()))
