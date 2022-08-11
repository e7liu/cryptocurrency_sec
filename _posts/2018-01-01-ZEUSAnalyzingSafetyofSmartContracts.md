---
layout: post
title: "ZEUS: Analyzing Safety of Smart Contracts"
categories: ['Topic: Security and Measurement', 'Topic: Smart Contracts', '2018', 'Venue: NDSS']
year: 2018
venue: NDSS
---
**Authors**: Sukrit Kalra, Seep Goel, Mohan Dhawan, Subodh Sharma

**Venue**: NDSS (2018)

**Abstract**: A smart contract is hard to patch for bugs once it is deployed, irrespective of the money it holds. A recent bug caused losses worth around $50 million of cryptocurrency. We present ZEUS--a framework to verify the correctness and validate the fairness of smart contracts. We consider correctness as adherence to safe programming practices, while fairness is adherence to agreed upon higher-level business logic. ZEUS leverages both abstract interpretation and symbolic model checking, along with the power of constrained horn clauses to quickly verify contracts for safety. We have built a prototype of ZEUS for Ethereum and Fabric blockchain platforms, and evaluated it with over 22.4K smart contracts. Our evaluation indicates that about 94.6% of contracts (containing cryptocurrency worth more than $0.5 billion) are vulnerable. ZEUS is sound with zero false negatives and has a low false positive rate, with an order of magnitude improvement in analysis time as compared to prior art.
