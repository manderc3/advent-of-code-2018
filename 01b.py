# THIS SOLUTION TAKES TOO LONG :(

def calculate_from_sample(seq):
    visited_frequencies = [0]
    val = 0

    while(True):
        for i in seq:
            val += i
            if val in visited_frequencies:
                return val
            visited_frequencies.append(val)

    return val

def process_sample(file):
    operands = []
    operand = ''
    pos = True

    for i in file:
        if i == '+':
            pos = True
        elif i == '-':
            pos = False
        elif i in "1234567890":
            operand += i
        elif i == '\n':
            if pos:
                operands.append(int(operand))
            else:
                operands.append(int(operand) * -1)

            operand = ''

    return operands

sample = open("01-sample.txt", "r")

sequence = process_sample(sample.read())

result = calculate_from_sample(sequence)

print(result)
