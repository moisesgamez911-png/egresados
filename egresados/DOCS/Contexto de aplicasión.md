**Descripción funcional del software web para el seguimiento a egresados de la formación titulada Centro Industrial y de Energías Alternativas – SENA Regional La Guajira** 

# **1. Contexto** 

# **1.1. Rol del SENA y del Centro en la formación titulada** 

El Servicio Nacional de Aprendizaje (SENA) tiene a su cargo la formación profesional integral, con énfasis en la formación titulada (programas técnicos y tecnológicos). El Centro Industrial y de Energías Alternativas, con sedes en Riohacha y Maicao, ofrece programas alineados con la vocación productiva del departamento: **Tecnología en Análisis y Desarrollo de Software** , **Tecnología en Mantenimiento Electromecánico Industrial** , **Técnico en Mantenimiento e Instalación de Sistemas Solares Fotovoltaicos** , **Profundización Técnica en Montaje y Mantenimiento de Sistemas Solares Fotovoltaicos** y **Mantenimiento de Sistemas de Generación Eólica** , entre otros. Estos programas responden al potencial eólico y solar de La Guajira, la región con mayor potencial de energías renovables del país, así como a los sectores industrial, eléctrico y de software. 

# **1.2. Importancia del seguimiento a egresados** 

El seguimiento a egresados es un proceso estratégico para el SENA porque permite medir la **empleabilidad formal** , la **pertinencia de la formación** , el **emprendimiento** y la **vinculación con el sector productivo** . Los lineamientos institucionales (Resolución 1-5224 de 2020) exigen realizar seguimiento trimestral a egresados de formación titulada para determinar su nivel de empleabilidad y la relación entre las actividades desempeñadas y lo aprendido en el SENA. La Política de Egresados (Resolución 1229 de 2018) busca “promover un vínculo constante y directo entre la entidad y sus egresados, que conlleve al fortalecimiento ocupacional” mediante servicios institucionales. Los indicadores de **vinculación laboral formal** (por ejemplo, la meta nacional del 60 % de egresados vinculados) y las tasas reportadas (57,3 % al semestre siguiente y 65,98 % al primer año) son insumos clave para la rendición de cuentas y la toma de decisiones sobre la oferta formativa. 

# **1.3. Particularidades regionales y sectoriales** 

La Guajira presenta una **alta demanda de talento humano en energías renovables** (eólica y solar), pero también una **limitada presencia empresarial** y pocas oportunidades de empleo formal para los jóvenes. El Centro Industrial y de Energías Alternativas es la única entidad que forma talento en energías renovables en el departamento, y su laboratorio 

eólico (primero del país) beneficiará a más de 25 000 personas, incluyendo técnicos y tecnólogos. Además, el centro atiende a población indígena Wayúu y a municipios con condiciones de infraestructura limitada, lo que exige un sistema de seguimiento que reconozca **trayectorias diversas** (empleo formal, emprendimiento, continuidad educativa, actividades tradicionales) y que sea **accesible en conectividad intermitente** . La región también depende de sectores como turismo, agroindustria y servicios, por lo que el seguimiento debe cubrir **múltiples rutas de egreso** . 

# **1.4. Problema que resuelve el software** 

Actualmente, el seguimiento a egresados se realiza mediante **encuestas aisladas, hojas de cálculo y reportes manuales** , lo que genera: 

- **Dispersión y desactualización** de la información de contacto y laboral. 

- **Dificultad para consolidar indicadores** de empleabilidad, emprendimiento y pertinencia por programa, ficha y cohorte. 

- **Baja trazabilidad** de las acciones de orientación y acompañamiento. 

- **Poca participación del egresado** en la actualización de sus datos. 

El software web resuelve estos problemas al centralizar el registro de egresados, automatizar la aplicación de encuestas de seguimiento, permitir la actualización de la información por parte del propio egresado y generar **reportes e indicadores en tiempo real** para la toma de decisiones del Centro y de la Regional. 

# **1.5. Alcance funcional general** 

El sistema cubrirá los siguientes procesos: 

- **Registro y validación de egresados** a partir de la información de certificación (Sofía Plus / actas). 

- **Vinculación del egresado** con el programa de formación, la ficha y la cohorte correspondiente. 

- **Gestión de estados del egresado** (por validar, activo, en seguimiento, desactualizado, etc.). 

- **Captura y actualización de información laboral y de emprendimiento** (empleo formal, informal, independiente, emprendimiento propio, continuidad educativa). 

