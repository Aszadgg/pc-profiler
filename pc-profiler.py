import subprocess
import psutil
import os
from datetime import datetime

output_folder = "C:\\pcprofiler"
os.makedirs(output_folder, exist_ok=True)
output_file = os.path.join(output_folder, "reporte.html")

# Ejecutar netstat para obtener procesos con conexiones activas
result = subprocess.check_output("netstat -ano", shell=True, text=True)
lines = result.splitlines()

# Obtener PIDs únicos con conexiones activas
pids = set()
for line in lines:
    if "TCP" in line or "UDP" in line:
        parts = line.split()
        if len(parts) >= 5:
            try:
                pid = int(parts[-1])
                pids.add(pid)
            except:
                continue

data = []

for pid in pids:
    try:
        proc = psutil.Process(pid)
        exe = proc.exe() if proc.exe() else "Desconocido"
        name = proc.name()
        io = proc.io_counters()
        sent = io.write_bytes
        recv = io.read_bytes

        data.append({
            "pid": pid,
            "name": name,
            "exe": exe,
            "sent": sent,
            "recv": recv,
        })
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        continue

# Crear HTML
html = f"""
<html>
<head>
    <title>Reporte de procesos con tráfico de red (por conexión activa)</title>
    <style>
        table {{ border-collapse: collapse; width: 100%; }}
        th, td {{ border: 1px solid #ccc; padding: 8px; text-align: left; }}
        th {{ background-color: #f2f2f2; cursor: pointer; }}
    </style>
    <script>
        function sortTable(n) {{
            var table = document.getElementById("procTable");
            var rows = table.rows;
            var switching = true;
            var dir = "asc";
            var switchcount = 0;

            while (switching) {{
                switching = false;
                for (var i = 1; i < (rows.length - 1); i++) {{
                    var x = rows[i].getElementsByTagName("TD")[n];
                    var y = rows[i + 1].getElementsByTagName("TD")[n];
                    var xContent = isNaN(parseFloat(x.innerHTML)) ? x.innerHTML.toLowerCase() : parseFloat(x.innerHTML);
                    var yContent = isNaN(parseFloat(y.innerHTML)) ? y.innerHTML.toLowerCase() : parseFloat(y.innerHTML);
                    if ((dir == "asc" && xContent > yContent) || (dir == "desc" && xContent < yContent)) {{
                        rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
                        switching = true;
                        switchcount++;
                        break;
                    }}
                }}
                if (switchcount == 0 && dir == "asc") {{
                    dir = "desc";
                    switching = true;
                }}
            }}
        }}
    </script>
</head>
<body>
<h2>Procesos con conexiones activas</h2>
<p>Generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
<table id="procTable">
<tr>
    <th onclick="sortTable(0)">PID</th>
    <th onclick="sortTable(1)">Nombre</th>
    <th onclick="sortTable(2)">Ubicación</th>
    <th onclick="sortTable(3)">Bytes Leídos</th>
    <th onclick="sortTable(4)">Bytes Escritos</th>
</tr>
"""

for item in data:
    html += f"<tr><td>{item['pid']}</td><td>{item['name']}</td><td>{item['exe']}</td>" \
            f"<td>{item['recv'] / 1024:.2f} KB</td><td>{item['sent'] / 1024:.2f} KB</td></tr>"

html += "</table></body></html>"

# Guardar HTML
with open(output_file, "w", encoding="utf-8") as f:
    f.write(html)

print(f"✅ Reporte generado en: {output_file}")
