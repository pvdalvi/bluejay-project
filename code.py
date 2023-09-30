def check_consecutive_days(start_dates):
    for i in range(len(start_dates) - 6):
        if all((start_dates[i + j + 1] - start_dates[i + j] == timedelta(days=1)) for j in range(6)):
            return True
    return False

def check_time_between_shifts(shifts):
    for i in range(len(shifts) - 1):
        time_diff = shifts[i + 1] - shifts[i]
        if timedelta(hours=1) < time_diff < timedelta(hours=10):
            return True
    return False

def check_single_shift_duration(shifts):
    for shift in shifts:
        if shift > timedelta(hours=14):
            return True
    return False

def parse_datetime(datetime_str):
    return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')

def print_employees(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row if present
        for row in reader:
            name = row[0]
            positions = row[1:]
            start_dates = [parse_datetime(date_str) for date_str in positions[::2]]
            shifts = [parse_datetime(date_str) for date_str in positions[1::2]]
            
            if check_consecutive_days(start_dates):
                print(f"Employee {name} has worked for 7 consecutive days.")
            
            if check_time_between_shifts(shifts):
                print(f"Employee {name} has less than 10 hours of time between shifts but greater than 1 hour.")
            
            if check_single_shift_duration(shifts):
                print(f"Employee {name} has worked for more than 14 hours in a single shift.")

# Example usage
file_path = 'employee_records.csv'
print_employees(file_path)