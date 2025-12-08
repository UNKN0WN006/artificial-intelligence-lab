# WMN 2022 — FULL SOLUTIONS (Answer all questions)

Source: WMN @22.pdf (Question Paper) and Lecture Notes.

---

## Q.1 Answer any one (10 marks total)

### (a) i) Describe the steps used in a handoff process of a cellular system. (5 marks)

**Definition:** Handoff (or Handover, **HO**) is the process of transferring an active call or data session from the current serving cell (Base Transceiver Station, **BTS**) to a new target cell as the Mobile Station (**MS**) moves.

#### 📝 Handoff Steps:
1.  **Measurement:** The MS continuously measures the signal strength/quality (e.g., RSSI, BER) of the serving BTS and all neighboring BTSs, sending **Measurement Reports** back to the Serving BTS/BSC.
2.  **Decision:** The Serving **BSC/MSC** (or the network) decides whether a handoff is necessary, typically based on signal quality thresholds (e.g., serving signal drops below a threshold, or a neighbor's signal exceeds the serving signal by a margin).
3.  **Resource Reservation:** The network checks the target BTS/BSC for available radio resources (channel, time-slot) and reserves them for the MS.
4.  **Handoff Command:** The Serving BSC/MSC issues a **Handoff Command** to the MS (and the target BTS) instructing the MS to switch its channel and timing parameters.
5.  **Link Establishment & Switching:** The MS tunes to the new reserved channel and establishes a connection with the target BTS. The process concludes with an **HO Complete Acknowledge**.
6.  **Release Old Resources:** The network releases the channel resources previously occupied by the MS on the old serving BTS/BSC.
7.  **Update Databases:** Location registers (**VLR/HLR**) are updated if the handoff crosses a Mobile Switching Center (**MSC**) boundary.

> **Remarks:** **Hard Handoff** (2G, FDMA/TDMA) is 'break-before-make', where the old link is dropped before the new one is established. **Soft Handoff** (CDMA/3G) is 'make-before-break', maintaining simultaneous links to multiple cells during the transition.



---

### (a) ii) Main physical reason for failure of wired MACs in wireless & the wired remedy. (5 marks)

#### 1. Reason for Failure in Wireless
The main reason for the failure of wired MAC schemes like **CSMA/CD** (Carrier Sense Multiple Access with Collision Detection) in wireless networks is the **hidden-terminal problem** and the **inability to sense collisions while transmitting**.
* **Hidden Terminal:** Nodes cannot hear each other, resulting in simultaneous transmission to a common receiver (collision), despite their individual carrier sense showing the channel is idle.
* **Half-Duplex Radios:** Wireless radios are typically half-duplex, meaning they **cannot transmit and listen (detect collisions) simultaneously** due to the high difference in power between the transmitted signal and the received signal.

#### 2. Wired Network Remedy
In wired Ethernet, **CSMA/CD** is used. It avoids the issues above because:
* The wired medium allows a node to reliably detect a collision (e.g., by monitoring the energy level or signal signature on the wire) while it is transmitting.
* Upon detecting a collision, the node sends a **jam signal** and executes a **binary exponential backoff** algorithm before retrying.

#### 3. Wireless Remedy (Brief)
Wireless networks (e.g., 802.11 WLAN) use **CSMA/CA** (**Collision Avoidance**), relying on mechanisms like **RTS/CTS** (Request-to-Send/Clear-to-Send) and **NAV** (Network Allocation Vector) to **prevent** collisions, rather than attempting to detect them after they occur.

---

### (b) i) Comment on the services provided by 1G, 2G, 3G, 4G, and 5G wireless systems. (5 marks)

| Generation | Key Technology & Standard | Primary Service / Capability |
| :--- | :--- | :--- |
| **1G** | Analog (AMPS, NMT) | **Analog Voice** (mobile telephony). |
| **2G** | Digital (GSM, CDMAOne) | **Digital Voice** (better security/capacity) + **SMS** + basic circuit-switched data. |
| **3G** | Packet Switching (UMTS, CDMA2000) | **Mobile Broadband** (multimedia, web browsing, email) with higher data rates ($\sim$384 kbps to 2 Mbps). |
| **4G** | All-IP (LTE, WiMAX) | **High-Speed Mobile Broadband** (HD video, fast browsing, seamless multimedia, low latency). All services delivered over IP. |
| **5G** | New Radio (NR) | **Enhanced Mobile Broadband** (eMBB), **Ultra-Reliable Low-Latency Communications** (URLLC), and **Massive IoT** (mMTC). Supports network slicing. |

---

### (b) ii) Channel calculation — numerical (5 marks)

**Given:**
* Total System Bandwidth ($B_{total}$) = 33 MHz = 33,000 kHz.
* Bandwidth per full-duplex voice/control channel = two 25 kHz simplex channels = $2 \times 25 \text{ kHz} = 50 \text{ kHz}$.
* Frequency Reuse Factor ($K$) = 4 cells.

**Calculation:**

1.  **Total Duplex Channels Available ($C_{total}$):**
    $$C_{total} = \frac{B_{total}}{\text{BW per duplex channel}}$$
    $$C_{total} = \frac{33{,}000 \text{ kHz}}{50 \text{ kHz}} = 660 \text{ channels}$$

2.  **Channels Per Cell ($C_{cell}$):**
    $$C_{cell} = \frac{C_{total}}{K}$$
    $$C_{cell} = \frac{660}{4} = 165 \text{ channels per cell}$$

**Answer:** There are **165 channels per cell**.

---
---

## Q.2 Answer any one (12 marks total)

### (a) i) CDMA chip question — detect bits (7 marks)

**Given Chip Sequences (Bipolar):**
| User | Original Sequence (0, 1) | Bipolar Sequence ($\mathbf{C}$) (+1, -1) |
| :--- | :--- | :--- |
| A | (0, 1, 0, 0, 1, 1) | $\mathbf{A} = (-1, +1, -1, -1, +1, +1)$ |
| B | (1, 1, 0, 1, 0, 1) | $\mathbf{B} = (+1, +1, -1, +1, -1, +1)$ |

**Given Transmission:** A sends bit $\mathbf{1}$ (sends $\mathbf{A}$); B sends bit $\mathbf{0}$ (sends $-\mathbf{B}$).

#### 1. Compute Transmitted Signal $\mathbf{S}$:
$$\mathbf{S} = \mathbf{A} + (-\mathbf{B})$$
$$\mathbf{A}: \quad (-1, \phantom{-}1, -1, -1, \phantom{-}1, \phantom{-}1)$$
$$-\mathbf{B}: (-1, -1, \phantom{-}1, -1, \phantom{-}1, -1)$$
$$\mathbf{S}: \quad (-2, \phantom{-}0, \phantom{-}0, -2, \phantom{-}2, \phantom{-}0)$$

#### 2. Compute Received Signal $\mathbf{R}$ (with Noise $\mathbf{N}$):
Given Noise $\mathbf{N} = (1, -1, 0, 1, 0, -1)$.
$$\mathbf{R} = \mathbf{S} + \mathbf{N}$$
$$\mathbf{S}: \quad (-2, \phantom{-}0, \phantom{-}0, -2, \phantom{-}2, \phantom{-}0)$$
$$\mathbf{N}: \quad (\phantom{-}1, -1, \phantom{-}0, \phantom{-}1, \phantom{-}0, -1)$$
$$\mathbf{R}: \quad (-1, -1, \phantom{-}0, -1, \phantom{-}2, -1)$$

#### 3. Detection (Correlate $\mathbf{R}$ with Chip Sequences):

* **For User A:** Calculate inner product $\mathbf{R} \cdot \mathbf{A}$
    $$\mathbf{R} \cdot \mathbf{A} = (-1)(-1) + (-1)(1) + (0)(-1) + (-1)(-1) + (2)(1) + (-1)(1)$$
    $$\mathbf{R} \cdot \mathbf{A} = 1 - 1 + 0 + 1 + 2 - 1 = 2$$
    Since the result is **positive** ($+2$), User A's transmitted bit is $\mathbf{1}$.

* **For User B:** Calculate inner product $\mathbf{R} \cdot \mathbf{B}$
    $$\mathbf{R} \cdot \mathbf{B} = (-1)(1) + (-1)(1) + (0)(-1) + (-1)(1) + (2)(-1) + (-1)(1)$$
    $$\mathbf{R} \cdot \mathbf{B} = -1 - 1 + 0 - 1 - 2 - 1 = -6$$
    Since the result is **negative** ($-6$), User B's transmitted bit is $\mathbf{0}$ (since $\text{negative } \to \mathbf{-1} \to \text{bit } \mathbf{0}$).

**Answer:** The receiver detects that User A sent bit **1** and User B sent bit **0**.

---

### (a) ii) Role of HLR and VLR in WWAN architecture (5 marks)

#### 1. HLR (Home Location Register)
* **Role:** The **permanent, central database** for a subscriber within their home network.
* **Functions:** Stores the subscriber's profile (e.g., services allowed, authentication keys), their permanent Mobile Station ISDN Number (**MSISDN**), and, crucially, the address of the **VLR** currently serving the subscriber. It is the primary reference point for incoming calls.

#### 2. VLR (Visitor Location Register)
* **Role:** A **temporary, distributed database** associated with an MSC.
* **Functions:** Stores a copy of the essential subscriber information (e.g., authentication parameters) and the precise location area of every mobile user **currently roaming within that MSC's geographic service area**. It caches data from the HLR when a user enters the area, enabling local call setup and mobility management without querying the HLR for every transaction.

---

### (b) i) CDMA bandwidth per user (6 marks)

**Given:** Total BW = 200 MHz, Number of Users = 100.

**Assumption:** Assuming the bandwidth is shared equally (a simple, required allocation based on the typical exam context).

$$\text{BW per user} = \frac{\text{Total Bandwidth}}{\text{Number of Users}}$$
$$\text{BW per user} = \frac{200 \text{ MHz}}{100} = 2 \text{ MHz per user}$$

**Answer:** The bandwidth per user is **2 MHz**.

---

### (b) ii) Three important entities in GSM architecture and functions (6 marks)

| Entity | Full Name | Primary Functions |
| :--- | :--- | :--- |
| **BTS** | **Base Transceiver Station** | Handles the **radio interface** with the MS: transmitting/receiving radio signals, modulation/demodulation, channel coding. |
| **BSC** | **Base Station Controller** | Controls multiple BTSs: manages **radio resource allocation**, **frequency assignment**, and handles **handovers** between BTSs within its control area. |
| **MSC** | **Mobile Switching Center** | The core network switch: provides **switching functions**, handles mobility management, interfaces with HLR/VLR, and provides **interconnection to the PSTN/other networks**. |

---
---

## Q.3 Answer any one (12 marks total)

### (a) i) Compare CSMA/CD with CSMA/CA (3 marks)

| Feature | CSMA/CD (Collision Detection) | CSMA/CA (Collision Avoidance) |
| :--- | :--- | :--- |
| **Where Used** | Wired Networks (Ethernet) | Wireless Networks (IEEE 802.11 WLAN) |
| **Collision Handling** | **Detects** collisions during transmission, then aborts and retries. | Attempts to **Prevent** collisions before transmission. |
| **Mechanism** | Carrier Sense, **Collision Detection**, Jam signal, Backoff. | Carrier Sense, **Inter-Frame Spaces (IFS)**, **Random Backoff**, RTS/CTS, NAV. |
| **Feasibility** | Feasible in wired media where nodes can monitor own signal. | Necessary in wireless where collision detection is unreliable (half-duplex, hidden terminal). |

---

### (a) ii) Method for clock synchronization in infrastructure WLAN (3 marks)

The primary method for clock synchronization in an infrastructure WLAN (802.11) is **Beacon-Based Synchronization**.

* **Mechanism:** The **Access Point (AP)** periodically transmits **Beacon frames**.
* These Beacons contain a **Timestamp** value (the AP's current local time).
* All associated **Stations (STAs)** listen for these beacons and synchronize their local clocks to the AP’s timestamp.
* This ensures that all devices in the Basic Service Set (**BSS**) operate on a common time base, which is crucial for power management and channel coordination.

---

### (a) iii) How fairness is solved in IEEE 802.11 — with diagram (6 marks)

IEEE 802.11 employs several mechanisms to ensure fairness and prevent a single station from capturing the channel:

1.  **Inter-Frame Spaces (IFS):** Different priorities are enforced by different waiting times (e.g., **DIFS** for standard data, **SIFS** for ACKs/CTS, **PIFS** for priority traffic). Longer waits ensure lower-priority traffic gives way to high-priority traffic.
2.  **Random Backoff and Contention Window (CW):** After sensing the channel idle for DIFS, a station chooses a **random slot** from its Contention Window ($CW$). This probabilistic delay ensures that even if multiple stations want to transmit, they will likely choose different slots, granting access to a different station each time. The CW size increases upon collision, further dampening aggressive channel attempts.
3.  **RTS/CTS and NAV (Virtual Carrier Sense):**
    * **RTS/CTS** mitigates the **hidden terminal problem**.
    * Any station that hears the CTS (or RTS) frame reads the **duration field** and sets its **Network Allocation Vector (NAV)**.
    * The **NAV** acts as a timer for a reserved duration, ensuring the station remains silent even if its physical carrier sense shows the channel is idle. This virtual carrier sense ensures all stations, including hidden ones, respect the reservation, providing fairness and channel control.



---

### (b) i) Roaming in WLAN (4 marks)

**Roaming** occurs when a Mobile Station (**MS**) moves its connection from one Access Point (**AP1**) to another (**AP2**) within the same Extended Service Set (**ESS**) or Distribution System (**DS**).

#### 📝 Roaming Steps (Reassociation):
1.  **Scanning:** The MS actively or passively scans for and detects beacons from neighboring APs (e.g., AP2).
2.  **Authentication:** The MS authenticates with the target AP (AP2).
3.  **Reassociation Request:** The MS sends a **Reassociation Request** to AP2, which forwards it to the Distribution System (**DS**).
4.  **Context Transfer:** The DS/AP system transfers the MS's connection context (e.g., security keys, QoS profile) from AP1 to AP2 to ensure continuity.
5.  **Data Flow Switch:** The DS updates its internal routing table to forward the MS's packets to AP2. The old AP (AP1) releases the MS's resources.



---

### (b) ii) Power management scheme for infrastructure WLAN (4 marks)

The standard IEEE 802.11 Power Management scheme is **Power Save Mode (PSM)**:

1.  **Sleep Mode Notification:** The Station (**STA**) informs the **AP** (by setting a bit in its frames) that it is going into sleep (Power Save) mode.
2.  **Buffering:** The AP buffers any frames destined for the sleeping STA.
3.  **Traffic Indication Map (TIM):** The AP includes a **TIM** in its periodic **Beacon** frames, indicating which sleeping STAs have buffered data waiting.
4.  **Wake-up & PS-Poll:** The STA wakes up periodically (matching the beacon interval), checks the TIM in the beacon. If the TIM indicates buffered data, the STA sends a **PS-Poll** frame to the AP to request the frames.
5.  **Delivery:** The AP sends the buffered data frames to the STA, which then returns to sleep.

This mechanism minimizes the time the radio is 'on', significantly saving battery power.

---

### (b) iii) How collision is avoided using NAV in WLAN (4 marks)

**NAV (Network Allocation Vector):** The virtual carrier-sensing mechanism used in 802.11.

* **Setting the NAV:** When a node (Station or AP) overhears a frame that reserves the medium (e.g., RTS, CTS, or DATA), it reads the **Duration/ID field** in the frame header.
* The node then sets its **NAV** timer to this duration.
* **Collision Avoidance:** While a node's NAV counter is running ($NAV > 0$), the node is **precluded from transmitting**—even if its physical carrier sensing indicates the channel is momentarily idle.
* This effectively reserves the channel time (virtually) for the primary sender/receiver pair, ensuring that terminals (especially hidden terminals) defer transmission, thus avoiding collisions.

---
---

## Q.4 Answer any one (12 marks total)

### (a) i) What is neighbor discovery / address autoconfiguration in MIPv6? (3 marks)

**Neighbor Discovery (ND) Protocol** in IPv6 allows a Mobile Node (**MN**) to discover routers and configure IP addresses autonomously (autoconfiguration).

* **Stateless Autoconfiguration:** The MN uses **Router Advertisement (RA)** messages sent by local routers to learn the network prefix. It then combines this prefix with its interface ID (derived from its MAC address) to form a unique IPv6 address (its **Care-of-Address, CoA**).
* **MIPv6 Relevance:** In MIPv6, the MN uses ND to quickly learn the foreign network prefix and auto-configure a valid, local **Co-located Care-of-Address (CCoA)** upon arriving in a foreign network, eliminating the need for a Foreign Agent (FA).

---

### (a) ii) Method to achieve soft handoff in MIPv4 & triangular routing solution (4 marks)

#### Soft Handoff in MIPv4 (Conceptual)
The MIPv4 standard does not natively define soft handoff, but the concept is achieved by:
1.  Maintaining tunnels to **both the old Foreign Agent (FA) and the new FA** during the transition period (**make-before-break**).
2.  The Home Agent (HA) can simultaneously forward duplicate packets to both FAs for a short duration, minimizing packet loss.
3.  Once the MN is successfully registered with the new FA, the old tunnel is released.

#### Triangular Routing Problem
* **Problem:** In MIPv4, a Correspondent Node (**CN**) always sends packets to the MN's **Home Address (HoA)**. The **Home Agent (HA)** intercepts these packets and **tunnels** them to the MN's current Care-of-Address (**CoA**) at the Foreign Agent (**FA**).
* **Effect:** This creates a long, inefficient path (**CN $\to$ HA $\to$ FA $\to$ MN**), forming a "triangle" and introducing unnecessary latency and load on the HA.

---

### (a) iii) When/how is mobility binding created between CN and MN? How does binding optimize the route? (5 marks)

#### When/How Binding is Created
1.  **Trigger:** After the MN moves to a new location and registers its new **Care-of-Address (CoA)** with its Home Agent (**HA**).
2.  **Binding Update (BU):** The MN sends a **Binding Update (BU)** message directly to the Correspondent Node (**CN**) to inform the CN of its current CoA.
3.  **Binding Acknowledgement (BA):** The CN receives the BU and replies with a **Binding Acknowledgement (BA)**.
4.  **Binding Cache:** Upon receiving the BU, the CN stores the $\text{Home Address} \leftrightarrow \text{Care-of-Address}$ mapping in its **Binding Cache**.

#### Route Optimization Effect
By storing the binding, the CN can bypass the HA detour:
* Subsequent packets from the CN are sent **directly to the MN's CoA**.
* This removes the triangular path, resulting in **lower latency**, **reduced network load** on the HA, and **improved overall throughput**.

---

### (b) i) Pre-handoff & post-handoff mechanisms in MIP (3 marks)

| Mechanism | Description | Goal |
| :--- | :--- | :--- |
| **Pre-handoff** | Actions taken *before* the attachment point changes: e.g., predictive handover initiation, requesting resources/pre-registering a CoA in the target network. | Minimize packet loss and latency during the transition. |
| **Post-handoff** | Actions taken *after* the new connection is established: e.g., completing registration with the target FA/HA, sending **Binding Update (BU)** to the CNs, retrieving buffered packets. | Re-establish full connectivity and initiate route optimization quickly. |

---

### (b) ii) Difference between care-of-address and co-located care-of-address (2 marks)

| Address Type | Description | MIPv4/MIPv6 |
| :--- | :--- | :--- |
| **Care-of-Address (CoA)** | A temporary address used by the MN while away from home. Typically the address of the **Foreign Agent (FA)** in MIPv4. | MIPv4/MIPv6 |
| **Co-located CoA (CCoA)** | An address the MN configures and uses on its own interface. The MN obtains the address (e.g., via DHCP or stateless autoconfig) and registers it directly with the HA. **No FA is involved.** | MIPv4/MIPv6 (Prevalent in MIPv6) |

---

### (b) iii) MIPv6: message sending based on CN knowledge. Advantages of MIPv6 vs MIPv4 (7 marks)

#### 1. Message Sending based on CN Knowledge

| CN's Knowledge | Packet Destination (Initial) | Path |
| :--- | :--- | :--- |
| **CN knows MN's CoA** | CN sends to MN's **CoA** using a **Routing Header** to carry the original Home Address semantics. | **Route-optimized** (direct path). |
| **CN does NOT know CoA** | CN sends to MN's **Home Address (HoA)**. | **Triangular path** (HoA $\to$ HA $\to$ MN). HA forwards the packet to the CoA. |

#### 2. Advantages of MIPv6 over MIPv4

* **No Foreign Agent (FA) Needed:** MNs can easily use **Co-located Care-of-Addresses** via IPv6 Stateless Autoconfiguration, eliminating the need for FA infrastructure.
* **Built-in Route Optimization:** Route optimization is natively supported using standard IPv6 extension headers (Routing Header and Destination Options), making the process more seamless and efficient.
* **Security:** MIPv6 has improved security features, specifically using the **Return Routability Procedure** (for verifying ownership of CoA) and better integration with **IPsec** for securing Binding Updates.
* **Efficiency:** The design of MIPv6 (e.g., larger address space, simplified autoconfiguration) inherently provides a more scalable and efficient mobility solution.

---
---

## Q.5 Answer any one (12 marks total)

### (a) i) Compare source routing and hop-by-hop routing (3 marks)

| Feature | Source Routing (e.g., DSR) | Hop-by-Hop Routing (e.g., AODV, DSDV) |
| :--- | :--- | :--- |
| **Route Storage** | Route stored entirely in the **packet header** by the source. | Route stored in **routing tables** at each intermediate node. |
| **Overhead** | High **header overhead** (header size grows with path length). | Low header overhead, but high **routing table maintenance overhead**. |
| **Forwarding** | Intermediate nodes simply read the next hop from the header. | Intermediate nodes look up the next hop in their routing table. |

---

### (a) ii) Why is routing in multi-hop ad-hoc networks complicated? (3 marks)

Routing in Mobile Ad-hoc Networks (**MANETs**) is complicated due to:

* **Highly Dynamic Topology:** Node mobility causes frequent, unpredictable link breakages and topology changes, making route maintenance extremely difficult.
* **Limited Resources:** Nodes often run on battery power, requiring routing protocols to be **energy-aware** and minimize control traffic overhead.
* **Wireless Link Unreliability:** Wireless links suffer from fading, interference, and noise, leading to high bit error rates (**BER**) and **asymmetric** link quality, which complicates reliable path selection.
* **Lack of Infrastructure:** The network is completely distributed, requiring protocols to perform costly distributed route discovery and maintenance.

---

### (a) iii) Why DSR better than AODV in highly dynamic environments? (3 marks)

**DSR (Dynamic Source Routing)** is often considered better than **AODV (Ad-hoc On-demand Distance Vector)** in highly dynamic environments primarily due to its **caching of multiple routes** and its **reactive nature**.

* **Route Caching:** DSR caches multiple discovered routes in its **Route Cache**. When the active link breaks, DSR can immediately switch to an alternate cached route without initiating a new, costly **Route Discovery** process.
* **AODV Overhead:** AODV relies on a single, fresh routing table entry. A link break necessitates a new route discovery via a network-wide broadcast, which adds significant delay and control overhead under rapid topology changes.

---

### (a) iv) How does DSDV avoid count-to-infinity? (3 marks)

**DSDV (Destination-Sequenced Distance-Vector)** avoids the classical Distance Vector **count-to-infinity** problem using **Destination Sequence Numbers**.

1.  **Sequence Numbers:** Each destination maintains and attaches a **monotonically increasing sequence number** to every route update it originates.
2.  **Freshness Preference:** When a node receives two updates for the same destination, it prefers the route with the **highest (freshest) sequence number**, regardless of hop count.
3.  **Loop Prevention:** If two routes have the same sequence number, the node chooses the one with the better metric (fewer hops). This sequence number mechanism ensures that stale, looped routes are immediately discarded, preventing the metric from counting to infinity in a loop.

---

### (b) i) DSR — Route Discovery & Route Maintenance (5 marks)

#### 1. Route Discovery (Finding a Route)
* **Initiation:** Source node broadcasts a **Route Request (RREQ)** packet containing the full route taken so far.
* **Route Accumulation:** Intermediate nodes append their own addresses to the route list in the RREQ header (this is **Source Routing**).
* **Reply:** The destination (or an intermediate node that has a valid route to the destination in its cache) replies by sending a **Route Reply (RREP)** back to the source, carrying the full source route.
* **Caching:** The source caches this route and uses it for subsequent data packets.

#### 2. Route Maintenance (Handling Breaks)
* **Link Monitoring:** Nodes monitor the status of the links they are using (e.g., by listening for link-layer ACKs or using a passive acknowledgment mechanism).
* **Error Reporting:** Upon detecting a link break (e.g., failed transmission/no ACK), the intermediate node immediately sends a **Route Error (RERR)** packet back to the original source. The RERR identifies the broken link.
* **Re-Discovery:** The source removes the faulty route from its cache and, if no alternate route is available, re-initiates Route Discovery.

---

### (b) ii) Compare DSDV, DSR and AODV (3 marks)

| Protocol | Type | Routing Information | Overhead | Best Use |
| :--- | :--- | :--- | :--- | :--- |
| **DSDV** | **Proactive** (Table-Driven) | Full routing tables (periodic updates) | High (periodic updates) | Small, stable networks. |
| **DSR** | **Reactive** (On-Demand) | Source routes in packet headers + caches | Low control overhead | High mobility, where caching helps. |
| **AODV** | **Reactive** (On-Demand) | Routing tables with sequence numbers | Moderate (discovery on demand) | Balanced mobility scenarios. |

---

### (b) iii) Promiscuous receive mode (2 marks)

**Definition:** A node operating in promiscuous receive mode is configured to **listen to and process all packets** transmitted on the wireless medium, regardless of whether those packets are explicitly addressed to that node.

**MANET Use:** This mode is used in protocols like **DSR** to enable **passive route caching**. A node can overhear data packets intended for other nodes, extract the source route from the header, and cache that route for its own future use, thereby significantly reducing the need for costly Route Discovery broadcasts.

---

### (b) iv) Example areas of ad-hoc networks (2 marks)

1.  **Military and Tactical Communications:** Rapid deployment in areas without infrastructure.
2.  **Disaster Recovery/Emergency Networks:** Establishing temporary communication links after infrastructure failure (e.g., earthquake).
3.  **Vehicular Ad-hoc Networks (VANETs):** Communication between vehicles (V2V) for safety and traffic management.
4.  **Sensor Networks:** Distributed data collection in remote or inaccessible areas.

---
---

## Q.6 Answer any one (12 marks total)

### (a) i) TCP reaction to packet loss; why problematic in wireless; is UDP a solution? (7 marks)

#### 1. TCP Reaction to Packet Loss
* TCP primarily assumes that packet loss is due to **network congestion** (buffer overflow) in the wired network.
* Upon detecting loss (via duplicate ACKs or retransmission timeout), TCP's congestion control mechanism triggers: it drastically **reduces its Congestion Window (cwnd)** (multiplicative decrease) and enters **Slow Start**.
* It then retransmits the lost packet.

#### 2. Why Problematic in Wireless
* In wireless, packet losses are frequently caused by **non-congestion factors** like:
    * High Bit Error Rate (**BER**) from fading and interference.
    * Temporary disconnections during **handoff**.
* When TCP responds to these non-congestion losses by reducing its sending rate, it causes **unnecessary throughput reduction** and performance collapse (**pseudo-congestion**), which harms the performance of the wireless link without alleviating any congestion.

#### 3. Is UDP a Solution?
* **No, not a full solution.** UDP avoids TCP's mistaken slowdowns because it has no congestion control, no reliability, and no flow control.
* **Where Useful:** It is suitable for real-time applications (VoIP, streaming) where latency and timeliness are more critical than perfect reliability.
* **Why Dangerous:** Uncontrolled UDP traffic can **overwhelm the network capacity**, leading to true congestion for other TCP flows and fairness issues (as UDP continues to pump data even under heavy load), potentially causing a congestion collapse.

---

### (a) ii) Localization approaches to improve TCP performance (5 marks)

Localization approaches modify the network stack (typically at the Base Station/Access Point) to **hide wireless link losses** from the distant sender, preventing unnecessary TCP slowdowns.

1.  **Snoop Protocol:**
    * The Base Station (**BS**) snoops on TCP packets, caches un-ACKed data, and monitors ACKs.
    * If a wireless loss occurs, the BS performs a **local retransmission** of the cached packet.
    * The BS suppresses or manipulates duplicate ACKs headed toward the sender, preventing the sender from reducing its $cwnd$.

2.  **Split-Connection (I-TCP):**
    * The end-to-end TCP connection is **split** into two separate connections at the BS/FA.
    * The wired segment ($\text{CN} \leftrightarrow \text{BS}$) uses standard TCP.
    * The wireless segment ($\text{BS} \leftrightarrow \text{MN}$) uses a separate, optimized protocol (or a highly tuned TCP variant) for the unreliable wireless link.
    * This completely isolates the end-to-end TCP connection from wireless losses.

3.  **Link-Layer ARQ/FEC:**
    * Implementing robust **Automatic Repeat Request (ARQ)** and/or **Forward Error Correction (FEC)** at the Data Link Layer to recover most losses locally.
    * This makes the wireless link appear more reliable to the network layer (TCP), reducing the number of losses that reach the TCP sender.

---

### (b) i) Handoff effect on TCP performance (5 marks)

The handoff process (moving from one BTS/AP to another) negatively impacts TCP performance:

1.  **Temporary Disruption:** Handoff requires a transition period (especially hard handoffs) during which the MS cannot send or receive data, leading to **packet loss** and potentially **packet reordering**.
2.  **TCP Congestion Control:** The TCP sender interprets the packet loss and delayed/reordered ACKs as signs of congestion. This triggers a **slow-start** or **multiplicative decrease** of the **congestion window ($cwnd$)**.
3.  **Throughput Collapse:** The resulting $cwnd$ reduction causes a significant, unnecessary **throughput collapse** and slow recovery after the handoff completes, leading to high application latency and poor user experience.
4.  **Mitigation:** Mitigation requires local buffering and fast retransmissions at the point of attachment during the handoff phase.

---

### (b) ii) High wireless loss rate impact & mechanism to improve TCP (7 marks)

#### 1. Impact of High Wireless Loss Rate
High BER due to interference/fading causes frequent, sustained packet loss.
* **Repeated $cwnd$ Reduction:** TCP constantly misinterprets these losses as congestion, leading to continuous and repeated reduction of the $cwnd$.
* **Persistent Slow-Start:** The sender may never leave slow-start or may repeatedly fall back into it, resulting in severe **throughput degradation** (pseudo-congestion).
* **Increased Latency:** Frequent retransmission timeouts increase the effective round-trip time and application latency.

#### 2. Mechanism to Improve TCP: TCP Snoop Protocol (Stepwise)

The Snoop Protocol is a performance-enhancing proxy located at the Base Station (**BS**) to localize loss recovery:

1.  **Snooping & Caching:** The BS (acting as the proxy) passively inspects ($\text{snoops}$) all packets passing through it on the wired and wireless sides, **caching** all un-ACKed data packets destined for the MN.
2.  **Local Loss Detection:** The BS monitors the wireless link and detects a loss (e.g., via a missing link-layer ACK or arrival of duplicate TCP ACKs).
3.  **Local Retransmission:** Upon detecting a loss, the BS **immediately retransmits** the cached packet over the wireless link to the MN.
4.  **ACK Suppression/Manipulation:** Crucially, the BS intercepts and **suppresses** duplicate ACKs or converts them into local link-layer ACKs, preventing them from reaching the original sender.
5.  **Result:** The original TCP sender never sees the wireless loss, keeping its **congestion window large** and its high sending rate preserved, thus maximizing throughput.

---
---
