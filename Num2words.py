######### this block let the user input the name of the .txt file located on his/her desktop 
txt_file = input('Enter the name of the .txt file that sits in your Destop WITHOUT the .txt extension: ')

######### this block is the routine to extract the string from a txt file in your desktop
txt_file = open(txt_file + '.txt', 'r')
input_str = txt_file.read()
txt_file.close()

######### this block is the routine to check if the number in the input string is valid. It is based on 2 functions:
######### first function - hasNumbers checks if there are numbers in the string
######### second function - check_before_after_num checks if there is anything different from a space before or after the number in the string
######### last function - extract_number runs the above two functions 
import re
def hasNumbers(input_str):
    return any(char.isdigit() for char in input_str)

def check_before_after_num(input_str):
    check  = ['1', '2', '3', '4', '5', '6', '7','8', '9']
    char_in_list = [i for i in input_str]
    char_in_list.insert(0,' ')
    char_in_list.insert(len(char_in_list), ' ')
    
    index_num_in_string = [index for index,value in enumerate(char_in_list) if value in check]
    before_first_num, after_last_num = index_num_in_string[0]-1 , index_num_in_string[-1] +1
    
    if char_in_list[before_first_num] and char_in_list[after_last_num] != ' ':
        raise Exception('number invalid')
    elif char_in_list[before_first_num] != ' ':
        raise Exception('number invalid')
    elif char_in_list[after_last_num] != ' ':
        raise Exception('number invalid')
    else:
        pass
    return 

def extract_number(input_str):
    check_before_after_num(input_str)
    if hasNumbers(input_str):
        t = [int(num) for num in re.findall(r'\d+', input_str)] # extracts numbers as consecutive digits and puts them in a list
        assert len(t) == 1, 'number invalid' # if lenght is >1 it means there are more numbers or the number is wrongly input with spaces
    else:
        t = ' '
    return t[0]

######### this routine transforms numbers into words
######### the idea is to loop thru groups of 3 digits (hundreds, tens, units), for each group we use the function num999 to transform the 3 digits into words
ones = ['', 'one ','two ','three ','four ', 'five ', 'six ','seven ','eight ','nine ','ten ','eleven ','twelve ', 'thirteen ', 'fourteen ', 'fifteen ','sixteen ','seventeen ', 'eighteen ','nineteen '] 
twenties = ['','','twenty-','thirty-','forty-', 'fifty-','sixty-','seventy-','eighty-','ninety-'] 
thousands = ['','thousand, ','million, ', 'billion, ', 'trillion, ', 'quadrillion, ', 'quintillion, ', 'sextillion, ', 'septillion, ','octillion, ', 'nonillion, ', 'decillion, ', 'undecillion, ', 'duodecillion, ', 'tredecillion, ', 'quattuordecillion, ', 'quindecillion, ', 'sexdecillion, ', 'septendecillion, ', 'octodecillion, ', 'novemdecillion, ', 'vigintillion, ', 'unvigintillion, ', 'dovigintillion, ', 'trevigintillion, ', 'quattuorvigintillion, ', 'quinvigintillion, ', 'sexvigintillion, ', 'septenvigintillion, ', 'octovigintillion, ', 'novemvigintillion, ', 'trigintillion, ', 'untrigintillion, ', 'dotrigintillion, ', 'tretrigintillion, ', 'quattuortrigintillion, ', 'quintrigintillion, ', 'sextrigintillion, ', 'septentrigintillion, ', 'octotrigintillion, ', 'novemtrigintillion, '] 

def num999(num, k, n): # function to return the words for the groups of hundreds-tens-units
    c = int(num % 10) # units digit 
    b = int(((num % 100) - c) / 10) # tens digit 
    a = int(((num % 1000) - (b * 10) - c) / 100) # hundreds digit 
    t = ''
    h = '' 

    if k == 0 and n == '' or k != 0:
        if a != 0 and b == 0 and c == 0: 
            t = ones[a] + 'hundred '
        elif a != 0: 
            t = ones[a] + 'hundred and ' 

        if b <= 1: 
            h = ones[num%100] 
        elif b > 1: 
            h = twenties[b] + ones[c] 
        st = t + h

    if k == 0 and n != '': # I differentiated between the first iteration of the loop and the others as it should include an "and"
        if a != 0 and b == 0 and c == 0: 
            t = 'and ' + ones[a] + 'hundred ' 
        elif a != 0:
            t = ones[a] + 'hundred and ' 

        if b <= 1: 
            h = ones[num%100] 
        elif b > 1: 
            h = twenties[b] + ones[c] 
        if t == '':
            h = 'and ' + h
        st = t + h    

    if a == 0 and b == 0 and c == 0:
        st = ''

    return st

def num2words(num):
    if num == 0: return 'zero' 
    i = 3
    n = str(num) # it needs to be trasnformed into a string to use the vector
    word = ''
    k = 0
    while(i == 3): # 3 by 3, separate the number in groups of hundreds
        nw = n[-i:]
        n = n[:-i] 
        if int(nw) == 0:
            word = num999(int(nw),k,n) + thousands[int(nw)] + word 
        else: 
            word = num999(int(nw),k,n) + thousands[k] + word
        if n == '':
            i = i+1
        k += 1
    if word[-2] == ',':
        word = word[:-1]
    return word[:-1]

print(num2words(extract_number(input_str)))

