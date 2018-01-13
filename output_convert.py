import os
import linecache

filelist=open('output_little.txt').readlines()
count = len(filelist)
#face_num=1
face_num_pre=1
face_num_cur=1
findsame_flag=False
switch_flag=False
data_tmp=[]
txtName = "output_my_convert.txt"
f_convert=file(txtName, "a+")
for i in range(count-1):  
    fst_line=linecache.getline('output_my.txt',i)
    sec_line=linecache.getline('output_my.txt',i+1)  
    fst_line_name=fst_line.split("\t")[0]
    sec_line_name=sec_line.split("\t")[0]
    fst_line_data_raw=fst_line.split("\t")[-5:]
    sec_line_data_raw=sec_line.split("\t")[-5:]
    fst_line_data=' '.join(fst_line_data_raw).rstrip('\n')
    sec_line_data=' '.join(sec_line_data_raw).rstrip('\n')
    if findsame_flag: 
       if fst_line_name == sec_line_name:
          face_num_cur = face_num_pre + 1
          face_num_pre = face_num_cur
         # f_convert.write(str(sec_line_data)+'\n')
          data_tmp.append(sec_line_data)
          findsame_flag = True
       else:
           f_convert.write(str(face_num_pre)+'\n')
           data_writedown='\n'.join(data_tmp)
           f_convert.write(data_writedown+'\n')
           data_tmp=[]
           face_num_cur = 1
           findsame_flag = False
    else:
        f_convert.write(str(fst_line_name)+'\n')
        if fst_line_name == sec_line_name:
          face_num_cur = face_num_cur + 1
          face_num_pre = face_num_cur
       
          data_tmp.append(fst_line_data)
          data_tmp.append(sec_line_data)
#          f_convert.write(str(face_num_cur)+'\n')
 ##         f_convert.write(str(fst_line_data)+'\n')
   #       f_convert.write(str(sec_line_data)+'\n')
          findsame_flag = True
        else:
            face_num_cur = 1
            f_convert.write(str(face_num_cur)+'\n')
            f_convert.write(str(fst_line_data)+'\n')
            findsame_flag = False
f_convert.close()    


  
