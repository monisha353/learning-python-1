
## **Input/Output, String Manipulation, and Comments**

### **1. Input and Output in Python**

#### **1.1 Input from the User:**
name = input("Enter your name: ")
age = int(input("Enter your age: "))  # Convert input to integer


#### **1.2 Output to the Console:**
print("Hello, " + name + "! You are " + str(age) + " years old.")


#also use **f-strings** (formatted string literals) for more readable code:
print(f"Hello, {name}! You are {age} years old.")

### **2. String Manipulation**
#### **2.1 Common String Operations:**
#**Concatenation**: Joining two or more strings together using the `+` operator.
 
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # Output: "John Doe"
  

#**Repetition**: Repeating a string multiple times using the `*` operator.
  
greeting = "Hello! " * 3
print(greeting)  # Output: "Hello! Hello! Hello! "


#### **2.2 String Methods:**
message = "  Hello, World!  "
print(message.strip())  # Output: "Hello, World!"
print(message.upper())  # Output: "HELLO, WORLD!"
print(message.replace("World", "Python"))  # Output: "Hello, Python!"
#### **2.3 Accessing String Characters:**
text = "Python"
print(text[0])  # Output: P
print(text[2])  # Output: t
print(text[-1])  # Output: n
print(text[-3])  # Output: h


#### **2.4 Slicing Strings:**
text = "Python Programming"
print(text[0:6])  # Output: Python (extracts from index 0 to 5)
print(text[:6])  # Output: Python (same as above)
print(text[7:])  # Output: Programming (from index 7 to the end)
### **3. Comments in Python**

  # This is a single-line comment
print("Hello, World!")


# **Multi-line comments** can be written using triple quotes (`"""` or `'''`). These are often used to write detailed explanations or temporarily block sections of code:
print("Hello, Python!")

### **4. Escape Sequences**
#### **Example:**

print("Hello\nWorld")  # Output: 
# Hello
# World

print("Hello\tPython")  # Output: Hello    Python


## **Operators in Python**
#### **Examples**:

x = 5  # Assigns 5 to x
x += 3  # Equivalent to x = x + 3, now x is 8
x -= 2  # Equivalent to x = x - 2, now x is 6
x *= 4  # Equivalent to x = x * 4, now x is 24
x /= 6  # Equivalent to x = x / 6, now x is 4.0

#### **Examples**:
a = 10
b = 20

print(a == b)  # Output: False
print(a != b)  # Output: True
print(a > b)  # Output: False
print(a < b)  # Output: True
print(a >= 10)  # Output: True
print(b <= 25)  # Output: True

#### **Examples**:
x = 5
y = 10
z = 15

# and operator
print(x > 0 and y > 5)  # Output: True (both conditions are True)

# or operator
print(x > 10 or z > 10)  # Output: True (one of the conditions is True)

# not operator
print(not(x > 10))  # Output: True (reverses False to True)

#### **Examples**:
my_list = [1, 2, 3, 4, 5]
my_string = "Python"

print(3 in my_list)  # Output: True (3 is in the list)
print(6 not in my_list)  # Output: True (6 is not in the list)
print("P" in my_string)  # Output: True ("P" is in the string)
print("z" not in my_string)  # Output: True ("z" is not in the string)

### **5. Bitwise Operators**
#### **Examples**:
a = 5  # In binary: 101
b = 3  # In binary: 011

# Bitwise AND
print(a & b)  # Output: 1 (binary: 001)

# Bitwise OR
print(a | b)  # Output: 7 (binary: 111)

# Bitwise XOR
print(a ^ b)  # Output: 6 (binary: 110)

# Bitwise NOT
print(~a)  # Output: -6 (inverts all bits)

# Left shift
print(a << 1)  # Output: 10 (binary: 1010)

# Right shift
print(a >> 1)  # Output: 2 (binary: 010)

