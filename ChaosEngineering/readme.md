# CPU Utilization Utility

This Python utility allows you to increase CPU utilization for testing purposes. It spawns multiple processes that perform CPU-intensive tasks, helping you simulate high CPU load scenarios.

**Disclaimer: Use this utility with caution and only in controlled environments for testing purposes. High CPU utilization can impact system performance.**

## Requirements

- Python 3.x
- `multiprocessing` module (comes with Python standard library)

## Usage

1. Clone the repository or download the `cpu_utilization.py` file.

2. Open a terminal or command prompt and navigate to the directory containing the `cpu_utilization.py` file.

3. Run the utility using the following command:

   ```shell
   python cpu_utilization.py
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

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License
This CPU Utilization Utility is open-source and distributed under the MIT License.

```arduino
Feel free to modify this `README.md` template according to your specific need
```