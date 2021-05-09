from os import walk, sep

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
    for scene_num,number in enumerate(count.values(),start=1):
        if scene_num == stop_scene:
            break
        total+=number
    return total

def word_count_log(scene_folder):
    log_file='word_count'
    wc_dict=word_count_by_scene(scene_folder)
    with open(log_file+'.csv','w') as wfile:
        wfile.write('Filename,Word Count\n')
        for filename,count in wc_dict.items():
            write_values=filename[:-4],',',str(count),'\n'
            for val in write_values:
                wfile.write(val)

if __name__ == '__main__':
    scene_folder=sep.join(['.','raw'])
    wc=word_count_calculator(scene_folder)
    message='\nThe word count is: %d.'%wc
    print(message)
    word_count_log(scene_folder)
