# Import modulu physics
import physics 

def main():
    # Výpočet váhy na Zemi a na Měsíci
    weight_input = input("Zadej vahu v kg:") # Hmotnost v kg
    earth_weight = physics.calculate_weight(weight_input,physics.EARTH_GRAVITY)
    moon_weight = physics.calculate_weight(weight_input, physics.MOON_GRAVITY)
    print(f"Váha na Zemi: {earth_weight:.2f} N")
    print(f"Váha na Měsíci: {moon_weight:.2f} N")

    distance_input = input("Zadej delku v km:")

    time_light = physics.calculate_light_distance(distance_input)
    time_sound = physics.calculate_sound_distance(distance_input)

    print(f"Zvuk tuto vzdalenost urazi za:{time_light:.6f} ")
    print(f"Svetlo tuto vzdalenost urazi za:{time_sound:.2f}")



main()
