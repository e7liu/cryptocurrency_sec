---
layout: post
title: "Zero-Knowledge Contingent Payments Revisited: Attacks and Payments for Services"
categories: ['Topic: Security and Measurement', 'Topic: Protocols', '2017', 'Venue: CCS']
year: 2017
venue: CCS
---
**Authors**: Matteo Campanelli, R. Gennaro, Steven Goldfeder, Luca Nizzardo

**Venue**: CCS (2017)

**Abstract**: Zero Knowledge Contingent Payment (ZKCP) protocols allow fair exchange of sold goods and payments over the Bitcoin network. In this paper we point out two main shortcomings of current proposals for ZKCP, and propose ways to address them. First we show an attack that allows a buyer to learn partial information about the digital good being sold, without paying for it. This break in the zero-knowledge condition of ZKCP is due to the fact that in the protocols we attack, the buyer is allowed to choose common parameters that normally should be selected by a trusted third party. We implemented and tested this attack: we present code that learns, without paying, the value of a Sudoku cell in the "Pay-to-Sudoku" ZKCP implementation. We also present ways to fix this attack that do not require a trusted third party. Second, we show that ZKCP are not suited for the purchase of digital services} rather than goods. Current constructions of ZKCP do not allow a seller to receive payments after proving that a certain service has been rendered, but only for the sale of a specific digital good. We define the notion of Zero-Knowledge Contingent Service Payment (ZKCSP) protocols and construct two new protocols, for either public or private verification. We implemented our ZKCSP protocols for Proofs of Retrievability, where a client pays the server for providing a proof that the client's data is correctly stored by the server.We also implement a secure ZKCP protocol for "Pay-to-Sudoku" via our ZKCSP protocol, which does not require a trusted third party. A side product of our implementation effort is a new optimized circuit for SHA256 with less than a quarter than the number of AND gates of the best previously publicly available one. Our new SHA256 circuit may be of independent use for circuit-based MPC and FHE protocols that require SHA256 circuits.
