import time
import threading


def add():
    global x
    for i in range(10000000):
        x += 1

def subtract():
    global x
    for i in range(10000000):
        x -= 1

if __name__ == "__main__":
    x = 0
    start = time.perf_counter()
    t1 = threading.Thread(target = add)
    # 1. Add 1 line of code to create a new thread that will run the subtract function 
    t1.start()
    # 2. Add 1 line of code to  start the new thread that you created in step 1
    t1.join()
    # 3. Add 1 line of code to cause the program to wait until your thread started in step 2 has completed. 
    end = time.perf_counter()
    print('final x =' + str(x))
    print(f'elapsed time = {end - start}')
    
# 4. Run the program multiple times. Describe what happens with x.

# 5. In a couple of sentences, explain why you think the value of x changes the way it does.