import math

# Adım 1: Noktaların listesini tanımlayın
points = [(1, 2), (3, 4), (5, 6), (7, 8)]  # Örnek noktalar

# Adım 2: Öklid mesafesini hesaplayan fonksiyonu tanımlayın
def oklidMesafesi(nokta1, nokta2):
    return math.sqrt((nokta2[0] - nokta1[0])**2 + (nokta2[1] - nokta1[1])**2)

# Adım 3: Her nokta çifti arasındaki mesafeyi hesaplayın ve mesafeleri bir listede saklayın
mesafeler = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        mesafe = oklidMesafesi(points[i], points[j])
        mesafeler.append(mesafe)

# Adım 4: Minimum mesafeyi bulun
min_mesafe = min(mesafeler)

# Sonucu yazdırın
print(f"Minimum Öklid mesafesi: {min_mesafe}")
