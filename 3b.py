class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, book_title):
        new_node = Node(book_title)
        new_node.next = self.top
        self.top = new_node
        print(f'Pushed: "{book_title}"')

    def pop(self):
        if self.top is None:
            print("Stack is empty. No book to pop.")
            return None
        popped_book = self.top.data
        self.top = self.top.next
        print(f'Popped: "{popped_book}"')
        return popped_book

    def display(self):
        current = self.top
        if current is None:
            print("Stack is empty.")
            return
        print("Stack contents:")
        while current:
            print(f' - {current.data}')
            current = current.next

# Main program to interact with the user
library_stack = Stack()

while True:
    print("\nChoose operation:")
    print("1. Push a book title")
    print("2. Pop a book title")
    print("3. Display stack")
    print("4. Exit")
    choice = input("Enter choice (1-4): ")

    if choice == '1':
        book = input("Enter book title to push: ")
        library_stack.push(book)

    elif choice == '2':
        library_stack.pop()

    elif choice == '3':
        library_stack.display()

    elif choice == '4':
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3 or 4.")
