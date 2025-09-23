SIZE = 5
queue = []
   
def enqueue(item):
    if len(queue) == SIZE:
        print("Queue is FULL!")
    else:
        queue.append(item)
        print(f"Inserted {item}")

def dequeue():
    if not queue:
        print("Queue is EMPTY!")
    else:
        print(f"Deleted {queue.pop(0)}")

def display():
    if not queue:
        print("Queue is EMPTY!")
    else:
        print("Queue elements:", queue)


while True:
    print("\n1. Enqueue  2. Dequeue  3. Display  4. Exit")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        val = int(input("Enter value: "))
        enqueue(val)
    elif ch == 2:
        dequeue()
    elif ch == 3:
        display()
    elif ch == 4:
        break
    else:
        print("Invalid choice!")
