class Student:
    def __init__(self, enrollment_id, name, course):
        self.enrollment_id = enrollment_id
        self.name = name
        self.course = course

    def __str__(self):
        return f"ID: {self.enrollment_id}, Name: {self.name}, Course: {self.course}"

class AVLNode:
    def __init__(self, student):
        self.student = student
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root, student):
        if not root:
            return AVLNode(student)

        if student.enrollment_id < root.student.enrollment_id:
            root.left = self.insert(root.left, student)
        elif student.enrollment_id > root.student.enrollment_id:
            root.right = self.insert(root.right, student)
        else:
            print(f"❌ Duplicate Enrollment ID {student.enrollment_id} not allowed.")
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        # Balance the tree
        if balance > 1 and student.enrollment_id < root.left.student.enrollment_id:
            return self.right_rotate(root)

        if balance < -1 and student.enrollment_id > root.right.student.enrollment_id:
            return self.left_rotate(root)

        if balance > 1 and student.enrollment_id > root.left.student.enrollment_id:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and student.enrollment_id < root.right.student.enrollment_id:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def search_by_id(self, root, enrollment_id):
        if not root:
            return None
        if enrollment_id == root.student.enrollment_id:
            return root.student
        elif enrollment_id < root.student.enrollment_id:
            return self.search_by_id(root.left, enrollment_id)
        else:
            return self.search_by_id(root.right, enrollment_id)

    def search_by_name(self, root, name):
        result = []
        self._search_by_name_helper(root, name.lower(), result)
        return result

    def _search_by_name_helper(self, node, name, result):
        if not node:
            return
        if node.student.name.lower() == name:
            result.append(node.student)
        self._search_by_name_helper(node.left, name, result)
        self._search_by_name_helper(node.right, name, result)

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.student)
            self.inorder(root.right)



def main():
    avl = AVLTree()
    root = None

    while True:
        print("\n--- Student Enrollment Menu ---")
        print("1. Add new student")
        print("2. Search by Enrollment ID")
        print("3. Search by Name")
        print("4. Display all students (in-order)")
        print("5. Exit")
        choice = input("Enter choice (1-5): ")

        if choice == '1':
            try:
                eid = int(input("Enter Enrollment ID: "))
                name = input("Enter Student Name: ").strip()
                course = input("Enter Course Name: ").strip()
                student = Student(eid, name, course)
                root = avl.insert(root, student)
                print("✅ Student added successfully.")
            except ValueError:
                print("❌ Invalid input. Enrollment ID must be an integer.")
        elif choice == '2':
            try:
                eid = int(input("Enter Enrollment ID to search: "))
                student = avl.search_by_id(root, eid)
                if student:
                    print("✅ Student Found:\n", student)
                else:
                    print("❌ Student not found.")
            except ValueError:
                print("❌ Invalid input. Enrollment ID must be an integer.")
        elif choice == '3':
            name = input("Enter name to search: ").strip()
            results = avl.search_by_name(root, name)
            if results:
                print("✅ Students Found:")
                for s in results:
                    print(s)
            else:
                print("❌ No student found with that name.")
        elif choice == '4':
            print("\n📘 List of Enrolled Students (sorted by ID):")
            avl.inorder(root)
        elif choice == '5':
            print("👋 Exiting program.")
            break
        else:
            print("❌ Invalid choice. Please select from 1 to 5.")

if __name__ == "__main__":
    main()
