def sum_odd_n(n):
    total=0
    j=2*n-1
    i=1
    if i>j:
        return 1
    else: 
        total =((j+1)/2)**2
    i+=2
    return total


> >>> sum_odd_n(5)
> 25.0
> >>> sum_odd_n(4)
> 16.0
> >>> sum_odd_n(1)
> 1.0
pythonpython-3.xrecursion