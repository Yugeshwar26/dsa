from datetime import datetime

class LogEntry:
    def __init__(self, visitor_name, entry_time, purpose=""):
        self.visitor_name = visitor_name
        self.entry_time = entry_time 
        self.purpose = purpose

    def __str__(self):
        return f"{self.entry_time.strftime('%Y-%m-%d %H:%M:%S')} - {self.visitor_name} - {self.purpose}"


class BSTNode:
    def __init__(self, entry):
        self.entry = entry
        self.left = None
        self.right = None


class LogBookBST:
    def __init__(self, sort_by='entry_time'):
        # sort_by can be 'entry_time' or 'visitor_name'
        self.root = None
        self.sort_by = sort_by

    def _compare(self, entry1, entry2):
        key1 = getattr(entry1, self.sort_by)
        key2 = getattr(entry2, self.sort_by)
        return (key1 > key2) - (key1 < key2)

    def insert(self, entry):
        def _insert(node, entry):
            if node is None:
                return BSTNode(entry)
            cmp = self._compare(entry, node.entry)
            if cmp < 0:
                node.left = _insert(node.left, entry)
            else:
                node.right = _insert(node.right, entry)
            return node

        self.root = _insert(self.root, entry)

    def search(self, key):
        def _search(node, key):
            if node is None:
                return None
            node_key = getattr(node.entry, self.sort_by)
            if key == node_key:
                return node.entry
            elif key < node_key:
                return _search(node.left, key)
            else:
                return _search(node.right, key)

        return _search(self.root, key)

    def delete(self, key):
        def _min_value_node(node):
            current = node
            while current.left:
                current = current.left
            return current

        def _delete(node, key):
            if not node:
                return None
            node_key = getattr(node.entry, self.sort_by)

            if key < node_key:
                node.left = _delete(node.left, key)
            elif key > node_key:
                node.right = _delete(node.right, key)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                temp = _min_value_node(node.right)
                node.entry = temp.entry
                node.right = _delete(node.right, getattr(temp.entry, self.sort_by))
            return node

        self.root = _delete(self.root, key)

    def traverse(self):
        def _inorder(node):
            if node:
                yield from _inorder(node.left)
                yield node.entry
                yield from _inorder(node.right)

        return list(_inorder(self.root))

    def count(self):
        def _count(node):
            if not node:
                return 0
            return 1 + _count(node.left) + _count(node.right)
        return _count(self.root)
def main():
    print("Welcome to Log Book System")
    sort_by = input("Sort log by 'entry_time' or 'visitor_name': ").strip()

    if sort_by not in ['entry_time', 'visitor_name']:
        print("Invalid sort key. Defaulting to 'entry_time'.")
        sort_by = 'entry_time'

    logbook = LogBookBST(sort_by=sort_by)

    def get_datetime_input(prompt):
        while True:
            try:
                time_str = input(prompt + " (format YYYY-MM-DD HH:MM): ")
                return datetime.strptime(time_str, "%Y-%m-%d %H:%M")
            except ValueError:
                print("Invalid format. Please try again.")

    while True:
        print("\n===== Log Book Menu =====")
        print("1. Insert a log entry")
        print("2. Delete a log entry")
        print("3. Search for a log entry")
        print("4. Display all entries")
        print("5. Count total entries")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            name = input("Visitor name: ").strip()
            entry_time = get_datetime_input("Entry time")
            purpose = input("Purpose of visit: ").strip()
            logbook.insert(LogEntry(name, entry_time, purpose))
            print("Log entry inserted.")

        elif choice == '2':
            if sort_by == 'entry_time':
                key = get_datetime_input("Enter entry time to delete")
            else:
                key = input("Enter visitor name to delete: ").strip()
            logbook.delete(key)
            print("Entry deleted (if existed).")

        elif choice == '3':
            if sort_by == 'entry_time':
                key = get_datetime_input("Enter entry time to search")
            else:
                key = input("Enter visitor name to search: ").strip()
            result = logbook.search(key)
            if result:
                print("Entry found:")
                print(result)
            else:
                print("Entry not found.")

        elif choice == '4':
            print("\n--- All Log Entries ---")
            for entry in logbook.traverse():
                print(entry)

        elif choice == '5':
            print(f"Total entries: {logbook.count()}")

        elif choice == '6':
            print("Exiting log book system.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