- **Aplicación de encuestas de seguimiento** en momentos definidos (al egreso, a los 6 meses, al año) y registro de respuestas. 

- **Generación de reportes e indicadores** de empleabilidad, emprendimiento, pertinencia y caracterización de la población egresada. 

- **Administración de usuarios y roles** , parametrización de catálogos y gestión de la seguridad funcional. 

**Queda fuera del alcance** : el diseño de base de datos, la arquitectura técnica, la selección de tecnologías de implementación y la integración transaccional con sistemas externos (Sofía Plus, PILA, etc.); el sistema podrá consumir datos de estas fuentes mediante mecanismos de intercambio definidos en la fase técnica. 

# **2. Reglas de negocio** 

Las reglas se expresan de forma **verificable** e indican **cuándo aplican** y **qué resultado producen** . Se agrupan por dominio funcional. 

# **2.1. Registro y validación de egresados** 

|ID|Regla|Condición /<br>Disparador|Resultado|
|---|---|---|---|
||Un egresado solo puede ser<br>registrado si existe una<br>**ii**||El sistema rechaza el|
|**RN-**<br>**01**|**certificación válida**de un<br>programa de formación<br>titulada del Centro (acta de<br>grado o registro en Sofía<br>Plus).|Al intentar<br>crear un<br>egresado.|registro y muestra el<br>mensaje “No se encontró<br>certificación válida para el<br>documento [número]”.|
|**RN-**<br>**02**|El**número de documento**<br>**de identidad**es el<br>identificador único del<br>egresado en el sistema.|Al crear o<br>actualizar un<br>egresado.|El sistema impide<br>duplicados y muestra “Ya<br>existe un egresado con este<br>documento”.|
|**RN-**<br>**03**|Los campos**nombres,**<br>**apellidos, tipo y número de**<br>**documento, programa de**<br>**formación y ficha**son|Al intentar<br>cambiar el<br>estado a|El sistema no permite el<br>cambio y lista los campos<br>faltantes.|



|ID|Regla|Condición /<br>Disparador|Resultado|
|---|---|---|---|
||**obligatorios**para que un<br>egresado pase al estado<br>“Validado”.|“Validado”.||
|**RN-**<br>**04**|La**fecha de egreso**debe ser<br>igual o posterior a la fecha<br>de certificación registrada<br>en el acta.|Al registrar o<br>editar la fecha<br>de egreso.|El sistema rechaza fechas<br>inconsistentes y muestra<br>“La fecha de egreso no<br>puede ser anterior a la<br>fecha de certificación”.|
|**RN-**<br>**05**|El egresado debe**autorizar**<br>**el tratamiento de sus datos**<br>**personales**(Ley 1581 de<br>2012) para que su<br>información pueda ser<br>usada en encuestas y<br>reportes.|Al crear el<br>registro o al<br>primer inicio<br>de sesión.|Sin autorización, el<br>egresado queda en estado<br>“Pendiente de autorización”<br>y no se le pueden enviar<br>encuestas ni incluir en<br>reportes nominales.|



# **2.2. Vinculación a programas y fichas de formación** 

Condición / ID Regla Resultado Disparador Un egresado puede estar vinculado a **uno o más programas** El sistema crea una Al asociar un **vinculación** con de formación titulada (por **RN-** ejemplo, técnico y luego programa al estado “Activa” o **06** tecnólogo), pero cada vinculación egresado. “Histórica” según la debe tener **ficha y cohorte** fecha de egreso. independientes. La **ficha** debe existir en el catálogo Si la ficha no está **RN-** Al seleccionar de fichas del Centro y debe estar vigente, el sistema la 

