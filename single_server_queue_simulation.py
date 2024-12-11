import heapq
import random

# Constants
NUM_JOBS = 1000
LAMBDA = 2  # Rate for Poisson process (jobs per second)


# Define the Job class
class Job:
    def __init__(self, job_id, arrival_time):
        self.job_id = job_id
        self.arrival_time = arrival_time
        self.finishing_time = None
        self.life_time = 0  # Initially 0

    def __repr__(self):
        return f"Job(id={self.job_id}, arrival={self.arrival_time:.2f}, finish={self.finishing_time}, lifetime={self.life_time})"

class Server:
    def __init__(self):
        self.queue = []  # Queue for waiting jobs
        self.current_job_id = None  # ID of the job currently being served
        self.service_time = 0  # Total service time of the server
        self.remaining_time = 0  # Time remaining to complete the current job

    def __repr__(self):
        return (f"Server(current_job_id={self.current_job_id}, "
                f"queue_size={len(self.queue)}, "
                f"service_time={self.service_time}, "
                f"remaining_time={self.remaining_time:.2f})")


def create_server(service_time):
    """
    Creates and initializes a Server instance with the given service time.
    
    Args:
        service_time (float): The service time for the server.
        
    Returns:
        Server: An initialized Server instance.
    """
    server = Server()
    server.service_time = service_time
    return server


# Example 1 service times for each server
service_time_server_1 = 0.4
service_time_server_2 = 0.6
service_time_server_3 = 0.95

# Creating the servers
server_1 = create_server(service_time_server_1)
server_2 = create_server(service_time_server_2)
server_3 = create_server(service_time_server_3)

# Displaying the created servers
print(server_1)
print(server_2)
print(server_3)
