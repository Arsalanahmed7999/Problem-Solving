# Iterate through the grades dictionary and print each subject along with its grade.

# Create a dictionary where the keys are months (e.g., "January", "February") and the values are the number of days in each month. Iterate through the dictionary and print the months with 31 days.

months = {
    "January": 31,
    "Febuary": 28,
    "March" : 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July" : 31,
    "August": 31,
    "September":30,
    "October":31,
    "November":30,
    "December":31
}

for month, value in months.items():
    if(value == 31):
        print(month)
        