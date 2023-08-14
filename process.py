# Junnan Shimizu
# 2/22/22
# Project_Two
# Course: CS337

class Process:
    def __init__(self, id, duty, arrival_time, priority):
        self.id = id
        self.duty = duty
        self.initial_arrival = arrival_time
        self.arrival_time = arrival_time
        self.priority = priority
        self.wait_time = 0
        self.turnaround_time = 0
        self.response_time = 0
        self.status = "running"
        self.queue = 0
        self.burst_time = duty[0]

    def get_id(self):
        return self.id

    def get_duty(self, index):
        return self.duty[index]

    def set_duty(self, index, value):
        self.duty[index] = value

    def get_initial_arrival(self):
        return self.initial_arrival

    def get_arrival_time(self):
        return self.arrival_time

    def set_arrival_time(self, value):
        self.arrival_time = value

    def get_priority(self):
        return self.priority

    def set_priority(self, value):
        self.priority = value

    def get_wait_time(self):
        return self.wait_time

    def set_wait_time(self, value):
        self.wait_time = value

    def get_turnaround_time(self):
        return self.turnaround_time

    def set_turnaround_time(self, value):
        self.turnaround_time = value

    def get_response_time(self):
        return self.response_time

    def set_response_time(self, value):
        self.response_time = value

    def get_status(self):
        return self.status

    def set_status(self, value):
        self.status = value

    def get_queue(self):
        return self.queue

    def set_queue(self, value):
        self.queue = value

    def get_burst_time(self):
        return self.burst_time
