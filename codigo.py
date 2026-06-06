
import random
import time

# Inicializamos la vida de los luchadores
vida_subzero = 100
vida_scorpion = 100

print("¡FIGHT!")
print("-" * 30)

# El bucle sigue mientras ambos tengan más de 0 de vida
while vida_subzero > 0 and vida_scorpion > 0:
    
    # --- Turno de Scorpion ---
    golpe_scorpion = random.randint(2, 10)
    vida_subzero -= golpe_scorpion
    # Evitamos que la vida quede en números negativos
    if vida_subzero < 0: vida_subzero = 0
    
    print(f"🔥 Scorpion mete un combo y quita {golpe_scorpion} de vida.")
    print(f"❄️ Sub-Zero queda con {vida_subzero} HP.\n")
    
    # Verificamos si Sub-Zero ya cayó para terminar la pelea inmediatamente
    if vida_subzero <= 0:
        break
        
    time.sleep(1) # Una pequeña pausa para darle emoción a la consola
    
    # --- Turno de Sub-Zero ---
    golpe_subzero = random.randint(2, 10)
    vida_scorpion -= golpe_subzero
    if vida_scorpion < 0: vida_scorpion = 0
    
    print(f"❄️ Sub-Zero congela el piso y quita {golpe_subzero} de vida.")
    print(f"🔥 Scorpion queda con {vida_scorpion} HP.\n")
    
    time.sleep(1)
    print("-" * 30)

# --- Fin de la pelea ---
print("¡FIN DE LA PELEA!")
if vida_subzero > 0:
    print("❄️ ¡SUB-ZERO WINS! FLAWLESS VICTORY.")
else:
    print("🔥 ¡SCORPION WINS! TOASTY.")
