class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time

def calculate_waiting_time(processes):
    completed_processes = []
    current_time = 0
    total_processes = len(processes)
    waiting_times = {}

    while len(completed_processes) < total_processes:
        shortest = None

        for process in processes:
            if process.arrival_time <= current_time and process.remaining_time > 0:
                if shortest is None or process.remaining_time < shortest.remaining_time:
                    shortest = process

        if shortest is None:
            current_time += 1
            continue

        shortest.remaining_time -= 1
        current_time += 1

        if shortest.remaining_time == 0:
            completed_processes.append(shortest)
            waiting_time = current_time - shortest.burst_time - shortest.arrival_time
            waiting_times[shortest.pid] = waiting_time

    return waiting_times

# Creating processes (PID, arrival_time, burst_time)
processes = [
    Process(1, 0, 6),
    Process(2, 1, 4),
    Process(3, 2, 2),
    Process(4, 3, 3)
]

# Calculate waiting times
waiting_times = calculate_waiting_time(processes)

# Calculating average waiting time
average_waiting_time = sum(waiting_times.values()) / len(waiting_times)

# Outputting results
print("Waiting times:", waiting_times)
print("Average waiting time:", average_waiting_time)
