from character import Character

def main():
    hero = Character("Knight", 40, 6)  # Slightly boosted stats to handle two enemies
    enemies = [
        Character("Goblin 1", 20, 3),
        Character("Goblin 2", 20, 3)
    ]

    print(hero)
    for enemy in enemies:
        print(enemy)
    print()

    # Continue loop as long as the hero is alive AND at least one enemy is alive
    while hero.is_alive() and any(e.is_alive() for e in enemies):
        # Hero attacks the first living enemy in the list
        target = next((e for e in enemies if e.is_alive()), None)
        if target:
            hero.attack(target)

        # Each living enemy attacks the hero back
        for enemy in enemies:
            if enemy.is_alive() and hero.is_alive():
                enemy.attack(hero)

        print(hero)
        for enemy in enemies:
            print(enemy)
        print()

    print("Battle over!")
    if hero.is_alive():
        print(f"{hero.name} wins!")
    else:
        print("The enemies win!")

if __name__ == "__main__":
    main()