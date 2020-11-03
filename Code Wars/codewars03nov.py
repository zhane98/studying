#https://www.codewars.com/kata/50654ddff44f800200000007/train/python

def solution(a, b):

    first = len(a)
    second = len(b)

    if first > second:
        return b + a + b

    elif second > first:
        return a + b + a
    
    else:
        print("incorrect")


print(solution('45', '1')) #'1451'),
print(solution('13', '200')) #, '1320013'),
print(solution('Soon', 'Me')) #, 'MeSoonMe'),
print(solution('U', 'False')) #, 'UFalseU')


Simple answer = return a+b+a if len(a)<len(b) else b+a+b