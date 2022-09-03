from stack import Stack
from queue import Queue

print("Stack")
my_stack = Stack(5)
my_stack.push(6)
my_stack.push(7)
my_stack.pop()
my_stack.print_stack()

print("Queue")
my_queue = Queue(6)
my_queue.enqueue(7)
my_queue.enqueue(8)
my_queue.dequeue()
my_queue.print_queue()
