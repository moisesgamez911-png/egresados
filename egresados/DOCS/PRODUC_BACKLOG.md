|**PRODUCT BACKLOG - APLICATIVO WEB DE GESTIÓN DE EGRESADOS**|||
| - | :- | :- |
|*Centro Industrial y de Energías Alternativas – SENA Regional La Guajira*|||
||||
|**ID PBI**|**Módulo**|**Rol Principal**|
|PBI001|Administración y Seguridad|Administrador|
|PBI002|Administración y Seguridad|Administrador|
|PBI003|Administración y Seguridad|Administrador|
|PBI004|Gestión de Egresados|Funcionario|
|PBI005|Gestión de Egresados|Funcionario|
|PBI006|Gestión de Egresados|Funcionario|
|PBI007|Gestión de Egresados|Funcionario|
|PBI008|Gestión de Egresados|Funcionario|
|PBI009|Gestión de Egresados|Funcionario|
|PBI010|Gestión de Egresados|Funcionario|
|PBI011|Gestión de Egresados|Funcionario|
|PBI012|Información Laboral y Emprendimiento|Funcionario|
|PBI013|Información Laboral y Emprendimiento|Funcionario|
|PBI014|Información Laboral y Emprendimiento|Funcionario|
|PBI015|Información Laboral y Emprendimiento|Funcionario|
|PBI016|Portal Egresado|Egresado|
|PBI017|Portal Egresado|Egresado|
|PBI018|Información Laboral y Emprendimiento|Egresado|
|PBI019|Encuestas y Seguimiento|Egresado|
|PBI020|Encuestas y Seguimiento|Administrador|
|PBI021|Encuestas y Seguimiento|Funcionario|
|PBI022|Administración y Seguridad|Administrador|
|PBI023|Gestión de Egresados|Funcionario|
|PBI024|Alertas y Gestión de Campo|Funcionario|
|PBI025|Reportes y Analítica|Funcionario|
|PBI026|Reportes y Analítica|Visor (Coordinador Académico)|
|PBI027|Reportes y Analítica|Visor (Bienestar al Aprendiz)|
|PBI028|Administración y Seguridad|Administrador|
|PBI029|Administración y Seguridad|Administrador|
|PBI030|Administración y Seguridad|Administrador|
|PBI031|Alertas y Gestión de Campo|Funcionario|



