l = int(input())
s = input()

def is_palindrome(string):
    reversed_string = string [::-1]
    if string[:len(string)//2] == reversed_string[:len(string)//2]:
        return True
    else:
        return False

if is_palindrome(s):
    print(len(s))
    print(s)
else:
    s = [char for char in s]
    s.sort()
    middle = ""
    
    count = 1
    i = 0
    while i < len(s)-1:
        if s[i] == s[i+1]:
            count += 1
            i += 1
        else:
            if count%2:
                if middle == "":
                    middle = s[i]
                s.pop(i)
            else:
                i += 1
            count = 1
    if count%2:
        if middle == "":
            middle = s[-1]
        s.pop(-1)
        
    left = "".join([s[i] for i in range(0,len(s),2)])
    right = left[::-1]
    s = left+middle+right
    
    print (len(s))
    print(s)