import numpy as np

def roll_dice():
    # Simulates rolling two six-sided dice and returns their sum.
    return np.random.randint(1, 7) + np.random.randint(1, 7)

def play_craps():
    # Simulates a single game of craps according to the specific rules.
    first_roll = roll_dice()  # Get the sum of the first roll.
    
    # Check if the first roll is an immediate win (7 or 11) or loss (2, 3, 12).
    if first_roll in [7, 11]:
        return True  # Player wins.
    elif first_roll in [2, 3, 12]:
        return False  # Player loses.
    else:
        # The game enters the second phase if the first roll is not decisive.
        # The player rerolls until they either match their first roll (win)
        # or roll a 7 (lose).
        while True:
            roll = roll_dice()
            if roll == 7:
                return False  # Player loses.
            elif roll == first_roll:
                return True  # Player wins.

# Main simulation loop
num_trials = 10000  # Number of games to simulate.
wins = sum(play_craps() for _ in range(num_trials))  # Count how many games are won.
win_percentage = (wins / num_trials) * 100  # Calculate the win percentage.

print(win_percentage,'%')  # Display the calculated win percentage.



# Define the probabilities and offsets for patient arrival times (in minutes).
arrival_offsets = [-15, -5, 0, 10, 15]  # Early by 15 mins, 5 mins, on time, late by 10, 15 mins.
arrival_probabilities = [0.10, 0.25, 0.50, 0.10, 0.05]

# Appointment lengths distribution and probabilities from Table 21.
appointment_lengths = [24, 27, 30, 33, 36, 39]  # Appointment lengths in minutes from the table.
appointment_probabilities = [0.10, 0.20, 0.40, 0.15, 0.10, 0.05]  # Probabilities from the table.

def simulate_day():
    current_time = 0  # Start at 9:00 AM in minutes.
    patient_scheduled_time = current_time
    for _ in range(16):  # For each of the 16 patients.
        arrival_time_offset = np.random.choice(arrival_offsets, p=arrival_probabilities)
        appointment_length = np.random.choice(appointment_lengths, p=appointment_probabilities)
        patient_arrival_time = patient_scheduled_time + arrival_time_offset
        # The doctor sees the patient immediately if they're present, or waits for them.
        current_time = max(current_time, patient_arrival_time)
        current_time += appointment_length  # Add the length of the appointment.
        patient_scheduled_time += 30  # Next patient scheduled 30 mins after the previous one.
    return current_time  # Return the total minutes.

# Simulate multiple days and calculate average length of the doctor's day.
num_days = 1000
total_time = sum(simulate_day() for i in range(num_days))
average_length_minutes = total_time / num_days

# Convert average length back to hours and minutes.
average_hours = average_length_minutes // 60
average_minutes = average_length_minutes % 60

print(average_hours,'h', average_minutes, 'min')