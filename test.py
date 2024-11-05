
F = input("Magneticka sila (F), zadejte 'x' : ")
Phi = input("Magnetický tok (Φ), zadejte 'x' : ")
R = input("Reluktance (𝓡), zadejte 'x' : ")

try:
    if F != 'x':
        F = float(F)
    if Phi != 'x':
        Phi = float(Phi)
    if R != 'x':
        R = float(R)

    if F == 'x':  
        if R == 0 or Phi == 0:
            print("Chyba nelze delit nulou.")
        else:
            F = Phi * R  
            print(f"Magneticka síla (F) = {F} At")

    elif Phi == 'x': 
        if R == 0:
            print("Chyba nelze delit nolou.")
        else:
            Phi = F / R 
            print(f"Magnetický tok (Φ) = {Phi} Wb")

    elif R == 'x': 
        if Phi == 0:
            print("Chyba nelze delit nulou.")
        else:
            R = F / Phi 
            print(f"Reluktance (𝓡) = {R} At/Wb")

except ValueError:
    print("Chybne zadane cislo nebo 'x'.")