class VerboseList(list):
    def append(self, element):
        super().append(element)
        print(f"Added [{element}] to the list.")

    def extend(self, list1):
        super().extend(list1)
        n_of_el = len(list1)
        print(f“Extended the list with [{n_of_el}] items.” where [] is the number of items added)

    def remove(self, element):
        super().remove(element)
        print(f“Removed [{element}] from the list.”)
    
    def pop(self, index=-1):
        super().pop(index)
        print(f"If the index is not specified, default behavior is to pop the last item.)"
