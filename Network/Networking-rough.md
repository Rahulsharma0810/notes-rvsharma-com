
## Computer Networking

### OSI model layers

[![img](https://github.com/vald-phoenix/the-osi-model/raw/master/media/osi-model-7-layers.svg)](https://github.com/vald-phoenix/the-osi-model/blob/master/media/osi-model-7-layers.svg)

**Figure:** the OSI layers and their usage.

| Layer | OSI model layer | Protocol Data Unit | Devices                                    | Protocols                                                    |
| ----- | --------------- | ------------------ | ------------------------------------------ | ------------------------------------------------------------ |
| 7     | Application     | Data               | L7 firewall                                | HTTP, DNS, DHCP, FTP, Telnet, SSH, SMTP, POP, IMAP, NTP, SNMMP, TLS/SSL, GBP, RIP, SIP, etc. |
| 6     | Presentation    | Data               | L7 firewall                                | All the above                                                |
| 5     | Session         | Data               | L7 firewall                                | All the above                                                |
| 4     | Transport       | Segments           | L4 firewall                                | TCP (connection oriented), UDP (connectionless oriented)     |
| 3     | Network         | Packets            | Router, Multiplayer Switch, Router         | IPv4, IPv6, IPSec, OSPF, EIGRP                               |
| 2     | Data Link       | Frames             | Switch, Bridge, NIC, Wireless Access Point | MAC, ARP Ethernet 802.3 (Wired), CDP, LLDP, HDLC, PPP, DSL, L2TP, IEEE 802.11 (Wireless), SONET/SDH |
| 1     | Physical        | Bits               | All the above                              | Electrical signal (copper wire), Light signal (optical fibre), Radio signal (air) |

#### L7 the application layer

[![img](https://github.com/vald-phoenix/the-osi-model/raw/master/media/7-application-layer.svg)](https://github.com/vald-phoenix/the-osi-model/blob/master/media/7-application-layer.svg)

**Figure:** L7 the application layer

This is the only layer that directly interacts with data from the user. Software applications like web browsers and email clients rely on the application layer to initiate communications. But it should be made clear that client software applications are not part of the application layer; rather the application layer is responsible for the protocols and data manipulation that the software relies on to present meaningful data to the user. Application layer protocols include [HTTP](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/), HTTPS, FTP, SFTP, DNS as well as SMTP (Simple Mail Transfer Protocol is one of the protocols that enables email communications), etc.

#### L6 the presentation layer

[![img](https://github.com/vald-phoenix/the-osi-model/raw/master/media/6-presentation-layer.svg)](https://github.com/vald-phoenix/the-osi-model/blob/master/media/6-presentation-layer.svg)

**Figure:** L6 the presentation layer.

This layer is primarily responsible for preparing data so that it can be used by the application layer; in other words, layer 6 makes the data presentable for applications to consume. The presentation layer is responsible for translation, [encryption](https://www.cloudflare.com/learning/ssl/what-is-encryption/), and compression of data.

Two communicating devices communicating may be using different encoding methods, so layer 6 is responsible for translating incoming data into a syntax that the application layer of the receiving device can understand (UTF8 -> ASCII or ASCII -> EBCDIC).

If the devices are communicating over an encrypted connection, layer 6 is responsible for adding the encryption on the sender’s end as well as decoding the encryption on the receiver's end so that it can present the application layer with unencrypted, readable data (usually through SSL/TLS).

Finally, the presentation layer is also responsible for compressing data it receives from the application layer before delivering it to layer 5. This helps improve the speed and efficiency of communication by minimizing the amount of data that will be transferred, moreover, data compression may be of two types: lossy (data integrity isn't guaranteed) or lossless (data integrity is guaranteed).

#### L5 the session layer

[![img](https://github.com/vald-phoenix/the-osi-model/raw/master/media/5-session-layer.svg)](https://github.com/vald-phoenix/the-osi-model/blob/master/media/5-session-layer.svg)

**Figure:** L5 the session layer.

This is the layer responsible for opening and closing communication between the two devices. The time between when the communication is opened and closed is known as the session. The session layer ensures that the session stays open long enough to transfer all the data being exchanged, and then promptly closes the session in order to avoid wasting resources.

The session layer also synchronizes data transfer with checkpoints. For example, if a 100 megabyte file is being transferred, the session layer could set a checkpoint every 5 megabytes. In the case of a disconnect or a crash after 52 megabytes have been transferred, the session could be resumed from the last checkpoint, meaning only 50 more megabytes of data need to be transferred. Without the checkpoints, the entire transfer would have to begin again from scratch.

Usually, the main tasks of L5 is authentication and authorisation, downloads files as data packets, session management.

#### L4 the transport layer

[![img](https://github.com/vald-phoenix/the-osi-model/raw/master/media/4-transport-layer.svg)](https://github.com/vald-phoenix/the-osi-model/blob/master/media/4-transport-layer.svg)

**Figure:** L4 the transport layer.

This layer is separated by two protocols like Transport Control Protocol and User Datagram Protocol. TCP is following connection-oriented transmission. It's slower but provides feedback (HTTP, FTP, etc). UDP is following connectionless transmission. It's faster but doesn't provide feedback and used when we don't care about the fullness of data (video games, music, movies, etc.).

Layer 4 is responsible for end-to-end communication between the two devices. This includes taking data from the session layer and breaking it up into chunks called segments (or datagrams in case of UDP) before sending it to layer 3. The transport layer on the receiving device is responsible for reassembling the segments into data the session layer can consume.

The transport layer is also responsible for flow control and error control,. Flow control determines an optimal speed of transmission to ensure that a sender with a fast connection doesn’t overwhelm a receiver with a slow connection. The transport layer performs error control on the receiving end by ensuring that the data received is complete , and checks checksums of data units and make use of automatic repeat request if it isn’t.

#### L3 the network layer

[![img](https://github.com/vald-phoenix/the-osi-model/raw/master/media/3-network-layer.svg)](https://github.com/vald-phoenix/the-osi-model/blob/master/media/3-network-layer.svg)

**Figure:** L3 the network layer.

The network layer is responsible for facilitating data transfer between two different networks. **If the two devices communicating are on the same network, then the network layer is unnecessary.** The network layer breaks up segments from the transport layer into smaller units, called packets, on the sender’s device, and reassembling these packets on the receiving device. The network layer also finds the best physical path for the data to reach its destination; this is known as routing.

Main duties of this layer usually are logical addressing (IPv4, IPv6, mask, IP), routing (to whom send packets), Path determination (Open Shortest Path First, Border Gateway Protocol, intermediate system-intermediate system).

#### L2 the data link layer

[![img](https://github.com/vald-phoenix/the-osi-model/raw/master/media/2-data-link-layer.svg)](https://github.com/vald-phoenix/the-osi-model/blob/master/media/2-data-link-layer.svg)

**Figure:** L2 the data link layer.

The data link layer is very similar to the network layer, except the data link layer facilitates data transfer between two devices on the SAME network. The data link layer takes packets from the network layer and breaks them into smaller pieces called frames. Like the network layer, the data link layer is also responsible for flow control and error control in intra-network communication (The transport layer only does flow control and error control for inter-network communications).

Duties usually are logical addressing (network layer), physical addressing (data link layer via MAC addresses of Network Interface Card, Switches), access media, controls how data is placed and received from the media (media access control, error detection).

#### L1 the physical layer

[![img](https://github.com/vald-phoenix/the-osi-model/raw/master/media/1-physical-layer.svg)](https://github.com/vald-phoenix/the-osi-model/blob/master/media/1-physical-layer.svg)

**Figure:** L1 the physical layer.

This layer includes the physical equipment involved in the data transfer, such as the cables and switches. This is also the layer where the data gets converted into a bit stream, which is a string of 1s and 0s. The physical layer of both devices must also agree on a signal convention so that the 1s can be distinguished from the 0s on both devices.


**Transport layer ports**

| Category         | Range       | Comments                                                     |
| ---------------- | ----------- | ------------------------------------------------------------ |
| Well Known Ports | 0 - 1023    | Used by system processes e.g. SSH(22), DNS(53), FTP(21), etc. |
| Registered Ports | 1024-49151  | For specific services e.g. PostgreSQL(5432), Redis(6379), etc. |
| Private Ports    | 49152-65535 | For private purposes e.g. to run an application              |

**Important ports on transport layer**

| Port Number | Protocol | Application                     |
| ----------- | -------- | ------------------------------- |
| 20          | TCP      | FTP data                        |
| 21          | TCP      | FTP control                     |
| 22          | TCP      | SSH                             |
| 23          | TCP      | Telnet                          |
| 25          | TCP      | SMTP                            |
| 53          | UDP, TCP | DNS                             |
| 67, 68      | UDP      | DHCP                            |
| 69          | UDP      | TFTP                            |
| 80          | TCP      | HTTP                            |
| 110         | TCP      | POP3                            |
| 161         | UDP      | SNMP                            |
| 443         | TCP      | SSL                             |
| 16384-32767 | UDP      | TRP-base Voice (VoIP) and Video |

**Acronyms**

These acronyms are useful to remember the OSI model.

All People Seem To Need Data Processing (**L7**-**L1**).
Please Do Not Throw Sausage Pizza Away (**L1**-**L7**).

### TCP/IP model vs OSI model

**TCP/IP Model** helps you to determine how a specific computer should be connected to the internet and how data should be transmitted between them. It helps you to create a virtual network when multiple computer networks are connected together. The purpose of TCP/IP model is to allow communication over large distances.

TCP/IP stands for Transmission Control Protocol/ Internet Protocol. It is specifically designed as a model to offer highly reliable and end-to-end byte stream over an unreliable internetwork.

| OSI Layer |     OSI      | TCP/IP Layer |     TCP/IP     | Protocol Data Unit |
| :-------: | :----------: | :----------: | :------------: | :----------------: |
|     7     | Application  |      4       |  Application   |        Data        |
|     6     | Presentation |      4       |  Application   |        Data        |
|     5     |   Session    |      4       |  Application   |        Data        |
|     4     |  Transport   |      3       |   Transport    |      Segments      |
|     3     |   Network    |      2       |    Internet    |      Packets       |
|     2     |  Data Link   |      1       | Network Access |       Frames       |
|     1     |   Physical   |      1       | Network Access |        Bits        |


The TCP/IP model defines two end-to-end transport layer protocols: TCP and UDP. The choice will depend on the requirements of the application protocol being used. TCP is connection-oriented, is reliable, and includes flow control, while UDP is a much simpler option that provides *best effort* delivery of individual packets. UDP is connectionless and unreliable, but nevertheless well suited for real-time traffic (such as voice and video) and other applications that use a client-server communication model with simple request- reply queries.

#### IP Header
On the massive network known as the Internet, computing devices send all kinds of messages to other computing devices. A message might be a tiny ping to check if another device is online or a message could be an entire webpage.

But there's a limit to how large a message can be, since there's a limit to how much data can be reasonably transmitted at once by the physical network connections between devices.

That's why many networking protocols split each message into multiple small **packets**. The Internet Protocol (IP) describes the structure of the packets that whizz around the Internet.

Each IP packet contains both a header (20 or 24 bytes long) and data (variable length). The header includes the IP addresses of the source and destination, plus other fields that help to route the packet. The data is the actual content, such as a string of letters or part of a webpage.

**Packet format**

![A diagram of an IP packet. The header is 24 bytes long and contains 15 fields, including 4 bytes for source IP address and 4 bytes for destination IP address. The payload is variable length.](https://cdn.kastatic.org/ka-perseus-images/337190cba133e19ee9d8b5878453f915971a59cd.svg)

A diagram of an IP packet. The header is 24 bytes long and contains 15 fields, including 4 bytes for source IP address and 4 bytes for destination IP address. The payload is variable length.

You can think of IP packets like postal letters: the header is the envelope with all the routing information that's needed by the post office, and the payload is the letter that's read only by the recipient.

![Diagram of an IP packet as a postal letter. An envelope is shown with "Source IP address" as the return address and "Destination IP address" as the mailing address. The envelope is then shown in an open state, with a letter that says "Data" poking out.](https://cdn.kastatic.org/ka-perseus-images/ee135be8f541bd55939b0ea21a1429fd06158766.svg)

Diagram of an IP packet as a postal letter. An envelope is shown with "Source IP address" as the return address and "Destination IP address" as the mailing address. The envelope is then shown in an open state, with a letter that says "Data" poking out.

Just like the postal system routes postal letters around the world, the Internet Protocol routes IP packets around the Internet.

#### TCP Header

The **Transmission Control Protocol (TCP)** is a transport protocol that is used on top of IP to ensure reliable transmission of packets.

TCP includes mechanisms to solve many of the problems that arise from packet-based messaging, such as lost packets, out of order packets, duplicate packets, and corrupted packets.

Since TCP is the protocol used most commonly on top of IP, the Internet protocol stack is sometimes referred to as **TCP/IP**.

**Packet format**

When sending packets using TCP/IP, the data portion of each [IP packet(Opens in a new window)](https://www.khanacademy.org/a/ip-packets) is formatted as a **TCP segment**.

![Diagram of a TCP segment within an IP packet. The IP packet contains header and data sections. The IP data section is the TCP segment, which itself contains header and data sections.](https://cdn.kastatic.org/ka-perseus-images/e5fdf560fdb40a1c0b3c3ce96f570e5f00fff161.svg)

Diagram of a TCP segment within an IP packet. The IP packet contains header and data sections. The IP data section is the TCP segment, which itself contains header and data sections.

Each TCP segment contains a header and data. The TCP header contains many more fields than the UDP header and can range in size from 202020 to 606060 bytes, depending on the size of the options field.

The TCP header shares some fields with the UDP header: source port number, destination port number, and checksum. To remember how those are used, review the [UDP article](https://www.khanacademy.org/a/user-datagram-protocol-udp).


Let's step through the process of transmitting a packet with TCP/IP.

##### Step 1: Establish connection

When two computers want to send data to each other over TCP, they first need to establish a connection using a **three-way handshake**.

![Diagram of two computers with arrows between.  * Arrow goes from Computer 1 to Computer 2 with "SYN" label. * Arrow goes from Computer 2 to Computer 1 with "ACK SYN" label. * Arrow goes from Computer 1 to Computer 2 with "ACK" label.](https://cdn.kastatic.org/ka-perseus-images/d09f9d37ff2a2deb21a8822f8c99ba6b86319f0b.svg)

Diagram of two computers with arrows between.Arrow goes from Computer 1 to Computer 2 with "SYN" label.Arrow goes from Computer 2 to Computer 1 with "ACK SYN" label.Arrow goes from Computer 1 to Computer 2 with "ACK" label.

The first computer sends a packet with the SYN bit set to 111 (SYN = "synchronize?"). The second computer sends back a packet with the ACK bit set to 111 (ACK = "acknowledge!") plus the SYN bit set to 111. The first computer replies back with an ACK.

The SYN and ACK bits are both part of the TCP header:

![A diagram of the TCP header with rows of fields. Each row is 32 bits long. The first row contains a 16-bit source port number and 16-bit destination port number. The second row contains a 32-bit sequence number. The third row contains a 32-bit acknowledgement number. The fourth row contains a 4-bit data offset number, 6 bits that are marked as reserved, 6 control bits (URG, ACK, PSH, RST, SYN, and FIN), and a 16-bit window size number. The fifth row contains a 16-bit checksum and 16-bit urgent pointer. The header ends with options and padding which can be of variable length.](https://cdn.kastatic.org/ka-perseus-images/9a4a79816965be53e1071cf6b0e2991cb4d170ca.svg)

A diagram of the TCP header with rows of fields. Each row is 32 bits long. The first row contains a 16-bit source port number and 16-bit destination port number. The second row contains a 32-bit sequence number. The third row contains a 32-bit acknowledgement number. The fourth row contains a 4-bit data offset number, 6 bits that are marked as reserved, 6 control bits (URG, ACK, PSH, RST, SYN, and FIN), and a 16-bit window size number. The fifth row contains a 16-bit checksum and 16-bit urgent pointer. The header ends with options and padding which can be of variable length.

The ACK and SYN bits are highlighted on the fourth row of the header.

In fact, the three packets involved in the three-way handshake do not typically include any data. Once the computers are done with the handshake, they're ready to receive packets containing actual data.

##### Step 2: Send packets of data

When a packet of data is sent over TCP, the recipient must always acknowledge what they received.

![Diagram of two computers with arrows between.  * Arrow goes from Computer 1 to Computer 2 and shows a box of binary data and the label "Sequence #1". * Arrow goes from Computer 2 to Computer 1 with "ACK" label.](https://cdn.kastatic.org/ka-perseus-images/2cfc6b88b3b5c3a27386503d347524c2065a57d9.svg)

Diagram of two computers with arrows between.Arrow goes from Computer 1 to Computer 2 and shows a box of binary data and the label "Sequence #1".Arrow goes from Computer 2 to Computer 1 with "ACK" label.

The first computer sends a packet with data and a sequence number. The second computer acknowledges it by setting the ACK bit and increasing the acknowledgement number by the length of the received data.

The sequence and acknowledgement numbers are part of the TCP header:

![A diagram of the TCP header with rows of fields. Each row is 32 bits long. The first row contains a 16-bit source port number and 16-bit destination port number. The second row contains a 32-bit sequence number. The third row contains a 32-bit acknowledgement number. The fourth row contains a 4-bit data offset number, 6 bits that are marked as reserved, 6 control bits (URG, ACK, PSH, RST, SYN, and FIN), and a 16-bit window size number. The fifth row contains a 16-bit checksum and 16-bit urgent pointer. The header ends with options and padding which can be of variable length.](https://cdn.kastatic.org/ka-perseus-images/ec71832edb1f2ff1d2ad12da494033ce2b25aafa.svg)

A diagram of the TCP header with rows of fields. Each row is 32 bits long. The first row contains a 16-bit source port number and 16-bit destination port number. The second row contains a 32-bit sequence number. The third row contains a 32-bit acknowledgement number. The fourth row contains a 4-bit data offset number, 6 bits that are marked as reserved, 6 control bits (URG, ACK, PSH, RST, SYN, and FIN), and a 16-bit window size number. The fifth row contains a 16-bit checksum and 16-bit urgent pointer. The header ends with options and padding which can be of variable length.

The 32-bit sequence and acknowledgement numbers are highlighted.

Those two numbers help the computers to keep track of which data was successfully received, which data was lost, and which data was accidentally sent twice.

##### Step 3: Close the connection

Either computer can close the connection when they no longer want to send or receive data.

![Diagram of two computers with arrows between.  * Arrow goes from Computer 1 to Computer 2 with "FIN" label. * Arrow goes from Computer 2 to Computer 1 with "ACK FIN" label. * Arrow goes from Computer 1 to Computer 2 with "ACK" label.](https://cdn.kastatic.org/ka-perseus-images/f158ea181534ee675d0928fa657897cefc04359e.svg)

Diagram of two computers with arrows between.Arrow goes from Computer 1 to Computer 2 with "FIN" label.Arrow goes from Computer 2 to Computer 1 with "ACK FIN" label.Arrow goes from Computer 1 to Computer 2 with "ACK" label.

A computer initiates closing the connection by sending a packet with the FIN bit set to 1 (FIN = finish). The other computer replies with an ACK and another FIN. After one more ACK from the initiating computer, the connection is closed.

**Detecting lost packets**

TCP connections can detect lost packets using a timeout.

![Diagram demonstrating re-transmission of a packet from one computer to another computer. Arrow goes from first computer to second computer and is labeled with "sequence #1" and a string of binary data. A stopwatch is shown in various stages after the arrow, first with 0 time passed, then half the time passed, then all time passed and in an alarm state. The another arrow goes from the first laptop to second laptop, labeled the same as the first.](https://cdn.kastatic.org/ka-perseus-images/b1017461d232cd46fa5b445f80e75568bf31c57c.svg)

Diagram demonstrating re-transmission of a packet from one computer to another computer. Arrow goes from first computer to second computer and is labeled with "sequence #1" and a string of binary data. A stopwatch is shown in various stages after the arrow, first with 0 time passed, then half the time passed, then all time passed and in an alarm state. The another arrow goes from the first laptop to second laptop, labeled the same as the first.

After sending off a packet, the sender starts a timer and puts the packet in a retransmission queue. If the timer runs out and the sender has not yet received an ACK from the recipient, it sends the packet again.

The retransmission may lead to the recipient receiving duplicate packets, if a packet was not actually lost but just very slow to arrive or be acknowledged. If so, the recipient can simply discard duplicate packets. It's better to have the data twice than not at all!

**Handling out of order packets**

TCP connections can detect out of order packets by using the sequence and acknowledgement numbers.

![Diagram of two computers with arrows between.  * Arrow goes from Computer 1 to Computer 2 and shows a box of binary data with the label "Seq #1". * Arrow goes from Computer 2 to Computer 1 with the label "Ack #37". * Arrow goes from Computer 1 to Computer 2 and shows a box of binary data with the label "Seq #73". * Arrow goes from Computer 2 to Computer 1 with the label "Ack #37".](https://cdn.kastatic.org/ka-perseus-images/27f4fa1915c98689623e0ee224416c5290afc65a.svg)

Diagram of two computers with arrows between.Arrow goes from Computer 1 to Computer 2 and shows a box of binary data with the label "Seq #1".Arrow goes from Computer 2 to Computer 1 with the label "Ack #37".Arrow goes from Computer 1 to Computer 2 and shows a box of binary data with the label "Seq #73".Arrow goes from Computer 2 to Computer 1 with the label "Ack #37".

When the recipient sees a higher sequence number than what they have acknowledged so far, they know that they are missing at least one packet in between. In the situation pictured above, the recipient sees a sequence number of #73 but expected a sequence number of #37. The recipient lets the sender know there's something amiss by sending a packet with an acknowledgement number set to the expected sequence number.

Sometimes the missing packet is simply taking a slower route through the Internet and it arrives soon after.

![Diagram of TCP packets arriving out of order. Two computers are shown with arrows going back and forth, with their vertical location indicating the time of sending and arrival:  * An arrow labeled "Seq #1" starts from Computer 1 and ends soon after at Computer 2. * An arrow labeled "Ack #37" starts from Computer 2 and ends soon after at Computer 1. * An arrow labeled "Seq #37" starts from Computer 1 and doesn't end until much later at Computer 2.  * An arrow labeled "Seq #73" starts from Computer 1 and ends soon after at Computer 2 (before the arrow for "Seq #37"). * An arrow labeled "Ack #37" starts from Computer 2 and ends soon after at Computer 1 (before the arrow for "Seq #37").](https://cdn.kastatic.org/ka-perseus-images/c96ec5ae0784f98e14d7a1c45b0dc65203b6bf48.svg)

Diagram of TCP packets arriving out of order. Two computers are shown with arrows going back and forth, with their vertical location indicating the time of sending and arrival:An arrow labeled "Seq #1" starts from Computer 1 and ends soon after at Computer 2.An arrow labeled "Ack #37" starts from Computer 2 and ends soon after at Computer 1.An arrow labeled "Seq #37" starts from Computer 1 and doesn't end until much later at Computer 2.An arrow labeled "Seq #73" starts from Computer 1 and ends soon after at Computer 2 (before the arrow for "Seq #37").An arrow labeled "Ack #37" starts from Computer 2 and ends soon after at Computer 1 (before the arrow for "Seq #37").

Other times, the missing packet may actually be a lost packet and the sender must retransmit the packet.

![Diagram of TCP packets arriving out of order. Two computers are shown with arrows going back and forth, with their vertical location indicating the time of sending and arrival:  * An arrow labeled "Seq #1" starts from Computer 1 and ends soon after at Computer 2. * An arrow labeled "Ack #37" starts from Computer 2 and ends soon after at Computer 1. * An arrow labeled "Seq #37" starts from Computer 1 and ends before reaching Computer 2, with an X indicating it was lost.  * An arrow labeled "Seq #73" starts from Computer 1 and ends soon after at Computer 2. * An arrow labeled "Ack #37" starts from Computer 2 and ends soon after at Computer 1. * An arrow labeled "Seq #37" starts from Computer 1 and ends soon after at Computer 2.](https://cdn.kastatic.org/ka-perseus-images/bdeaf7f92aa9f48d5d103888a63a34704b755104.svg)

Diagram of TCP packets arriving out of order. Two computers are shown with arrows going back and forth, with their vertical location indicating the time of sending and arrival:An arrow labeled "Seq #1" starts from Computer 1 and ends soon after at Computer 2.An arrow labeled "Ack #37" starts from Computer 2 and ends soon after at Computer 1.An arrow labeled "Seq #37" starts from Computer 1 and ends before reaching Computer 2, with an X indicating it was lost.An arrow labeled "Seq #73" starts from Computer 1 and ends soon after at Computer 2.An arrow labeled "Ack #37" starts from Computer 2 and ends soon after at Computer 1.An arrow labeled "Seq #37" starts from Computer 1 and ends soon after at Computer 2.

In both situations, the recipient has to deal with out of order packets. Fortunately, the recipient can use the sequence numbers to reassemble the packet data in the correct order.

![A diagram of TCP data reassembly. ](https://cdn.kastatic.org/ka-perseus-images/5fbe9cbfb51c95ad73beb2c536749908a8057889.svg)