
🏦 Proyecto Banking - Gestión de Países
📋 Descripción
Sistema de gestión de países desarrollado en Django con base de datos Supabase. Implementa las funcionalidades CRUD completas según las especificaciones del PDF.

🚀 Configuración Rápida
1. Clonar el repositorio
bash
git clone [https://github.com/AndresMalua/banking.git]
cd banking
2. Configurar variables de entorno
Crear archivo .env en la raíz del proyecto con:
env
# CREDENCIALES SUPABASE Obtener de los comentarios de la plataforma
DB_NAME=[NAME_PROPORCIONADA_EN_PLATAFORMA]
DB_USER=[USER_PROPORCIONADA_EN_PLATAFORMA]
DB_PASSWORD=[PASSWORD_PROPORCIONADA_EN_PLATAFORMA]
DB_HOST=[HOTS_PROPORCIONADA_EN_PLATAFORMA]
DB_PORT=[PORT_PROPORCIONADA_EN_PLATAFORMA]

3. Instalar dependencias
bash
pip install -r requirements.txt
4. Configurar base de datos
bash
python manage.py migrate
5. Ejecutar servidor de desarrollo
bash
python manage.py runserver
6. Acceder a la aplicación
Abrir en el navegador: http://127.0.0.1:8000/countries/