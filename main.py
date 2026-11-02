from character import Character

def main():
    hero = Character("Knight", 30, 5)
    enemy = Character("Goblin", 20, 3)

    print(hero)
    print(enemy)
    print()

    while hero.is_alive() and enemy.is_alive():
        hero.attack(enemy)
        if enemy.is_alive():
            enemy.attack(hero)
        print(hero)
        print(enemy)
        print()

    print("Battle over!")
    if hero.is_alive():
        print(f"{hero.name} wins!")
    else:
        print(f"{enemy.name} wins!")

if __name__ == "__main__":
    main()
