class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}, {self.description}"

    def get(self):
        print(f"The {self.name} was picked up!")

    def drop(self):
        print(f"The {self.name} was dropped!")
