---
layout: post
title: "Replay Attacks and Defenses Against Cross-shard Consensus in Sharded Distributed Ledgers"
categories: ['Topic: Security and Measurement', 'Topic: Protocols', '2019', 'Venue: EuroS&P']
year: 2019
venue: EuroS&P
---
**Authors**: A. Sonnino, S. Bano, Mustafa Al-Bassam, G. Danezis

**Venue**: EuroS&P (2019)

**Abstract**: We present a family of replay attacks against sharded distributed ledgers targeting cross-shard consensus protocols, such as the recently proposed Chainspace and Omniledger. They allow an attacker, with network access only, to double-spend or lock resources with minimal efforts. The attacker can act independently without colluding with any nodes, and succeed even if all nodes are honest; most of the attacks can also exhibit themselves as faults under periods of asynchrony. These attacks are effective against both shard-led and client-led cross-shard consensus approaches. We present Byzcuit-a new cross-shard consensus protocol that is immune to those attacks. We implement a prototype of Byzcuit and evaluate it on a real cloud-based testbed, showing that our defenses impact performance minimally, and overall performance surpasses previous works.