|ID|Regla|Condición /<br>Disparador|Resultado|
|---|---|---|---|
|**07**|**vigente**para la cohorte<br>correspondiente.|la ficha.|muestra como “No<br>disponible” y no<br>permite guardar la<br>vinculación.|
|**RN-**<br>**08**|El**programa de formación**debe<br>pertenecer a la oferta del Centro<br>Industrial y de Energías<br>Alternativas (código y nombre<br>registrados).|Al crear la<br>vinculación.|El sistema solo lista<br>los programas del<br>Centro; no permite<br>seleccionar<br>programas de otros<br>centros.|
|**RN-**<br>**09**|Un egresado no puede tener**dos**<br>**vinculaciones activas simultáneas**<br>para el mismo programa y ficha.|Al intentar<br>crear una<br>segunda<br>vinculación<br>activa.|El sistema bloquea la<br>operación y sugiere<br>editar la vinculación<br>existente.|
|**2.3. E**|**stados del egresado**|||
|ID|Regla|Condición /<br>Disparador|Resultado|
|**RN-**<br>**10**|Los estados posibles del egresado<br>son:**Pendiente de validación,**<br>**Validado, En seguimiento,**<br>**Desactualizado, Inactivo (fallecido**<br>**o por solicitud) y Egresado no**<br>**localizable**.|Cambio de<br>estado manual<br>o automático.|El sistema registra la<br>fecha y el usuario<br>que realizó el<br>cambio.|
|**RN-**<br>**11**|El paso de**Pendiente de validación**<br>a**Validado**requiere que se|Al intentar<br>validar.|Si no se cumplen, el<br>estado permanece<br>en “Pendiente de|



|ID|Regla|Condición /<br>Disparador|Resultado|
|---|---|---|---|
||cumplan las reglas RN-03 y RN-05.||validación”.|
|**RN-**<br>**12**|Un egresado pasa a<br>**Desactualizado**si no ha<br>actualizado su información<br>(laboral, de contacto o de<br>emprendimiento) en los**últimos**<br>**12 meses**.|Evaluación<br>automática<br>nocturna.|El sistema cambia el<br>estado y genera una<br>alerta para el<br>funcionario.|
||Un egresado en estado**Egresado**||El sistema muestra|
||**no localizable**no puede recibir|Al intentar|“El egresado no tiene|
|**RN-**<br>**13**|nuevas encuestas hasta que se<br>actualice al menos un dato de<br>contacto válido.|enviar una<br>encuesta.|datos de contacto<br>válidos” y no permite<br>el envío.|
||El estado**Inactivo**solo puede ser||El sistema exige el|
|**RN-**<br>**14**|asignado por un**Funcionario**o<br>**Administrador**, con**justificación**<br>**obligatoria**(máximo 200<br>caracteres).|Al cambiar a<br>“Inactivo”.|campo de<br>justificación y<br>registra la<br>trazabilidad.|
|**2.4. C**|**aptura y actualización de información**|**laboral y de empren**|**dimiento**|
|ID|Regla|Condición /<br>Disparador|Resultado|
||La información laboral debe<br>registrar al menos:**situación**||Si falta alguno de estos|
|**RN-**|**actual**(empleado formal,|Al guardar el|<br>campos, el sistema no|
|**15**|informal, independiente,<br>desempleado, emprendedor,<br>estudiando),**empresa o**<br>**negocio**(nombre y sector),|registro laboral.|permite guardar y<br>resalta los faltantes.|



|ID|Regla|Condición /<br>Disparador|Resultado|
|---|---|---|---|
||**cargo o rol**y**fecha de inicio**.|||
||Si la situación es|||
||**“Emprendedor”**, es obligatorio||El sistema habilita los|
|**RN-**|registrar**nombre del**|Al seleccionar|campos adicionales y|
|**16**|**emprendimiento, sector**<br>**económico y etapa**(idea, en<br>marcha, consolidado).|“Emprendedor”.|los marca como<br>obligatorios.|
||La**fecha de inicio**de la||El sistema rechaza la|
|**RN-**<br>**17**|actividad laboral o de<br>emprendimiento no puede ser<br>anterior a la**fecha de egreso**<br>del programa correspondiente.|Al validar la<br>fecha.|fecha y muestra “La<br>fecha de inicio no<br>puede ser anterior al<br>egreso”.|
|**RN-**<br>**18**|Si el egresado está<br>**desempleado**, debe registrarse<br>la**fecha de último empleo**(si<br>aplica) y el**motivo principal**<br>(opciones predefinidas: falta<br>de oportunidades, continuidad<br>de estudios, motivos<br>personales, otro).|Al seleccionar<br>“Desempleado”.|El sistema exige estos<br>campos antes de<br>guardar.|
||Un egresado puede tener||El sistema marca|
|**RN-**<br>|**múltiples registros laborales**a<br>lo largo del tiempo; solo**uno**|Al guardar un<br>nuevo registro|automáticamente el<br>registro anterior como|
|**19**|i<br>puede estar marcado como<br>**“Actual”**.|laboral.|“Histórico” y el nuevo<br>como “Actual”.|
|**2.5. G**|**eneración de encuestas y registros d**|**e seguimiento**||



