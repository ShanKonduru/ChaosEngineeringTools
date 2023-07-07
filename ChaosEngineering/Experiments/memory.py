import ctypes
import numpy as np
import time

def increase_memory_utilization(target_utilization, duration):
    # Calculate the target memory allocation size based on the percentage
    total_memory = psutil.virtual_memory().total
    target_bytes = int((target_utilization / 100) * total_memory)

    # Allocate a memory block with the target size
    mem_block = np.zeros(target_bytes, dtype=np.uint8)

    # Access each element in the memory block to ensure it is actually allocated
    for i in range(len(mem_block)):
        mem_block[i] = 1

    # Sleep for the desired duration
    time.sleep(duration)


if __name__ == '__main__':
    target_utilization = 90  # Target memory utilization percentage
    duration = 60  # Duration in seconds for which memory should be utilized
    increase_memory_utilization(target_utilization, duration)
