---

# 🖥️ **PCProfiler**  
### _Reporte de procesos con conexiones activas_

PCProfiler es una herramienta en Python que genera un **reporte en formato HTML** detallando los procesos del sistema con **conexiones de red activas**, junto con estadísticas de entrada y salida de datos.

---

> ### 🚀 **¿Qué hace este script?**
> - Ejecuta `netstat -ano` para identificar los procesos con conexiones activas (TCP/UDP).
> - Usa la librería `psutil` para recopilar información como:
>   - **Nombre del proceso**
>   - **Ruta del ejecutable**
>   - **Bytes leídos y escritos por el proceso**
> - Genera automáticamente un archivo `reporte.html` con todos los datos recogidos.
> - Incluye una **tabla ordenable por columnas** (PID, Nombre, Ubicación, Bytes Leídos, Bytes Escritos).

---

> ### 📁 **Ruta de salida**
> El reporte se guarda automáticamente en:
> ```
> C:\pc-profiler\report.html
> ```

---

> ### 📷 **Vista previa del HTML**
> - Diseño claro y ordenado  
> - Tabla interactiva con ordenamiento al hacer clic en los encabezados  
> - Estilo limpio y minimalista  

---

> ### 🛠️ **Requisitos**
> - Python 3.x  
> - Módulo `psutil`  
>
> Instalación:
> ```bash
> pip install psutil
> ```

---

> ### 📝 **Uso**
> Ejecuta el script directamente desde consola:
> ```bash
> python pcprofiler.py
> ```
> Una vez generado, abre `report.html` con tu navegador para visualizar los resultados.

---
