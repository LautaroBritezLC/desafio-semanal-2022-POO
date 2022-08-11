
def fib(lim):
    pre = 0
    pos  = 1
    while(pre < lim):
        print(pre, end= " - ")
        pre, pos = pos, pre+pos
        
fib(50)
        