def text_analytics(file_path)->tuple:
    char_count1 = 0
    char_count2 = 0 # with spaces
    word_count = 0
    line_count = 0
    with open(file_path) as file:
        lines = file.readlines()
        line_count = len(lines)
        for line in lines:
            words = line.split()
            word_count += len(words)
            char_count2 += len(line)
            for word in words:
                char_count1 += len(word)
    return line_count, word_count, char_count1, char_count2

lc, wc, cc1, cc2 = text_analytics("book/chapter1.txt")
print(f"""
Word Count: {wc}
Char Count w/o spaces: {cc1}
Char Count w/ spaces: {cc2}
Line Count: {lc}""")

lc, wc, cc1, cc2 = text_analytics("book/chapter2.txt")
print(f"""
Word Count: {wc}
Char Count w/o spaces: {cc1}
Char Count w/ spaces: {cc2}
Line Count: {lc}""")