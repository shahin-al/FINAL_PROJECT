import getpass
import time 
import itertools
import re
password = getpass.getpass('\033[1m Password: \033[0m')

'''
TIME COMPLEXITY: O=N^M    #N-size of alphabet     #M-length of password    --->  60^8 = 1,679*10^14
'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            '0','1','2','3','4','5','6','7','8','9','_','-','!','$','#','@','.',' ']
attempts = 1

def cracking(passw):
    print('\033[1;35mCracking started...\033[0m')
    time.sleep(1)
    global alltime, attempts, z
    start = time.time()
    for y in itertools.product(alphabet, repeat=len(passw)):
        current_attempt = ''.join(y)
        if current_attempt!=passw:
            attempts += 1
            print(current_attempt)
        elif current_attempt == passw:
            print(f'\033[1;31m{current_attempt}\033[0m', end='\r')  
            end = time.time()
            z = current_attempt
            alltime = end - start 
            break

cracking(password)

print('\n\033[1;35mPassword is cracked successfully!\n')
time.sleep(1)
print('Printing information...')
time.sleep(1)
print(f'\n\033[1;32mPassword:\033[1;36m {z} \033[0m' )
print(f'\033[1;32mTotal time:\033[1;37m {alltime} seconds')
print(f'\033[1;32mTotal attempts:\033[1;37m {attempts}\033[0m')
def checking_p(passw):
    s=0
    m=0
    w=0
    if len(passw)<6:
        w+=3
    elif len(passw)<=8:
        m+=1
    else:
        s+=1
    if re.search(r'[a-z]',passw):
        w+=1
        m+=1
        s+=1
    if re.search(r'[A-Z]',passw):
        m+=1
        s+=2
    if re.search(r'[0-9]',passw):
        s+=2
    if re.search(r'_-!$#@ ' ,passw ):
        s+=2
    if re.search(r'123|456|12345|qwerty|abcde|qwerty123|ufaz|mama|papa|password|aaa|bbb|ccc|ddd|eee|fff|ggg|hhh|iii|jjj|kkk|lll|mmm|nnn|ooo|rrr|sss|ttt|uuu|qqq|vvv|www|xxx|yyy|zzz|AAA|BBB|CCC|DDD|EEE|FFF|GGG|HHH|III|JJJ|KKK|LLL|MMM|NNN|OOO|RRR|SSS|TTT|UUU|QQQ|VVV|WWW|XXX|YYY|ZZZ', passw):
        w+=3
    if alltime<=29:
        w+=3
    elif alltime<60 and alltime>29:
        m+=3
    else:
        s+=2
    if max(s,m,w)==s:
        print('\033[1;32mPassword strenght: \033[1;37mstrong\033[0m')
    elif max(s,m,w)==m:
        print('\033[1;32mPassword strenght: \033[1;37mmedium\033[0m')
    else:
        print('\033[1;32mPassword strenght: \033[1;37mweak\033[0m')
checking_p(password)
