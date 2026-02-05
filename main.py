from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# instancia de la aplicación (como @SpringBootApplication)
app = FastAPI()

# dto equivalente (como tus record o clases dto en java)
class ProductoDTO(BaseModel):
    id: Optional[int] = None
    nombre: str
    precio: float
    stock: int

# simulación de base de datos en memoria
# simulación de base de datos con datos de prueba
producto_db = [
    {
        "id": 1,
        "nombre": "Laptop Dell XPS 15",
        "precio": 1899.99,
        "stock": 15
    },
    {
        "id": 2,
        "nombre": "Mouse Logitech MX Master 3",
        "precio": 99.99,
        "stock": 50
    },
    {
        "id": 3,
        "nombre": "Teclado Mecánico Keychron K2",
        "precio": 89.99,
        "stock": 30
    },
    {
        "id": 4,
        "nombre": "Monitor Samsung 27'' 4K",
        "precio": 449.99,
        "stock": 8
    },
    {
        "id": 5,
        "nombre": "Webcam Logitech C920",
        "precio": 79.99,
        "stock": 25
    },
    {
        "id": 6,
        "nombre": "Audífonos Sony WH-1000XM5",
        "precio": 399.99,
        "stock": 12
    },
    {
        "id": 7,
        "nombre": "SSD Samsung 1TB",
        "precio": 129.99,
        "stock": 100
    },
    {
        "id": 8,
        "nombre": "Router TP-Link AX3000",
        "precio": 149.99,
        "stock": 20
    },
    {
        "id": 9,
        "nombre": "Mousepad XL Gamer",
        "precio": 24.99,
        "stock": 75
    },
    {
        "id": 10,
        "nombre": "Cable USB-C 2m",
        "precio": 14.99,
        "stock": 200
    }
]

# endpoints (como @RestController + @RequestMapping)
@app.get("/")
def root():
    return {"mensaje": "API funcionando"}

@app.get("/producto")
def listar_producto():
    # equivalente a un @GetMapping en spring
    return producto_db

@app.get("/producto/{producto_id}")
def obtener_producto(producto_id: int):
    # path variable como en spring
    for producto in producto_db:
        if producto["id"] == producto_id:
            return producto
    return {"error": "Producto no encontrado"}

@app.post("/producto")
def crear_producto(producto: ProductoDTO):
    # validación automática del request body (como @Valid en spring)
    nuevo_producto = producto.dict()
    nuevo_producto["id"] = len(producto_db) + 1
    producto_db.append(nuevo_producto)
    return nuevo_producto

@app.put("/producto/{producto_id}")
def actualizar_producto(producto_id: int, producto: ProductoDTO):
    for idx, prod in enumerate (producto_db):
        if prod["id"] == producto_id:
            producto_actualizado = producto.dict()
            producto_actualizado["id"] = producto_id
            producto_db[idx] = producto_actualizado
            return producto_actualizado
    return {"error": "Producto no encontrado"}

@app.delete("/producto/{producto_id}")
def eliminar_producto(producto_id: int):
    for idx, prod in enumerate(producto_db):
        if prod["id"] == producto_id:
            producto_db.pop(idx)
            return {"mensaje": "Producto eliminado"}
    return {"error": "Producto no encontrado"}
