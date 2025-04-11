from Pesona import Persona


class libro():
    def __init__(self, titulo, posho,ISBN, páginas, edicion,editorial,lugar, fecha):
        self.titulo = titulo
        self.autor = posho
        self.ISBN = ISBN
        self.páginas = páginas
        self.edicion = edicion
        self.editorial = editorial
        self.lugar = lugar
        self.fecha = fecha
    
    def setear(self,):
        input1=input("ingrese un titulo nuevo")
        self.titulo = input1
        

    def __str__(self):
        return f'Título: {self.titulo}\nAutor: {self.autor.nombre}\nISBN: {self.ISBN}\nPáginas: {self.páginas}\nEdición: {self.edicion}\nEditorial: {self.editorial}\nLugar: {self.lugar}\nFecha: {self.fecha}'
    


