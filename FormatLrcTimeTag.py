import os
import string

path = eval(input("请输入文件路径："))
output_lines = []
with open(path, 'r', encoding='utf-8') as lrc:
    lines = lrc.readlines()
    for line in lines:
        if line.find(":",5,7) != -1:
            temp = list(line)
            temp[6] = '.'
            line = ''.join(temp)
            print("replaced")
        output_lines.append(line)
with open(path, 'w', encoding='utf-8') as output_file:
    output_file.writelines(output_lines)
    print("success.")
