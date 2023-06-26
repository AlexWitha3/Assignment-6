from datetime import datetime, timedelta

# Add 1 day
dt = datetime.now()
new_dt = dt + timedelta(days=1)
print("After adding 1 day:", new_dt)

# Subtract 60 seconds
new_dt = dt - timedelta(seconds=60)
print("After subtracting 60 seconds:", new_dt)

# Add 2 years
new_dt = dt.replace(year=dt.year + 2)
print("After adding 2 years:", new_dt)
