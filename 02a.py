def process_sample(file):
    lines = file.readlines()
    lines = [x.strip() for x in lines]
    return lines

def get_occurrences(lines):
    occurrences = {}

    for line in lines:
        line_occurrences = {}

        for letter in line:
            if letter in line_occurrences:
                line_occurrences[letter] += 1
            else:
                line_occurrences[letter] = 1

        line_occurrences = {k:v for k,v in line_occurrences.items() if v > 1}

        filtered = {}
        for k, v in line_occurrences.items():
            if v not in filtered.values():
                filtered[k] = v

        line_occurrences = filtered

        for letter, occurrence in line_occurrences.items():
           if occurrence in occurrences:
                occurrences[occurrence] += 1
           else:
                occurrences[occurrence] = 1

    return occurrences

def get_checksum(occurrences):
    checksum = 1

    for key, value in occurrences.items():
        checksum *= value

    return checksum

sample = open("02-sample.txt", "r")
lines = process_sample(sample)
occurrences = get_occurrences(lines)
checksum = get_checksum(occurrences)

print(checksum)
