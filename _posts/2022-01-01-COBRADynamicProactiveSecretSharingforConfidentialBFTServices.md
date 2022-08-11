---
layout: post
title: "COBRA: Dynamic Proactive Secret Sharing for Confidential BFT Services"
categories: ['Topic: New Systems and Protocols', '2022', 'Venue: IEEE S&P']
year: 2022
venue: IEEE S&P
---
**Authors**: Robin Vassantlal, E. Alchieri, Bernardo Ferreira, A. Bessani

**Venue**: IEEE S&P (2022)

**Abstract**: --Byzantine Fault-Tolerant (BFT) State Machine Replication (SMR) is a classical paradigm for implementing trustworthy services that has received renewed interest with the emergence of blockchains and decentralized infrastructures. A fundamental limitation of BFT SMR is that it provides integrity and availability despite a fraction of the replicas being controlled by an active adversary, but does not offer any confidentiality protection. Previous works addressed this issue by integrating secret sharing with the consensus-based framework of BFT SMR, but without providing all features required by practical systems, which include replica recovery, group reconfiguration, and acceptable performance when dealing with a large number of secrets. We present COBRA, a new protocol stack for Dynamic Proactive Secret Sharing that allows implementing confidentiality in practical BFT SMR systems. COBRA exhibits the best asymp- totic communication complexity and optimal storage overhead, being able to renew 100k shares in a group of ten replicas 5 x faster than the current state of the art.
