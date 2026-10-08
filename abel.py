import getpass

def main():
    # Code PIN correct (à remplacer par le vôtre)
    pin_correct = 3456

    max_tentatives = 3

    for i in range(1, max_tentatives + 1):
        print(f"\nTentative {i}/{max_tentatives}")
        pin = getpass.getpass("Saisissez votre code PIN à 4 chiffres : ")

        # Vérification : 4 chiffres exactement
        if len(pin) != 4 or not pin.isdigit():
            print("❌ Le code doit contenir exactement 4 chiffres.")
            continue

        if pin == pin_correct:
            print("\n✅ Connexion réussie ! Bienvenue sur votre compte.")
            return
        else:
            print("❌ Code PIN incorrect.")

    print("\n🔒 Compte bloqué après 3 tentatives échouées.")

if __name__ == "__main__":
    main()
