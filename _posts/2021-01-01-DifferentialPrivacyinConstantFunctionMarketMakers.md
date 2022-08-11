---
layout: post
title: "Differential Privacy in Constant Function Market Makers"
categories: ['Topic: New Systems and Protocols', '2021', 'Venue: FC']
year: 2021
venue: FC
---
**Authors**: T. Chitra

**Venue**: FC (2021)

**Abstract**: Constant function market makers (CFMMs) are the most popular mechanism for facilitating decentralized trading. While these mechanisms have facilitated hundreds of billions of dollars of trades, they provide users with little to no privacy. Recent work illustrates that privacy cannot be achieved in CFMMs without forcing worse pricing and/or latency on end users. This paper more precisely quantifies the trade-off between pricing and privacy in CFMMs. We analyze a simple privacy-enhancing mechanism called Uniform Random Execution and prove that it provides ( , d)-differential privacy. The privacy parameter depends on the curvature of the CFMM trading function and the number of trades executed. This mechanism can be implemented in any blockchain system that allows smart contracts to access a verifiable random function. We also investigate the worst case complexity over all private CFMM mechanisms using recent results from private PAC learning. These results suggest that one cannot do much better than Uniform Random Execution in CFMMs with non-zero curvature. Our results provide an optimistic outlook on providing partial privacy in CFMMs.
