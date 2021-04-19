from os import walk, sep

def replace_quote(line):
    k=0
    new_line=''
    for word in line:
        if word == '\"':
            if not k % 2:
                word='``'
            k+=1
        new_line+=word
    return new_line

def replace_squote(line):
    line=line.split(sep=' ')
    new_line=[]
    for word in line:
        if word[0] == '\'' and word[-1] == '\'':
            word='`'+word[1:-1]+'\''
        if len(word) > 2:
            triquotes=tuple(word[:3])
            if triquotes == ('`','`','\''):
                word='``\\,`'+word[3:]
        new_line.append(word)
    return ' '.join(new_line)

def replace_ssquote(line):
    if line.count('\'') % 2:
        return line
    k=0
    new_line=''
    for n,word in enumerate(line):
        if word == '\'':
            if k % 2 == 0:
                if n > 0:
                    if line[n-1] == ' ':
                        word='`'
                else:
                    word='`'
                    print(line)
            k+=1
        new_line+=word
    return new_line

def fix_file_quote(file):
    suffix=file[0]
    new_lines=()
    with open(file,'r') as rfile:
        for line in rfile.readlines():
            line=replace_ssquote(line)
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
            file=story_folder+sep+file
            fix_file_quote(file)

if __name__ == '__main__':
    fix_prose()
