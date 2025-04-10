from ejercicio1 import Punto
punto_a = Punto(1, 2)
punto_b = Punto(3, 4)
class Linea:
    def __init__(self, punto_a, punto_b):
       
        self._punto_a = punto_a
        self._punto_b = punto_b
    
    def mueve_derecha(self, distancia):
       
        self._punto_a.x += distancia
        self._punto_b.x += distancia
    
    def mueve_izquierda(self, distancia):
        
        self._punto_a.x -= distancia
        self._punto_b.x -= distancia
    
    def mueve_arriba(self, distancia):
        
        self._punto_a.y += distancia
        self._punto_b.y += distancia
    
    def mueve_abajo(self, distancia):
       
        self._punto_a.y -= distancia
        self._punto_b.y -= distancia
    
    def __str__(self):
        
        return f"Línea desde {self._punto_a} hasta {self._punto_b}"
    
linea_prueba = Linea(punto_a, punto_b)
print(linea_prueba)