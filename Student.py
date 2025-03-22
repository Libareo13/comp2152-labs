from Person import Person


class Student(Person):
    def __init__(self, name, age, height, major):
        super().__init__(name, age, height)
        self.major = major
        print("This time it's a Student object")


# Create an instance of the Person class
person = Person("Mark", 20, 6)

# Print the public attribute
print(person.public_prop)

# Try printing the private name property directly (should cause an AttributeError)
# print(person.__name)  # This would cause an error

# Access the get_name() and set_name() methods
print(person.get_name())
person.set_name("Anna")
print(person.get_name())

# Now use magic getters and setters
# Comment out the old get_name and set_name functions

print(person.name)  # Access the name using magic getter
person.name = "Bob"  # Modify the name using magic setter
print(person.name)  # Confirm the change

# Create an instance of the Student class
student = Student("Maria", 22, 6, "Computer Science")