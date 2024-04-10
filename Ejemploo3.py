# Función para calcular el área de un rectángulo
def calcularAreaRectangulo(baseRectangulo, alturaRectangulo):
    areaRectangulo = baseRectangulo * alturaRectangulo
    return areaRectangulo

# Función para calcular el área de un triángulo
def calcularAreaTriangulo(baseTriangulo, alturaTriangulo):
    areaTriangulo = 0.5 * baseTriangulo * alturaTriangulo
    return areaTriangulo

# Función principal
def main():
    base1 = 4
    altura1  = 6
    rect_area = calcularAreaRectangulo(base1, altura1)
    print("Área del rectángulo:", rect_area)

    base2 = 5
    altura2 = 8
    tri_area = calcularAreaTriangulo(base2, altura2)
    print("Área del triángulo:", tri_area)

main()
