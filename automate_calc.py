time_to_automate = 10 # Time it takes to automate the task
time_to_perform = 15  # Time it takes to perform the task manually
amount_of_times_done = 60 # Number of times the task is done manually

if time_to_automate < (time_to_perform * amount_of_times_done):
    print("It's worth automating this task.")
else:
    print("It may not be worth automating this task.")