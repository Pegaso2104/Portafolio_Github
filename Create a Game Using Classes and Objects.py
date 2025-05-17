class Creature:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, other_creature):
        """Simulate an attack on another creature."""
        if self.is_alive():
            other_creature.health -= self.power
            print(f"{self.name} attacks {other_creature.name} for {self.power} damage!")
        else:
            print(f"{self.name} is knocked out and cannot attack!")

    def is_alive(self):
        """Check if the creature is still alive."""
        return self.health > 0

    def __repr__(self):
        return f"{self.name} (Health: {self.health}, Power: {self.power})"


class Trainer:
    def __init__(self, name):
        self.name = name
        self.creatures = []

    def add_creature(self, creature):
        """Add a creature to the trainer's team."""
        self.creatures.append(creature)

    def battle(self, other_trainer):
        """Simulate a battle between two trainers."""
        print(f"Battle begins between {self.name} and {other_trainer.name}!")
        while self.creatures and other_trainer.creatures:
            creature1 = self.creatures[0]
            creature2 = other_trainer.creatures[0]

            # Each creature attacks once
            creature1.attack(creature2)
            if not creature2.is_alive():
                print(f"{creature2.name} has been knocked out!")
                other_trainer.creatures.pop(0)

            if not other_trainer.creatures:  # Check if other trainer has no creatures left
                print(f"{other_trainer.name} is out of creatures! {self.name} wins!")
                break

            creature2.attack(creature1)
            if not creature1.is_alive():
                print(f"{creature1.name} has been knocked out!")
                self.creatures.pop(0)

            if not self.creatures:  # Check if current trainer has no creatures left
                print(f"{self.name} is out of creatures! {other_trainer.name} wins!")
                break

    def __repr__(self):
        return f"Trainer {self.name} with {len(self.creatures)} creatures"


# Create two creatures
charizard = Creature("Charizard", 100, 20)
pikachu = Creature("Pikachu", 50, 10)

# Create two trainers
ash = Trainer("Ash")
misty = Trainer("Misty")

# Add creatures to trainers
ash.add_creature(charizard)
misty.add_creature(pikachu)

# Show initial state
print(ash)
print(misty)

# Start a battle
ash.battle(misty)
