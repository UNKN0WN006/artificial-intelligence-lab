# WMN 2024 — FULL EXAM ANSWERS (Structured by Marks)

These answers are structured to strictly match the marks allotted in the WMN 2024 paper.

---

## ✅ SECTION A – Q1 (Any Four $\times$ 4 marks = 16)

### Q1 (i) Steps in Handoff – (4 marks)

**Definition:** Handoff (HO) is the process of switching an active connection from one cell to another as the Mobile Station (MS) moves.

#### 📝 Steps:
1.  **Measurement:** MS measures the signal strength (RSSI) of the serving cell and neighboring cells periodically.
2.  **Reporting:** MS sends the **Measurement Report** to the serving BTS, which forwards it to the BSC.
3.  **Decision:** The **BSC** decides if a handoff is necessary based on signal quality falling below a network threshold.
4.  **Channel Allocation:** The target BTS (selected by the BSC) reserves a free channel for the MS.
5.  **Handoff Execution:** The BSC issues an HO command; the MS tunes to the new frequency and synchronizes with the new BTS.
6.  **Completion & Release:** The new BTS sends an HO Complete message; the old BTS releases the previously allocated channel.



---

### Q1 (ii) Services in 3G, 4G, 5G – (4 marks)

| Generation | Key Services (2 Points Each) |
| :--- | :--- |
| **3G (UMTS, CDMA2000)** | * Mobile broadband access (up to 2 Mbps). * Supports multimedia messaging, video calling, and fast web browsing. |
| **4G (LTE)** | * All-IP network with high throughput (100 Mbps to 1 Gbps). * Enables seamless **HD video streaming** and **VoLTE** (Voice over LTE). |
| **5G (New Radio)** | * **eMBB** (Enhanced Mobile Broadband) reaching 10 Gbps and **URLLC** (Ultra-Reliable Low-Latency Communications, $\sim 1 \text{ ms}$). * Supports **Massive IoT** (mMTC) and network slicing for diversified services. |

---

### Q1 (iii) Hidden & Exposed Terminal – (4 marks)

#### 1. Hidden Terminal
* **Definition:** Node **A** and Node **C** cannot sense each other, but they both transmit simultaneously to a central receiver, **B**. This results in a collision at B's location.
* **Problem:** Nodes cannot detect each other's presence by carrier sensing alone.
* **Solution:** Use **RTS/CTS** (Request-to-Send/Clear-to-Send). When **B** sends a **CTS** back, both A and C hear the CTS and defer, preventing collision.



