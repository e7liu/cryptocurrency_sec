---
layout: post
title: "Cyclic Arbitrage in Decentralized Exchange Markets"
categories: ['Topic: Security and Measurement', 'Topic: Exchanges', '2021', 'Venue: Defi']
year: 2021
venue: Defi
---
**Authors**: Ye Wang, Yan Chen, Shuiguang Deng, Roger Wattenhofer

**Venue**: Defi (2021)

**Abstract**: Decentralized Exchanges (DEXes) such as UniSwap allow users to create trading pools between any pair of cryptocurrencies. The exchange rate of each trading pool is independent, which introduces arbitrage opportunities with trading through different cryptocurrencies: Traders are able to trade cryptocurrencies cyclically: A trader can exchange currency A for B, then B for C , and finally C for A again through three different trading pools. Almost surely, the three floating exchange rates are not perfectly in sync, which opens up arbitrage possibilities for cyclic trading. In this paper, we study cyclic arbitrages in DEXes of cryptocurrencies with transaction-level data on Uniswap, measuring 285,127 cyclic arbitrages over nine months. We conduct a theoretical analysis and an empirical evaluation to understand cyclic arbitrages systematically. We study the market size (the revenue and the cost) of cyclic arbitrages, the influence of cyclic arbitrages, and the implementations of cyclic arbitrages. Beyond the understanding of cyclic arbitrages, this paper suggests that with the smart contract technology and the replicated state machine setting of Ethereum, arbitrage strategies are easier implemented in DEXes than in Centralized Exchanges (CEXes). We find that deploying private smart contracts to implement cyclic arbitrages is more resilient to front-running attacks than applying cyclic arbitrages through public (opensource) smart contracts.
