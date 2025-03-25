GRAVITY = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14,
    "Earth": 1.0
}


def calculate_weight(weight:float, planet:str):

    convert = planet.capitalize()
     
    if convert in GRAVITY:
        calculate = round( weight * GRAVITY[convert], 2)
        print(calculate)
    else:
        print("\nYour Planet Is Not Found")


def main():
    print("\n🌍 Welcome to the Planetary Weight Calculator\n")
    try:
        user_weight : float = float(input("Enter your weight on Earth (kg): "))

        print("\nAvailable planets: Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune")

        user_Planet = input("\nEnter the planet name: ")

        if user_Planet == "" and user_weight == "":
            print("\nPlease Enetr Number")
        else:
            calculate_weight(user_weight, user_Planet)
    except ValueError as e:
        print("Please Enter Only Number")

    
if __name__ in "__main__":
    main()