from os import walk
from os.path import sep

def word_count_by_scene(scene_folder):
    count={}
    for root,subfolders,files in walk(scene_folder):
        if root != scene_folder:
            continue
        for text_file in files:
            filename=text_file
            count[filename]=0
            text_file=sep.join((scene_folder,text_file))
            with open(text_file,mode='r') as rfile:
                for line in rfile.readlines():
                    line=line.split(' ')
                    count[filename]+=len(line)
    return count

def word_count_calculator(scene_folder,stop_scene=0):
    count=word_count_by_scene(scene_folder)
    total=0
    current_scene=1
    for number in count.values():
        if current_scene == stop_scene:
            break
        total+=number
        current_scene+=1
    return total

wc=word_count_calculator('scenes')
exit(code=wc)

if __name__ == '__main__':
    pass
