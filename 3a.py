class BookStack:
    def __init__(self, max_size=100):
        self.stack = []
        self.max_size = max_size

    def push(self, book_title):
        if len(self.stack) >= self.max_size:
            print("Stack Overflow! Cannot add more books.")
        else:
            self.stack.append(book_title)
            print(f'Book "{book_title}" added to the stack.')

    def pop(self):
        if len(self.stack) == 0:
            print("Stack Underflow! No books to retrieve.")
            return None
        else:
            book_title = self.stack.pop()
            print(f'Book "{book_title}" retrieved from the stack.')
            return book_title

    def display(self):
        if len(self.stack) == 0:
            print("Stack is empty.")
        else:
            print("Books in the stack (top to bottom):")
            for book in reversed(self.stack):
                print(f"- {book}")

def main():
    max_size = int(input("Enter maximum stack size: "))
    library_stack = BookStack(max_size)

    while True:
        print("\nChoose operation:")
        print("1. Add a book (push)")
        print("2. Retrieve a book (pop)")
        print("3. Display all books")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == '1':
            book_title = input("Enter book title to add: ")
            library_stack.push(book_title)
        elif choice == '2':
            library_stack.pop()
        elif choice == '3':
            library_stack.display()
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1-4.")

if __name__ == "__main__":
    main()
