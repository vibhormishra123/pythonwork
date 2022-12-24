def demo_bad_catch():
    try:
        raise ValueError('Represents a hidden bug, do not catch this')
        raise Exception('This is the exception you expect to handle')
    except Exception as error:
        print('Caught this error: ' + repr(error))

>>> demo_bad_catch()
Caught this error: ValueError('Represents a hidden bug, do not catch this',)