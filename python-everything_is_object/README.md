Understanding Python’s Objects: Mutable vs Immutable, IDs, and Function Behavior

In this post, I’ll walk through what I’ve learned while exploring Python’s object model: the difference between mutable and immutable objects, how Python uses IDs and types, and why this matters when passing objects to functions. Understanding these concepts helped me write clearer, bug-resistant code — and I hope it helps you too!

📌 id and type
In Python, every object has an id and a type. The id() function returns a unique identifier for an object (its memory address), and type() shows its class.
Example:

python
Copy
Edit
a = 42
print(id(a))         # e.g., 140705977994320
print(type(a))       # <class 'int'>

b = "Hello"
print(id(b))         # e.g., 140705983175600
print(type(b))       # <class 'str'>
IDs matter when we talk about whether two variables refer to the same object or to equal but different objects.

✏️ Mutable objects
Mutable objects can be changed in place. Lists, dictionaries, and sets are classic examples:

python
Copy
Edit
my_list = [1, 2, 3]
print(id(my_list))  # e.g., 140705983217664

my_list.append(4)
print(my_list)      # [1, 2, 3, 4]
print(id(my_list))  # same id as before!
Notice how after adding an element, the list’s ID stays the same — it’s the same object, just updated.

🔒 Immutable objects
Immutable objects cannot be changed after creation. Integers, floats, strings, and tuples are immutable:

python
Copy
Edit
x = 10
print(id(x))       # e.g., 140705977994320

x += 1             # creates a new object
print(x)           # 11
print(id(x))       # different id!
Here, x += 1 doesn’t change the original object — instead, it creates a new integer 11 and reassigns x.

🤔 Why does it matter?
Python treats mutable and immutable objects differently, which affects your code in subtle ways.
With mutable objects, you can accidentally modify them:

python
Copy
Edit
a = [1, 2, 3]
b = a
b.append(4)

print(a)  # [1, 2, 3, 4] -- a changed too!
Both a and b point to the same list.

Immutable objects prevent this kind of side effect:

python
Copy
Edit
a = "hello"
b = a
b += " world"

print(a)  # "hello"
print(b)  # "hello world"
b becomes a new string — a stays unchanged.

🧪 Arguments and functions
In Python, arguments are passed by assignment: functions receive references to objects.
If the object is mutable, the function can change it:

python
Copy
Edit
def add_item(lst):
    lst.append(99)

items = [1, 2, 3]
add_item(items)
print(items)  # [1, 2, 3, 99]
If the object is immutable, the function cannot change it outside:

python
Copy
Edit
def increment(n):
    n += 1
    print("Inside:", n)

num = 5
increment(num)       # Inside: 6
print("Outside:", num)  # Outside: 5
n += 1 creates a new integer, leaving num unchanged.

🚀 Advanced learnings
While diving deeper, I also learned about:

Shallow vs deep copies: copy() copies references inside lists/dicts; deepcopy() duplicates all nested objects.

Custom immutable classes: using @property and no setters to create classes whose instances can't change.

python
Copy
Edit
class ImmutablePoint:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
Immutable objects make your code easier to reason about.

✅ Conclusion
Understanding id, type, mutability, and argument passing helps avoid bugs, makes your code cleaner, and clarifies what’s really happening in Python.
I encourage you to experiment: print IDs, modify objects inside functions, and observe what changes!

📢 I published this post on Medium & shared it on LinkedIn!
📝 Blog post: [<Paste your Medium URL here>]

🔗 LinkedIn post: [<Paste your LinkedIn post URL here>]

If you liked it, please leave a comment or share your own experiences with Python mutability! 🚀

If you'd like, I can also help you:
✅ Format it perfectly for Medium / LinkedIn,
✅ Create a cover image,
✅ Even suggest hashtags for sharing!