---
layout: post
title: "SquirRL: Automating Attack Analysis on Blockchain Incentive Mechanisms with Deep Reinforcement Learning"
categories: ['Topic: Security and Measurement', 'Topic: Protocols', '2021', 'Venue: NDSS']
year: 2021
venue: NDSS
---
**Authors**: Charlie Hou, Mingxun Zhou, Yan Ji, Philip Daian, Florian Tramer, G. Fanti, A. Juels

**Venue**: NDSS (2021)

**Abstract**: Incentive mechanisms are central to the functionality of permissionless blockchains: they incentivize participants to run and secure the underlying consensus protocol. Designing incentive-compatible incentive mechanisms is notoriously challenging, however. As a result, most public blockchains today use incentive mechanisms whose security properties are poorly understood and largely untested. In this work, we propose SquirRL, a framework for using deep reinforcement learning to analyze attacks on blockchain incentive mechanisms. We demonstrate SquirRL's power by first recovering known attacks: (1) the optimal selfish mining attack in Bitcoin [56], and (2) the Nash equilibrium in block withholding attacks [18]. We also use SquirRL to obtain several novel empirical results. First, we discover a counterintuitive flaw in the widely used rushing adversary model when applied to multi-agent Markov games with incomplete information. Second, we demonstrate that the optimal selfish mining strategy identified in [56] is actually not a Nash equilibrium in the multi-agent selfish mining setting. In fact, our results suggest (but do not prove) that when more than two competing agents engage in selfish mining, there is no profitable Nash equilibrium. This is consistent with the lack of observed selfish mining in the wild. Third, we find a novel attack on a simplified version of Ethereum's finalization mechanism, Casper the Friendly Finality Gadget (FFG) that allows a strategic agent to amplify her rewards by up to 30%. Notably, [12] shows that honest voting is a Nash equilibrium in Casper FFG; our attack shows that when Casper FFG is composed with selfish mining, this is no longer the case. Altogether, our experiments demonstrate SquirRL's flexibility and promise as a framework for studying attack settings that have thus far eluded theoretical and empirical understanding. Keywords--Blockchain, Deep reinforcement learning, Incentive mechanisms *Equal contribution