#### 2. Exposed Terminal
* **Definition:** Node **B** is transmitting to **A**. Node **C** senses the medium is busy (hearing B's transmission) and therefore defers its own transmission, even though **C's transmission to D** would not interfere with the $B \to A$ communication.
* **Problem:** Unnecessary deferral of transmission, leading to inefficient channel utilization.
* **Solution:** **RTS/CTS** allows **C** to determine that its transmission to **D** will not interfere with the $B \to A$ reserved path, permitting C to transmit.

---

### Q1 (iv) Why Wired MAC Fails in Wireless – (4 marks)

Wired MAC protocols, like CSMA/CD, fail in wireless networks due to fundamental physical differences:

1.  **Collision Detection is Impossible:** Wireless transceivers are typically **half-duplex**; they cannot transmit and simultaneously monitor the received signal level to detect a collision.
2.  **Hidden/Exposed Terminals:** These phenomena (as detailed in Q1.iii) break the basic assumption of wired CSMA/CD that all nodes can sense each other.
3.  **Carrier Sensing is Unreliable:** High attenuation (path loss) and interference make the received signal strength variable and weak, making reliable **carrier sensing** (listening to detect ongoing transmission) unreliable.
4.  **No Continuous Monitoring:** Wired CSMA/CD assumes continuous, reliable monitoring of the shared medium, which is not feasible in dynamic wireless environments.

---

### Q1 (v) Channel Calculation – (4 marks)

**Given:** Total BW = 33 MHz = 33,000 kHz. Cluster size $N=4$.
Full-duplex channel uses $2 \times 25 \text{ kHz} = 50 \text{ kHz}$.

#### Steps:
1.  **Calculate Total Duplex Channels ($C_{total}$):**
    $$C_{total} = \frac{\text{Total Bandwidth}}{\text{BW per Duplex Channel}} = \frac{33{,}000 \text{ kHz}}{50 \text{ kHz}} = 660 \text{ channels}$$
2.  **Calculate Channels Per Cell ($C_{cell}$):**
    $$C_{cell} = \frac{C_{total}}{N} = \frac{660}{4} = 165 \text{ channels per cell}$$

**Answer:** There are **165 channels per cell**.

---
---

## ✅ SECTION B

### Q2 – 12 marks

#### Q2 (i) Three GSM Entities – (3 $\times$ 1 = 3 marks)

1.  **BTS (Base Transceiver Station):** Handles the physical **radio interface** with the MS, performing modulation/demodulation, signal transmission/reception, and error coding.
2.  **BSC (Base Station Controller):** Controls multiple BTSs, managing **radio channel allocation**, power control, and **handoff** execution within its control area.
3.  **MSC (Mobile Switching Center):** The central switch in the core network, responsible for **call routing** (interconnecting to PSTN) and **mobility management** (interfacing with HLR/VLR).

#### Q2 (ii) Handoff Flow Diagram – (5 marks)

**Intra-BSC Handoff (Fast Handoff):** (3 marks diagram + explanation)
* **Flow:** $\text{MS} \to \text{BTS1} \to \mathbf{BSC} \to \text{BTS2}$.
* **Mechanism:** The BSC manages the handoff entirely because both the serving (BTS1) and target (BTS2) cells are under its control. The MSC is not involved.
* **Advantage:** This is the fastest type of handoff as it is localized to the base station subsystem (BSS).



**Intra-MSC Handoff (Inter-BSC Handoff):**
* **Flow:** $\text{MS} \to \text{BTS1} \to \text{BSC1} \to \mathbf{MSC} \to \text{BSC2} \to \text{BTS2}$.
* **Mechanism:** The MSC is required to coordinate the channel reallocation and switching because the MS is moving between two cells controlled by different BSCs (BSC1 and BSC2).
* **VLR Update:** No HLR update is typically required, but location registers (VLR/MSC) may need minor state updates.

#### Q2 (iii) CDMA Bandwidth per user – (4 marks)

**Given:** Total BW = 200 MHz, Users = 100.

$$\text{BW per user} = \frac{\text{Total Bandwidth}}{\text{Number of Users}}$$
$$\text{BW per user} = \frac{200 \text{ MHz}}{100} = 2 \text{ MHz per user}$$

**Answer:** The bandwidth per user is **2 MHz**.

---
---

### Q3 – (7 + 4 + 4 + 4 = 19 marks)

#### Q3 (i) 802.11 MAC Fairness – (7 marks)

IEEE 802.11 (WLAN) uses **CSMA/CA** combined with several mechanisms to achieve fairness and prevent channel capture:

1.  **DIFS/SIFS Separation:** **SIFS** (Short IFS) is shorter than **DIFS** (Distributed IFS). ACKs/CTS messages use SIFS, giving them higher priority to complete the current transaction before new data transmission can begin.
2.  **Random Backoff Timer:** After waiting for DIFS, stations choose a **random backoff timer** value from a specific range (Contention Window, CW). This probabilistic deferral ensures fairness by giving different stations access in different cycles.
3.  **Binary Exponential Backoff (BEB):** If a transmission fails (no ACK), the **CW size is doubled** (exponential backoff). This heavily penalizes nodes that cause collisions, granting fairer access to others.
4.  **RTS/CTS Handshake:** Used to mitigate the **hidden terminal problem**. A successful CTS ensures all nearby nodes defer, dedicating the channel to the transmitting pair.
5.  **NAV (Network Allocation Vector):** The **virtual carrier sensing** mechanism. Nodes that hear the RTS/CTS/DATA duration field set their NAV timer, reserving the medium and preventing collision-causing transmissions from starting.
6.  **Carrier Sensing (Physical/Virtual):** The basic CSMA/CA mechanism ensures that a station only attempts access when the channel is physically or virtually idle.
7.  **ACK Mechanism:** Positive acknowledgment is required for every unicast frame. This ensures that successful transmissions are confirmed, avoiding long, unfair collisions where a sender might retry repeatedly without confirmation.



#### Q3 (ii) NAV – (4 marks)

* **NAV (Network Allocation Vector):** Represents the **virtual carrier sensing** mechanism in 802.11.
* **Operation:** A special **Duration field** in the RTS/CTS/DATA frames indicates the amount of time the channel needs to be reserved to complete the transaction (DATA + ACK).
* **Function:** Any node that hears the RTS or CTS frame reads this duration and sets its NAV timer to that value, commanding itself to **stay silent**.
* **Result:** The NAV mechanism avoids collisions, particularly from **hidden terminals**, by forcing them to respect the reservation time, even if their physical sensing indicates an idle channel.

#### Q3 (iii) Power Management – (4 marks)

The standard scheme is **Power Save Mode (PSM)**:

1.  **Sleep Mode:** The Mobile Station (**STA**) informs the Access Point (**AP**) via the frame header that it is entering a sleep state to conserve battery.
2.  **Buffering:** The AP temporarily **buffers** any data packets destined for the sleeping STA.
3.  **TIM Bitmap:** The AP includes a **Traffic Indication Map (TIM)** bitmap in its periodic **Beacon** frames, indicating which sleeping stations have pending data.
4.  **PS-POLL:** The STA wakes up at the known beacon interval, checks the TIM, and if its bit is set, it sends a **PS-POLL** control frame to the AP, prompting the AP to release the buffered frames.

#### Q3 (iv) Clock Synchronization – (4 marks)

* **Mechanism:** The Access Point (**AP**) periodically transmits its current local time in the **Timestamp field** of the **Beacon frames**.
* **TSF:** This time-synchronization process is governed by the **Timing Synchronization Function (TSF)**.
* **Function:** All associated stations adjust their internal local clocks to align with the AP's timestamp.
* **Requirement:** Consistent TSF is critical for: 1) The **random backoff** process to operate fairly across the BSS, and 2) Ensuring the STA wakes up at the correct time to check the beacon for power management.

