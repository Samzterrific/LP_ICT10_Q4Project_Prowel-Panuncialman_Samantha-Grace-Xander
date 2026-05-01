import numpy as np, matplotlib.pyplot as plt
from pyscript import document, window

x = np.arange(0, 5)
mo = 0
tu = 0
we = 0
th = 0
fr = 0
positions = [0, 1, 2, 3, 4]
labels = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

def plot():
    plt.clf()
    global mo, tu, we, th, fr
    day = document.getElementById("day").value
    n = int(document.getElementById("num").value)
    if day == 'monday':
        mo = n
    elif day == 'tuesday':
        tu = n
    elif day == 'wednesday':
        we = n
    elif day == 'thursday':
        th = n
    elif day == 'friday':
        fr = n
    y = np.array([mo,tu,we,th,fr])
    plt.plot(x, y, color = 'red')
    plt.plot(y, marker = 'o', color = 'red')
    plt.title("Weekly Attendance (Absences)")
    plt.xlabel('Day')
    plt.xticks(positions, labels)
    plt.ylabel('Number of Absences')
    plt.savefig('plot.png')
    plt.show()
    print("clicked")

window.plot = plot