class Player:
    def __init__(self, pseudo,health,attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.gun = None
        print(f"Welcome to the player : {pseudo}\nyour health points is : {health}\nyour attack points is : {attack}\n" )

    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack

    def damage(self, damage):
        self.health-= damage

    def attack_player(self, target_player):
        damage = self.attack

#dégât plus important le joueur attaque avec l'arme

        if self.has_gun():
            damage += self.gun.get_damage_amount()
            target_player.damage(damage)

#méthode pour le changement d'arme
    def set_gun(self, gun):
        self.gun = gun

#verifier que le joueur à une arme
    def has_gun(self):
        return  self.gun is not None






