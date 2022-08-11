---
layout: post
title: "As Strong As Its Weakest Link: How to Break Blockchain DApps at RPC Service"
categories: ['Topic: Security and Measurement', 'Topic: DApps', '2021', 'Venue: NDSS']
year: 2021
venue: NDSS
---
**Authors**: Kai Li, Jiaqi Chen, Xianghong Liu, Y. Tang, Xiaofeng Wang, Xiapu Luo

**Venue**: NDSS (2021)

**Abstract**: Modern blockchains have evolved from cryptocurrency substrates to trust-decentralization platforms, supporting a wider variety of decentralized applications known as DApps. Blockchain remote procedure call (RPC) services emerge as an intermediary connecting the DApps to a blockchain network. In this work, we identify the free contract-execution capabilities that widely exist in blockchain RPCs as a vulnerability of denial of service (DoS) and present the DoERS attack, a Denial of Ethereum RPC service that incurs zero Ether cost to the attacker. To understand the DoERS exploitability in the wild, we conduct a systematic measurement study on nine real-world RPC services which control most DApp clients' connection to the Ethereum mainnet. In particular, we propose a novel measurement technique based on orphan transactions to discover the previously unknown behaviors inside the blackbox RPC services, including load balancing and gas limiting. Further DoERS strategies are proposed to evade the protection intended by these behaviors. We evaluate the effectiveness of DoERS attacks on deployed RPC services with minimal service interruption. The result shows that all the nine services tested (as of Apr. 2020) are vulnerable to DoERS attacks that can result in the service latency increased by 2.1X ~ 50X . Some of these attacks require only a single request. In addition, on a local Ethereum node protected by a very restrictive limit of 0.65 block gas, sending 150 DoERS requests per second can slow down the block synchronization of the victim node by 91%. We propose mitigation techniques against DoERS without dropping service usability, via unpredictable load balancing, performance anomaly detection, and others. These techniques can be integrated into a RPC service transparently to its clients.
