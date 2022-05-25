# Conectandose

Este duplica que es lo que se hace en tanto 

# Tipos de configuracion

## AUX

Te permite configurar el router/switch desde afuera (como por un modem o marcando)

## Consola 

Es el cable fisico detras de la madre. Necesitas conectar desde tu compu al otro lado.

# Inicio

## `en`

> enable para poder mandar comandos

## `show start`

> ver la configuracion

## `erase start`

> borra toda la configuracion

## `config t`

> modo configuracion

## `no ip domain lookup`

> No busca cosas si te equivocas en el comando

## `line con 0`

> Abre prueto de consola

## `logging synchronous`

> Que no corte la comunicacion en el texto, hace que puedas seguir escribiendo si te manda algo la consola. Nota: requiere estan en consola con `line con 0`

## `interface (gigabit/fast)Ethernet 0/0` (solo router)

### `int (g/f)0/0` (chico)

> Tienes que entrar desde `config t`. Sirve para configurar el puerto de salida con el switch. Tienes que checar que dice la parte de atras de tu router. Porque tambien teines que checar el numero en el que estas

## `ip adress <ip del router> <mascara>`

> Para poder configurar la IP a la que va a llamar las compus, (para tener una red ip, llamas esta funcion desde la interfaz)

## `no shut`

> Prende la interfaz en la que estas. requiere int

## `exit`

> sal de la config actual y regresa uno

## `ip dhcp pool <nombre>`

> Sirve para nombrar el pool de IPs que esestes buecando. 

    > Nombre se refiere a lo que buscas


## `network <ip.0> <mascara>`

> Le estamos diciendo cuales van a ser las posibles direcciones de la red a la que se va a conectar. Al poner el 0 al final, decimos que son todas, la mascara ayuda a saber que no

## `default-router <gateway>`

> Define el gateway que se va a usar en el router.

## `dns-server <ip>`

> encoges cual es el DNS del router

## `ip dhcp excluded-adress <ip {inicial}> {<ip final>}`

> Excluye ip de IPs automaticas para que las puedas guardar para tus propios servidores.

## `ip dchp binding`

> Muestra todos los ips dados desde dchp.

