def your_function(arg1, arg2, argn):
    * do stuff *


new_thread = threading.Thread(target=your_function, args=(arg1, arg2, argn))
new_thread.name = 'your name'
new.thread.start()