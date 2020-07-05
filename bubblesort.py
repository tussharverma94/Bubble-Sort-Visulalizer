import time


def bubble_sort(data, drawData, timetick):
    for _ in range(len(data) - 1):
        for j in range(len(data) - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                drawData(data, ['green' if x == j or x == j+1 else 'red' for x in range(len(data))])
                time.sleep(timetick)
    drawData(data, ['green' for x in range(len(data))])

"""
data = [1,2,3,1,1,4,56,2]
answer = bubble_sort(data)
print(answer)
"""
