# Conecciones de computadora a compu

# Modo 3 capas

Es diseño LAN de 3 capas. Antes era 5, pero ya no.

## Nucleo

La madre donde sacas todo

> Se recomienda poner un switch multicapas (tambienc conocido como switch nivel 3)
> Tambien puedes usar un router

## Direccionamiento

El madre donde se va todo a donde tiene que llegar

> Puedes usar switch nivel 2

## Acceso

Tu pinshi compu

# Niveles

## Aplicacion (capa 7)

Esta es la que se programa. Nromalemente es la que interactua el programador final, y define su propia forma de mandar y organizar datos.

> Normalmente es desde se crea y madna la informacion, se programa

## Pesentacion (capa 6)

En esta capa se arreglan los datos para enviarlos por el internet.

> Sueles tambien programar esta parte, auqneu es mas normal que ya lo maneje tu framework

Un ejemplo es conversion de ASCCI a Unicode

## Sesion (capa 5)

Aunque ya casi no se usa, dado que capas de abajo se encargan de llevar esto a cabo, se encarga de porporcionar de forma continua la comunicacion entre el transporte y la aplicacion final. Basicamente, ayuda a que la coneccion siga hasta que la quieras apagar.

> sigue siendo al nivel de tu lo programas, pero diversos frameworks manejan esto

## Transporte (capa 4)

Es el inicio de tu programa al internet de afuera. Este processo hace varias cosas. Como parte de ellos, hace lo que sigue:

1. Fregmenta paquetes
    > Es importante que los paquetes que se envien no se manden mas grandes de lo que se puede enviar, el OS se encarga de separarlo en pequeños "paquetes" para que el internet siga feliz

1. Confirma mensajes

    > En caso de algunos mensajes, es fundamental que si hay un error, puedas enterarte, y que se intente mandar todo el mensaje completo. Para esto, el sitema operativo tiene checks entre la comunicacion.

1. Se encarga de recibir y enviar mensajes en orden

    > Es importante que se manden y reciban los paquetes lo mas rapido posible, y al mismo tiempo que se manden en todo lo que necesitas, esto incluye:
    > - si tienes varias apps abiertas, las administra
    > - si necesitas que tu app tenga varios clientes, los administra
    > - si se llena el buffer te avisa, para no perder informacion.
    > - recibe todos los paquetes para que esten disponibles cuando los necesites

1. Se encarga de mantener las sesiones vivas y llendo al lugar correcto

    > Si tienes una coneccion a google que necesitas constantemente, la mantiene como un app y ahorra tiempo en un futuro.

Como parte del OS, solo ve a donde tiene que llegar, no le importa el como. Eso se encarga abajo

> Se lleva a cabo en el nivel del sistema operativo

## Nivel de red (capa 3)

> Pimer paso fuera de la computadora

Para este nivel, se encarga de enviar todos los datos de un punto a otro, anormalmente no se sabe hasta donde tiene que llegar, pero el internet se encarga de crear los saltos necesarios para terminar encontrande lo mas rapido posible el servidor al que se necesita llegar.

Esto es parecido al juego de DHL, donde primero lo envian al centro de distribucion, luego ven a que cuidad tiene que ir (normalmente una cercana), luego se va a la cuidad destino, luego brinca a la ciudad destino, luego al lugar de distribucion local y por fin llega.
> Palabras clabe:
> - enrrutamiento
> - direccionamiento

## Enlace de datos (capa 2)

> El router es el primer nodo de esto

Es cada nodo de la red, cada equipo decide como enviarlo al que sigue, asegurandose que los paquetes cada vez lleguen mas cerca. 

Es como las señas de la esquina, donde te dicen que calles tiene y a donde van, te acercan, pero al fin y al cabo, le toca o otra seña llegar.

> Tambien lleva a cabo las siguientes:
> - Establece y finaliza vinculos
> - Controla trafico de trama
> - Sequencia trama
> - Verifica que haya llegado correctamente al siguiente trama
> - Delimita tramas
> - Administra acesso al trama

> Tambien maja el MAC adress

## Nivel fisico (capa 1)

Es el cable de cobre que conecta a con b (puede ser otra cosa aparte de cobre pero me entiendes)

> lit es fisico, puedes tocarlo y lo puedes joder

# Interconecciones de Dispositivos

## Crear y gestionar una red en sus primeras faces

### Cableado Estructurado