|ID|Regla|Condición /<br>Disparador|Resultado|
|---|---|---|---|
|**RN-**<br>**20**|Las encuestas de<br>seguimiento se aplican en<br>**tres momentos**: al egreso<br>(encuesta de<br>caracterización), a los**6**<br>**meses**y al**año**de la fecha de<br>egreso.|Cálculo<br>automático de<br>fechas.|El sistema genera las<br>encuestas pendientes y<br>las asigna al egresado.|
||Un egresado solo puede|||
||responder**una vez**cada|Al intentar|El sistema bloea el|
|**RN-**<br>**21**|encuesta de un mismo<br>momento (por ejemplo, una<br>sola encuesta de 6 meses por<br>vinculación).|responder una<br>encuesta ya<br>completada.|qu<br>acceso y muestra “Ya<br>respondió esta encuesta”.|
||La encuesta de**6 meses**solo||Si el estado es “Pendiente<br>”|
|**RN-**|está disponible si el egresado|Al habilitar la|de validación o<br>“lid” l|
|**22**|se encuentra en estado<br>**Validado**o**En seguimiento**.|encuesta.|Desactuazao, a<br>encuesta aparece como<br>“No disponible”.|
||Las respuestas a las<br>encuestas son**obligatorias**||El sistema no permite el|
|**RN-**|para todas las preguntas|Al enviar la|envío hasta que se|
|**23**|marcadas como<br>“obligatorias” en el<br>formulario.|encuesta.|respondan todas las<br>preguntas obligatorias.|
|**RN-**|El sistema debe registrar la<br>**fecha y hora de**|Al guardar una|La información queda<br>disponible para auditoría|
|**24**|**diligenciamiento**de cada<br>encuesta, así como el**canal**|respuesta.|<br>y reportes.|



Condición / ID Regla Resultado Disparador (web, móvil, presencial asistido). 

# **2.6. Condiciones de validez, obligatoriedad y restricción de datos** 

|ID|Regla|Condición /<br>Disparador|Resultado|
|---|---|---|---|
|**RN-**|Los**datos de contacto**(correo<br>electrónico y teléfono) deben<br>cumplir con formato válido: el|Al guardar datos|El sistema rechaza<br>formatos inválidos y|
|**25**|correo debe contener “@” y<br>dominio; el teléfono debe<br>tener al menos 7 dígitos.|de contacto.|muestra el mensaje de<br>error correspondiente.|
|**RN-**<br>**26**|La**edad**del egresado debe<br>estar entre**14 y 99 años**(rango<br>institucional).|Al registrar o<br>actualizar la<br>fecha de<br>nacimiento.|El sistema rechaza<br>fechas que produzcan<br>edades fuera de ese<br>rango.|
||El**estrato socioeconómico**solo||El sistema solo|
|**RN-**|puede tomar valores de**1 a 6**|Al seleccionar el|muestra las opciones|
|**27**|(según recibo de servicios<br>públicos).|estrato.|válidas y no permite<br>otros valores.|
|**RN-**<br>**28**|Los datos de**población**<br>**vulnerable**(indígena,<br>afrodescendiente, víctima del<br>conflicto, persona con<br>discapacidad, campesino) son<br>**opcionales**, pero si se registran<br>deben seleccionarse de las|Al marcar una<br>casilla de<br>vulnerabilidad.|El sistema habilita la<br>lista correspondiente y<br>no permite texto libre.|



Condición / Resultado Disparador 

|ID|Regla|<br>Disparador|Resultado|
|---|---|---|---|
||listas predefinidas.|||
||Un egresado**no puede**<br>**modificar**su**programa de**||El sistema bloquea la|
||**formación, ficha o fecha de**||edición para el|
|**RN-**|**egreso**una vez que la|Al intentar editar|egresado y el|
|**29**|vinculación está en estado<br>“Validada”; solo un<br>**Administrador**puede hacer<br>correcciones con justificación.|estos campos.|funcionario; solo el<br>administrador ve la<br>opción “Corregir”.|
||Los reportes nominales (con<br>identificación de personas) solo<br>pueden ser generados por||El sistema filtra las|
|**RN-**|usuarios con rol**Visor –**|Al solicitar un|columnas de|
|**30**|**Coordinador Académico**o<br>**Administrador**; el**Visor –**<br>**Bienestar al Aprendiz**solo|reporte.|identificación según el<br>rol.|
||accede a reportes agregados.|||



# **3. Roles y permisos** 

