---
layout: post
title: "Extracting Godl [sic] from the Salt Mines: Ethereum Miners Extracting Value"
categories: ['Topic: Security and Measurement', 'Topic: Mining', '2022', 'Venue: WEIS']
year: 2022
venue: WEIS
---
**Authors**: Julien Piet, Jaiden Fairoze, N. Weaver

**Venue**: WEIS (2022)

**Abstract**: Cryptocurrency miners have great latitude in deciding which transactions they accept, including their own, and the order in which they accept them. Ethereum miners in particular use this flexibility to collect MEV--Miner Extractable Value-- by structuring transactions to extract additional revenue. Ethereum also contains numerous bots that attempt to obtain MEV based on public-but-not-yet-confirmed transactions. Private relays shelter operations from these selfsame bots by directly submitting transactions to mining pools. In this work, we develop an algorithm to detect MEV exploitation present in previously mined blocks. We use our implementation of the detector to analyze MEV usage and profit redistribution, finding that miners make the lion's share of the profits, rather than independent users of the private relays. More specifically, (i) 73% of private transactions hide trading activity or re-distribute miner rewards, and 87.6% of MEV collection is accomplished with privately submitted transactions, (ii) our algorithm finds more than $6M worth of MEV profit in a period of 12 days, two thirds of which go directly to miners, and (iii) MEV represents 9.2% of miners' profit from transaction fees. Furthermore, in those 12 days, we also identify four blocks that contain enough MEV profits to make time-bandit forking attacks economically viable for large miners, undermining the security and stability of Ethereum as a whole.
