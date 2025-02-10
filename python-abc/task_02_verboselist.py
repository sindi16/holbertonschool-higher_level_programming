#!/usr/bin/env python3

class VerboseList(list):
    """
    A custom list class that prints a notification message every time an item
    is added (using the append or extend methods) or removed (using the remove
    or pop methods)."""

    def append(self, item):
        """Appends an item to the list and prints a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extends the list with the items from the iterable and prints
        a notification."""
        num_items = len(list(iterable))
        super().extend(iterable)
        print(f"Extended the list with [{num_items}] items.")

    def remove(self, item):
        """Removes an item from the list and prints a notification."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pops an item from the list and prints a notification."""
        if index == -1:
            item = super().pop()
        else:
            item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item


if __name__ == '__main__':
    vl = VerboseList([1, 2, 3])
    vl.append(4)
    vl.extend([5, 6])
    vl.remove(2)
    vl.pop()
    vl.pop(0)