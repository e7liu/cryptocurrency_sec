---
layout: post
title: "MatRiCT+: More Efficient Post-Quantum Private Blockchain Payments"
categories: ['Topic: New Systems and Protocols', '2022', 'Venue: IEEE S&P']
year: 2022
venue: IEEE S&P
---
**Authors**: Muhammed F. Esgin, Ron Steinfeld, Raymond K. Zhao

**Venue**: IEEE S&P (2022)

**Abstract**: We introduce MatRiCT, a practical private blockchain payment protocol based on "post-quantum" lattice assumptions. MatRiCT builds on MatRiCT due to Esgin et al. (ACM CCS'19) and, in general, follows the Ring Confidential Transactions (RingCT) approach used in Monero, the largest privacy-preserving cryptocurrency. In terms of the practical aspects, MatRiCT has 2-17x shorter proofs (depending on the number of input accounts, M ) and runs 3-8x faster (for a typical transaction) in comparison to MatRiCT. A significant advantage of MatRiCT is that the proof length's dependence on M is very minimal (only O(logM)), while MatRiCT has a proof length linear in M . To support its efficiency, we devise several novel techniques in our design of MatRiCT to achieve compact lattice-based zeroknowledge proof systems, exploiting the algebraic properties of power-of-2 cyclotomic rings commonly used in practical latticebased cryptography. Along the way, we design an "optimal" challenge space with minimal `1-norm and invertible challenge differences (with overwhelming probability), while supporting highly-splitting power-of-2 cyclotomic rings. We believe all these results to be widely applicable and of independent interest.
