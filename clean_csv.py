import re
with open("google-tag.csv") as input_fh:
    with open("g-tag.csv", "w", encoding="UTF-8") as output_fh:
        for line in input_fh:
            line = line.strip()
            arr = line.split(',')
            if arr[0].isdigit():
                line = '\n' + line
            line = re.sub(r'[,]+', ',', line)
            print(line)
            output_fh.write(line)
