<p align="center">
  <img src="https://github.com/addy1997/RL-Algorithms/blob/master/logo.jpg"/>
</p>

[![Software License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](LICENSE)  [![Build Status](https://ci.appveyor.com/api/projects/status/8e784doc5sye7c41?svg=true)](https://ci.appveyor.com/project/addy1997/RL-Algorithms)  [![Stars](https://img.shields.io/github/stars/addy1997/RL-Algorithms.svg?style=flat&label=Star&maxAge=86400)](STARS) [![Contributions](https://img.shields.io/github/commit-activity/m/addy1997/RL-Algorithms.svg?color=%09%2346c018)](https://github.com/addy1997/RL-Algorithms/graphs/commit-activity) [![Coverage Status](https://coveralls.io/repos/github/addy1997/RL-Algorithms/badge.svg?branch=master)](https://coveralls.io/github/addy1997/RL-Algorithms?branch=master)
[![CodeFactor](https://www.codefactor.io/repository/github/addy1997/rl-algorithms/badge)](https://www.codefactor.io/repository/github/addy1997/rl-algorithms)
[![Lines Of Code](https://tokei.rs/b1/github/addy1997/RL-Algorithms?category=code)](https://github.com/addy1997/RL-Algorithms)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/addy1997/RL-Algorithms.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/addy1997/RL-Algorithms/alerts/) [![Code](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
#### Table of Contents

* [Epsilon Greedy](#Epsilon-Greedy)
* [Epsilon Decay](#Epsilon-Decay)
* [Gradient Bandits](#Gradient-Bandits) 
* [SARSA](#SARSA)
* [Q_learning](#Q_learning)
* [Monte_Carlo](#Monte_Carlo)

## [Epsilon Greedy](#RL-Algorithms)

## [Epsilon Decay](#RL-Algorithms)

## [Gradient-Bandits](#RL-Algorithms)

## [SARSA](#RL-Algorithms)

# Algorithm 
![logo](https://github.com/addy1997/RL-Algorithms/blob/master/SARSA/SARSA_psuedo.png)

# Theory

**SARSA** is algorithm based on **on-policy** **TD(0)** method fro control tasks in reinforcement learning.
It follows **Generalised Policy Iteration** strategy: as the policy **π** becomes greedy with respect to the state-action value function, the state-action value function becomes more optimal.

* We learn the **state-action value** function **Q(s,a)** rather than **state-value** **V(s)**.
* Here, **qπ(s,a)** is the estimate for the current **behavior policy π** for all the state-actions pairs (s,a).
* Initialising a suitable state **s** (s should not be a terminal state).
* Choose an appropriate action **A** under the policy **epsilon-greedy or epsilon-soft**.
* Record the values of the **state S'** and the **reward R**.
* Update the function -> _Q(S, A) ← Q(S, A) + αR + γQ(S′, A′) − Q(S, A)_

* This loop runs till it encounters a terminal state where **Q(s',a')** = 0.

## [Q_learning](#RL-Algorithms)

## [Monte_carlo](#RL-Algorithms)





