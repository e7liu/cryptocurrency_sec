---
layout: post
title: "Revisiting Nakamoto Consensus in Asynchronous Networks: A Comprehensive Analysis of Bitcoin Safety and Chain Quality"
categories: ['Topic: Security and Measurement', 'Topic: Decentralized Systems', '2021', 'Venue: CCS']
year: 2021
venue: CCS
---
**Authors**: Muhammad Saad, Afsah Anwar, Srivatsan Ravi, David A. Mohaisen

**Venue**: CCS (2021)

**Abstract**: The Bitcoin blockchain safety relies on strong network synchrony. Therefore, violating the blockchain safety requires strong adversaries that control a mining pool with 51% hash rate. In this paper, we show that the network synchrony does not hold in the real world Bitcoin network which can be exploited to lower the cost of various attacks that violate the blockchain safety and chain quality. Towards that, first we construct the Bitcoin ideal functionality to formally specify its ideal execution model in a synchronous network. We then develop a large-scale data collection system through which we connect with more than 36K IP addresses of the Bitcoin nodes and identify 359 mining nodes. We contrast the ideal functionality against the real world measurements to expose the network anomalies that can be exploited to optimize the existing attacks. Particularly, we observe a non-uniform block propagation pattern among the mining nodes showing that the Bitcoin network is asynchronous in practice. To realize the threat of an asynchronous network, we present the HashSplit attack that allows an adversary to orchestrate concurrent mining on multiple branches of the blockchain to violate common prefix and chain quality properties. We also propose the attack countermeasures by tweaking Bitcoin Core to model the Bitcoin ideal functionality. Our measurements, theoretical modeling, proposed attack, and countermeasures open new directions in the security evaluation of Bitcoin and similar blockchain systems.
