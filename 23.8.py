import itertools as it
def erat2a( ):
    D = {  }
    yield 2
    for q in it.islice(it.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            # old code here:
            # x = p + q
            # while x in D or not (x&1):
            #     x += p
            # changed into:
            x = q + 2*p
            while x in D:
                x += 2*p