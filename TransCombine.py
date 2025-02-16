import os
work_mode = int(input("请输入工作模式：\n1、词典笔模式；2、mp3通用格式（逐行，索尼可用）；3、mp3通用格式（直接拼接）"))

def merge_files(dir_a, dir_b, output_dir):
    count = 0
    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)
    
    # 列出目录A中的所有文件
    files_a = os.listdir(dir_a)

    # 设定指针
    a_flag = 0
    b_flag = 0
    B_exist  = 0
    for file_a in files_a:
        file_name = file_a
        file_a_path = os.path.join(dir_a, file_name)
        file_b_path = os.path.join(dir_b, file_name)
        merged_lines = []
        # print(file_name)
        with open(file_a_path, 'r', encoding='utf-8') as file_a:
            # 读入文件A
            lines_a = file_a.readlines()
            # 检查目录B中是否存在对应的文件
            if os.path.exists(file_b_path):
                B_exist = 1
                with open(file_b_path, 'r', encoding='utf-8') as file_b:
                    # 读入文件B
                    lines_b = file_b.readlines()
	                # print(f'{lines_a}\n{lines_b}')
                    
                    if work_mode == 3:
                        merged_lines.append(lines_a)
                        merged_lines.append(lines_b)
                    else:
                        # 遍历文件A的每一行
                        for line_a in lines_a:
                            merged_lines.append(line_a.strip() + '\n')
                            
                            for line_b in lines_b:
                                
                                # 检查前10个字符是否相同
                                if line_a[:10] == line_b[:10]:
                                    temp = line_b.strip()
                                    if work_mode == 2:
                                        # 逐行模式下不删除时间头
                                        merged_lines.append(temp + '\n')
                                        break
                                    #merged_lines.append(line_a.strip() + '\n' + line_b.strip() + '\n')
                                    elif work_mode == 1:
                                        # 单词笔模式
                                        merged_lines.append(temp[10:] + '\n')
                                        break
            else:# 目录B中不存在对应文件时
                merged_lines = lines_a
                print(f"警告: 目录B中不存在文件 {file_name}，将直接输出原文歌词")
        # 将合并后的内容写入输出目录中的新文件
        output_file_path = os.path.join(output_dir, file_name)
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            # print(output_file_path)
            if work_mode == 3:
                output_file.writelines(lines_a)
                if B_exist :
                    output_file.writelines(lines_b)
            else:
                output_file.writelines(merged_lines)
            
            count = count + 1
            print(f"成功处理第{count}共{len(files_a)}个歌词{file_name}")
        # print(f"{file_b_path}")
    return count



# 示例用法
# 目录用双斜杠防止转义
# repr()和【r'\ntdsibd'】相同，都能禁用转义

path = input("请输入工作根目录，程序会自动识别对应原文/翻译：")
path.replace("'","")
#path += r"\"
patha = path + "lyrics"
pathb = path + "tlyrics"
pathout = path + "outs"

print(f'{path}\n{patha}\n{pathb}\n{pathout}\nover.')
num = merge_files(patha, pathb, pathout)

# num = merge_files("D:\ych_WorkSpace\Cache\歌词\\12.10\lyrics", "D:\ych_WorkSpace\Cache\歌词\\12.10\\tlyrics", "D:\ych_WorkSpace\Cache\歌词\\12.10\outs")
input(f"共已成功处理{num}个文件，按回车键退出。")



