day="monday"
tem=30
raining=True

if day=="monday" and tem>27 and not raining:
    print("no rain ")
else:
    print("since false value ")


if (day=="monday" and tem>27) or not raining:
    print("no rain ")
else:
    print("since false value ")