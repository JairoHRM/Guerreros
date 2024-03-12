# Definimos la interfaz para el comportamiento de guerra
class AccionGuerrera:
    def accion(self):
        pass

# Implementación del comportamiento de guerra para guerreros de ataque
class Disparar(AccionGuerrera):
    def accion(self):
        print("¡Estoy disparando mis flechas!")

# Implementación del comportamiento de guerra para guerreros de defensa
class Defender(AccionGuerrera):
    def accion(self):
        print("Escudos arriba")

# Definimos la interfaz para el comportamiento de plan de guerra
class TipoEstrategia:
    def alineacion(self):
        pass

# Implementación del comportamiento de ataque
class Ataque(TipoEstrategia):
    def alineacion(self):
        print("Alisten, apunten, disparen!")

# Implementación del comportamiento de defensa
class RepelerAtaque(TipoEstrategia):
    def alineacion(self):
        print("Adelante, formación en V, escudos arriba!")

# Implementación del comportamiento de planeación
class Avance(TipoEstrategia):
    def alineacion(self):
        print("Avanzan escuderos, arqueros atrás!")

# Clase base para los guerreros
class Guerrero:
    def __init__(self, AccionGuerrera, TipoEstrategia):
        self.AccionGuerrera = AccionGuerrera
        self.TipoEstrategia = TipoEstrategia

    def perform_accion(self):
        self.AccionGuerrera.accion()

    def perform_alineacion(self):
        self.TipoEstrategia.alineacion()

    def planeacion(self):
        print("Analizamos el terreno y las fuerzas opositoras para la batalla")

# Clase concreta para un guerrero de ataque
class Arquero(Guerrero):
    def __init__(self):
        super().__init__(Disparar(), Ataque())

# Clase concreta para un guerrero de defensa
class Escudero(Guerrero):
    def __init__(self):
        super().__init__(Defender(), RepelerAtaque())

# Ejemplo de uso
if __name__ == "__main__":
    arquero_flechas = Arquero()
    escudero_escudos = Escudero()

    print("Guerrero Arquero:")
    arquero_flechas.perform_accion()
    arquero_flechas.perform_alineacion()
    arquero_flechas.planeacion()

    print("\nGuerrero Escudero:")
    escudero_escudos.perform_accion()
    escudero_escudos.perform_alineacion()
    escudero_escudos.planeacion()