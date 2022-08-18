from collections import deque

seats = input().split(", ")
numbers1 = input().split(", ")
numbers2 = input().split(", ")

numbers1 = deque([int(e) for e in numbers1])
numbers2 = deque([int(e) for e in numbers2])

seatsMatched = []
rotations = 0

while len(numbers2) > 0:
    if rotations == 10 or len(seatsMatched) == 3:
        break

    seatFound = False
    e1 = numbers1.popleft()
    e2 = numbers2.pop()
    ch = chr(e1 + e2)
    
    for k in range(0, len(seats)):
        if str(e1) + ch == seats[k] or str(e2) + ch == seats[k]:
            if not seats[k] in seatsMatched:
                seatsMatched.append(seats[k])
            seatFound = True
            break
    
    if seatFound == False:
        numbers1.append(e1)
        numbers2.appendleft(e2)

    rotations += 1



print(f"Seat matches: {', '.join(seatsMatched)}\nRotations count: {rotations}")

"""
17K, 20B, 3C, 15D, 31Z, 28F
20, 35, 15, 3, 2, 10
1, 15, 64, 53, 45, 46
"""

"""
25A, 16B, 44T, 49D, 27M, 44F
25, 3, 31, 49, 26, 13
10, 15, 44, 40
"""

"""
15C, 25C, 36C, 43P, 40E, 38G
15, 25, 80, 40, 15, 99, 52
15, 42, 29
"""