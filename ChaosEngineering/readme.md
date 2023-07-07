# CPU Utilization Utility

This Python utility allows you to increase CPU utilization for testing purposes. It spawns multiple processes that perform CPU-intensive tasks, helping you simulate high CPU load scenarios.

**Disclaimer: Use this utility with caution and only in controlled environments for testing purposes. High CPU utilization can impact system performance.**

## Requirements

- Python 3.x
- `multiprocessing` module (comes with Python standard library)

## Usage

1. Clone the repository or download the `cpu.py` file.

2. Open a terminal or command prompt and navigate to the directory containing the `cpu.py` file.

3. Run the utility using the following command:

   ```shell
   python cpu.py
   ```

4. By default, the utility will spawn 4 processes to increase CPU utilization. You can adjust the num_processes variable in the script to control the number of processes.

5. To stop the utility and terminate the CPU-intensive tasks, press Ctrl+C.

## Checking CPU Utilization

To check CPU utilization while the utility is running, you can use system monitoring tools provided by your operating system. Here are a few options for different platforms:

## Linux

Use the top command or the htop command for a more interactive view. Look for the CPU usage percentage in the output.

## Windows

Open the Task Manager (Ctrl+Shift+Esc), go to the "Performance" tab, and observe the CPU usage graph or the percentage value.
There is another way to get the CPU utilization %, use the following command from the command prompt.

```shell
wmic cpu get loadpercentage
```
## Mac

Open the Activity Monitor (found in the Utilities folder within the Applications folder), go to the "CPU" tab, and check the CPU usage percentage.
Keep in mind that these tools show the overall CPU utilization for the system, so you might see an increase in CPU usage caused by the utility's processes.


# Memory Utilization Utility

This Python utility allows you to increase memory utilization up to a specific percentage for a certain duration. It allocates memory to reach the desired utilization and holds it for the specified duration.

**Disclaimer: Use this utility with caution and only in controlled environments for testing purposes. High memory utilization can impact system performance.**

## Requirements

- Python 3.x
- `numpy` module: To install, run `pip install numpy`
- `psutil` module: To install, run `pip install psutil`

## Usage

1. Clone the repository or download the `memory.py` file.

2. Open a terminal or command prompt and navigate to the directory containing the `memory.py` file.

3. Run the utility using the following command:

```shell
python memory.py
```

By default, the utility will increase memory utilization to 90% for a duration of 60 seconds. You can modify the target_utilization and duration variables in the script to set your desired values.

After the specified duration has elapsed, the utility will release the allocated memory and the script will exit.

## Checking Memory Utilization

To check memory utilization while the utility is running, you can use system monitoring tools provided by your operating system. Here are a few options for different platforms:

## Linux

Use the free command or the htop command for a more detailed view. Look for the memory utilization percentage in the output.

## Windows

Open the Task Manager (Ctrl+Shift+Esc), go to the "Performance" tab, and observe the memory usage graph or the percentage value.

## Mac

Open the Activity Monitor (found in the Utilities folder within the Applications folder), go to the "Memory" tab, and check the memory utilization percentage.
Keep in mind that these tools show the overall memory utilization for the system, so you might see an increase in memory usage caused by the utility's memory allocation.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License
This CPU Utilization Utility is open-source and distributed under the MIT License.

```arduino
Feel free to modify this `README.md` template according to your specific need
```
