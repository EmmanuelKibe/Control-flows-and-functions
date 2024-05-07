class Person:
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender
        
    def introduce(self):
        print(f"This is {self.name}. He is a {self.age} year old {self.gender}")


person1 = Person("Emmanuel", 19, "Male")
person1.introduce()