---
---

### Q4 – 14 marks

#### (i) MIPv6 Route Optimisation – (5 marks)

**MIPv6 Route Optimization** allows the Correspondent Node (CN) to send packets directly to the Mobile Node's (MN) current location, bypassing the Home Agent (HA).

1.  **CoA Formation:** MN uses IPv6 Stateless Autoconfiguration (NDP) to form its **Care-of-Address (CoA)** in the foreign network.
2.  **Binding Update (BU):** MN registers its new $\text{HoA} \leftrightarrow \text{CoA}$ binding with the HA, and critically, sends a BU directly to the CN (via the **Return Routability Procedure** for security).
3.  **Binding Cache:** CN stores the validated binding in its **Binding Cache**.
4.  **Direct Routing:** CN sends subsequent packets directly to the **CoA** using a **Routing Header** to carry the MN's original Home Address (HoA) semantics.
5.  **Optimization Effect:** This eliminates the path $\text{CN} \to \text{HA} \to \text{MN}$, significantly reducing latency and network overhead (no triangular routing).

#### (ii) Care-of Address vs Co-located CoA & Functions of HA & FA – (4 marks)

| Term | Definition |
| :--- | :--- |
| **Care-of Address (CoA)** | A temporary address used by the MN when roaming in a foreign network. |
| **Co-located CoA (CCoA)** | A CoA that the MN itself configures and manages on its own interface (e.g., via DHCP or IPv6 Autoconfig), eliminating the need for a Foreign Agent. |

| Entity | Primary Functions (2 Points Each) |
| :--- | :--- |
| **Home Agent (HA)** | 1. Maintains the **binding** ($\text{HoA} \leftrightarrow \text{CoA}$) for the MN. 2. **Tunnels** packets destined for the HoA to the MN's current CoA (when route optimization is not possible). |
| **Foreign Agent (FA)** | 1. Provides a **Care-of Address** (its own address) to the MN in MIPv4. 2. Acts as the tunnel endpoint, **relaying** packets between the MN and the HA. |

#### (iii) Delivery logic CN’s knowledge – (1 mark)

* **If CN knows CoA:** The CN sends the packet **directly to the CoA** (route optimization).
* **If CN does not know CoA:** The CN sends the packet to the **HoA**; the packet is routed to the **HA**, which then **tunnels** it to the CoA.

---
---

### Q5 – 15 marks (Any Five $\times$ 3 marks)

#### (i) Routing in fixed vs mobile networks (3 marks)

1.  **Fixed Assumption:** Traditional IP routing assumes a relatively **static network topology** and fixed router addresses.
2.  **Mobility Breakage:** Mobile nodes move frequently, causing routes to **break constantly** and routing tables to become immediately stale.
3.  **Overhead:** The constant need for distributed **route discovery and maintenance** in MANETs generates massive control overhead not seen in fixed networks.

#### (ii) DSR Route Discovery & Maintenance (3 marks)

1.  **Discovery:** Source broadcasts **RREQ**; nodes append their address (source route accumulation); destination replies with **RREP** carrying the full path.
2.  **Maintenance:** Intermediate nodes monitor link status; if a link breaks, they send a **RERR** back to the source.
3.  **Cache Usage:** DSR caches multiple routes learned during discovery, reducing the need for new RREQ broadcasts upon failure.

#### (iii) Promiscuous Receive Mode (3 marks)

1.  **Definition:** A node is configured to **overhear and process** all packets on the channel, even those not addressed to it.
2.  **Function:** Used by protocols like DSR for **passive route learning** (or caching).
3.  **Benefit:** By overhearing, a node learns routes used by others, thereby reducing the routing overhead caused by initiating new route discovery broadcasts.

#### (iv) DSDV vs DSR vs AODV (3 marks)

