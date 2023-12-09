class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"Person: {self.name} ({self.age} years old)"

class Sports:
    def __init__(self, game):
        self.game = game

    def __repr__(self) -> str:
        return f"Sport: {self.game}"

class School:
    def __init__(self, school_name, level):
        self.school_name = school_name
        self.level = level

    def __repr__(self) -> str:
        return f"School: {self.school_name}, Level: {self.level}"

class Student(Person, Sports, School):
    def __init__(self, name, age, reading_hours, school_name, level, favorite_sport):
        self.reading_hours = reading_hours
        Person.__init__(self, name, age)
        Sports.__init__(self, favorite_sport)
        School.__init__(self, school_name, level)

    def __repr__(self) -> str:
        return f"{Person.__repr__(self)}\n{School.__repr__(self)}\n{Sports.__repr__(self)}\nReading Hours: {self.reading_hours} per day"

# Creating a student instance
nihad = Student(name="Nihad", age=22, reading_hours="8 hours", school_name="ABC High School", level=12, favorite_sport="cricket")

# Printing student details
print(nihad)
