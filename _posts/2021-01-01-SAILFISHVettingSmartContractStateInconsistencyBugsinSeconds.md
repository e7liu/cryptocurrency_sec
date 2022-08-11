---
layout: post
title: "SAILFISH: Vetting Smart Contract State-Inconsistency Bugs in Seconds"
categories: ['Topic: Security and Measurement', 'Topic: Smart Contracts', '2021', 'Venue: IEEE S&P']
year: 2021
venue: IEEE S&P
---
**Authors**: P. Bose, Dipanjan Das, Yanju Chen, Yu Feng, C. Kruegel, Giovanni Vigna

**Venue**: IEEE S&P (2021)

**Abstract**: This paper presents SAILFISH, a scalable system for automatically finding state-inconsistency bugs in smart contracts. To make the analysis tractable, we introduce a hybrid approach that includes (i) a light-weight exploration phase that dramatically reduces the number of instructions to analyze, and (ii) a precise refinement phase based on symbolic evaluation guided by our novel value-summary analysis, which generates extra constraints to over-approximate the side effects of whole-program execution, thereby ensuring the precision of the symbolic evaluation. We developed a prototype of SAILFISH and evaluated its ability to detect two state-inconsistency flaws, viz., reentrancy and transaction order dependence (TOD) in Ethereum smart contracts. Our experiments demonstrate the efficiency of our hybrid approach as well as the benefit of the value summary analysis. In particular, we show that SAILFISH outperforms five state-of the-art smart contract analyzers (SECURIFY, MYTHRIL, OYENTE, SEREUM and VANDAL) in terms of performance, and precision. In total, SAILFISH discovered 47 previously unknown vulnerable smart contracts out of 89,853 smart contracts from ETHERSCAN.