|**3.1. Descripción gene**|**ral de roles**||
|---|---|---|
|Rol|Propósito|Nivel de acceso|
|**Administrador**|Configurar el sistema, gestionar usuarios,<br>parametrizar catálogos y supervisar la operación.|Total (con restricciones<br>auditoría).|
|**Funcionario**|Registrar, actualizar y hacer seguimiento operativo a<br>los egresados.|Operativo sobre egresad<br>encuestas.|



|Rol|Propósito||Nivel de acceso|
|---|---|---|---|
|**Egresado**|Consultar y actualizar su propia infor<br>responder encuestas.|mación,|Solo sus propios datos.|
|**Visor – Coordinador**<br>**Académico**|Consultar información y reportes par<br>decisiones académicas.|a la toma de|Lectura amplia, incluyen<br>reportes nominales.|
|**Visor – Bienestar al**<br>**Aprendiz**<br>**3.2. Matriz de permisos  i**|Consultar información agregada para<br>bienestar y relacionamiento con egre<br>**(acciones permitidas / prohibidas)**|acciones de<br>sados.|Lectura de reportes agre<br>sin datos nominales.|
|Acción<br>Admin<br>dor|istra<br>Funcionario<br>Egresa<br>do|Visor –<br>Coord.<br>Académ<br>ico|Visor –<br>Bienes<br>tar|
|Crear<br>usuarios y<br>asignar roles||||
|Parametrizar<br>catálogos<br>(programas,<br>fichas,<br>estados,<br>preguntas<br>de encuesta)||||
|Registrar<br>egresado||||
|Validar<br>egresado||||



|Acción|Administra<br>dor|Funcionario|Egresa<br>do|Visor –<br>Coord.<br>Académ<br>ico|Visor –<br>Bienes<br>tar|
|---|---|---|---|---|---|
|(cambiar a<br>“Validado”)||||||
|Editar datos||||||
|de un||✅(excepto<br>i||||
|egresado||programa/ficha/||||
|(cualquier<br>campo)||fecha de egreso)||||
|Corregir<br>programa,<br>ficha o fecha<br>de egreso|✅(con<br>justificació<br>n)|||||
|Cambiar<br>estado a<br>“Inactivo”||✅(con<br>justificación)||||
|Registrar<br>información<br>laboral /<br>emprendimi<br>ento|||✅(solo<br>la<br>propia<br>)|||
|Enviar<br>encuestas a<br>egresados||||||
|Responder|||✅(solo<br>las|||



|Acción|Administra<br>dor|Funcionario|Egresa<br>do|Visor –<br>Coord.<br>Académ<br>ico|Visor –<br>Bienes<br>tar|
|---|---|---|---|---|---|
|encuestas|||propia<br>s)|||
|Ver reportes<br>agregados<br>(sin datos<br>personales)||||||
|Ver reportes<br>nominales<br>(con<br>identificació<br>n)||✅(solo datos<br>operativos)||||
|Exportar<br>datos||✅(solo de su<br>centro)||✅(solo<br>lectura)|✅(solo<br>agregado<br>s)|
|Auditar||||||
|cambios (log||||||
|de acciones)||||||



# **3.3. Funciones y restricciones por rol** 

# **Administrador** 

- **Funciones principales** : configurar parámetros del sistema (catálogo de programas, fichas, estados, preguntas de encuesta), crear y gestionar usuarios, asignar roles, supervisar la calidad de los datos, generar respaldos funcionales y auditar la trazabilidad de los cambios. 

- **Información a la que accede** : toda la información del sistema, incluyendo logs de auditoría y configuraciones. 

- **Acciones permitidas** : todas las de la matriz, con la obligación de registrar **justificación** en correcciones de datos sensibles (RN-29) y en cambios a estado “Inactivo” (RN-14). 

- **Acciones prohibidas** : **eliminar** egresados o registros históricos (solo se permite inactivar); modificar la **fecha de diligenciamiento** de una encuesta ya enviada; alterar los logs de auditoría. 

# **Funcionario** 

- **Funciones principales** : registrar egresados a partir de la certificación, validar su información, actualizar datos de contacto y laborales, realizar seguimiento telefónico o presencial, enviar encuestas y gestionar las alertas de desactualización. 

- **Información a la que accede** : datos de los egresados del Centro Industrial y de Energías Alternativas; reportes operativos de su centro; **no** accede a configuraciones del sistema ni a logs de auditoría. 

