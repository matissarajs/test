#!/usr/bin/env python3
import re
import csv

def analyze_syslog(file_path):
    # Error count
    error_count = {}

    pattern = r'ERROR (.+?) \((.+?)\)'

    with open(file_path, "r") as log_file:
        for log_line in log_file:
            match = re.search(pattern, log_line)
            if match:
                error_message_text = match.group(1).strip()  # Extract and strip whitespace
                username = match.group(2).strip()  # Extract and strip whitespace
                
                # Update error count dictionary
                if error_message_text in error_count:
                    error_count[error_message_text] += 1
                else:
                    error_count[error_message_text] = 1

    # Return error count
    return error_count

def analyze_user_statistics(file_path):
    # Define a dictionary to store user statistics
    user_statistics = {}

    # Define regex patterns for INFO and ERROR log lines
    info_pattern = r'INFO (.+?) \((.+?)\)'
    error_pattern = r'ERROR (.+?) \((.+?)\)'

    with open(file_path, "r") as log_file:
        for log_line in log_file:
            # Check if the log line is an INFO log
            if "INFO" in log_line:
                match = re.search(info_pattern, log_line)
                if match:
                    username = match.group(2).strip()
                    # Update INFO count for the user
                    if username in user_statistics:
                        user_statistics[username]["INFO"] += 1
                    else:
                        user_statistics[username] = {"INFO": 1, "ERROR": 0}
            # Check if the log line is an ERROR log
            elif "ERROR" in log_line:
                match = re.search(error_pattern, log_line)
                if match:
                    username = match.group(2).strip()
                    # Update ERROR count for the user
                    if username in user_statistics:
                        user_statistics[username]["ERROR"] += 1
                    else:
                        user_statistics[username] = {"INFO": 0, "ERROR": 1}

    # Return user statistics
    return user_statistics

def write_to_csv(data, file_name):
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for item in data:
            writer.writerow(item)

# Example usage
if __name__ == "__main__":
    file_path = "syslog.log"
    error_count = analyze_syslog(file_path)
    user_statistics = analyze_user_statistics(file_path)
    
    # Write error count to CSV
    error_data = [["Error", "Count"]]
    for error, count in error_count.items():
        error_data.append([error, count])
    write_to_csv(error_data, "error_message.csv")
    
    # Write user statistics to CSV
    user_data = [["User", "INFO Count", "ERROR Count"]]
    for user, counts in user_statistics.items():
        user_data.append([user, counts['INFO'], counts['ERROR']])
    write_to_csv(user_data, "user_statistics.csv")