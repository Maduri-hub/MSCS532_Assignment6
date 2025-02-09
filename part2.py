import array

print("Array:")
# Creating an array of integers
arr = array.array('i', [1, 2, 3, 4, 5])
print(arr)
# Insertion
arr.insert(2, 10)  # Insert 10 at index 2
print(arr)
# Deletion
arr.remove(3)  # Remove the first occurrence of 3
print(arr)
# Access
element = arr[1]  # Access element at index 1
print(element)

print("\nMatrix")
# Creating a 3x3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)
# Accessing an element
element = matrix[1][2]  # Access element at row 1, column 2 (0-indexed)
print(element)

print("\nStack:")
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError("Pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        raise IndexError("Peek from an empty stack")

    def is_empty(self):
        return len(self.stack) == 0
stack = Stack()

# Create/Push items to the stack
stack.push(10)  # Stack: [10]
top_element = stack.peek()
print("Top element:", top_element)
stack.push(20)  # Stack: [10, 20]
top_element = stack.peek()
print("Top element:", top_element)
stack.push(30)  # Stack: [10, 20, 30]
# Read/Peek the top element
top_element = stack.peek()
print("Top element:", top_element)  # Output: Top element: 30
# Delete an element (pop)
stack.pop()  # Stack after pop: [10]
top_element = stack.peek()
print("Top element:", top_element)
stack.pop()  # Stack after pop: []
top_element = stack.peek()
print("Top element:", top_element)

from collections import deque
print("\nQueue:")
class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        raise IndexError("Dequeue from an empty queue")

    def is_empty(self):
        return len(self.queue) == 0
queue = Queue()

# Create/Enqueue items to the queue
queue.enqueue(10)  # Queue: [10]
print("Queue after enqueueing 10:", list(queue.queue))

queue.enqueue(20)  # Queue: [10, 20]
print("Queue after enqueueing 20:", list(queue.queue))

queue.enqueue(30)  # Queue: [10, 20, 30]
print("Queue after enqueueing 30:", list(queue.queue))
# Read/Peek the front element (accessing the first element)
if not queue.is_empty():
    front_element = queue.queue[0]
    print("Front element:", front_element)  # Output: Front element: 10
# Delete an element (dequeue)
queue.dequeue()  # Queue after dequeue: [30]
print("Queue after dequeueing again:", list(queue.queue))  # Output: Queue after dequeueing again: [30]

queue.dequeue()  # Queue after dequeue: []
print("Queue after dequeueing all elements:", list(queue.queue))  # Output: Queue after dequeueing all elements: []

print("\nLinked List:")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        current = self.head
        previous = None
        while current and current.data != key:
            previous = current
            current = current.next
        if current is None:
            return  # Key not found
        if previous is None:
            self.head = current.next  # Deleting the head node
        else:
            previous.next = current.next

    def traverse(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
linked_list = SinglyLinkedList()

# Create/Insert elements at the beginning of the list
linked_list.insert_at_beginning(10)  # Linked List: [10]
print("Linked List after inserting 10:")
linked_list.traverse()

linked_list.insert_at_beginning(20)  # Linked List: [20, 10]
print("Linked List after inserting 20:")
linked_list.traverse()

linked_list.insert_at_beginning(30)  # Linked List: [30, 20, 10]
print("Linked List after inserting 30:")
linked_list.traverse()
# Read/Traverse the list
print("Traversing the list:")
linked_list.traverse()  # Output: 30, 20, 10
# Update/Delete a node by key (delete an element)
linked_list.delete(20)  # Linked List: [30, 10]
print("Linked List after deleting 20:")
linked_list.traverse()

linked_list.delete(10)  # Linked List: [30]
print("Linked List after deleting 10:")
linked_list.traverse()
# Delete an element (delete a node)
linked_list.delete(30)  # Linked List: []
print("Linked List after deleting 30:")
linked_list.traverse()  # Output: (empty list)
