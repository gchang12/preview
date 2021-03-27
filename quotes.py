from os import walk, sep

def replace_quote(line):
    k=0
    new_line=''
    for word in line:
        if word == '\"':
            if k % 2 == 0:
                word='``'
            k+=1
        elif word == '``':
            k=0
        new_line+=word
    return new_line

def replace_squote(line):
    line=line.split(sep=' ')
    new_line=[]
    for word in line:
        if word[0] == '\'' and word[-1] == '\'':
            word='`'+word[1:-1]+'\''
        new_line.append(word)
    return ' '.join(new_line)

def fix_file_quote(file):
    suffix=file[0]
    new_lines=()
    with open(file,'r') as rfile:
        for line in rfile.readlines():
            line=replace_quote(line)
            line=replace_squote(line)
            new_lines+=(line,)
    with open(file,'w') as wfile:
        for line in new_lines:
            wfile.write(line)

def fix_prose():
    story_folder=sep.join(['.','scenes'])
    for dirpath,dirnames,filenames in walk(story_folder):
        if dirpath != story_folder:
            continue
        for file in filenames:
            file=sep.join((story_folder,file))
            fix_file_quote(file)

if __name__ == '__main__':
    fix_prose()
