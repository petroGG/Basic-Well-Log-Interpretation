'''
Walakpa1 Well data is available in LAS format.
In file:
- curves names are located at the beginning of lines 20 - 31; 
- log data start at the line 37.
'''
start_curves_names=19
end_curves_names=31
start_log_data=36

lasfile='WA1.las'
txtfile='WA1.txt'

lines = open(lasfile).read().splitlines()

#Read the name of the curves from las and write them in txt file:
curves=[]
for line in lines[start_curves_names:end_curves_names]:
        curves.append(line.split()[0].split('.')[0])
        header=str(curves).replace("['","").replace("']","").replace("', '"," ")
f=open(txtfile,'w')
f.write(header+'\n')

#Then read the log data which starts at line 37 (In Python is 36) and write it in the same .txt file:
for text in lines[36:]:
        f.write(str(text).replace("['","").replace("']","")+'\n')
f.close()
