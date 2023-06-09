

#Reading and Writing Files
#open(filename, mode, encoding=None)
f = open("file1.txt",'w', encoding="utf-8")

#Example try_except
"""
Tao file
try:
    f = open('file2.txt','x')
except Exception as e:
    print(e)
finally:
    f.close()
"""


#use with replace try_catch
"""
#with open('file1.txt', encoding="utf-8") as f:
    read_data = f.read()

f.close()
"""

#Doc file 'r'
try:
    with open("file1.txt" , 'r') as f:
        content = f.read()
        print(content)
except Exception as e:
    print(e)

#Doc file theo dong use readline
try:

    with open("file1.txt", 'r') as f:
        list_content = f.readlines();
        i = 0;
        for x in list_content:
            print(str(i) +" : " +x)
            i+=1
except Exception as e:
    print(e)