No mames no hagas cableado del asco

#### Estandares

Necesitas asegurarte que el cable que pases, siga lo que se llaman los "estandares", puedes meter 12 cables si quieres en un mini hollito, pero se dice que no puedes hacer eso, debes de poner max 40% de todo. 

EL cable UTP viene con varios estandares, dentro de ellos, son:

- cat 5e (max 1Gb)
- cat 6 
- cat 7
- cat 8 (overkill para lo de hoy)

En general, no hagas cosas de 90°

> La idea de los estandares, es que lo que compres sirva como lo que compras. Si hay perdidas, tienes muchos problemas. 

**Menos es mas!!!**

Siempre que puedas, intenta reducir la cantidad de cables que hay. Usar un estandar para todo es mejor, y te ayuda a ahorrar costos y tiempo cuando estructuras todo. 

## Entrada al edificio.

Imaginate que llega Telmex y te dice, donde te lo dejo? Bueno, necesitas ver por donde es que tiene que pasa el cable

## Cuarto de equipos

Es el cerebro de la red. Una vez que entras al edificio, necesitas ver donde pones el servidor, conmutador, switch, etc. Ayuda a mantener todo en orden y arreglar cosas facil.

## Cableado de backbone

Este cableado interconecta el cuarto de equipo con absolutamente todo, ya sean los AP, hasta cada entrada y puerto.

## Gabinete o rack de comunicaciones

Puedes separar cada area con un pequeño rack de comunicaciones, Este se conecta al cuarto de equipos, y proporciona de forma local una mejor comunicacion. 

## Cambiado horizontal

Es cuando ya pasas del backbone al area de trabajo. Suele ser por piso. 

Cuando sacas del switch, te conectas a:

- Un panel
> Cambia de un cable utp, al outlet que vamos a conectar
- Outlet
> La mierda donde conectas el cable para tu compu bonito (rj45) se le llama jack al conector (f) y el plug (m) 
- Entrada de pc
> Ira que bonito, ya llegamos UwU

## Poniendo orden y facilitando cosas despues

### Nomeclatura

Es buena idea tener planos, tags, y mas para poder administrar una red y darle administracion.

### Rebundancia

Cuando es importante tener algo, puedes crear sistemas de redundancia, o bien, sistemas paralelos que te permitan administrar, dar mantenimientos, e incluso tener perdidas sin terminar funcionamiento.

Para diseñar una red, necesitas preguntarte para que va a servir la red. Un ejemplo es cuantos celulares se van a conectar, cuantos refris, y la cantidad de compus.

# Diseño red lan

Para crear una red lan, necesitas pensar en cuantas personas van a acceder, y basado en eso, seguir una jerarquia.

## Capa de acesso

Es donde te conectas como *usuario*. Es donde normalmente se encuentra la capa inalambrica.

> Aqui se encuentran switches baratos y en general el wifi (o AP)

## Capa de distribuicion

En esta capa es donde se maneja todo relacionado con como se conecta todo el lan. Se encargan de llevar todo el backbone.

> Suele solo haber cables

## Capa del core

Puedes usar switches para poder manejar paquetes de forma sencilla, pero estos switches son mas caros.

> Aqui se encuentran los routers

## Puertos de router contra switch

Cada puerto de router tiene una red **differente** por lo que si quieres tener una red igual, necesitas switches. Los switches manejan **la misma red**.

> Nota: Por red se refiere a un LAN differente. Si quieres conectar 2 redes juntas, necesitas un switch y un protocolo para que se comuniquen.

# El formato http

Para poder conectarte a internet, se manda algo como:

```
GET (/index.html) HTTP/1.1

Host: www.example.com
Accept-Language: en
```

Donde:

`GET` > Comando a correr (puede ser GET, POST, DELETE, PUT o PATCH)

`(/index.html)` > La ruta a donde te quieres conectar

`HTTP/1.1` > El formato que se esta usando

`Host` > A donde se conecto el usuario

`Accept-Language` > El lenguaje que busca el usuario

## HTTPS vs HTTP

Cuando tienes un certificado ssl, puedes encriptar tu trafico en HTTPS. Lo que esto significa para nosotros es que mientras cualquier persona puede escuchar nuestras conversaciones, nadie mas que tu y el servidor al que te conectas puede desifrar lo que tienes.

Cuando usas HTTP solamente, se manda todo en formato de texto plano. Puedes conectarte a 