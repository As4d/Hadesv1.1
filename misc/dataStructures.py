class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def size(self):
        return len(self.stack)

    def isEmpty(self):
        return self.stack == []


class Queue:
    def __init__(self):
        self.queue = []

    def getLenQueue(self):
        return len(self.queue)

    def isEmpty(self):
        return True if len(self.stack) == 0 else False

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)
