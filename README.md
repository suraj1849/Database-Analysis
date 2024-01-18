
# 🕒 Employee Timecard Analyzer 🕵️‍♂️

This program analyzes employee timecard data to identify specific patterns and conditions related to employee shifts. It performs the following analyses:

1. Identifies employees who have worked for 7 consecutive days.
2. Identifies employees who have less than 10 hours of time between shifts but greater than 1 hour.
3. Identifies employees who have worked for more than 14 hours in a single shift.

## Requirements

- Python 3.x 🐍
- Libraries: `csv`, `datetime`, `timedelta`

## Usage

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/employee-timecard-analyzer.git
    ```

2. Navigate to the project directory:

    ```bash
    cd employee-timecard-analyzer
    ```

3. Execute the program with your timecard data file:

    ```bash
    python employee_analyzer.py /path/to/your/timecard.csv
    ```

4. The program will analyze the data and print the results to the console.

## Input Data Format

Assumes that the input CSV file has the following columns:

- 'Employee Name': Name of the employee
- 'Time': Timestamp of the shift in the format '%m/%d/%Y %I:%M %p'
- 'Timecard Hours (as Time)': Hours worked in the format 'HH:MM'

## Output

The program will output information about employees meeting the specified conditions to the console.

## Example

```bash
python employee_analyzer.py /path/to/your/timecard.csv
```

## Contact

For any issues or questions, please contact [surajpatil110110@gmail.com] 📧.
