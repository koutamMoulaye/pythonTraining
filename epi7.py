from model.player import Player
from model.gun import Gun

knife =Gun("knife", 1)
rifle =Gun("shotpit", 2)
player1= Player("jack",5,2)
player2= Player("daniel",5,3)


player1.set_gun(rifle)
player1.attack_player(player2)

print(f"player1 : {player1.get_pseudo()} attack player2 : {player2.pseudo}")

print(f"Welcome to the player : {player1.get_pseudo()}\nyour health points is : {player1.get_health()}\nyour attack points is : {player1.get_attack()}\n" )
print(f"Welcome to the player : {player2.get_pseudo()}\nyour health points is : {player2.get_health()}\nyour attack points is : {player2.get_attack()}\n" )

