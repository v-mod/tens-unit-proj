# Maths: Tens and Units Project
#
# This Code was made by Vivaan Modi
# NOTE: It will generate the sequnce forever until you kill the program!
print('Maths: Tens and Units Project')
print('')
print('This Code was made by Vivaan Modi')
print('NOTE: It will generate the sequnce forever until you kill the program!')
possible_num=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19']
start_repeat=0
def check_repeat(start_repeat,num,possible_num):
    if str(num) in ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19'] and start_repeat==int(num):
        quit()
        return start_repeat
    elif str(num) in ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19'] and str(start_repeat) != str(num):
        start_repeat=int(num)
        return int(num)
def generate_seqeunce(length,num,start_repeat,possible_num):
    start_repeat=check_repeat(start_repeat,num,possible_num)
    if length == '1':
        return int(num)*2, start_repeat
    elif length=='2':
        num1=str(num)[0]
        num2=str(num)[1]
        return str(int(num2)*2+int(num1)), start_repeat
num=input('Number to start sequence on: ')
while True:
    if len(str(num))==1:
        num,start_repeat=generate_seqeunce('1',num,start_repeat,possible_num)
        print(str(num)+', ', end="")
    elif len(str(num))==2:
        num, start_repeat=generate_seqeunce('2',num,start_repeat,possible_num)
        print(str(num)+', ', end="")
