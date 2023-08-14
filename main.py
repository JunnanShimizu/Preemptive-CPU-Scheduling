# Junnan Shimizu
# 2/22/22
# Project_Two
# Course: CS337

import pandas as pd

import process
import scheduler

if __name__ == '__main__':
    cpu = []
    ready = []
    time = 0
    average_wait_time = 0
    average_turnaround_time = 0

    process0 = process.Process(0, [5, 6, 7], 0, 30)
    process1 = process.Process(1, [4, 2, 3], 2, 35)
    process2 = process.Process(2, [2, 3, 4], 5, 36)
    process3 = process.Process(3, [5, 2, 7], 6, 20)
    processes = [process0, process1, process2, process3]

    scheduler.add_ready(processes, ready, time)

    while len(ready) > 0:
        time = scheduler.round_robin_scheduler(processes, ready, cpu, time, 2)

    for process in processes:
        average_wait_time += process.get_wait_time()
        average_turnaround_time += process.get_turnaround_time()

    average_wait_time = average_wait_time / len(processes)
    average_turnaround_time = average_turnaround_time / len(processes)

    df = pd.DataFrame(cpu)
    df = df.append({'Wait_Time': average_wait_time, 'Turnaround_Time': average_turnaround_time},
                   ignore_index=True)
    df.to_csv("results.csv", index=False)
