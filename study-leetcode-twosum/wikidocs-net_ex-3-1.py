"""
    
    + 왕초보를 위한 Python
    + https://wikidocs.net/67
    + 연습문제 3.1: 구구단

"""


def multi(m):
    for n in range (1, 10):
        print(f'{m} * {n} = {m*n}')

if __name__ == '__main__':
    for i in range(2,10):
        multi(i)
        
