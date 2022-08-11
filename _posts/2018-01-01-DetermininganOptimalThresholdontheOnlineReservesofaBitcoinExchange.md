---
layout: post
title: "Determining an Optimal Threshold on the Online Reserves of a Bitcoin Exchange"
categories: ['Topic: Security and Measurement', 'Topic: Exchanges', '2018', 'Venue: WEIS']
year: 2018
venue: WEIS
---
**Authors**: Samvit Jain, E. Felten, Steven Goldfeder

**Venue**: WEIS (2018)

**Abstract**: Online and offline storage of digital currency present conflicting risks for a Bitcoin exchange. While bitcoins stored on online devices are continually vulnerable to malware and other network-based attacks, offline reserves are endangered on access, as transferring bitcoins requires the exposure of otherwise encrypted and secured private keys. In particular, fluctuations in customer demand for deposited bitcoin require exchanges to periodically refill online storage systems with bitcoins held offline. This raises the natural question of what upper limit on online reserves minimizes losses due to theft over time. In this article, we investigate this optimization problem, developing a model that predicts the optimal ceiling on online reserves, given average rates of deposits, withdrawals, and theft. We evaluate our theory with an event-driven simulation of the setup, and find that our equation yields a numerical value for the threshold that differs by less than 2% from experimental results. We conclude by considering open questions regarding more complex storage architectures.
