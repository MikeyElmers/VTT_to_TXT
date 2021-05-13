import os.path
import re 

def VTT_converter(filename):
    # Set file input for reading and file output for writing 
    filename_in = filename
    filename_out = filename + ".txt"

    # Check if filename exists
    if not os.path.isfile(filename_in):
        print('File does not exist.')

    # Create lists
    time_list = []
    time_list2 = []
    word_list = []
    word_list2 = []
    word_list3 = []

    # Open file as one giant text 
    buffer = open(filename_in).read()
    #print(buffer)

    # Collect time stamps before the arrow "-->"
    time_list = re.findall(r"([^\r\n]*)-->", buffer)

    # Collect time stamps between "<" and ">"
    time_list2 = re.findall(r"<([0-9]*:[0-9]*:[0-9]*.[0-9]*)>", buffer)

    # Combine both time lists together
    for i in time_list2:
        time_list.append(i)

    # Sort time list 
    time_list.sort()

    # Collect all words (and other characters on the same line)
    word_list = re.findall(r"-->.*%[\n\r].*[\r\n]([^\r\n]*)", buffer)

    # Removes unwanted characters from the word and append to word_list2
    # word_list2 is a list that contains a list of words from for each line
    # [['hello'], [], ["we're", 'going', 'to', 'have', 'a', 'quick', 'look', 'at', 'how'], [],
    # ['to', 'take', 'a', 'recording', 'of', 'a', 'conversation'], [], ['and', 'transform', 'it', 'into', 'graphical']]
    for i in word_list:
        mod_str = re.sub(r"<([0-9]*:[0-9]*:[0-9]*.[0-9]*)>", '', i)
        mod_strv2 = re.sub(r"<c>|</c>", "", mod_str)
        temp = mod_strv2.split()
        word_list2.append(temp)


    # Converts word_list2 (list of lists) in a word_list3 (single list)
    # Converts single word lines and "" (silent lines) into strings
    for i in range(len(word_list2)):
        if len(word_list2[i]) > 1:
            for j in word_list2[i]:
                word_list3.append(j)
        else:
            word_list3.append(str(word_list2[i]))

    # Removes extraneous characters and converts silence to '' 
    for i in range(len(word_list3)):
        word_list3[i] = re.sub('\[|\]|\'|"', "", word_list3[i])

    # Prints to console (FOR TESTING) 
    ##for i in range(len(time_list)):
    ##    print(time_list[i] + " " + word_list3[i])

    # Open output file and write "time (space) word" 
    with open(filename_out, 'w') as f_out:
        for i in range(len(time_list)):
            f_out.write(time_list[i] + " " + word_list3[i])
            f_out.write("\n")

    # close files
    f_out.close()
        
print(os.listdir())
for f in os.listdir():
    if re.search(r'.vtt$', f):    
        VTT_converter(f)


