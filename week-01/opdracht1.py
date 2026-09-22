# Oefening 1
# Print de volgende zin "Hello World"

print("hello world")


# Oefening 2
# Verander de waarde van de onderstaande variabelen.
# Print deze daarna 1 voor 1 uit

naam = "Yehor"
leeftijd = 18
woonstad = "Montfoort"


# Oefening 3
# Gebruik nu bovenstaande variabelen om zinnen te bouwen
# Bijvoorbeeld print("Hallo mijn naam is ", naam) of print(f"Mijn naam is {naam}")

print("Hallo mijn naam is ", naam)
print(f"Mijn naam is {naam}")

# Oefening 4
# Maak variabelen aan voor je favoriete game, hoe veel uur je deze hebt gespeeld en welk cijfer je dit spel zou geven
# Print deze daarna in zinnen uit, bijvoorbeeld "Mijn favoriete game is Minecraft" "Ik heb deze game 150 uur gespeeld", "Ik geef deze game een 8.5"

game_naam = "Dota 2"
uur_gespeeld = 3500
fav_hero = "Meepo"

print(f"Mijn favorite game is {game_naam}, ik heb deze game {uur_gespeeld} uur gespeeld, mijn favorite hero is {fav_hero}")

# Oefening 5
# Maak twee variabelen aan, number1 en number2
# Bereken daarna de som (+), het verschil (-) en het product (*) uit van deze nummers.
# Print daarna de uitkomsten uit

num1= 5
num2= 10
num3= 2

result=num1*num3+num2

print("5*2+10=",result)

# Oefening 6
# Maak een simpel game character met minimaal de volgende variabelen: name, health, level, damage
# Print deze vervolgens uit
# Zorg er daarna voor dat je character 20 damage neemt, print nu de nieuwe waarde van zijn health uit

hero_naam = "Meepo"

health = 1200
level = 10
damage = 80

print(f"{hero_naam} {level} lvl\nhealth: {health}\ndamage: {damage}")

health=health-20

print(f"{hero_naam} {level} lvl\nhealth: {health}\ndamage: {damage}")

# Oefening 7
# Ga verder met je character van de vorige oefening. Voeg nu een nieuw variabel "weapon" toe.
# Geef het wapen een naam, verhoog de damage van je character en verhoog het level met 1
# Print daarna de nieuwe waardes uit 

weapon = "Divine Rapier"

damage += 200
level += 1

print(f"{hero_naam} {level} lvl\nhealth: {health}\ndamage: {damage}\nweapon: {weapon}")

# Oefening 8
# Maak een programma dat een profiel van een gamer laat zien
# Maak minimaal de volgende variabelen: name, age, favouriteGame, hoursPlayed, level, score
# Print al deze informatie netjes uit
# Verhoog daarna de score van het profiel met 250 en print de nieuwe waarde
# Bonus! Voeg zelf 3 nieuwe variabelen toe

name = "Yehor"
age = 18
favouriteGame = "Dota 2"
hoursPlayed = 3500
level = 10
score = 1000

rank = "Guardian"
mainHero = "Meepo"
wins = 2000

print(f"""
Name: {name}
Age: {age}
Favourite game: {favouriteGame}
Hours played: {hoursPlayed}
Level: {level}
Score: {score}
Rank: {rank}
Main hero: {mainHero}
Wins: {wins}
""")

score += 250

print(f"\nNew score: {score}")