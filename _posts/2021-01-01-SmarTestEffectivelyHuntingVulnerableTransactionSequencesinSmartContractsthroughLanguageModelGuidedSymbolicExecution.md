---
layout: post
title: "SmarTest: Effectively Hunting Vulnerable Transaction Sequences in Smart Contracts through Language Model-Guided Symbolic Execution"
categories: ['Topic: Security and Measurement', 'Topic: Smart Contracts', '2021', 'Venue: Usenix Security']
year: 2021
venue: Usenix Security
---
**Authors**: Sunbeom So, Seongjoon Hong, Hakjoo Oh

**Venue**: Usenix Security (2021)

**Abstract**: We present SMARTEST, a novel symbolic execution technique for effectively hunting vulnerable transaction sequences in smart contracts. Because smart contracts are stateful programs whose states are altered by transactions, diagnosing and understanding nontrivial vulnerabilities requires generating sequences of transactions that demonstrate the flaws. However, finding such vulnerable transaction sequences is challenging as the number of possible combinations of transactions is intractably large. As a result, most existing tools for smart contract analysis use abstractions and merely point out the locations of vulnerabilities, which in turn imposes a steep burden on users of understanding the bugs, or have limited power in generating transaction sequences. In this paper, we aim to overcome this challenge by combining symbolic execution with a language model for vulnerable transaction sequences, so that symbolic execution effectively prioritizes program paths that are likely to reveal vulnerabilities. Experimental results with real-world smart contracts show that SMARTEST significantly outperforms existing tools by finding more vulnerable transaction sequences including critical zero-day vulnerabilities.
