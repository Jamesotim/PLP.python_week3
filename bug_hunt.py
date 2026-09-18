count = 1
total = 0

# BUG: Added a colon after the while condition because Python requires it.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Changed < to <= so that the loop includes the number 5.
# BUG: Used a comma instead of + because total is an integer.
print("Sum of 1 to 5 is:", total)
