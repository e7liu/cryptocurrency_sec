---
layout: post
title: "Be Aware of Your Leaders"
categories: ['Topic: Security and Measurement', 'Topic: Protocols', '2021', 'Venue: FC']
year: 2021
venue: FC
---
**Authors**: Shir Cohen, Rati Gelashvili, Lefteris Kokoris-Kogias, Zekun Li, D. Malkhi, A. Sonnino, A. Spiegelman

**Venue**: FC (2021)

**Abstract**: . Advances in blockchains have influenced the State-Machine-Replication (SMR) world and many state-of-the-art blockchain-SMR so-lutions are based on two pillars: Chaining and Leader-rotation . A prede-termined round-robin mechanism used for Leader-rotation, however, has an undesirable behavior: crashed parties become designated leaders infinitely often, slowing down overall system performance. In this paper, we provide a new Leader-Aware SMR framework that, among other desir-able properties, formalizes a Leader-utilization requirement that bounds the number of rounds whose leaders are faulty in crash-only executions. We introduce Carousel, a novel, reputation-based Leader-rotation solution to achieve Leader-Aware SMR. The challenge in adaptive Leader-rotation is that it cannot rely on consensus to determine a leader, since consensus itself needs a leader. Carousel uses the available on-chain information to determine a leader locally and achieves Liveness despite this difficulty. A HotStuff implementation fitted with Carousel demonstrates drastic performance improvements: it increases throughput over 2x in faultless settings and provided a 20x throughput increase and 5x latency reduction in the presence of faults.
