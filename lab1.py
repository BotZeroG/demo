
def string_alternate(s):
    ret = ""
    i = True  # capitalize
    for char in s:
        if i:
            ret += char
        else:
            ret += ""
        if char != ' ':
            i = not i
    return ret


print("enter four values in lbs:")
x, y ,a, b= raw_input().split()
print("Weight converted to kilos: ")
print [round(int(x) / 2.205, 2), round(int(y) / 2.205, 2), round(int(a) / 2.205,  2), round(int(b) / 2.205,  2)]


print("enter any word or sentence:")
i = raw_input().split()
print string_alternate(str(i))

with open('scratch.txt') as f:
    lines = f.readlines()

with open('scratch.txt', 'w') as f:
    for index, value in enumerate(lines):
        number_of_words = len(value.split())
        f.write('Line number {} has {} words.\n'.format(index + 1, number_of_words))

print("file uploaded has been changed.")