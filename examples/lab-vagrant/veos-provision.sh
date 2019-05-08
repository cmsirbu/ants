#!/usr/bin/env bash
FastCli -p 15 -c"
enable
configure
hostname veos
!
interface Ethernet1
description VBOXNET0 INTERNAL DIRECT MANAGEMENT
no switchport
ip address 10.250.0.112/24
!
interface Ethernet2
description INFRA LINK2
no switchport
ip address 10.2.0.112/24
!
interface Ethernet3
description INFRA LINK3
no switchport
ip address 10.3.0.112/24
!
ip routing
!
interface Loopback0
ip address 100.100.100.112/32
!
write memory
"
