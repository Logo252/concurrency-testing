# Create venv in current directory:
`python3 -m venv ./venv`

# Install the dependencies
`pip install -r requirements.txt`

# Threading vs Multiprocessing
# ==========================
Threading - A thread is a sequence of instructions within a program that can be executed independently of other code.
Multiprocessing - A process is an instance of a computer program that is being executed. It contains the program code and its current activity.
Differences:
1. Threading is a subset of multiprocessing. Multiprocessing is a superset of threading.
2. Threading is a lightweight process. Multiprocessing is a heavyweight process.
3. Threading shares memory. Multiprocessing does not share memory.
4. Threading is faster than multiprocessing.
5. Threading is used for I/O bound tasks. Multiprocessing is used for CPU bound tasks.
6. Threading is used for GUI applications. Multiprocessing is used for server applications.
7. Threading is used for asynchronous tasks. Multiprocessing is used for synchronous tasks.
8. Threading is used for real-time applications. Multiprocessing is used for non-real-time applications.
9. Threading is used for short-lived tasks. Multiprocessing is used for long-lived tasks.
10. Threading is used for cooperative multitasking. Multiprocessing is used for preemptive multitasking.


# Multi threading
Report the default number of worker threads on your system
```
from concurrent.futures import ThreadPoolExecutor
# create a thread pool with the default number of worker threads
executor = ThreadPoolExecutor()
# report the number of worker threads chosen by default
print(executor._max_workers)
```

# TO DO:
# ======
1. The goal is to convert the single threaded script to multithreaded and multi processed scripts. Then compare the performance of the three scripts.
2. The exercises are under the folder `exercises`
3. Each exercise contains folder which contains single threaded script
4. As the example, `factorial` folder contains completed exercise - script to calculate factorial of a number in 3 ways:
    1. Single threaded
    2. Multithreaded
    3. Multiprocessed
