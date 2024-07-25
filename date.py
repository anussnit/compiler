from datetime import datetime

# Get the current date
current_date = datetime.now()

# Print the current date in various formats
print("Original Date:", current_date.strftime('%Y-%m-%d'))  # 2024-07-24
print("Month/Day/Year:", current_date.strftime('%m/%d/%Y'))  # 07/24/2024
print("Day-Month-Year:", current_date.strftime('%d-%m-%Y'))  # 24-07-2024
print("Full Month Name Day, Year:", current_date.strftime('%B %d, %Y'))  # July 24, 2024
print("Day Month Year:", current_date.strftime('%d %B %Y'))  # 24 July 2024
print("Weekday, Month Day, Year:", current_date.strftime('%A, %B %d, %Y'))  # Wednesday, July 24, 2024

