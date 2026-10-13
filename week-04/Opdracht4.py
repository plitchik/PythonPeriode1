# Opdracht - Weapon Selector
#
# Je gaat een programma maken waarin een speler een wapen kan kiezen.
# Ieder wapen heeft zijn eigen damage en een speciale eigenschap.
#
# Stap 1 - Variabelen
# Maak de volgende variabelen aan:
# - Een variabele voor de naam van de speler
# - Een variabele voor het gekozen wapen
# - Een variabele voor de damage van het wapen


"""
Ik besloot deze code zelf te schrijven,
ik heb hem zelf ontwikkeld met behulp van AI
puur om iets nieuws te leren en het te kunnen gebruiken.
"""

speler=input('Wat is your name?')

#alle beschikbare wapens
wapen={
    'knife': 20,
    'gun': 50,
    'stone': 5
}
all_wapen=list(wapen.keys())

#Een while wordt gebruikt om de keuze in de toekomst te bevestigen.
while True:
    print("beschikbare een wapen -", ", " .join(all_wapen))
    wapen_kiezen=input("Kiez een wapen: ").lower()

    match wapen_kiezen:
        case "knife":
            print("interessante keuze, knife heeft",wapen[wapen_kiezen],"beschadigingen.")
        case "gun":
            print("prachtige keuze, gun heeft",wapen[wapen_kiezen],"beschadigingen.")
        case "stone":
            print(".... stone heeft", wapen[wapen_kiezen],'beschadigingen.')
        case _:
            print("Dit wapen bestaat niet!")
            continue

    bevestiging=input("Weet je zeker dat je dit wapen wilt kiezen? (ja/nee): ").lower()
    
    if bevestiging == "ja":
        print("Speler:",speler)
        print('Wapen:',wapen_kiezen)
        print('Damage:',wapen[wapen_kiezen])
        break
    elif bevestiging =="nee":
        print("Kiez op niuwe")





# Geef de speler zelf een naam en kies alvast een wapen.
#
# LET OP:
# Gebruik voor alle variabelen de juiste Python naming conventions!
# Bijvoorbeeld: player_name in plaats van playerName.


# Stap 2 - Match Case
# Gebruik een match case om te controleren welk wapen de speler heeft.
#
# De speler kan kiezen uit de volgende wapens:
#
# Sword:
# - Doet 20 damage
# - Print "Je gebruikt een zwaard!"
#
# Bow:
# - Doet 15 damage
# - Print "Je gebruikt een boog!"
#
# Staff:
# - Doet 25 damage
# - Print "Je gebruikt een magische staf!"
#
# Axe:
# - Doet 30 damage
# - Print "Je gebruikt een bijl!"
#
# Zorg ervoor dat de damage variabele de juiste waarde krijgt.
#
# Als de speler een onbekend wapen heeft gekozen:
# - Zet de damage op 0
# - Print "Onbekend wapen!"
#
# TIP:
# Gebruik case _ voor een onbekende waarde.


# Stap 3 - Resultaat printen
# Print na de match case de volgende informatie:
#
# Speler: Steve
# Wapen: Sword
# Damage: 20
#
# Zorg ervoor dat de informatie uit je variabelen komt.


# Stap 4 - Comments
# Voeg minimaal 3 eigen comments toe aan je programma.
#
# Leg met deze comments uit:
# - Wat een bepaald stuk code doet
# - Waarom je een match case gebruikt
# - Wat er gebeurt als het wapen niet bestaat
#
# Schrijf duidelijke comments die iemand anders helpen
# om jouw code te begrijpen.


# Stap 5 - Naming Conventions
# Controleer of je code voldoet aan de Python naming conventions.
#
# - Gebruik snake_case voor variabelen
# - Gebruik duidelijke Engelse namen
# - Begin variabelen met een kleine letter
# - Gebruik geen spaties in variabelenamen
#
# FOUT: playerDamage = 20
# GOED: player_damage = 20
#
# FOUT: x = "Sword"
# GOED: selected_weapon = "Sword"


# BONUS 1
# Voeg zelf minimaal 2 nieuwe wapens toe aan je match case.
# Bedenk voor ieder wapen een eigen damage en beschrijving.


# BONUS 2
# Maak een variabele enemy_health met de waarde 100.
# Laat de speler 3 keer aanvallen met zijn gekozen wapen.
#
# Gebruik hiervoor een for-loop.
#
# Print na iedere aanval hoeveel health de vijand nog heeft.
# Zorg ervoor dat de health niet onder de 0 komt.


# BONUS 3
# Gebruik een while-loop om de vijand aan te vallen
# totdat de vijand geen health meer heeft.
#
# Print daarna "Vijand verslagen!"