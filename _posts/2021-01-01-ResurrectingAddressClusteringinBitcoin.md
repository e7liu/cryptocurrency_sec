---
layout: post
title: "Resurrecting Address Clustering in Bitcoin"
categories: ['Topic: Security and Measurement', 'Topic: Deanonymization / Privacy', '2021', 'Venue: FC']
year: 2021
venue: FC
---
**Authors**: Malte Moser, A. Narayanan

**Venue**: FC (2021)

**Abstract**: . Blockchain analysis is essential for understanding how cryptocurrencies like Bitcoin are used in practice, and address clustering is a cornerstone of blockchain analysis. However, current techniques rely on heuristics that have not been rigorously evaluated or optimized. In this paper, we tackle several challenges of change address identification and clustering. First, we build a ground truth set of transactions with known change from the Bitcoin blockchain that can be used to validate the efficacy of individual change address detection heuristics. Equipped with this data set, we develop new techniques to predict change outputs with low false positive rates. After applying our prediction model to the Bitcoin blockchain, we analyze the resulting clustering and develop ways to detect and prevent cluster collapse. Finally, we assess the impact our enhanced clustering has on two exemplary applications.