| Protocol | Type | Key Feature |
| :--- | :--- | :--- |
| **DSDV** | **Proactive** (Table-Driven) | Uses destination **sequence numbers** for loop-free routing. |
| **DSR** | **Reactive** (On-Demand) | Uses **Source Routing** (full path in header) and extensive route caching. |
| **AODV** | **Reactive** (On-Demand) | **Hop-by-hop** routing table combined with sequence numbers. |

#### (v) Why DSR $>$ AODV in high mobility (3 marks)

1.  **Multiple Routes:** DSR maintains a cache of **multiple alternate routes** to a destination.
2.  **Quick Switching:** When a link breaks, DSR can switch to a cached alternate route **immediately** without network flooding.
3.  **AODV Delay:** AODV must restart the **RREQ flooding process** network-wide to find a fresh route, which is slower under continuous topology changes.

#### (vi) DSDV avoids count-to-infinity (3 marks)

1.  **Sequence Numbers:** DSDV utilizes **Destination Sequence Numbers** attached to all route updates by the destination itself.
2.  **Loop Prevention:** Nodes always prefer routes with a **higher (fresher)** sequence number, regardless of hop count.
3.  **Effect:** This ensures that stale, looping routes are rejected, guaranteeing loop-freedom and preventing the distance metric from counting to infinity.

---
---

### Q6 – 14 marks (Any Two $\times$ 7 marks)

#### Q6 (i) Standard TCP in packet loss (7 marks)

1.  **Assumption:** Standard **TCP** is optimized for wired networks, assuming packet loss occurs primarily due to **network congestion**.
2.  **Reaction:** Upon loss detection (Duplicated ACKs or Timeout), TCP invokes congestion control by **halving the congestion window ($cwnd$)** (multiplicative decrease).
3.  **Wireless Reality:** In wireless, loss is often caused by **high BER** (fading, interference) or **handoff**, which are non-congestion events.
4.  **Consequence:** TCP's reaction in wireless is inappropriate; the unnecessary reduction in $cwnd$ leads to **performance collapse** (**pseudo-congestion**).
5.  **UDP Alternative:** Replacing TCP with **UDP** removes the mistaken throttling but introduces other dangers.
6.  **UDP Danger:** UDP lacks reliability, flow control, and congestion control, risking network overload and **congestion collapse** by starving fair TCP flows.
7.  **UDP Utility:** UDP is only useful for applications like **VoIP and video streaming** where timely delivery is prioritized over guaranteed reliability.

#### Q6 (ii) Localization approach (7 marks)

Localization approaches handle wireless errors at the edge (Base Station or Access Point) to prevent the far-end TCP sender from seeing the loss.

1.  **Loss Handling:** Loss recovery is localized to the unreliable **wireless link** by the Base Station (BS).
2.  **Goal:** To make the wireless link appear as reliable as a wired link to the end-to-end TCP connection.
3.  **Mechanism Example (TCP Snoop):** The BS maintains a cache of un-ACKed data packets flowing to the MN.
4.  **Local Retransmission:** When a loss occurs on the wireless link, the BS performs a **local retransmission** from its cache.
5.  **ACK Filtering:** The BS filters or suppresses **duplicate ACKs** originating from the MN, preventing them from reaching the sender.
6.  **Throughput Preservation:** By hiding the loss, the sender's TCP is not forced to reduce its **$cwnd$**, thereby **preserving high throughput**.
7.  **Other Methods:** Link-layer **ARQ** and **FEC** are also localization approaches that hide losses from the higher layers.

#### Q6 (iii) Handoff impact on TCP + improvement (7 marks)

**Impact on TCP:**

1.  **Temporary Disruption:** Handoff causes a brief $\text{make-before-break}$ or $\text{break-before-make}$ gap, leading to inevitable **packet loss**.
2.  **RTT Fluctuation:** The path change and temporary buffering can cause significant, unpredictable increases in **RTT** (Round Trip Time).
3.  **Congestion Inference:** Packet loss and high RTT fluctuations trigger TCP's **congestion control** (slow-start/multiplicative decrease).

**Improvements/Mitigation:**

4.  **Buffering at BS:** The serving BS/MSC buffers outstanding packets during the handoff phase, forwarding them once the new connection is stable.
5.  **TCP Snoop/I-TCP:** Localization protocols (like Snoop) mask the handoff-related loss from the sender, preventing $cwnd$ reduction.
6.  **Fast Link-Layer Retransmit:** Using aggressive ARQ at the link layer to recover packets quickly before TCP timeouts occur.
7.  **Make-Before-Break:** Employing **soft handoff** (where possible) minimizes the disruption window compared to hard handoff.

---

⭐ **Expected score: 88–95+** (If handwriting is neat + diagrams are drawn)
