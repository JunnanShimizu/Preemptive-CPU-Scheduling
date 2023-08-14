# Junnan Shimizu
# 2/22/22
# Project_Two
# Course: CS337

def find_lowest_arrival(ready):
    minimum = 999999
    process = ready[:1]

    for current in ready:
        if current.get_arrival_time() < minimum:
            minimum = current.get_arrival_time()
            process = current

    return process


def add_ready(processes, ready, time):
    for current in processes:
        if current.get_arrival_time() == time:
            ready.append(current)
            return 1

    return 0


def find_shortest(ready):
    minimum = 999999
    process = ready[:1]

    for current in ready:
        if current.get_duty(0) < minimum:
            minimum = current.get_duty(0)
            process = current

    return process


def find_highest_priority(ready):
    maximum = -999999
    process = ready[:1]

    for current in ready:
        if current.get_priority() > maximum:
            maximum = current.get_priority()
            process = current

    return process


def find_lowest_remaining_time(ready):
    minimum = 999999
    process = ready[:1]

    for current in ready:
        if current.get_duty() > minimum:
            minimum = current.get_duty
            process = current

    return process


def remove_finished_processes(ready, end_time):
    for current in ready:
        if current.get_duty(0) == 0:
            current.set_turnaround_time(end_time - current.get_initial_arrival())
            ready.remove(current)


def fcfs_scheduler(processes, ready, cpu, time, verbose=True):
    process = find_lowest_arrival(ready)
    ready.remove(process)

    start_time = time

    while process.get_burst_time() > 0:
        process.set_burst_time(process.get_burst_time() - 1)
        time += 1
        add_ready(processes, ready, time)

    end_time = time

    for current in processes:
        current.set_turnaround_time(end_time - current.get_arrival_time())
        current.set_wait_time(start_time - current.get_arrival_time())

    cpu.append(dict(process=process.get_id(),
                    Start=start_time,
                    Finish=end_time,
                    Priority=process.get_priority(),
                    Arrival_Time=process.get_arrival_time(),
                    Wait_Time=process.get_wait_time(),
                    Turnaround_Time=process.get_turnaround_time()))

    return time


def sjf_scheduler(processes, ready, cpu, time, verbose=True):
    process = find_shortest(ready)
    ready.remove(process)

    start_time = time

    while process.get_burst_time() > 0:
        process.set_burst_time(process.get_burst_time() - 1)
        time += 1
        add_ready(processes, ready, time)

    end_time = time

    for current in processes:
        current.set_turnaround_time(end_time - current.get_arrival_time())
        current.set_wait_time(start_time - current.get_arrival_time())

    cpu.append(dict(process=process.get_id(),
                    Start=start_time,
                    Finish=end_time,
                    Priority=process.get_priority(),
                    Arrival_Time=process.get_arrival_time(),
                    Wait_Time=process.get_wait_time(),
                    Turnaround_Time=process.get_turnaround_time()))

    return time


def priority_scheduler(processes, ready, cpu, time, verbose=True):
    process = find_highest_priority(ready)
    ready.remove(process)

    start_time = time

    while process.get_burst_time() > 0:
        process.set_burst_time(process.get_burst_time() - 1)
        time += 1
        add_ready(processes, ready, time)

    end_time = time

    for current in processes:
        current.set_turnaround_time(end_time - current.get_arrival_time())
        current.set_wait_time(start_time - current.get_arrival_time())

    cpu.append(dict(process=process.get_id(),
                    Start=start_time,
                    Finish=end_time,
                    Priority=process.get_priority(),
                    Arrival_Time=process.get_arrival_time(),
                    Wait_Time=process.get_wait_time(),
                    Turnaround_Time=process.get_turnaround_time()))

    return time


def round_robin_scheduler(processes, ready, cpu, time, quantum):
    process = find_lowest_arrival(ready)
    start_time = time

    for i in range(quantum):
        process.set_duty(0, (process.get_duty(0) - 1))
        time += 1
        add_ready(processes, ready, time)
        process.set_arrival_time(time)
        if process.get_duty(0) == 0:
            remove_finished_processes(ready, time)
            break

    end_time = time
    process.set_wait_time(process.get_turnaround_time() - process.get_burst_time())

    cpu.append(dict(process=process.get_id(),
                    Start=start_time,
                    Finish=end_time,
                    Priority=process.get_priority(),
                    Arrival_Time=process.get_arrival_time(),
                    Wait_Time=process.get_wait_time(),
                    Turnaround_Time=process.get_turnaround_time()))

    return time


def srt_scheduler(processes, ready, cpu, time, blank):
    process = find_shortest(ready)
    start_time = time

    while process.get_duty(0) > 0:
        process.set_duty(0, (process.get_duty(0) - 1))
        time += 1
        remove_finished_processes(ready, time)
        if add_ready(processes, ready, time) == 1 and find_shortest(ready) != process:  # a new value was added
            break

    end_time = time
    process.set_wait_time(process.get_turnaround_time() - process.get_burst_time())

    cpu.append(dict(process=process.get_id(),
                    Start=start_time,
                    Finish=end_time,
                    Priority=process.get_priority(),
                    Arrival_Time=process.get_arrival_time(),
                    Wait_Time=process.get_wait_time(),
                    Turnaround_Time=process.get_turnaround_time()))

    return time


def preemptive_priority_scheduler(processes, ready, cpu, time, blank):
    process = find_highest_priority(ready)
    start_time = time

    while process.get_duty(0) > 0:
        process.set_duty(0, (process.get_duty(0) - 1))
        time += 1
        remove_finished_processes(ready, time)
        if add_ready(processes, ready, time) == 1:  # a new value was added
            break

    end_time = time
    process.set_wait_time(process.get_turnaround_time() - process.get_burst_time())

    cpu.append(dict(process=process.get_id(),
                    Start=start_time,
                    Finish=end_time,
                    Priority=process.get_priority(),
                    Arrival_Time=process.get_arrival_time(),
                    Wait_Time=process.get_wait_time(),
                    Turnaround_Time=process.get_turnaround_time()))

    return time

