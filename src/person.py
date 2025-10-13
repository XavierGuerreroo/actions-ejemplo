class Person:
    """
    Clase Person que representa una persona con nombre y apellido.
    
    Esta clase implementa el método especial __str__ para mostrar
    el nombre completo de la persona en formato capitalizado.
    """
    
    def __init__(self, first_name, last_name):
        """
        Inicializa una persona con nombre y apellido.
        
        Args:
            first_name (str): El nombre de la persona
            last_name (str): El apellido de la persona
        """
        self.first_name = first_name
        self.last_name = last_name
    
    def __str__(self):
        """
        Retorna una representación en string de la persona.
        
        El formato es "Nombre Apellido" con la primera letra de cada
        palabra en mayúscula (capitalizado).
        
        Returns:
            str: Nombre completo capitalizado
        """
        # .title() maneja bien nombres compuestos como "de la cruz"
        return f"{self.first_name.title()} {self.last_name.title()}"
    
# Crear personas
p1 = Person("juan", "perez")
p2 = Person("MARIA", "LOPEZ")
p3 = Person("carlos", "gonzalez")

# Al imprimir, __str__ se ejecuta automáticamente
print(p1)   # Juan Perez
print(p2)   # Maria Lopez
print(p3)   # Carlos Gonzalez    
