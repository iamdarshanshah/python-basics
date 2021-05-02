import queue

q = queue.Queue()

q.put(100)
q.put(200)
q.put(300)
q.put(400)
q.put(50)

while not q.empty():
    print(q.get(), end=" | ")

print()

q = queue.LifoQueue()

q.put(100)
q.put(200)
q.put(300)
q.put(400)
q.put(50)

while not q.empty():
    print(q.get(), end=" | ")

print()

q = queue.PriorityQueue()

q.put(100)
q.put(200)
q.put(300)
q.put(400)
q.put(50)

while not q.empty():
    print(q.get(), end=" | ")