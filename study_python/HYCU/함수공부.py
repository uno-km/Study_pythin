a=['mon','tue','web','thu','fri','sat','sun']
for week in a:
    idx = a.index(week)
    a[idx] = a[idx].capitalize()
print(a)