||
| - |
||
||
|**Historia de Usuario**|
|Como Administrador, quiero parametrizar los catálogos del sistema, para que las opciones de registro, vinculación y encuestas correspondan a la operación del Centro.|
|Como Administrador, quiero gestionar usuarios y asignar roles funcionales, para que cada persona acceda únicamente a las funciones que le corresponden.|
|Como Administrador, quiero auditar los cambios realizados en el sistema, para conservar la trazabilidad de las acciones sobre egresados, estados y encuestas.|
|Como Funcionario, quiero registrar egresados a partir de una certificación válida, para asegurar que solo se incluya población realmente egresada de la formación titulada del Centro.|
|Como Funcionario, quiero que el número de documento de identidad sea único, para evitar egresados duplicados en el sistema.|
|Como Funcionario, quiero validar los campos obligatorios y la coherencia de fechas antes de validar un egresado, para asegurar que la información mínima esté completa y sea consistente.|
|Como Funcionario, quiero registrar la autorización de tratamiento de datos personales del egresado, para que su información pueda usarse en encuestas y reportes conforme a la normativa.|
|Como Funcionario, quiero vincular a un egresado con uno o más programas, fichas y cohortes, para reflejar correctamente su trayectoria de formación titulada en el Centro.|
|Como Funcionario, quiero gestionar los estados del egresado, para reflejar su situación real durante el seguimiento y conservar la trazabilidad de cada cambio.|
|Como Funcionario, quiero que el sistema marque automáticamente a los egresados desactualizados, para priorizar las acciones de actualización de información.|
|Como Funcionario, quiero gestionar el estado “Egresado no localizable”, para evitar enviar encuestas a egresados sin datos de contacto válidos.|
|Como Funcionario, quiero registrar la información laboral del egresado con los campos mínimos obligatorios, para medir su situación ocupacional de forma completa.|
|Como Funcionario, quiero registrar la información de emprendimiento del egresado, para caracterizar correctamente esta ruta de egreso.|
|Como Funcionario, quiero registrar la situación de desempleo del egresado, para identificar motivos y necesidades de acompañamiento.|
|Como Funcionario, quiero mantener el historial laboral del egresado, para conservar su trayectoria y distinguir la situación actual de las anteriores.|
|Como Egresado, quiero actualizar mis datos de contacto, para mantener informado al Centro y recibir las encuestas de seguimiento.|
|Como Egresado, quiero consultar mi propia información, para conocer los datos académicos y de seguimiento registrados por el Centro.|
|Como Egresado, quiero registrar o actualizar mi información laboral y de emprendimiento, para mantener actualizada mi situación ante el Centro.|
|Como Egresado, quiero responder las encuestas de seguimiento asignadas, para aportar la información necesaria para los indicadores del Centro.|
|Como Administrador, quiero que el sistema genere y asigne automáticamente las encuestas de seguimiento, para asegurar su aplicación en los momentos definidos.|
|Como Funcionario, quiero enviar encuestas a los egresados, para obtener información de seguimiento oportuna.|
|Como Administrador, quiero corregir programa, ficha o fecha de egreso con justificación, para resolver errores sin perder la trazabilidad del dato.|
|Como Funcionario, quiero validar los datos sociodemográficos del egresado, para asegurar que cumplan los rangos y catálogos institucionales.|
|Como Funcionario, quiero consultar y gestionar las alertas de desactualización, para priorizar el contacto con egresados que requieren actualización.|
|Como Funcionario, quiero generar reportes agregados y exportar datos operativos de mi centro, para apoyar el seguimiento sin acceder a información de toda la Regional.|
|Como Visor con perfil Coordinador Académico, quiero generar reportes nominales y agregados con filtros académicos, para analizar la pertinencia de la formación y apoyar la revisión curricular.|
|Como Visor con perfil Bienestar al Aprendiz, quiero generar reportes agregados con filtros poblacionales, para orientar acciones de bienestar y relacionamiento con los egresados.|
|Como Administrador, quiero restringir la generación de reportes nominales según el rol, para proteger la identificación de las personas en los reportes.|
|Como Administrador, quiero que el sistema aplique las restricciones funcionales por rol, para que cada usuario realice únicamente las acciones permitidas.|
|Como Administrador, quiero generar respaldos funcionales de la información, para conservar la operación y la trazabilidad del sistema.|
|Como Funcionario, quiero registrar las acciones de seguimiento telefónico o presencial, para dejar evidencia de la gestión realizada con cada egresado.|



