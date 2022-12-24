def test_range(n):
    if n in range(10,20):
        print( "Number %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
test_range(15)