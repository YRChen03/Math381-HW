import random

# Constants
# Starting time of the workday in minutes past 9:00 AM
workday_start = 0  
# Interval between appointments in minutes
appointment_interval = 30  
# Number of simulation runs
num_simulations = 10000

# Function to determine the length of a patient's appointment
def meet_length():
    # Generate a random number between 0 and 1
    rand = random.uniform(0, 1)
    # Return appointment length based on the probability distribution given
    if rand <= 0.1:
        return 24
    elif rand <= 0.1 + 0.2:
        return 27
    elif rand <= 0.1 + 0.2 + 0.4:
        return 30
    elif rand <= 0.1 + 0.2 + 0.4 + 0.15:
        return 33
    elif rand <= 0.1 + 0.2 + 0.4 + 0.15 + 0.1:
        return 36
    else:
        return 39

# Function to determine a patient's arrival time relative to their appointment
def arrive_time():
    # Generate a random number between 0 and 1
    rand = random.uniform(0, 1)  
    # Return arrival time based on the probability distribution given
    if rand <= 0.10:
        # 15 minutes early
        return -15  
    elif rand <= 0.10 + 0.25:
        # 5 minutes early
        return -5   
    elif rand <= 0.10 + 0.25 + 0.50:
        # On time
        return 0    
    elif rand <= 0.10 + 0.25 + 0.50 + 0.10:
        # 10 minutes late
        return 10   
    else:
        # 15 minutes late
        return 15   

# Simulation function for a single day
def simulation():
    # Start the simulation at the beginning of the workday
    current_time = workday_start  
     # Iterate over each of the 16 patients
    for i in range(16): 
        # Calculate patient's scheduled arrival time and adjust based on actual arrival
        patient_arrival_time = workday_start + appointment_interval * i + arrive_time()
        # Get the length of the appointment
        appointment_length = meet_length() 

        # If patient arrives before the current time, wait until the current time
        if patient_arrival_time < current_time:
            patient_arrival_time = current_time
        
        # Update current time to reflect the end of this appointment
        current_time = patient_arrival_time + appointment_length
    # Return the total length of the workday in minutes
    return current_time - workday_start

# Run the simulation multiple times and calculate the average day length
total_day_length = 0
for _ in range(num_simulations):
    # Accumulate total length of all simulated days
    total_day_length += simulation()

# Calculate the average length of the doctor's workday in hours
average_day_length = total_day_length / num_simulations / 60
print(average_day_length)