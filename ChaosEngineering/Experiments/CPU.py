import multiprocessing
import time


def cpu_intensive_task():
    while True:
        # Perform CPU-intensive operations here
        pass


def increase_cpu_utilization(num_processes):
    processes = []

    for _ in range(num_processes):
        process = multiprocessing.Process(target=cpu_intensive_task)
        process.start()
        processes.append(process)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        for process in processes:
            process.terminate()
            process.join()


if __name__ == '__main__':
    num_processes = 10  # Number of processes to spawn (increase this value to increase CPU utilization)
    increase_cpu_utilization(num_processes)
