# crear 3 prroductos para agregar a la factura nombre detalle1, detalle2, detalle3

from cliente import Cliente
from factura import Factura
from pago import Pago
from producto import Producto

def main():
    cliente = Cliente( 1, "nombre", "direccion", "telefono", "tipo")


    detalle1 = Producto(1, "detalle1", 10, 2)
    detalle2 = Producto(2, "detalle2", 20, 3)
    detalle3 = Producto(3, "detalle3", 30, 4)

    factura1 = Factura(1, "123456", "Razon Social", cliente, [detalle1, detalle2, detalle3])

    factura1.imprimir()

    # agregar pago a la factura
    pago1 = Pago(100, "2021-09-01", "Efectivo")
    factura1.agregar_pago(pago1)

    factura1.imprimir()
    

if __name__ == "__main__":
    main()