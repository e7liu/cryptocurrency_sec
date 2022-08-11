---
layout: post
title: "VerX: Safety Verification of Smart Contracts"
categories: ['Topic: Security and Measurement', 'Topic: Smart Contracts', '2020', 'Venue: IEEE S&P']
year: 2020
venue: IEEE S&P
---
**Authors**: Anton Permenev, Dimitar I. Dimitrov, Petar Tsankov, Dana Drachsler-Cohen, Martin T. Vechev

**Venue**: IEEE S&P (2020)

**Abstract**: We present VerX, the first automated verifier able to prove functional properties of Ethereum smart contracts. VerX addresses an important problem as all real-world contracts must satisfy custom functional specifications.VerX is based on a careful combination of three techniques, enabling it to automatically verify temporal properties of infinite- state smart contracts: (i) reduction of temporal property verification to reachability checking, (ii) a new symbolic execution engine for the Ethereum Virtual Machine that is precise and efficient for a practical fragment of Ethereum contracts, and (iii) delayed predicate abstraction which uses symbolic execution during transactions and abstraction at transaction boundaries.Our extensive experimental evaluation on 83 temporal properties and 12 real-world projects, including popular crowdsales and libraries, demonstrates that VerX is practically effective.
