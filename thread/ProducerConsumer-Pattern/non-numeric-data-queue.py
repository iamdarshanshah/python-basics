import queue

q = queue.PriorityQueue()

q.put((100, "John"))
q.put((200, "Joe"))
q.put((300, "Josh"))
q.put((400, "Jerin"))
q.put((50, "Ja"))

while not q.empty():
    # print(q.get(), end=" | ")
    print(q.get()[1], end=" | ")