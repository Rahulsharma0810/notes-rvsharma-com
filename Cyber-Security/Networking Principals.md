The Course Is Presented By Hussein Nasser on [Udemy](https://www.udemy.com/course/fundamentals-of-networking-for-effective-backend-design/learn/lecture/31096404#overview)

# Section 1: Introduction

## Who Is This Course For?

### 1. Backend Engineers

- Primary Audience: The instructor designed the course for backend engineers who build applications consumed by client/front-end software.
- Key Focus:
    - Revealing what happens “behind the scenes” at the OS/network level.
    - Explaining how incoming network segments (TCP segments) flow to the correct process.
    - Bridging the gap between application-level code and lower-level networking.

### 2. Frontend Engineers

- Motivation: Frontend developers often invoke backend APIs and need to know:
    - How a request travels from the client to the server.
    - Why certain slowdowns might occur in the network layers rather than in the backend code.
- Outcome:
    - Gain a deeper understanding of network bottlenecks.
    - Diagnose issues more effectively (e.g., distinguishing application-side delays from network latency or OS-level constraints).

### 3. Network Engineers

- Reason: Many network specialists have deep knowledge of Layers 1–7 but may not see the full picture of how application code (like Node.js, Python, etc.) interacts with the OS and network stack.
- Goal: Bridge the gap between network configuration/packet flow and how the application layer actually responds or resets connections.

## Why This Matters

### 1. Bridging the Foggy Gap

- Networking fundamentals are often treated as a “black box” by application developers.
- Likewise, network engineers may not grasp the specifics of how an application handles connections.

### 2. Diagnosing Issues

- Slow requests can arise from various layers:
    - Application logic
    - OS-level constraints
    - Network routing or capacity
- A holistic understanding prevents blaming the wrong layer (e.g., blaming backend code when the problem lies in network congestion).

### 3. Building End-to-End Mental Models

- Knowledge of how data flows from client → OS → network → backend code clarifies performance bottlenecks.
- Encourages better design decisions at both the frontend (request logic) and backend (server configuration, protocol usage).

## Additional Points to Remember

- Terminology: The instructor often refers to “segments,” which typically means TCP segments in the networking stack.
- OSI/TCP Model:
    - While the OSI model has 7 layers (with Layer 7 = Application), real-world protocols often blend layers (TCP/IP model).
    - Understanding which layer is responsible for each part of the process is crucial (e.g., TCP reset packets might be triggered by the OS or the application).
- Aim of the Course:
    - Reduce confusion by showcasing how the OS, networking stack, and application environment interact.
    - Help both developers and network professionals grasp the “why” behind certain behaviors (e.g., why certain connections get dropped or throttle).

---
# Section 2: Fundamentals Of Networking

Here is the reformatted response with no changes to the original text:

## Introduction

The Revolution: The client-server model fundamentally changed computing by separating the client and server, allowing different components to execute on separate machines.

Before vs. After:

Before: Mainframes ran everything centrally.

Now: Clients are lightweight, offloading heavy computation to powerful servers.


## Why Client-Server?

### Cost & Resource Efficiency

Machines are expensive; applications are complex. Splitting workload = cheaper commodity hardware for clients, while beefier servers handle intensive tasks.

### Modularity & Scalability

Breaking down applications into multiple components makes them easier to manage. Inspired micro services architecture, where small services interact with each other.

### Performance Optimization

Servers handle resource-intensive tasks (CPU-heavy, RAM-heavy, I/O-intensive). Clients stay lightweight (e.g., thin clients, tablets, IoT devices).



The Birth of Remote Procedure Call (RPC)

Concept: Clients send a request for the server to execute a function remotely and return results.

Evolution:

* Early RPCs (1960 s-70 s) lacked standardization.
* gRPC (Google RPC) is a modern standard that enables efficient cross-platform communication.

---

## Advantages of Client-Server Model
### Centralized Processing

Servers centralize workload, allowing for better scaling. Many clients can reuse a single powerful server instead of duplicating logic.

### Better Maintainability

Clients remain lightweight, reducing dependency bloat. Servers manage libraries, databases, and business logic.

### Improved Deployment & Updates

Changes in business logic only require server updates, not client-side modifications. This model simplifies version control and reduces compatibility issues.


## Client-Server & Microservices: Similar, but Different

Microservices borrow from the client-server model:

* Large monoliths were split into smaller services.
* Each service performs specific functions and interacts via network calls.

Caveat: The instructor warns against overusing microservices, citing complexity.

## Edge Computing & Modern Trends

Traditionally: Clients only performed lightweight tasks.

Now: Edge computing enables some computation on client-side.

Example: IoT devices (e.g., sensors) perform initial data processing before sending results to a central server.

## Reducing Client Dependencies

Monolith Problem: Older applications required all dependencies (drivers, libraries, database connectors) on a single machine.

Client-Server Fix:

* Clients now only send requests.
* Servers handle dependencies (e.g., database connections).
* Leads to smaller binaries, faster startups, and better modularity.

## Client-Server & 3-Tier Architecture

3-Tier Architecture is a specialized version of the client-server model:

* Client Layer: UI or frontend application.
* Application Layer: Server with business logic.
* Database Layer: Dedicated database backend.

Advantage: Improved scalability, security, and maintainability.

## The Need for a Standardized Communication Model

Problem: In early client-server systems, communication was unstructured.
Key Challenge: How do we reliably transfer data across machines?
Solution:
* Standardized networking protocols (e.g., TCP/IP).
* Remote communication standards (e.g., REST, RPC, gRPC).
* Middleware solutions to facilitate connectivity.

## Client Server Model: Key Takeaways

* Client-server model enables distributed computing by offloading expensive workloads to powerful servers.
* RPC introduced remote execution, leading to modern standards like gRPC.
* Microservices evolved from client-server but have their own trade-offs.
* Edge computing is shifting some workload back to clients.
* 3-tier architecture provides a structured way to separate UI, logic, and database.
* Standardized communication protocols are critical for interoperability.

## OSI Model:  Foundation of Network Communication

### **Introduction**
- The **OSI (Open Systems Interconnection) model** is a **theoretical framework** that standardizes network communication.
- It ensures interoperability across different network hardware, software, and mediums.
- **Why is it important?**  
  - It allows us to build #voc  **agnostic** applications that work across **Wi-Fi, Ethernet, LTE, fiber, and radio waves** without modification.
  - It provides a **structured approach** to understanding **where networking issues occur**.

### **Why Do We Need a Communication Model?**
1. **Standardization**  
   - Without a standard, devices wouldn’t know how to communicate (e.g., different interpretations of digital-to-analog conversion).
   - Enables seamless communication **across different hardware, mediums, and network types**.

2. **Decoupling Applications from Physical Medium**  
   - Imagine if an app needed **different versions** for Wi-Fi, LTE, and fiber—this would be a **disaster**.
   - **The OSI model abstracts this** so applications can work **independently** of the transmission medium.

3. **Modular Innovation**  
   - Network improvements can happen at **each layer separately** without disrupting the entire system.
   - Example: **Faster fiber optic technology** doesn’t require changes to **TCP/IP protocols**.

4. **Network Equipment Interoperability**  
   - **Routers, switches, firewalls, proxies**—all need a standard way to **process and route data**.
   - A **layered model** allows seamless upgrades and replacements.

### **The 7 Layers of the OSI Model**

Short - “PDNTSPA“

Each layer provides a **specific function** in the communication process.
#### **Layer 7 - Application Layer**
- **What it does**: This is where applications **interact** with the network.
- **Examples**:
  - **HTTP, HTTPS, FTP, DNS, SMTP, WebSockets, gRPC**.
  - **Web browsers, APIs, Load Balancers, Reverse Proxies (e.g., Nginx, Envoy)**.

#### **Layer 6 - Presentation Layer**
- **What it does**: **Encoding, encryption, and serialization.**
- **Examples**:
  - **JSON serialization**, **Base64 encoding**, **TLS encryption**.
  - Converting **structured data** (e.g., objects in Python/JS) into **bytes** for transmission.
#### **Layer 5 - Session Layer**
- **What it does**: Manages **sessions & stateful connections**.
- **Examples**:
  - **TCP handshake (SYN-ACK-ACK)**.
  - **TLS session negotiation**.
  - **Load balancer connection pooling**.
  - **Layer 5 Proxies (e.g., Linkerd, Envoy)**.
#### **Layer 4 - Transport Layer**
- **What it does**: Ensures reliable data delivery & flow control.
- **Examples**:
  - **TCP (stateful, connection-based, ordered packets)**.
  - **UDP (stateless, fast, unordered packets)**.
  - **QUIC (built on UDP for faster HTTP/3 communication)**.

QUIC was designed to address TCP’s relatively slow handshake procedures & **HOL (Head of Line ) Blocking,  HOL** is performance issue that occurs when a SEQ of packets is held up by the first packet in the line. The issue is common in TCP. On The other QUIC minimise the HOL by allowing multiple streams of data to be multiplex over a single connection. QUIC, loss or delay in one stream does not block other streams because QUIC handles packet loss and retransmissions at the individual stream level rather than at the connection level as TCP does.

Till L 4 Anyone or Intruder can read the because till at this layer nothing is encrypted.
Your ISP too.
#### **Layer 3 - Network Layer**
- **What it does**: Handles **routing, IP addressing, and packet forwarding**.
- **Examples**:
  - **IP, ICMP (ping), BGP (Border Gateway Protocol)**.
  - **VPNs operate at Layer 3** (e.g., encapsulating one IP packet inside another).

Most VPN work in Layer 2, As they add source IP. 

#### **Layer 2 - Data Link Layer**
- **What it does**: Deals with **MAC addresses, frames, and direct device-to-device communication**.
- **Examples**:
  - **Ethernet (802.3), Wi-Fi (802.11), ARP (Address Resolution Protocol)**.
  - **Switches operate at Layer 2**, forwarding frames based on **MAC addresses**.

Most VPNs are Layer 2
#### **Layer 1 - Physical Layer**
- **What it does**: Converts **bits into signals** for transmission over different mediums.
- **Examples**:
  - **Electric signals (Ethernet), radio waves (Wi-Fi, LTE), light pulses (fiber optics)**.
  - **Network Interface Cards (NICs), cables, Wi-Fi transmitters**.

## **How Data Moves Through the OSI Model**
Data follows a **structured flow** from **application → physical medium** and back.

### **Example: Sending an HTTP POST Request**
1. **Application Layer (Layer 7)**  
   - User submits a **POST request** to `https://example.com`.
   - Browser generates **HTTP headers** and request body.

2. **Presentation Layer (Layer 6)**  
   - JSON data is **Serialized** (Process of converting an object or data structure into json format strings )into bytes.
   - If **HTTPS**, data is **encrypted using TLS**.

3. **Session Layer (Layer 5)**  
   - If no session exists, a **TCP connection (SYN-ACK-ACK)** is initiated.
   - TLS handshake occurs if **HTTPS** is used.

4. **Transport Layer (Layer 4)**  
   - Data is segmented into **TCP packets**.
   - Port **443 (HTTPS)** is assigned.

5. **Network Layer (Layer 3)**  
   - **Source & destination IP addresses** are added.
   - Data is **routed through the internet**.

6. **Data Link Layer (Layer 2)**  
   - **MAC addresses** are assigned.
   - Frames are prepared for transmission.

7. **Physical Layer (Layer 1)**  
   - Data is transmitted **over radio, Fiber, or copper wires**.
   - On the receiving end, this process **reverses**.

## **The OSI Model & Networking Devices**
Each networking device operates at **specific OSI layers**:

| **Device**        | **OSI Layer** | **Function**                                                  |
| ----------------- | ------------- | ------------------------------------------------------------- |
| **Switch**        | Layer 2       | Routes frames using **MAC addresses**.                        |
| **Router**        | Layer 3       | Routes packets based on **IP addresses**.                     |
| **Firewall**      | Layer 3/4     | Filters traffic based on **IP, port, or protocol**.           |
| **Load Balancer** | Layer 4/7     | Distributes requests **(TCP-level or HTTP-level)**.           |
| **Proxy Server**  | Layer 7       | Intercepts & modifies HTTP requests (e.g., **CDN, caching**). |

## **Simplified TCP/IP Model**
- The **TCP/IP model** is a **simplified alternative** to OSI:
  - **Application Layer** (combines Layers **5, 6, 7**).
  - **Transport Layer** (Layer **4**).
  - **Internet Layer** (Layer **3**).
  - **Network Interface Layer** (combines Layers **1, 2**).

- **Pros of TCP/IP Model**:
  - Easier to understand.
  - More **practical** for real-world networking.
  - Reduces **unnecessary complexity**.

## **OSI Model Limitations & Criticism**

1. **Too Many Layers**
   - **Presentation & Session layers** are rarely discussed in practical applications.
   - Many **modern protocols** don’t strictly adhere to the OSI model.

2. **Rigid Classification**
   - Some applications span **multiple layers** (e.g., **TLS affects both Layer 5 & Layer 6**).
   - Real-world implementations are often **blended**.

3. **The TCP/IP Model is More Widely Used**
   - The **internet itself** is built around TCP/IP, **not OSI**.
   - **Networking professionals** often think in **TCP/IP terms** rather than **OSI layers**.

## **Key Takeaways**
- **OSI Model** provides a **structured way** to understand networking.
- **Layered abstraction** allows for **independent development & innovation**.
- **Networking devices operate at different layers** (switches = Layer 2, routers = Layer 3, firewalls = Layer 3/4, proxies = Layer 7).
- **Most real-world networking follows the TCP/IP model**, which simplifies OSI’s **7 layers into 4**.

---
# Section 3: Internet Protocol

### IP Building Block

![IPv4-Datagram-Header.jpg](blob:capacitor://localhost/56b85140-63de-4782-9bd0-704267a6880d)

![wireshark-capture-ip-header-fields.png](blob:capacitor://localhost/df9b9e5a-61e2-4294-9560-0faf219f9f2b)

## **Introduction**
- The **IP protocol** is the foundation of networking at **Layer 3 (Network Layer)**.
- This section covers **IP addresses, subnet masks, gateways, and routing fundamentals**.
- **Key questions to understand**:
  - What happens when you send an **IP packet**?
  - How does an **IP address** determine **network & host portions**?
  - Why do we need a **subnet mask** and **default gateway**?

## **IP Address Basics**
- An **IP address** is a **Layer 3 property** and uniquely identifies a device on a network.
- It can be **assigned dynamically (DHCP)** or **statically configured**.
- **IPv4** uses **4 bytes (32 bits)**, while **IPv6** uses **16 bytes (128 bits)**.
- **Structure**: `A.B.C.D /X`
  - Each **byte (A, B, C, D)** is **8 bits**.
  - The `/X` represents the **network portion** of the address.

## **Network vs. Host Portions**
- **An IP address consists of**:
  - **Network portion** (identifies the network/subnet)
  - **Host portion** (identifies a specific device in that subnet)
- Example: `192.168.254.0/24`
  - **First 24 bits** (`192.168.254`) = **Network ID**
  - **Last 8 bits** (`0-255`) = **Host ID**
  - Allows **256 possible addresses** (`0-255`), but **2 are reserved** (Network & Broadcast addresses).
## **Subnet Mask**
- Defines how **network & host portions** are divided.
- **Example**: `255.255.255.0`
  - **Binary**: `11111111.11111111.11111111.00000000`
  - The `1s` represent the **network portion**.
  - The `0s` represent the **host portion**.
- Used to determine if a destination IP is **in the same subnet** or not.

## **Default Gateway**
- A **router or network device** that directs packets **outside the subnet**.
- If a destination is **outside the subnet**, the packet is sent to the **default gateway**.
- **Each network device needs**:
  1. **IP Address**
  2. **Subnet Mask**
  3. **Default Gateway**
## **Routing and Packet Delivery**
- **Scenario 1: Host-to-Host (Same Subnet)**
  - Devices communicate using **MAC addresses** (Layer 2).
  - No routing required; packets are sent **directly**.

- **Scenario 2: Host-to-Host (Different Subnet)**
  - The subnet mask **reveals** that the destination is **outside the subnet**.
  - The packet is sent to the **default gateway**, which forwards it appropriately.

## **IP Routing Example**
### **Case 1: Same Subnet Communication**
- **Source**: `192.168.1.3/24`
- **Destination**: `192.168.1.12/24`
- **Subnet Mask**: `255.255.255.0`
- **Binary Calculation Confirms:** Both belong to `192.168.1.0/24`
- **Action**: Device sends packet directly using MAC address.

### **Case 2: Different Subnet Communication**
- **Source**: `192.168.1.3/24`
- **Destination**: `192.168.2.5/24`
- **Subnet Mask**: `255.255.255.0`
- **Binary Calculation Confirms:** Different networks (`192.168.1.0` vs `192.168.2.0`)
- **Action**: Send packet to **default gateway**, which routes it to `192.168.2.0` network.

## **Key Takeaways**
- **IP addresses** consist of **network and host portions**, defined by the **subnet mask**.
- **Subnet masks** help determine if a packet stays within a subnet or must be routed.
- **Default gateways** are used when the destination is **outside the local subnet**.
- **Routers make inter-subnet communication possible** by forwarding packets accordingly.
- Understanding subnets is crucial for **efficient network design and troubleshooting**.

## IP Packets

### **Introduction**
- Now that we have discussed the **building blocks of IP**, let's dive deeper into **IP packets**.
- The **IP packet** is the fundamental unit of data transmitted over a network.
- **Key components**:
  1. **Headers** – Contain metadata about the packet.
  2. **Data (Payload)** – The actual content being transmitted.

## **Anatomy of an IP Packet**
- **Two main sections**:
  - **Header (Metadata & Routing Information)**
  - **Data (Payload being transmitted)**
- The **header size is typically 20 bytes**, but can go up to **60 bytes** with options.
- The **maximum total packet size is 65,536 bytes**, but most packets are much smaller due to **MTU (Maximum Transmission Unit) constraints** (typically **1500 bytes** for Ethernet).

## **IP Packet Structure**
### **1. Header Fields**
| Field | Description |
|--------|-------------|
| **Version** | Specifies **IPv4 or IPv6** |
| **Internet Header Length (IHL)** | Defines the **header size** (default 20 bytes) |
| **Total Length** | Specifies the **entire packet size** (header + data) |
| **Time to Live (TTL)** | Prevents infinite loops by decrementing at each hop |
| **Protocol** | Indicates the **protocol inside the packet** (TCP, UDP, ICMP, etc.) |
| **Source IP Address** | Identifies the **sender** |
| **Destination IP Address** | Identifies the **recipient** |
| **Fragmentation Information** | Helps divide large packets into smaller chunks |

### **2. Data (Payload)**
- The **actual content** being sent.
- Can be **TCP/UDP data, HTTP requests, ICMP messages, etc.**.

## **Understanding MTU & Fragmentation**
- **MTU (Maximum Transmission Unit)**:
  - Defines the **maximum packet size** that can be transmitted **without fragmentation**.
  - Ethernet MTU is typically **1500 bytes**.
- **Fragmentation**:
  - Occurs when a packet is **larger than the MTU**.
  - The router **splits the packet** into multiple fragments.
  - Each fragment **carries part of the original data** and is reassembled at the destination.
- **Problems with Fragmentation**:
  - **Increases latency**.
  - **Higher chance of packet loss**.
  - Some protocols **disable fragmentation** for performance reasons (e.g., QUIC, which runs over UDP).

## **Time to Live (TTL) & Routing**
- **Why is TTL important?**
  - Prevents **packets from looping endlessly**.
  - Every time a packet **passes through a router**, the TTL value **decreases by 1**.
  - If TTL reaches **zero**, the packet is **discarded** and an ICMP **Time Exceeded** message is sent back to the sender.
- **Used in Traceroute**:
  - Sends packets with **incremental TTL values**.
  - Each router along the path **responds**, allowing mapping of the network route.

### **Explicit Congestion Notification (ECN)**
- Designed to **signal congestion before packet loss occurs**.
- **How it works**:
  - If a router is **experiencing congestion**, it marks the **ECN bits** in the packet.
  - The receiver **acknowledges the congestion**, allowing the sender to **slow down transmissions** before dropping packets.
- **Benefit**: **Prevents unnecessary packet loss & improves performance**.

### **IP Packet Lifecycle (Example)**
4. A **client** (192.168.1.2) sends a **TCP request** to a **server** (10.0.0.5).
5. The packet passes through **multiple routers**.
6. Each router **checks the TTL and decrements it**.
7. If the **packet size exceeds the MTU**, it gets **fragmented**.
8. The **destination server receives the packet**, reassembles it (if fragmented), and processes the request.

### **Key Takeaways**
- An **IP packet** consists of **headers + data**.
- The **header contains essential routing information**.
- **TTL prevents infinite loops** by expiring packets over time.
- **MTU constraints affect packet fragmentation & performance**.
- **Explicit Congestion Notification (ECN) helps prevent packet loss**.
- Understanding **IP packet structure** is crucial for **network debugging & performance optimization**.

## ICMP, Ping, TraceRoute

>  Backchannel Attacks: Kind of hidden and secondary communication channel, ICMP Used for getting data that not meant to share


### **Introduction**
- **ICMP (Internet Control Message Protocol)** is a crucial **Layer 3 (Network Layer)** protocol.
- Used for **network diagnostics and error reporting**.
- Common tools that use ICMP:
  - **Ping** – Checks if a host is reachable.
  - **Traceroute** – Maps the path packets take across networks.
- Unlike **TCP/UDP**, ICMP **does not use ports** – it communicates directly between IP addresses.

### **ICMP Features & Functions**
- Designed for **informational and error messages** between hosts and routers.
- **Key ICMP messages include**:
  1. **Echo Request & Echo Reply** – Used in `ping`.
  2. **Destination Unreachable** – When a host/network cannot be reached.
  3. **Fragmentation Needed** – Indicates MTU is too small for packet size.
  4. **Time Exceeded (TTL Expiry)** – Prevents infinite routing loops.
  5. **Redirect Message** – Suggests a better route for communication.
  6. **Source Quench (Deprecated)** – Used for congestion control in early networks.

## **ICMP Header Structure**
- **ICMP messages consist of**:
  - **Type (8 bits)** – Defines the message category.
  - **Code (8 bits)** – Subtype within the ICMP message type.
  - **Checksum (16 bits)** – Ensures message integrity.
  - **Rest of the Header** – Varies depending on the message type.
- **Example:** ICMP Echo Request (`ping`)
  - **Type = 8 (Echo Request)**
  - **Code = 0**
  - **Checksum**
  - **Identifier & Sequence Number**
  - **Payload Data**
## **Security & Firewall Considerations**
- Some **firewalls and ISPs block ICMP** due to security concerns.
- **Why?**
  - Used in **DDoS attacks (ICMP flood, Smurf attack, etc.)**.
  - Can be exploited for **network reconnaissance** (e.g., mapping networks).
- **Impact of Blocking ICMP**:
  - **Breaks ping & traceroute diagnostics.**
  - **Prevents fragmentation-needed messages**, leading to **TCP Black Hole issues**.
  - **May cause slow or broken connections in certain cases.**

## **ICMP in Action**
### **1. Ping (ICMP Echo Request/Reply)**
- Used to **check if a host is alive and measure round-trip time (RTT)**.
- Example:
  ```bash
  ping google.com
  ```
- Output:
  ```
  64 bytes from 142.250.191.142: icmp_seq=1 ttl=113 time=8.4 ms
  ```
- **Key fields explained**:
  - **64 bytes** – Packet size.
  - **icmp_seq** – Sequence number of request.
  - **ttl (Time To Live)** – Number of hops remaining.
  - **time** – Round-trip latency in milliseconds.

### **2. Traceroute (ICMP Time Exceeded)**
- Used to **map the path taken by packets** to a destination.
- Works by sending packets with **incrementing TTL values**, triggering ICMP `Time Exceeded` responses.
- Example:
  ```bash
  traceroute google.com  # Linux/macOS
  tracert google.com      # Windows
  ```
- Each hop along the path is recorded, showing latency per hop.

## **ICMP & TCP Black Hole Issue**
- **Some routers/firewalls block ICMP messages**, causing **hidden connectivity issues**.
- Example:
  - A TCP connection establishes successfully (small packets like SYN/SYN-ACK work).
  - **Large packets require fragmentation, but ICMP is blocked.**
  - The router cannot notify the sender that **fragmentation is needed**.
  - **Result:** TCP packets silently drop, causing mysterious connection failures.

## **Key Takeaways**
- **ICMP is an essential diagnostic protocol at Layer 3.**
- **Used for network testing, error reporting, and routing feedback.**
- **ICMP messages lack ports; they operate purely with IP addresses.**
- **Firewalls blocking ICMP can break troubleshooting tools and affect performance.**
- **Understanding ICMP helps in debugging network issues and optimizing connectivity.**

> **Next Chapter:** Understanding TCP – The Reliable Transport Protocol


## Address Resolution Protocol (ARP)

### **Introduction**
- **ARP (Address Resolution Protocol)** is essential for resolving **IP addresses to MAC addresses**.
- Although ARP is not an **IP protocol**, it helps in the **mapping of IP to MAC addresses** in local networks.
- **Key concepts to understand**:
  - Why do we need ARP?
  - How does ARP resolve MAC addresses?
  - What security risks are associated with ARP?

### **Why Do We Need ARP?**
- **Network communication occurs at multiple layers**:
  - **IP addresses** (Layer 3) are used for logical addressing and routing.
  - **MAC addresses** (Layer 2) are used for actual delivery within a local network.
- Devices **know the IP address** of the destination but **not the MAC address**.
- ARP helps map an IP address to a **corresponding MAC address** before a device can send a frame.

### **How ARP Works**
#### **1. ARP Request** (Broadcast)
- A device that **needs a MAC address** for a known **IP address** sends an ARP request.
- The **ARP request is a broadcast** packet sent to all devices in the subnet.
- Example:
  - **Host A (10.0.0.2) wants to send data to Host B (10.0.0.5).**
  - Host A sends an **ARP request**: *"Who has 10.0.0.5? Tell 10.0.0.2"*.

#### **2. ARP Reply** (Unicast)
- The **device with the matching IP address** (Host B) sends an ARP reply.
- The **reply is unicast**, meaning it is sent **directly** to the requesting device.
- Example:
  - Host B responds: *"10.0.0.5 is at MAC AA:BB:CC:DD:EE: FF"*.
  - Host A stores this in its **ARP table** for future use.

### **The ARP Table (Cache)**
- Each device maintains an **ARP cache** (table) mapping IPs to MAC addresses.
- **Cached ARP entries expire** after a certain period to prevent stale mappings.
- Command to view ARP table:
  - **Windows:** `arp -a`
  - **Linux/macOS:** `arp -n`

## **ARP in Different Scenarios**
### **1. ARP for Same Subnet Communication**
- When two devices are on the **same subnet**, they use ARP to find each other's MAC address.
- Example:
  - **Host A:** `10.0.0.2`
  - **Host B:** `10.0.0.5`
  - Host A sends an **ARP request** to discover Host B's MAC address.

### **2. ARP for Gateway Communication**
- If a device wants to communicate **outside its subnet**, it sends data to the **default gateway**.
- The **default gateway’s MAC address** must be known first.
- Example:
  - **Host A (10.0.0.2/24)** wants to communicate with **8.8.8.8 (Google DNS).**
  - Host A checks the subnet mask and realizes **8.8.8.8 is outside its network**.
  - Host A sends an **ARP request** to find the **gateway’s MAC address**.
  - Once learned, packets are **forwarded to the gateway**, which routes them to the Internet.

### **Security Risks: ARP Spoofing & Poisoning**
- ARP is **inherently insecure** because **it lacks authentication**.
- Attackers can **fake ARP replies**, tricking devices into sending data to a malicious machine.
- **ARP Spoofing Attack Example:**
  1. Attacker sends an ARP reply: *"I am the gateway"*.
	 -  Victim updates its ARP table with the attacker’s MAC address.
  2. The attacker intercepts and modifies all network traffic.
- **Mitigation Strategies:**
  - Use **static ARP entries** for critical devices.
  - Implement **dynamic ARP inspection (DAI)** on network switches.
  - Use **encryption protocols** like HTTPS to protect sensitive data.

### **Key Takeaways**
- **ARP maps IP addresses to MAC addresses** in a local network.
- **ARP requests are broadcasted**, while **ARP replies are unicast**.
- **Devices cache ARP results** in their ARP table to reduce network traffic.
- **ARP is vulnerable to spoofing attacks**, making security precautions necessary.

> **Next Topic:** Network Address Translation (NAT) and how IP addresses are managed across networks.

## Capturing  IP, ARP and ICMP Packets

See tcpdump man pages. 

## Routing Example.

Switch works as Layer 2, they are smart to know which physical port (RJ 45) to send the data.

Hubs are not smart they send the request to all. 

Router play role for Layer 3 and layer 2 as well if you don't have switch in between.


### UnderStanding Subnet Mask Calculations 

Usable IPs=2(32−subnet bits)−2

255.255.255.0 = 2 (8) -2 = 254
255.255.254.0 = 2 (9) -2 = 510
255.255.253.0= 2 (10) - 2 = 1022

# Section 4: User Datagram Protocol (UDP)

## **Introduction**
- **UDP (User Datagram Protocol)** is a simple, lightweight, and fast **Layer 4 protocol** that sits on top of **IP (Layer 3)**.
- Unlike **TCP**, UDP is **connectionless and stateless**, meaning it does not require prior communication or maintain any session information.
- UDP is widely used in applications where **low latency** and **real-time communication** are critical.
## **Why UDP?**
- **No connection establishment** – No handshake required; data can be sent immediately.
- **Low overhead** – Only an **8-byte header**, compared to TCP’s **20+ bytes**.
- **No retransmissions** – If a packet is lost, UDP does not attempt to recover it.
- **Fast and efficient** – Suitable for applications that **do not require reliability**.

## **Key Features of UDP**
- **Connectionless** – Each packet (datagram) is **independent**.
- **Unreliable** – No guarantee of delivery, order, or duplicate protection.
- **Stateless** – Server does not maintain any client session.
- **Uses Ports** – Allows multiple applications on the same device to communicate via **port numbers**.
- **Low Latency** – Used in real-time applications where speed is more important than reliability.
## **Common Use Cases for UDP**
9. **Video Streaming** – Minor data loss is acceptable for real-time performance.
10. **VoIP (Voice over IP) and WebRTC** – Communication protocols require fast, low-latency transmission.
11. **DNS (Domain Name System)** – Queries are small and need quick responses.
12. **Online Gaming** – High-speed data exchange where missing a few packets is tolerable.
13. **VPNs (Virtual Private Networks)** – Reduces overhead for encrypted tunnels.

## **UDP Packet Structure**
UDP packets have a **simple header format**, which consists of **only 4 fields (8 bytes total)**:

| Field          | Size  | Description |
|---------------|-------|-------------|
| **Source Port** | 2 Bytes | Port number of the sender |
| **Destination Port** | 2 Bytes | Port number of the receiver |
| **Length** | 2 Bytes | Total size of the UDP packet (header + data) |
| **Checksum** | 2 Bytes | Error-checking mechanism (optional) |
| **Data** | Variable | The actual application data |

- The **checksum** field is used for error detection but is **optional** in IPv 4 (mandatory in IPv 6).
- The **length** field helps in parsing the packet correctly.

## **Multiplexing and Demultiplexing in UDP**
- **Multiplexing** – Multiple applications can use UDP by **binding to different ports** on the same IP address.
- **Demultiplexing** – When a UDP packet arrives, the OS directs it to the correct application **based on the destination port**.
- **Example:**
  - A **DNS request (port 53)** and a **VoIP call (port 5060)** can occur simultaneously on the same machine.

## **How UDP Works (Example Communication)**
14. **Client Application (App A) wants to send data to Server Application (App X):**
   - **Client IP:** `10.0.0.1`, **Client Port:** `55555`
   - **Server IP:** `10.0.0.2`, **Server Port:** `53`
   - The packet structure:
     - **Source IP:** `10.0.0.1`
     - **Destination IP:** `10.0.0.2`
     - **Source Port:** `55555`
     - **Destination Port:** `53`
     - **Data:** DNS Query
15. **Server responds with a reply:**
   - The **destination and source ports are swapped** to correctly route the response.
   - This ensures the client receives the data at the correct process.
## **Limitations of UDP**
- **No Reliability** – If a packet is lost, the sender will not retransmit it.
- **No Flow Control** – No mechanism to prevent overwhelming the receiver.
- **No Congestion Control** – Can lead to network congestion.
- **Message Size Limit** – UDP packets are limited to **65,535 bytes**, but most networks impose a lower limit (~1500 bytes MTU).

## **Summary**
- **UDP is a lightweight, fast, and connectionless protocol** that operates at **Layer 4**.
- **Stateless and unreliable**, but **efficient for real-time communication**.
- **Used in video streaming, VoIP, gaming, DNS, and VPNs**.
- **Multiplexing and demultiplexing** allow multiple applications to use UDP simultaneously.
- **No built-in retransmission, congestion control, or flow control** (handled by the application layer if needed).

## Sockets, Sockets, and Queues

### **Introduction**
- In this section, we dive into **TCP sockets**, connection handling, and **kernel networking data structures**.
- Understanding how **connections are established, managed, and queued** is essential for optimizing network applications.
- We explore how **Linux handles sockets and connection queues**, and why efficient handling is critical for scalability.

## **Sockets and Their Role**
### **What is a Socket?**
- A **socket** is an abstraction that represents an **endpoint for communication**.
- In **Linux**, a socket is a **file descriptor**, while in **Windows**, it is an **object**.
- Sockets are used to **send and receive data over a network**.

### **Types of Sockets**
16. **Listening Socket** – A server socket that waits for connections.
17. **Connected Socket** – An established connection between a client and a server.

### **Listening on a Socket**
- A server **binds to an IP and port** and calls `listen()` to **start accepting connections**.
- It can **listen on all interfaces** (`0.0.0.0` for IPv 4 or `[::]` for IPv 6), which is risky as it exposes the service publicly.

## **Connection Lifecycle & TCP Handshake**
### **Three-Way Handshake (TCP)**
18. **Client sends SYN** to initiate a connection.
19. **Server responds with SYN-ACK** to acknowledge the request.
20. **Client sends ACK** to complete the handshake.

Once completed, a **full connection is established**, and data transfer can begin.

## **Socket Queues in the Kernel**
When a server listens, **two important queues** are created:
21. **SYN Queue** (Incomplete Connection Queue)
   - Holds **half-open connections** waiting for the final ACK.
   - If an attacker sends many SYNs but never completes the handshake, it can **exhaust this queue (SYN Flood Attack)**.
22. **Accept Queue** (Completed Connection Queue)
   - Holds **fully established connections** waiting for the application to accept them.
   - If the application is slow to accept connections, the queue fills up and **new connections get dropped**.

### **Backlog and Its Impact**
- `listen(backlog)` determines **how many connections can be queued** before being dropped.
- If the backlog is too small, high-traffic applications **may reject new connections**.

## **Accepting Connections**
### **How Accept Works**
23. A new connection is placed in the **Accept Queue**.
24. The application calls `accept()` to retrieve the connection.
25. A new **file descriptor** is assigned to the connection.
26. Each connection gets **its own socket descriptor**, allowing data exchange.

### **Potential Issues**
- If `accept()` is **not called fast enough**, the **Accept Queue fills up**, causing **denied connections**.
- Slow applications must **optimize accept handling** or scale with **multiple workers**.

## **Socket Sharding for Scalability**
### **What is Socket Sharding?**
- A technique that allows **multiple processes or threads** to listen on the **same port**, distributing connections efficiently.
- Implemented using `SO_REUSEPORT`, allowing **load balancing at the kernel level**.

### **Two Approaches**
27. **Forking Process After Binding**
   - A single process listens, then forks multiple child processes, sharing the **same socket file descriptor**.
   - Each child can accept connections from the **shared Accept Queue**.
28. **Separate Sockets for Each Process**
   - Each process **creates its own socket** but listens on the **same IP and port**.
   - The **kernel load-balances new connections** across the processes.

### **Who Uses Socket Sharding?**
- **NGINX, Envoy, HAProxy** use socket sharding to efficiently handle **high traffic loads**.

## **Security Concerns and DDoS Attacks**
### **SYN Flood Attack**
- Attackers **send many SYN requests** but never complete the handshake.
- This **fills up the SYN Queue**, preventing legitimate users from connecting.

### **Mitigation Strategies (Cloudflare & Linux Kernel)**
29. **SYN Cookies** – The server responds to SYNs with a cookie instead of storing state.
30. **Reducing SYN Timeout** – Dropping half-open connections faster.
31. **Rate Limiting & Firewalls** – Filtering out suspicious traffic.
32. **DDoS Protection Services** – Services like **Cloudflare**, which analyze and block malicious traffic.


## **Summary**
- **Sockets manage network connections**, with separate listening and connected sockets.
- **The Linux Kernel maintains connection queues**: `SYN Queue` and `Accept Queue`.
- **Backlog size affects scalability** – a small backlog causes dropped connections.
- **Socket sharding distributes traffic across multiple processes**, improving performance.
- **SYN Flood Attacks can overwhelm servers**, but **mitigation techniques like SYN Cookies help protect against them**.

---

# Section 5: Transmission Control Protocol (TCP)

## **Introduction**
- **TCP (Transmission Control Protocol)** is a **Layer 4 protocol** that provides **reliable, ordered, and error-checked** delivery of data.
- Unlike **UDP**, TCP is **connection-oriented** and **stateful**, meaning it establishes and maintains a connection before transmitting data.
- Used in applications where **accuracy and reliability** are more important than speed.

## **Why TCP?**
- **Reliable Delivery** – Ensures all packets arrive at the destination.
- **Order Guarantee** – Data arrives in the correct sequence.
- **Error Checking & Recovery** – Retransmits lost or corrupted packets.
- **Flow & Congestion Control** – Prevents overwhelming the receiver and network.
- **Bi-directional Communication** – Supports continuous two-way data exchange.

## **Key Features of TCP**
- **Connection-Oriented** – Requires a handshake to establish a connection.
- **Stateful** – Maintains a session with unique identifiers.
- **Reliable** – Ensures successful data transmission.
- **Segment Ordering** – Uses sequence numbers to reconstruct the correct order.
- **Error Detection & Correction** – Uses checksums to detect corruption.
- **Flow Control** – Adjusts transmission speed based on receiver capacity.
- **Congestion Control** – Adapts to network conditions to prevent congestion.

## **Common Use Cases for TCP**
- **Web Browsing (HTTP/HTTPS)** – Ensures reliable page loading.
- **File Transfers (FTP, SFTP)** – Guarantees data integrity.
- **Email (SMTP, IMAP, POP 3)** – Reliable message transmission.
- **Database Connections (MySQL, PostgreSQL)** – Ensures consistent transactions.
-  **Remote Shell Access (SSH, Telnet)** – Maintains stable and secure connections.

## **TCP Packet Structure**
TCP packets contain a **header** and **data payload**. The header is **at least 20 bytes** but can extend up to **60 bytes**.

| Field              | Size   | Description |
|------------------|--------|-------------|
| **Source Port**  | 2 Bytes | Port number of the sender |
| **Destination Port** | 2 Bytes | Port number of the receiver |
| **Sequence Number** | 4 Bytes | Order of the transmitted segments |
| **Acknowledgment Number** | 4 Bytes | Confirms received data |
| **Header Length** | 4 Bits | Specifies TCP header size |
| **Flags (SYN, ACK, FIN, etc.)** | 9 Bits | Control bits for connection handling |
| **Window Size** | 2 Bytes | Controls flow of data |
| **Checksum** | 2 Bytes | Error-checking mechanism |
| **Urgent Pointer** | 2 Bytes | Indicates priority data (rarely used) |
| **Options** | Variable | Extra parameters (e.g., maximum segment size) |
| **Data** | Variable | The actual application data |

- TCP headers contain **important control information** to manage the connection and ensure data integrity.
- **Flags** such as **SYN, ACK, FIN** are used to control the connection lifecycle.

## **TCP Connection Establishment (Three-Way Handshake)**
To establish a reliable connection, TCP follows a **three-step handshake**:
2. **Client sends SYN (Synchronize)** – Initiates connection with a sequence number.
3. **Server responds with SYN-ACK (Synchronize-Acknowledge)** – Acknowledges the request and sends its own sequence number.
4. **Client sends ACK (Acknowledge)** – Finalizes connection establishment.

Once this handshake is complete, data transmission can begin.


## **TCP Connection Termination (Four-Way Handshake)**
Closing a TCP connection involves **two FIN (Finish) and ACK (Acknowledge) messages**:
5. **Client sends FIN** – Requests to terminate connection.
6. **Server responds with ACK** – Acknowledges termination request.
7. **Server sends FIN** – Initiates server-side termination.
8. **Client responds with ACK** – Final acknowledgment before closing.

After termination, the connection enters the **TIME_WAIT state** to ensure all delayed packets are handled before fully closing.

## **Reliability Mechanisms in TCP**
9. **Acknowledgments (ACKs)** – Confirms received segments.
10. **Sequence Numbers** – Ensures proper data ordering.
11. **Retransmissions** – Lost packets are resent.
12. **Flow Control (Sliding Window)** – Adjusts data flow based on receiver’s buffer size.
13. **Congestion Control** – Adapts transmission rate based on network congestion.

## **Limitations of TCP**
- **Higher Overhead** – Large headers increase latency.
- **Slow Startup** – Handshakes add initial delay.
- **Not Suitable for Real-Time Applications** – Retransmissions cause delays.
- **Vulnerable to SYN Flood Attacks** – Attackers can exploit the handshake process to overwhelm a server.

---

## **Summary**
- **TCP is a connection-oriented, reliable protocol** designed for accurate data transmission.
- **Three-way handshake establishes connections**, ensuring communication integrity.
- **Ensures ordered, error-free data delivery** with retransmissions and acknowledgments.
- **Used in web browsing, file transfers, email, databases, and secure shell connections**.
- **Higher overhead than UDP but offers better reliability and control**.

##  **Congestion Control in TCP**

### **Introduction**
- In the previous section, we discussed **Flow Control**, which determines **how much data the receiver can handle**.  
- **Congestion Control**, on the other hand, determines **how much data the network can handle** without overwhelming intermediate routers.  
- The goal is to **maximize data flow without causing packet loss** due to congestion.  
- This is controlled using a new mechanism called **Congestion Window (CWND)**, which is maintained **by the sender**.

### **Why is Congestion Control Needed?**
- The **receiver might handle large amounts of data**, but **routers in between may not**.  
- Routers have **limited buffer memory**; if too many packets arrive at once, the buffer **fills up**, leading to **packet drops**.  
- If too many packets are dropped, **TCP retransmissions** flood the network, reducing efficiency.  
- **Congestion Control** prevents excessive retransmissions by dynamically adjusting the **rate of data transmission**.

## **The Congestion Window (CWND)**
- **CWND is a sender-side variable** that dictates how much data can be in-flight without being acknowledged.  
- **CWND starts small and grows dynamically based on network conditions.**  
- The sender **must not exceed the minimum** of:  
  - **Receiver Window (RWND)** → How much the receiver can handle.  
  - **Congestion Window (CWND)** → How much the network can handle.  

**Formula:**  
Effective Window Size = min(RWND, CWND)


## **TCP Congestion Control Algorithms**
TCP uses **two main congestion control algorithms**:

### **1. TCP Slow Start**
- **Goal**: Quickly find the optimal congestion window size **without overwhelming the network**.  
- **How it works**:  
  - The sender **starts with a small CWND (usually 1 MSS - Maximum Segment Size).**  
  - **Each ACK received doubles the CWND**, leading to **exponential growth**.  
  - This process continues **until the CWND reaches a predefined threshold** called **Slow Start Threshold (SSTHRESH)**.  
  - **Once SSTHRESH is reached, TCP switches to the next phase: Congestion Avoidance.**  

#### **Example of TCP Slow Start**
| Round | Packets Sent | ACKs Received | CWND (Max Segments) |
|--------|------------|--------------|---------------------|
| 1      | 1 MSS      | 1 ACK        | 2 MSS              |
| 2      | 2 MSS      | 2 ACKs       | 4 MSS              |
| 3      | 4 MSS      | 4 ACKs       | 8 MSS              |
| 4      | 8 MSS      | 8 ACKs       | 16 MSS             |
| ...    | ...        | ...          | ...                |

- **TCP doubles the CWND every round-trip time (RTT)**, leading to **rapid** but **controlled** growth.  
- Slow start **ends** when CWND reaches **SSTHRESH**, at which point TCP switches to **Congestion Avoidance**.

### **2. TCP Congestion Avoidance**
- **Goal**: Maintain efficient data transfer **without overwhelming the network**.  
- **How it works**:  
  - Instead of **exponential growth**, CWND now **grows linearly** (by 1 MSS per RTT).  
  - The congestion window **only increases if all packets in the window are acknowledged**.  
  - This gradual increase **prevents packet loss due to excessive sending**.  

#### **Example of TCP Congestion Avoidance**
| Round | Packets Sent | ACKs Received | CWND Increase |
|--------|------------|--------------|----------------|
| 1      | 16 MSS    | 16 ACKs      | +1 MSS         |
| 2      | 17 MSS    | 17 ACKs      | +1 MSS         |
| 3      | 18 MSS    | 18 ACKs      | +1 MSS         |
| ...    | ...       | ...          | ...            |

- Unlike **Slow Start**, where CWND grows **exponentially**, here it **increases linearly**.
- **This prevents sudden bursts of packets from overwhelming the network.**

## **Congestion Detection & Handling**
TCP must detect and **react to congestion** dynamically. It uses **two key indicators**:

### **1. Packet Loss (Detected by Timeouts or Triple ACKs)**
- **Timeout (No ACK received)** → Severe congestion detected → **Reset CWND to 1 MSS** and re-enter **Slow Start**.  
- **Triple Duplicate ACKs** → Mild congestion detected → **Reduce CWND by half and switch to Congestion Avoidance**.  

**Actions Taken:**
| Event | CWND Adjustment |
|-------|--------------------|
| Timeout (Severe Congestion) | CWND = 1 MSS, Restart Slow Start |
| Triple ACKs (Mild Congestion) | CWND = CWND / 2, Enter Congestion Avoidance |

## **Explicit Congestion Notification (ECN)**
- Instead of waiting for **packet loss**, routers can **proactively** notify senders **before dropping packets**.  
- **ECN allows routers to mark packets (instead of dropping them) when congestion is detected.**  
- The receiver **notifies the sender**, allowing it to slow down **without retransmissions**.  
- This **reduces packet loss, improves efficiency, and prevents unnecessary retransmissions**.

## **Key Takeaways**
- **Congestion Control** prevents **overloading the network** while maximizing throughput.  
- **CWND (Congestion Window) limits how much data can be in-flight** before ACKs arrive.  
- **TCP Slow Start** → Exponential increase in CWND **until reaching SSTHRESH**.  
- **Congestion Avoidance** → Linear growth **to prevent excessive congestion**.  
- **Packet loss signals congestion**:
  - **Timeouts (severe congestion)** → Reset CWND & Restart Slow Start.  
  - **Triple ACKs (mild congestion)** → Reduce CWND by half & Enter Congestion Avoidance.  
- **Explicit Congestion Notification (ECN)** helps routers **prevent packet loss proactively**.


# ** TCP Slow Start vs Congestion Avoidance**

## **Introduction**
- In the previous lecture, we discussed **Congestion Control** at a high level.
- This lecture provides a **detailed look at TCP Slow Start and Congestion Avoidance**.
- We'll analyze **when each algorithm kicks in, how they modify transmission rates, and what their impact looks like in a chart**.
- This is a **more advanced topic**, requested by many students.

## **Congestion Control Algorithms in TCP**
- There are **two primary congestion control algorithms**:
  1. **Slow Start** → Quickly increases the congestion window size in an **exponential** manner.
  2. **Congestion Avoidance** → Increases the congestion window **linearly** to prevent overwhelming the network.

## **Understanding TCP Slow Start**
### **Why is it called Slow Start?**
- **The congestion window (CWND) starts at 1 Maximum Segment Size (MSS)**.
- This is **considered "slow"** compared to what a fully stable connection might send.
- However, **CWND grows exponentially**, meaning it quickly increases its rate.

### **How Slow Start Works**
- **For every ACK received, the CWND increases by 1 MSS**.
- **If 10 packets are sent, and 10 ACKs are received, CWND increases by 10 MSS**.
- This aggressive expansion **helps quickly determine the available network bandwidth**.

### **Slow Start Growth Example**
| Round | Packets Sent | ACKs Received | New CWND (MSS) |
|--------|------------|--------------|----------------|
| 1      | 1 MSS     | 1 ACK        | 2 MSS          |
| 2      | 2 MSS     | 2 ACKs       | 4 MSS          |
| 3      | 4 MSS     | 4 ACKs       | 8 MSS          |
| 4      | 8 MSS     | 8 ACKs       | 16 MSS         |
| ...    | ...       | ...          | ...            |

- As seen in the table, **CWND doubles every round-trip time (RTT)**.
- **This continues until CWND reaches a threshold** called the **Slow Start Threshold (SSTHRESH)**.
- Once **SSTHRESH is reached, TCP switches to Congestion Avoidance**.

## **Understanding TCP Congestion Avoidance**
### **What Triggers Congestion Avoidance?**
- When **CWND reaches SSTHRESH**, **TCP stops exponential growth**.
- Instead, **it switches to a linear growth model**.

### **How Congestion Avoidance Works**
- **CWND now increases by only 1 MSS per RTT** (instead of doubling like in Slow Start).
- This **prevents overloading the network** while still **allowing for growth**.

### **Congestion Avoidance Growth Example**
| Round | Packets Sent | ACKs Received | New CWND (MSS) |
|--------|------------|--------------|----------------|
| 1      | 16 MSS    | 16 ACKs      | 17 MSS         |
| 2      | 17 MSS    | 17 ACKs      | 18 MSS         |
| 3      | 18 MSS    | 18 ACKs      | 19 MSS         |
| 4      | 19 MSS    | 19 ACKs      | 20 MSS         |

- Growth is now **linear rather than exponential**.
- This method **ensures TCP does not flood the network with excessive data**.

## **Congestion Detection: What Happens When There’s a Problem?**
- **Congestion is typically detected when a packet is lost.**
- There are **two ways TCP detects packet loss**:
  1. **Timeout occurs** (severe congestion).
  2. **Triple duplicate ACKs are received** (moderate congestion).

### **What Happens After Congestion is Detected?**
- **SSTHRESH is updated**: It is set to **half of the current CWND**.
- **CWND is reset**: It is reduced back to **1 MSS**.
- **TCP re-enters Slow Start**: It will now reach SSTHRESH **more quickly than before**.

### **Why SSTHRESH is Reduced**
- SSTHRESH **tracks the highest stable CWND before congestion occurred**.
- If congestion happened at **CWND = 20 MSS**, then **SSTHRESH is set to 10 MSS**.
- This prevents **future congestion issues**.

### **The Minimum SSTHRESH**
- TCP **never lets SSTHRESH go below 2 MSS**.
- This ensures **at least some network capacity is always used**.

## **TCP Slow Start vs. Congestion Avoidance: A Visual Representation**
- The graph below (from RFC 5681) illustrates **how TCP alternates between slow start and congestion avoidance**.

```plaintext
CWND (Bytes)
│
│
│
│            .-----.       .-----.
│           /       \     /       \
│          /         \   /         \
│         /           \_/           \
│-----------------------------------------> Time
        Slow Start    Congestion Avoidance


```


**Network Address Translation (NAT)**

  

**Overview**

• **Network Address Translation (NAT)** was created to address the **IPv4 limitation** of approximately **4 billion addresses**, which is insufficient for the growing number of internet-connected devices.

• **IPv6** offers a solution with a vastly larger address space, but it requires updating all network infrastructure, which is a massive undertaking.

• **NAT** allows multiple internal devices to share a single **public IP address** while maintaining their private IP addresses, enabling seamless access to the internet.

**Why NAT is Necessary**

• In a typical household, multiple devices (e.g., laptops, smartphones, IoT devices, gaming consoles, and TVs) need to access the internet, but not all of them have public IP addresses.

• These devices **share one public IP address** (the IP of the router) and use **private IP addresses** (e.g., 192.168.x.x, 10.x.x.x, 172.16.x.x) within the local network.

• **NAT** solves the problem of limited IPv4 addresses by mapping internal private IPs to a single public IP using unique **source ports**.

**How NAT Works**

• All devices on the internal network appear to the internet as coming from a **single public IP address**, which is the IP of the **router**.

• The **NAT Table** in the router keeps track of each device’s private IP address and port, mapping them to a unique public IP address and port combination.

• This enables the router to correctly route incoming responses back to the originating device within the internal network.

**Example of NAT Mapping**

• **Internal Devices**:

• 192.168.1.2 (Port 8992)

• 192.168.1.3 (Port 8993)

• **Public IP Address**:

• 44.115.70.1

• **NAT Table**:

|**Internal IP**|**Internal Port**|**Public IP**|**Public Port**|
|---|---|---|---|
|192.168.1.2|8992|44.115.70.1|7777|
|192.168.1.3|8993|44.115.70.1|7778|

• The router **rewrites** the source IP and port for outgoing packets and **stores the mapping** in the NAT Table.

• When a response comes back, the router **looks up the NAT Table** to **reverse** the translation and route the packet to the correct internal device.

**Types of NAT**

1. **Static NAT**

• One-to-one mapping between a private IP and a public IP.

• Useful for hosting services like web servers.

2. **Dynamic NAT**

• Maps multiple private IPs to a pool of public IPs dynamically.

• IPs are assigned temporarily and released after use.

1. **Port Address Translation (PAT)**

• Also known as **NAT Overload**.

• Multiple devices share a single public IP by using **different source ports**.

• Most common form of NAT in home and office networks.

**Limitations and Challenges of NAT**

• **Port Limitations**:

• A device can only make **65,535 connections** per public IP due to the **16-bit port range** (0-65535).

• If all ports are exhausted, **new connections will fail**.

• **Connection Tracking**:

• NAT is **stateful**, meaning it must keep track of each active connection.

• This **state tracking** can **consume memory and processing power** on the router.

• **End-to-End Connectivity**:

• NAT **breaks end-to-end connectivity** since internal IPs are hidden.

• Protocols like **IPsec** and peer-to-peer applications face challenges without NAT traversal techniques (e.g., STUN/TURN servers).

**Private vs. Public IP Addresses**

• **Private IP Addresses**:

• Defined by **RFC 1918** and not routable on the public internet.

• Used within private networks.

• Ranges:

• 10.0.0.0/8 (Class A)

• 172.16.0.0/12 (Class B)

• 192.168.0.0/16 (Class C)

• **Public IP Addresses**:

• Routable on the public internet.

• Assigned by **ISPs** and managed by **IANA**.

**Example: Packet Flow with NAT**

2. **Outbound Request**:

• Device 192.168.1.2 sends a request to 55.41.22.88 on port 80.

• Router:

• **Changes** source IP to 44.115.70.1.

• **Changes** source port to 7777.

• **Stores** mapping in the NAT Table.

3. **Inbound Response**:

• Server responds to 44.115.70.1:7777.

• Router:

• **Looks up** the NAT Table entry for port 7777.

• **Changes** destination IP back to 192.168.1.2.

• **Changes** destination port back to 8992.

• **Forwards** packet to 192.168.1.2.

**NAT and Port Forwarding**

• **Port Forwarding**:

• Used to allow external devices to access internal services (e.g., web servers, SSH, gaming servers).

• Example:

• Public 80 → Internal 192.168.1.2:8080

• **Static NAT entry** is created in the router to **map an external port** to an **internal IP and port**.

• **Use Cases**:

• Hosting a website on an internal server.

• Allowing remote SSH access.

• Running multiplayer gaming servers.

**Layer 4 Load Balancing using NAT**

• **Layer 4 Load Balancing**:

• Distributes traffic across multiple servers using **NAT rules**.

• Implemented using a **Virtual IP (VIP)** that maps to a pool of backend servers.

• Example:

• VIP 100.100.100.100 is mapped to backend servers:

• 192.168.1.10

• 192.168.1.11

• 192.168.1.12

• **Round-robin** or **Least Connection** algorithms are commonly used for balancing.

• **Advantages**:

• **Scalable**: Handles high traffic loads efficiently.

• **Redundancy**: Ensures high availability.

**Security Implications of NAT**

• **Advantages**:

• **Hides Internal IPs**: Devices behind NAT are not directly accessible from the internet.

• **Stateful Packet Inspection**: NAT maintains connection states, preventing unsolicited inbound traffic.

• **Disadvantages**:

• **Breaks End-to-End Connectivity**: Some protocols require additional configuration for NAT traversal.

• **Vulnerable to NAT Traversal Attacks**: Techniques like **NAT hole punching** can bypass NAT security.

• **Complicates Network Troubleshooting**: Tracking connections is harder due to address translation.

**NAT and IPv6**

• **IPv6**:

• Designed to **replace IPv4** with a much larger address space (2^128 addresses).

• **NAT is not needed** in IPv6, as every device can have a unique public IP.

• Adoption is **slow** due to the cost and complexity of updating infrastructure.

• **NAT64 and DNS64**:

• **NAT64** allows IPv6-only clients to access IPv4 servers.

• **DNS64** provides IPv6 addresses for IPv4-only resources.

**Key Takeaways**

• **NAT** solves the IPv4 address shortage by allowing multiple devices to share a single public IP.

• **NAT Table** keeps track of private-to-public IP mappings using unique source ports.

• **Port Forwarding** and **Layer 4 Load Balancing** are practical applications of NAT.

• **IPv6** eliminates the need for NAT but faces challenges in adoption.

• **Security and connectivity issues** arise due to NAT’s stateful nature and address translation.

Continue to the next topic: **Layer 4 Load Balancing**.