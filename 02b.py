def process_sample(file):
    lines = file.readlines()
    lines = [x.strip() for x in lines]
    return lines

def get_common_lines(lines):
    for first in lines:
        for second in lines:
            if first != second:

                diff_count = 0
                for letter_a, letter_b in zip(first, second):
                    if letter_a != letter_b:
                        diff_count += 1

                if diff_count <= 1:
                    return ''.join([x for x in first if x in first and x in second])

    return ""

sample = open("02-sample.txt", "r")
lines = process_sample(sample)
print(get_common_lines(lines))
