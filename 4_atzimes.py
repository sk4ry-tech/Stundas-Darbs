atzimes = [8, 6, 9, 7, 5, 10, 4]
print("Atzīmju skaits:", len(atzimes))
print("Vidējā atzīme:", sum(atzimes) / len(atzimes))
print("Lielākā atzīme:", max(atzimes))
skaits = 0
for a in atzimes:
    if a >= 7:
        skaits = skaits + 1
print("Atzīmes kas ir 7 vai lielākas:", skaits)
