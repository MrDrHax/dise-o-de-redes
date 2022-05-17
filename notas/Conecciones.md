# Conecciones de computadora a compu

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