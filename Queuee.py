from collections import deque
import time
import threading


class Queue:

    def __init__(self):
        self.queue = deque()

    def enqueue(self, val):
        self.queue.appendleft(val)

    def dequeue(self):
        if self.queue:
            return self.queue.pop()
        else:
            return

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def front(self):
        return self.queue[-1]

    def __str__(self):
        return f'{self.queue}'