- **Acciones permitidas** : crear, editar y validar egresados; cambiar estados (excepto “Inactivo” sin justificación); registrar información laboral y de emprendimiento; enviar encuestas; generar reportes agregados y exportar datos operativos de su centro. 

- **Acciones prohibidas** : modificar programa, ficha o fecha de egreso una vez validados (RN-29); crear usuarios o roles; acceder a información de otros centros; ver reportes nominales de toda la regional (solo de su centro y con fines operativos). 

# **Egresado** 

- **Funciones principales** : consultar su propia información, actualizar datos de contacto, registrar o actualizar su situación laboral o de emprendimiento, y responder las encuestas de seguimiento en los momentos definidos. 

- **Información a la que accede** : exclusivamente sus propios datos personales, académicos y de seguimiento. **No** accede a información de otros egresados ni a reportes agregados. 

- **Acciones permitidas** : iniciar sesión, ver y editar sus datos de contacto, registrar/actualizar información laboral o de emprendimiento (respetando RN-15 a 

RN-19), responder encuestas pendientes (RN-20 a RN-24) y descargar su propio certificado de egreso (si el sistema lo integra). 

- **Acciones prohibidas** : modificar su programa, ficha o fecha de egreso (RN-29); cambiar su estado; acceder a módulos de administración o de reportes; responder una encuesta más de una vez (RN-21). 

# **Visor – Coordinador Académico** 

- **Funciones principales** : consultar indicadores de empleabilidad, pertinencia y emprendimiento por programa, ficha y cohorte; analizar la relación entre la formación y las ocupaciones de los egresados; generar insumos para la revisión curricular y la toma de decisiones académicas. 

- **Información a la que accede** : reportes **nominales** y agregados de los egresados del Centro; datos de caracterización y de trayectoria laboral; **no** accede a configuraciones ni a logs de auditoría. 

- **Acciones permitidas** : generar y exportar reportes nominales y agregados; filtrar por programa, ficha, cohorte, sector económico y situación laboral; consultar el detalle de un egresado (solo lectura). 

- **Acciones prohibidas** : crear, editar o eliminar egresados; enviar encuestas; cambiar estados; modificar parámetros del sistema. 

# **Visor – Bienestar al Aprendiz** 

- **Funciones principales** : consultar información **agregada** sobre la situación de los egresados (tasas de empleabilidad, emprendimiento, continuidad educativa, distribución por municipio y población vulnerable) para orientar acciones de bienestar y relacionamiento con el egresado. 

- **Información a la que accede** : exclusivamente **reportes agregados** (sin identificación de personas) y datos de caracterización agrupados. **No** accede a datos nominales ni a información individual de egresados. 

- **Acciones permitidas** : generar y exportar reportes agregados; filtrar por programa, cohorte, municipio y grupo poblacional (siempre que el filtro no permita inferir identidades individuales). 

- **Acciones prohibidas** : ver datos personales de egresados; crear, editar o eliminar registros; enviar encuestas; modificar parámetros; acceder a reportes nominales. 

# **Supuestos explícitos** 

1. **Integración con Sofía Plus** : se asume que el sistema podrá **consumir** la información de certificación (programa, ficha, fecha de egreso) mediante un servicio de intercambio definido en la fase técnica; la validación de la certificación (RN-01) se realizará contra esa fuente. 

2. **Conectividad** : se asume que el sistema operará en un entorno web con conectividad intermitente en algunos municipios; las funcionalidades de registro y encuestas deben tolerar modos de operación offline‑first o sincronización posterior.

3. **Marco normativo** : se toman como referencia la Resolución 1‑5224 de 2020 (lineamientos de seguimiento a egresados), la Resolución 1229 de 2018 (Programa de Egresados) y la Ley 1581 de 2012 (protección de datos personales). 

4. **Alcance del Centro** : el sistema gestiona únicamente los egresados del **Centro Industrial y de Energías Alternativas** de la Regional La Guajira; no cubre otros centros de la regional. 

5. **Periodicidad de las encuestas** : se definen tres momentos (egreso, 6 meses y 1 año) con base en los lineamientos institucionales de seguimiento a la empleabilidad; el Administrador podrá parametrizar momentos adicionales. 

Este documento constituye la **descripción funcional** del software y sirve como insumo para la fase de diseño técnico y de implementación. Las reglas y roles aquí definidos son **verificables** y deberán reflejarse en los criterios de aceptación de las historias de usuario. 

