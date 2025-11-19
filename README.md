# YOLO Model - Automatic Image Cropping

Este proyecto utiliza un modelo YOLO entrenado para detectar la región válida de una imagen (caja-testigo) y recortarla automáticamente.

El script procesa todas las imágenes dentro de la carpeta `Raw/` y guarda los recortes en `Post/`.

---

## 🚀 Requisitos

Necesitas:

- Python 3.9, 3.10 o 3.11  
- Git (opcional)
- Librerías de Python listadas en `requirements.txt`


---

## 📂 Estructura del proyecto

```
my_model/
│
├── testing.py               # Script principal (recorte con YOLO)
├── best.pt                  # Tu modelo YOLO entrenado
├── requirements.txt         # Dependencias
├── README.md                # Este archivo
│
├── Raw/                       # Carpeta de entrada (pon tus imágenes aquí)
│   └── .gitkeep               # Se puedde borrar este archivo
│
└── Post/                      # Carpeta de salida (los recortes aparecerán aquí)
    └── .gitkeep               # Se puedde borrar este archivo
```

---

## 🚀 Cómo descargar y ejecutar este proyecto

Puedes usar este proyecto de dos formas:

---

# 🟩 Opción 1: Descargar como ZIP (más fácil)

1. Ve al repositorio en GitHub.  
2. Haz clic en el botón **Code** (arriba a la derecha).  
3. Selecciona **Download ZIP**.  
4. Extrae el archivo ZIP en tu ordenador.  
5. Abre una terminal dentro de la carpeta extraída.  
6. Instala las dependencias:

```
pip install -r requirements.txt
```

7. Coloca tus imágenes dentro de la carpeta `Raw/`.  
8. Ejecuta el script:

```
python testing.py
```

Los recortes se guardarán automáticamente en la carpeta `Post/`.

---

# 🟦 Opción 2: Clonar el repositorio (recomendado)

Si tienes Git instalado, puedes clonar directamente este repositorio:

```
git clone https://github.com/Wortaxx/YOLO-Model-Chopping-img.git
```

Entra en la carpeta del proyecto:

```
cd YOLO-Model-Chopping-img
```

Instala las dependencias requeridas:

```
pip install -r requirements.txt
```

Coloca tus imágenes dentro de la carpeta:

```
Raw/
```

Ejecuta el script de recorte:

```
python testing.py
```

Los recortes aparecerán en:

```
Post/
```

---

## 📝 Notas importantes

- Requiere **Python 3.9 – 3.11**  
- No requiere Anaconda (pero funciona si lo usas)  
- Asegúrate de que el archivo `best.pt` está en la misma carpeta que `testing.py`  
- Las carpetas `Raw/` y `Post/` pueden venir vacías; incluyen un archivo `.gitkeep` para poder subirlas al repositorio  
