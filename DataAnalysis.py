import csv
from datetime import datetime, timedelta

def analyze_employee_data(file_path):
    # Assumption: The CSV file has columns like 'EmployeeName', 'Timestamp', 'Timecard Hours (as Time)', etc.

    # Define constants for time durations
    CONSECUTIVE_DAYS_THRESHOLD = 7
    MIN_SHIFT_BREAK = timedelta(hours=1)
    MAX_SHIFT_DURATION = timedelta(hours=14)
    MIN_SHIFT_DURATION = timedelta(hours=1)

    # Store employee data in a dictionary
    employee_data = {}

    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            # Skip empty rows
            if not row['Employee Name']:
                continue

            employee_name = row['Employee Name']
            timestamp = datetime.strptime(row['Time'], '%m/%d/%Y %I:%M %p')
            hours_worked_str = row['Timecard Hours (as Time)']
            
            # Skip rows with empty timecard hours
            if not hours_worked_str:
                continue

            # Convert timecard hours to timedelta
            hours, minutes = map(int, hours_worked_str.split(':'))
            hours_worked = timedelta(hours=hours, minutes=minutes)

            if employee_name not in employee_data:
                employee_data[employee_name] = {'shifts': []}

            # Append shift details
            employee_data[employee_name]['shifts'].append({'timestamp': timestamp, 'hours_worked': hours_worked})

    # Analyze data
    for employee_name, data in employee_data.items():
        shifts = sorted(data['shifts'], key=lambda x: x['timestamp'])

        # Check for 7 consecutive days of work
        for i in range(len(shifts) - CONSECUTIVE_DAYS_THRESHOLD + 1):
            consecutive_days = [shifts[i + j]['timestamp'].date() for j in range(CONSECUTIVE_DAYS_THRESHOLD)]

            if consecutive_days == [(shifts[i]['timestamp'] + timedelta(days=j)).date() for j in range(CONSECUTIVE_DAYS_THRESHOLD)]:
                print(f"{employee_name} worked for 7 consecutive days starting from {shifts[i]['timestamp'].date()}")

        # Check for less than 10 hours between shifts but greater than 1 hour
        for i in range(len(shifts) - 1):
            time_between_shifts = shifts[i + 1]['timestamp'] - (shifts[i]['timestamp'] + shifts[i]['hours_worked'])

            if MIN_SHIFT_BREAK < time_between_shifts < MAX_SHIFT_DURATION:
                print(f"{employee_name} has less than 10 hours between shifts but greater than 1 hour")

        # Check for more than 14 hours in a single shift
        for shift in shifts:
            if shift['hours_worked'] > MAX_SHIFT_DURATION:
                print(f"{employee_name} worked for more than 14 hours in a single shift on {shift['timestamp'].date()}")

if __name__ == "__main__":
    file_path = "/Assignment_Timecard.xlsx - Sheet1.csv"  # Replace with the actual path to your dataset
    analyze_employee_data(file_path)
