# Sistema de Gestión de Reservas para Hotel

Una aplicación web avanzada para la gestión de reservas hoteleras en tiempo real. Diseñada para proporcionar una experiencia eficiente y segura, tanto para los clientes que realizan reservas como para los administradores que gestionan la disponibilidad y los recursos del hotel.

## Tecnologías Utilizadas

- **Django**: Framework backend que maneja la lógica de negocio, la gestión de usuarios y la interacción con la base de datos.
- **MySQL**: Base de datos relacional para almacenar información sobre usuarios, reservas, habitaciones y disponibilidad.
- **HTML/CSS**: Para la construcción y estilización de la interfaz de usuario.
- **JavaScript**: Añade interactividad y mejora la experiencia del usuario, incluyendo validaciones en tiempo real y actualización dinámica de la interfaz.

## Funcionalidades Clave

- **Reserva en Tiempo Real**: 
  - Los usuarios pueden buscar disponibilidad en función de fechas seleccionadas, tipo de habitación y número de personas.
  - Utiliza AJAX para enviar solicitudes al servidor sin recargar la página, proporcionando feedback instantáneo sobre la disponibilidad.
  - La información de la reserva, incluyendo datos personales y preferencias, se valida y guarda en la base de datos con protección CSRF para prevenir ataques maliciosos.
  
- **Gestión de Reservas para Administradores**: 
  - Un panel de administración, desarrollado con Django Admin, permite a los administradores visualizar todas las reservas con filtros avanzados para búsqueda por fecha, cliente o estado de la reserva.
  - Permite la modificación de reservas existentes, incluyendo cambios de fecha, tipo de habitación o detalles del cliente.
  - Incluye opciones para cancelar reservas, actualizando automáticamente la disponibilidad de las habitaciones en la base de datos.

- **Accesibilidad y Seguridad**: 
  - Implementación de medidas de seguridad, incluyendo la protección CSRF y la validación de entradas para prevenir inyecciones SQL.
  - Gestión de sesiones seguras para proteger la información personal de los usuarios durante todo el proceso de reserva.
  - Acceso restringido al panel de administración mediante autenticación de usuarios, con permisos diferenciados para distintos roles (administradores, recepcionistas, etc.).
 
 2023 - 
