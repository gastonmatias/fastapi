# FastAPI Demo - API de Productos

API REST simple construida con FastAPI (just 4 learning)

## Tecnologías

- Python 3.x
- FastAPI
- Uvicorn

## Instalación
```bash
# clonar repositorio
git clone https://github.com/gastonmatias/fastapi.git
cd fastapi

# crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# instalar dependencias
pip install -r requirements.txt
```

## Ejecutar
```bash
# con el venv activado
uvicorn main:app --reload
```

La API estará disponible en: http://127.0.0.1:8000

Documentación interactiva: http://127.0.0.1:8000/docs

## Endpoints

- `GET /` - Health check
- `GET /producto` - Listar todos los producto
- `GET /producto/{id}` - Obtener un producto específico
- `POST /producto` - Crear un nuevo producto
- `PUT /producto/{id}` - Actualizar un producto
- `DELETE /producto/{id}` - Eliminar un producto

## Autor

Gaston Matias
```
