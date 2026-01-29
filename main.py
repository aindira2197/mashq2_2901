class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def attack(self):
        pass


class Warrior(Character):
    def attack(self):
        print(f"{self.name} qilich bilan hujum qildi ⚔️")


class Mage(Character):
    def attack(self):
        print(f"{self.name} sehr ishlatdi 🔮")


w = Warrior("Thor", 100)
m = Mage("Gandalf", 80)

w.attack()
m.attack()
