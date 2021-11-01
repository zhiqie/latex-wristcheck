# -*- coding: utf-8 -*
from pylatexenc.latexencode import unicode_to_latex
def pdf(text,path,filename):
    import fileinput
    import os
    temp_file = path+ '/' +filename + '.tex'
    conv_text = []
   # os.makedirs(path)
    for item in text:
        conv_text.append(unicode_to_latex(item))

        
    # Read in the file
    with open('wrticheck.tex','r') as file:
        filedata = file.read()
        # Replace the target string
        filedata = filedata.replace('TIME', conv_text[0])
        filedata = filedata.replace('NAME', conv_text[1])
        filedata = filedata.replace('$No$', conv_text[2])
        filedata = filedata.replace('$Brand$', conv_text[3])
        filedata = filedata.replace('$Model$',conv_text[4])
        filedata = filedata.replace('$Serial$',conv_text[5])
        filedata = filedata.replace('$WB$',conv_text[6])
        filedata = filedata.replace('$WP$',conv_text[7])
        filedata = filedata.replace('$NWP$',conv_text[8])
        filedata = filedata.replace('$NWPF$',conv_text[9])
    with open(temp_file,'w') as file:
        file.write(filedata)
    os.system("pdflatex "+temp_file)
    if os.path.exists(temp_file):
        os.remove(temp_file)
    else:
        print("no such file")


    return

text=["14th October,2021","555 666","2","456","456","456","N","Y","HKD$456,456","HKD$456,456"]
pdf(text, './', 'namewww')   