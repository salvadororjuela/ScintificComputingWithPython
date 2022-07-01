# Class
class PartyAnimal:
    # Attribute
    x = 0

    # Method
    def party(self): # Special first parameter (self)
        self.x = self.x + 1
        print(f"So far: {self.x}")

# Create an object or instance of the PartyAnimal class
an = PartyAnimal()
# Call the party() for the instance created (an)
an.party()
an.party()
an.party()
# Another way to call the party() method for the instance (an) of the PartyAnimal class.
PartyAnimal.party(an)