||
| - |
||
||
|**Criterios de Aceptación**|
|1) Puede crear y editar programas del Centro con código y nombre, y solo estos quedan disponibles para vinculación\. 2) Puede crear y editar fichas con vigencia por cohorte, y el sistema las marca como disponibles o no disponibles\. 3) Puede parametrizar los estados del egresado y los momentos de encuesta: egreso, 6 meses, 1 año y momentos adicionales\. 4) Puede crear preguntas de encuesta y marcarlas como obligatorias u opcionales\. 5) Los cambios de catálogo se reflejan en nuevas operaciones sin borrar información histórica\.|
|1) Puede crear usuarios y asignar uno de los roles definidos: Administrador, Funcionario, Egresado o Visor\. 2) Puede asignar al Visor el perfil Coordinador Académico o Bienestar al Aprendiz\. 3) El sistema no permite asignar roles distintos a los definidos en la descripción funcional\. 4) El cambio de rol queda registrado con usuario y fecha\.|
|1) El sistema registra usuario, fecha y acción en cambios de estado, correcciones de datos y justificaciones\. 2) El Administrador puede consultar el log de cambios\. 3) El sistema no permite alterar los logs de auditoría\. 4) El sistema no permite modificar la fecha y hora de diligenciamiento de una encuesta ya enviada\.|
|1) El sistema rechaza el registro si no existe certificación válida y muestra el mensaje “No se encontró certificación válida para el documento [número]”\. 2) Permite registrar al egresado cuando existe acta de grado o registro válido en Sofía Plus\. 3) Asocia al registro el programa, la ficha y la fecha de certificación consultada\. 4) No permite registrar certificaciones de programas que no pertenecen al Centro\.|
|1) El número de documento de identidad es el identificador único del egresado\. 2) Al intentar crear un egresado con un documento existente, el sistema bloquea la operación y muestra “Ya existe un egresado con este documento”\. 3) Al actualizar datos, el sistema no permite cambiar el documento por uno ya registrado\. 4) La búsqueda por número de documento retorna un único egresado\.|
|1) El sistema no permite cambiar el estado a “Validado” si faltan nombres, apellidos, tipo y número de documento, programa de formación o ficha\. 2) Cuando faltan campos, el sistema lista los faltantes y mantiene el estado “Pendiente de validación”\. 3) El sistema rechaza una fecha de egreso anterior a la fecha de certificación y muestra “La fecha de egreso no puede ser anterior a la fecha de certificación”\. 4) El sistema acepta fechas de egreso iguales o posteriores a la fecha de certificación\.|
|1) Sin autorización, el egresado queda en estado “Pendiente de autorización”\. 2) Sin autorización, el sistema no permite enviar encuestas al egresado\. 3) Sin autorización, el egresado no se incluye en reportes nominales\. 4) Al registrar la autorización, el sistema guarda la fecha y habilita las operaciones permitidas según las reglas de negocio\.|
|1) El sistema permite una o más vinculaciones por egresado, cada una con ficha y cohorte independientes\. 2) Solo permite seleccionar fichas vigentes para la cohorte; si la ficha no está vigente, la muestra como “No disponible” y no permite guardar\. 3) Solo lista programas de la oferta del Centro Industrial y de Energías Alternativas\. 4) No permite dos vinculaciones activas simultáneas para el mismo programa y ficha; sugiere editar la vinculación existente\. 5) Crea la vinculación como “Activa” o “Histórica” según la fecha de egreso\.|
|1) El sistema maneja los estados: Pendiente de validación, Validado, En seguimiento, Desactualizado, Inactivo y Egresado no localizable\. 2) Cada cambio de estado registra fecha y usuario que lo realizó\. 3) El paso a “Validado” solo ocurre si se cumplen las reglas de campos obligatorios y autorización de datos\. 4) El estado “Inactivo” solo puede asignarlo un Funcionario o Administrador, con justificación obligatoria de máximo 200 caracteres\. 5) El sistema no elimina egresados ni registros históricos; solo permite inactivarlos\.|
|1) El sistema evalúa automáticamente si el egresado no ha actualizado información laboral, de contacto o de emprendimiento en los últimos 12 meses\. 2) Si no hay actualización en ese periodo, cambia el estado a “Desactualizado”\. 3) Al cambiar el estado, genera una alerta para el Funcionario\. 4) El cambio queda registrado con fecha y causa\.|
|1) El sistema permite asignar el estado “Egresado no localizable”\. 2) Al intentar enviar una encuesta a un egresado no localizable sin contacto válido, el sistema muestra “El egresado no tiene datos de contacto válidos” y no permite el envío\. 3) Si se actualiza al menos un dato de contacto válido, el sistema permite nuevas encuestas según las reglas del estado\. 4) El cambio de estado conserva trazabilidad de fecha y usuario\.|
|1) El sistema exige situación actual, empresa o negocio con nombre y sector, cargo o rol y fecha de inicio\. 2) Si falta alguno de estos campos, no permite guardar y resalta los faltantes\. 3) Rechaza una fecha de inicio anterior a la fecha de egreso del programa correspondiente y muestra “La fecha de inicio no puede ser anterior al egreso”\. 4) Permite las situaciones: empleado formal, informal, independiente, desempleado, emprendedor y estudiando\.|
|1) Al seleccionar la situación “Emprendedor”, el sistema habilita y exige nombre del emprendimiento, sector económico y etapa\. 2) La etapa solo permite las opciones idea, en marcha o consolidado\. 3) El sistema no guarda el registro si faltan los campos obligatorios de emprendimiento\. 4) El emprendimiento queda asociado al registro laboral actual del egresado\.|
|1) Al seleccionar “Desempleado”, el sistema exige el motivo principal de una lista predefinida\. 2) El sistema permite registrar la fecha del último empleo cuando aplique\. 3) No permite guardar si falta el motivo principal\. 4) Los motivos disponibles incluyen falta de oportunidades, continuidad de estudios, motivos personales y otro\.|
|1) El sistema permite múltiples registros laborales para un egresado\. 2) Solo un registro puede estar marcado como “Actual”\. 3) Al guardar un nuevo registro laboral, el anterior se marca automáticamente como “Histórico”\. 4) El Funcionario puede consultar el historial laboral del egresado\.|
|1) El egresado solo puede actualizar sus propios datos de contacto\. 2) El sistema valida que el correo contenga “@” y dominio, y que el teléfono tenga al menos 7 dígitos\. 3) Si el formato es inválido, rechaza el guardado y muestra el mensaje de error correspondiente\. 4) Al guardar datos válidos, la información se refleja en la consulta del egresado\.|
|1) El egresado accede exclusivamente a sus propios datos personales, académicos y de seguimiento\. 2) No puede ver información de otros egresados\. 3) No accede a módulos de administración ni a reportes\. 4) No puede cambiar su estado, programa, ficha ni fecha de egreso\.|
|1) El egresado puede registrar y actualizar únicamente su propia información laboral o de emprendimiento\. 2) El sistema aplica las reglas de campos obligatorios, fecha de inicio no anterior al egreso, emprendimiento y desempleo\. 3) El egresado no puede modificar programa, ficha ni fecha de egreso\. 4) El egresado no puede cambiar su estado en el sistema\.|
|1) El egresado solo ve las encuestas pendientes asignadas a su propia vinculación\. 2) Solo puede responder una vez cada encuesta de un mismo momento por vinculación; si intenta repetirla, el sistema bloquea el acceso y muestra “Ya respondió esta encuesta”\. 3) No permite enviar la encuesta si faltan preguntas obligatorias\. 4) Registra fecha, hora y canal de diligenciamiento: web (escritorio/dispositivo móvil) o presencial asistido\. 5) La encuesta de 6 meses solo está disponible si el estado es “Validado” o “En seguimiento”\.|
|1) El sistema genera encuestas al egreso, a los 6 meses y al año de la fecha de egreso\. 2) Las encuestas pendientes quedan asignadas al egresado\. 3) El sistema usa los momentos parametrizados, incluidos momentos adicionales definidos por el Administrador\. 4) No genera duplicados de una misma encuesta para el mismo momento y vinculación\.|
|1) El sistema permite enviar encuestas a egresados con contacto válido y estado permitido\. 2) Bloquea el envío a egresados no localizables sin datos de contacto válidos\. 3) No permite enviar una encuesta de un momento ya respondido por el egresado\. 4) Registra el envío realizado para consulta y trazabilidad\.|
|1) Solo el Administrador puede corregir programa, ficha o fecha de egreso de una vinculación validada\. 2) El egresado y el Funcionario tienen bloqueada la edición de estos campos\. 3) El sistema exige justificación antes de guardar la corrección\. 4) La corrección queda registrada con usuario, fecha y justificación\.|
|1) El sistema acepta edades entre 14 y 99 años y rechaza fechas de nacimiento que produzcan edades fuera de ese rango\. 2) El estrato socioeconómico solo permite valores de 1 a 6\. 3) Los datos de población vulnerable son opcionales y, si se registran, se seleccionan de listas predefinidas\. 4) El sistema no permite texto libre para población vulnerable\.|
|1) El Funcionario consulta las alertas de egresados en estado “Desactualizado” de su centro\. 2) Cada alerta muestra el egresado y la fecha del cambio de estado\. 3) El Funcionario no puede ver alertas de otros centros\. 4) Desde la alerta puede iniciar la actualización de la información del egresado\.|
|1) El Funcionario genera reportes agregados de los egresados de su centro\. 2) Puede exportar datos operativos únicamente de su centro\. 3) No puede ver reportes nominales de toda la Regional\. 4) No accede a configuraciones del sistema ni a logs de auditoría\.|
|1) Puede generar y exportar reportes nominales y agregados de los egresados del Centro\. 2) Puede filtrar por programa, ficha, cohorte, sector económico y situación laboral\. 3) Puede consultar el detalle de un egresado en modo solo lectura\. 4) No puede crear, editar ni eliminar egresados, enviar encuestas, cambiar estados ni modificar parámetros del sistema\.|
|1) Puede generar y exportar únicamente reportes agregados\. 2) Puede filtrar por programa, cohorte, municipio y grupo poblacional\. 3) No accede a datos nominales ni a información individual de egresados\. 4) Los filtros disponibles no permiten inferir identidades individuales\. 5) No puede crear, editar ni eliminar registros, enviar encuestas, cambiar estados ni modificar parámetros\.|
|1) Solo el Administrador y el Visor con perfil Coordinador Académico pueden generar reportes nominales\. 2) El Visor con perfil Bienestar al Aprendiz solo accede a reportes agregados\. 3) El sistema filtra las columnas de identificación según el rol del usuario\. 4) Si un rol no autorizado solicita un reporte nominal, el sistema no muestra datos personales\.|
|1) El Administrador accede a configuración, usuarios, catálogos y auditoría, con las restricciones de trazabilidad definidas\. 2) El Funcionario opera únicamente sobre egresados y encuestas de su centro\. 3) El Egresado accede únicamente a sus propios datos y encuestas\. 4) El Visor con perfil Coordinador Académico tiene lectura amplia, incluidos reportes nominales\. 5) El Visor con perfil Bienestar al Aprendiz solo accede a reportes agregados\. 6) Ningún rol definido puede ejecutar acciones por fuera de la matriz de permisos\.|
|1) El Administrador puede generar un respaldo funcional de egresados, vinculaciones y catálogos\. 2) El respaldo registra fecha y usuario que lo generó\. 3) La generación del respaldo no altera los datos del sistema\. 4) El respaldo no permite modificar logs de auditoría ni fechas de diligenciamiento de encuestas\.|
|1) El Funcionario puede registrar una acción de seguimiento asociada a un egresado\. 2) La acción registra fecha, medio de contacto y resultado de la gestión\. 3) El historial de seguimiento queda disponible para consulta del Funcionario\. 4) El registro de seguimiento no modifica las respuestas de encuestas ya enviadas\.|


|**RESUMEN Y MÉTRICAS DEL PRODUCT BACKLOG**|||
| - | - | :- |
|*Centro Industrial y de Energías Alternativas – SENA Regional La Guajira*|||
||||
|**Módulo del Sistema**|**Cantidad de PBIs**|**Porcentaje del Backlog**|
|Administración y Seguridad|7|22\.6%|
|Gestión de Egresados|9|29\.0%|
|Información Laboral y Emprendimiento|5|16\.1%|
|Portal Egresado|2|6\.5%|
|Encuestas y Seguimiento|3|9\.7%|
|Alertas y Gestión de Campo|2|6\.5%|
|Reportes y Analítica|3|9\.7%|
|**Total General**|**31**|**100.0%**|

