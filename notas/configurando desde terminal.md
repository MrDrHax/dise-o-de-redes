- [Conectandose](#conectandose)
- [Tipos de configuracion](#tipos-de-configuracion)
  - [AUX](#aux)
  - [Consola](#consola)
- [Inicio](#inicio)
  - [`en`](#en)
  - [`show start`](#show-start)
  - [`erase start`](#erase-start)
  - [`config t`](#config-t)
  - [`no ip domain lookup`](#no-ip-domain-lookup)
  - [`line con 0`](#line-con)
  - [`logging synchronous`](#logging-synchronous)
  - [`interface (gigabit/fast)Ethernet 0/0` (solo router)](#interface-gigabitfastethernet-00-solo-router)
    - [`int (g/f)0/0` (chico)](#int-gf00-chico)
  - [`ip adress <ip del router> <mascara>`](#ip-adress-ip-del-router-mascara)
  - [`no shut`](#no-shut)
  - [`exit`](#exit)
  - [`ip dhcp pool <nombre>`](#ip-dhcp-pool-nombre)
  - [`network <ip.0> <mascara>`](#network-ip0-mascara)
  - [`default-router <gateway>`](#default-router-gateway)
  - [`dns-server <ip>`](#dns-server-ip)
  - [`ip dhcp excluded-adress <ip {inicial}> {<ip final>}`](#ip-dhcp-excluded-adress-ip-inicial-ip-final)
  - [`ip dchp binding`](#ip-dchp-binding)
  - [`show run`](#show-run)
  - [`transport input telnet`](#transport-input-telnet)
  - [`password <password>`](#password-password)
  - [`no password <password a quitar>`](#no-password-password-a-quitar)
  - [`username <username> secret <password>`](#username-username-secret-password)
  - [`enable secret <user>`](#enable-secret-user)
  - [`login local`](#login-local)


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

## `show run`

> Te da info util del router

## `transport input telnet`

> activa el telnet para poderte conectar al dispositivo

NOTA: Telnet no cifra nada, plox no lo uses si esta afuera

## `password <password>`

> dar password, siempre usa cisco con equipo de escuela 

## `no password <password a quitar>`

> Quita el usuario del modem

## `username <username> secret <password>`

> Creas un nuevo usuario con una contraseña

## `enable secret <user>`

> Activa el password para el usuario dado y poder usar telnet

## `login local`

> Dertermina quien puede entrar

## `transport input ssh`

> deja de usar telnet. Util para cifrar con ssh

## `crypto key generate rsa`

> genera llaves para el ssh, con el formato rsa. 246 es medio seguro.

## `hostname <nombre>`

> cambia nombre al dispositivo

## `ip domain-name <nombre de red>`

> Le das un nombre a tu red

## `version ssh 2`

> cambia la version de ssh a una mas chida
