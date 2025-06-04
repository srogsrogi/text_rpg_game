import random
import math

class Character(object):
    def __init__(self, name, level, max_hp, hp, strength):
        self.name = name
        self.level = level
        self.max_hp = max_hp
        self.hp = hp
        self.strength = strength

    def attack(self):
        return self.strength * 5 + self.strength * random.randint(1, 3)

    def take_damage(self, damage):
        self.hp -= damage

    def is_alive(self):
        return self.hp > 0


class Player(Character):
    def __init__(self, name):
        level = 1
        max_hp = 100
        hp = max_hp
        strength = 5
        super().__init__(name, level, max_hp, hp, strength)
        self.exp = 0
        self.dex = 5
        self.int = 5

    def gain_exp(self, exp):
        self.exp += exp

    def required_exp(self):
        return 10 + round(self.level ** 1.3)

    def level_up(self):
        self.strength += 1
        self.dex += 1
        self.int += 1
        self.max_hp += 10
        self.exp -= self.required_exp()
        self.level += 1
        print("레벨 업! 올스탯이 1과 최대hp 10이 증가합니다.")

class Enemy(Character):
    def __init__(self, name, level, max_hp, exp_reward):
        hp = max_hp
        strength = level + 2
        super().__init__(name, level, max_hp, hp, strength)
        self.exp_reward = 3 + round(level ** 1.2)


player = Player("hg")
enemy = Enemy("goblin", 1, 50)