### **6. Arithmetic Operators** 
### **Examples:**
a = 10
b = 3
print(a + b)  # Output: 13
print(a - b)  # Output: 7
print(a * b)  # Output: 30
print(a / b)  # Output: 3.3333...
print(a // b)  # Output: 3 (Floor Division)
print(a % b)  # Output: 1 (Modulus)
print(a ** b)  # Output: 1000 (Exponentiation)


## **Lists in Python**

### **1. What is a List?**
### **Example**:

fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["apple", 3, True]


### **2. Accessing List Elements**
#### **Example**:
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple
print(fruits[2])  # Output: cherry


#You can also use **negative indexing** to access elements from the end of the list:

print(fruits[-1])  # Output: cherry
print(fruits[-2])  # Output: banana

### **3. Modifying Lists**
#### **Changing a specific element**:

fruits[1] = "orange"
print(fruits)  # Output: ['apple', 'orange', 'cherry']

#### **Adding elements**:
#append()`: Adds an element to the **end** of the list.

fruits.append("grape")
print(fruits)  # Output: ['apple', 'orange', 'cherry', 'grape']
  

#insert()`: Inserts an element at a **specific index**.
  
fruits.insert(1, "kiwi")
print(fruits)  # Output: ['apple', 'kiwi', 'orange', 'cherry']

#### **Removing elements**:
#remove()`: Removes the first occurrence of an element.
  
fruits.remove("orange")
print(fruits)  # Output: ['apple', 'kiwi', 'cherry']
  

#pop()`: Removes the element at a specific index (or the last item if no index is provided).

fruits.pop()  # Removes the last item
print(fruits)  # Output: ['apple', 'kiwi']
  
fruits.pop(0)  # Removes the first item
print(fruits)  # Output: ['kiwi']


 #clear()`: Removes all elements from the list.

fruits.clear()
print(fruits)  # Output: []
 
### **4. Slicing Lists**
#### **Examples**:
numbers = [0, 1, 2, 3, 4, 5, 6]
print(numbers[1:4])  # Output: [1, 2, 3] (from index 1 to 3)
print(numbers[:4])  # Output: [0, 1, 2, 3] (from start to index 3)
print(numbers[2:])  # Output: [2, 3, 4, 5, 6] (from index 2 to end)
print(numbers[::2])  # Output: [0, 2, 4, 6] (every 2nd element)

### **5. List Functions and Methods**
#### **5.1 Common Functions**:
#`len(list)`: Returns the number of elements in the list.
  
print(len(fruits))  # Output: 3

#sorted(list)`: Returns a new sorted list without changing the original list.

numbers = [5, 2, 9, 1]
print(sorted(numbers))  # Output: [1, 2, 5, 9]
print(numbers)  # Original list remains unchanged: [5, 2, 9, 1]


#sum(list)`: Returns the sum of elements in a list (for numerical lists).

numbers = [1, 2, 3, 4]
print(sum(numbers))  # Output: 10
  

#### **5.2 Common Methods**:
#index(element)`: Returns the index of the first occurrence of the specified element.
  
#rint(fruits.index("orange"))  # Output: 0


#count(element)`: Returns the number of occurrences of an element in the list.
  
numbers = [1, 2, 3, 1, 1]
print(numbers.count(1))  # Output: 3

#reverse()`: Reverses the elements of the list in place.

fruits.reverse()
print(fruits)  # Output: ['cherry', 'orange', 'apple']
 

#sort()`: Sorts the list in place (ascending by default).
  
numbers = [5, 2, 9, 1]
numbers.sort()
print(numbers)  # Output: [1, 2, 5, 9]
 

### **6. Nested Lists**

#### **Example**:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements in a nested list
print(matrix[0])  # Output: [1, 2, 3] (first row)
print(matrix[1][1])  # Output: 5 (element in the second row, second column)



## **Tuples and Sets in Python**

### **1. Tuples in Python**
### **Example**:
my_tuple = ("apple", "banana", "cherry")
numbers_tuple = (1, 2, 3, 4)


#### **Creating a Tuple with One Element**:
single_element_tuple = ("apple",)

### **2. Accessing Tuple Elements**

#### **Example**:
fruits = ("apple", "banana", "cherry")
print(fruits[0])  # Output: apple
print(fruits[-1])  # Output: cherry

#### **Slicing Tuples**:
print(fruits[1:3])  # Output: ('banana', 'cherry')

### **3. Tuple Operations**
#### **Tuple Concatenation**:
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print(combined_tuple)  # Output: (1, 2, 3, 4, 5, 6)

#### **Tuple Repetition**:
repeated_tuple = (1, 2) * 3
print(repeated_tuple)  # Output: (1, 2, 1, 2, 1, 2)

#### **Checking Membership**:
print("apple" in fruits)  # Output: True

### **4. Tuple Methods**
#count()`: Returns the number of times an element appears in the tuple.

my_tuple = (1, 2, 3, 1, 1)
print(my_tuple.count(1))  # Output: 3

#index()`: Returns the index of the first occurrence of an element.
my_tuple = ("apple", "banana", "cherry")
print(my_tuple.index("banana"))  # Output: 1
 
### **6. Sets in Python**
#### **Example**:
fruits_set = {"apple", "banana", "cherry"}
numbers_set = {1, 2, 3, 4, 5}

#### **Empty Set**:
empty_set = set()


### **7. Set Operations**
#### **Union**:
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # Output: {1, 2, 3, 4, 5}


#### **Intersection**:
intersection_set = set1 & set2  # Output: {3}

#### **Difference**:
difference_set = set1 - set2  # Output: {1, 2}

#### **Symmetric Difference**:
sym_diff_set = set1 ^ set2  # Output: {1, 2, 4, 5}


### **8. Set Methods**
#add()`: Adds an element to the set.
fruits_set.add("orange")
print(fruits_set)  # Output: {'apple', 'banana', 'cherry', 'orange'}


#remove()`: Removes a specified element from the set. Raises an error if the element does not exist.

fruits_set.remove("banana")
print(fruits_set)  # Output: {'apple', 'cherry'}

#discard()`: Removes a specified element without raising an error if it does not exist.

fruits_set.discard("banana")  # No error if "banana" is not in the set


#pop()`: Removes a random element from the set.
fruits_set.pop()


#clear()`: Removes all elements from the set.
fruits_set.clear()


## **Dictionaries in Python**
### **1. Creating a Dictionary**
#### **Example**:
karnataka_food = {
    "Bengaluru": "Bisi Bele Bath",
    "Mysuru": "Mysore Pak",
    "Mangaluru": "Neer Dosa"
}

### **2. Accessing Dictionary Elements**
#### **Example**:
print(karnataka_food["Mysuru"])  # Output: Mysore Pak
print(karnataka_food.get("Mangaluru"))  # Output: Neer Dosa
print(karnataka_food.get("Shivamogga", "Not Found"))  # Output: Not Found

### **3. Adding and Updating Dictionary Elements**

#### **Adding an Item**:
karnataka_food["Shivamogga"] = "Kadubu"
print(karnataka_food)

#### **Updating an Item**:
karnataka_food["Bengaluru"] = "Ragi Mudde"
### **4. Removing Elements from a Dictionary**
#op()`: Removes the specified key and returns the associated value.

mysuru_food = karnataka_food.pop("Mysuru")
print(mysuru_food)  # Output: Mysore Pak


#dl`: Removes the specified key.

del karnataka_food["Mangaluru"]

#cear()`: Empties the dictionary.

karnataka_food.clear()

### **5. Dictionary Methods**

#eys()`: Returns all the keys in the dictionary.
print(karnataka_food.keys())  # Output: dict_keys(['Bengaluru', 'Mysuru', 'Mangaluru'])

#alues()`: Returns all the values in the dictionary.
print(karnataka_food.values())  # Output: dict_values(['Bisi Bele Bath', 'Mysore Pak', 'Neer Dosa'])

#tems()`: Returns key-value pairs as tuples.
print(karnataka_food.items())  # Output: dict_items([('Bengaluru', 'Bisi Bele Bath'), ('Mysuru', 'Mysore Pak'), ('Mangaluru', 'Neer Dosa')])


#pdate()`: Updates the dictionary with another dictionary or iterable.
new_dishes = {"Hubballi": "Girmit"}
karnataka_food.update(new_dishes)
  