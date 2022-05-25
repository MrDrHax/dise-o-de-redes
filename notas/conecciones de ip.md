# Conectando un usuario a otro

## En un LAN

Cuando estas en un lan, necesitas 2 cosas, saber el ip del otro dispositivo, y saber que no puedes modificar del ip.

### IP

Esta es la direccion de tu computadora. Necesitas usarla junto a la mascara para poder identificarte dentro del LAN, y saber que puedes modificar para tener tu IP directa

### Mascara

Para poder ver que psuedes modificar de un IP, se usa una mascara. Esta mascara te permite saber que puedes y que no puedes editar del ip.

Visto como bits

|numero|bits|
|-|-|
|255.255.255.0|1111 1111 . 1111 1111 . 1111 1111 . 0000 0000|

Esto significa que los primeros 24 bits no pueden ser modificados, estos son la red, y los ultimos 8 bits son para identificar cada compu.

|numero|bits|
|-|-|
|255.255.255.128|1111 1111 . 1111 1111 . 1111 1111 . 1000 0000|

Esto significa que los primeros 25 bits no pueden ser modificados, estos son la red, y los ultimos 7 bits son para identificar cada compu.

## Saliendo afuera

### Ruta (route)

Es la direccion a la que te conectas para salir. Es la del router, te conectas a ella para decirle a donde es que quieres salir. Si tinees una ip que desconoces, usas un DNS.

Al conectarte a afuera pierdes control internamente de a donde vas, a menos que tengas una red de WANs.

### DNS

Cuando escribes algo como algo.example.com, tu app no sabe a donde es que tiene que ir. Para esto sirve un servicio de DNS, es una como libreria donde se preguta oye que es `algo.example.com` y regresa `0.0.0.0`.

