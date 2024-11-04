'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9.80665  # m/s^2, normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.622     # m/s^2, měsíční gravitace
SPEED_OF_LIGHT = 299792458  # m/s, rychlost světla ve vakuu
SPEED_OF_SOUND = 343       # m/s, rychlost zvuku při 20 °C v suchém vzduchu

''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''

def calculate_weight(weight, gravity):
    """
    Vypočítá váhu objektu na základě hmotnosti a gravitace.
    
    Args:
        mass (float): Hmotnost objektu v kilogramech.
        gravity (float): Tíhové zrychlení (defaultně pozemské).
        
    Returns:
        float: Váha objektu v newtonech.
    """
    return float(weight) * gravity

def calculate_sound_distance(distance_km):
    """
    Vypočítá čas potřebný pro zvuk, aby urazil zadanou vzdálenost v kilometrech.
    
    Parametry:
        vzdalenost_km (float): Vzdálenost v kilometrech.

    Vrací:
        float: Čas v sekundách pro zvuk na uražení zadané vzdálenosti.
    """
   
    return float(distance_km) * 1000 / SPEED_OF_SOUND 

def calculate_light_distance(distance_km):

    """
    Vypočítá čas potřebný pro světlo, aby urazilo zadanou vzdálenost v kilometrech.
    
    Parametry:
        vzdalenost_km (float): Vzdálenost v kilometrech.

    Vrací:
        float: Čas v sekundách pro světlo na uražení zadané vzdálenosti.
    """ 
    return float(distance_km) * 1000/ SPEED_OF_LIGHT 