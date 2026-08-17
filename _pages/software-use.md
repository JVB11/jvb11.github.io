---
layout: archive
permalink: /software/use/
title: "Software I Use"
excerpt: "This page describes which scientific software suites I use for advancing my research."
author_profile: true
---

I use several scientific software suites for my scientific endeavors - these software suites are typically [FOSS](https://en.wikipedia.org/wiki/Free_and_open-source_software) (with the exception of [Wolfram Mathematica](https://www.wolfram.com/mathematica/)).

> Additional information about the scientific software suites I use can be found on their websites, which can be accessed by clicking on the logos or hyperlinks.

## Modules for Experiments in Stellar Astrophysics ([MESA](https://docs.mesastar.org/en/stable/)) + [GYRE](https://gyre.readthedocs.io/en/stable/) stellar oscillation code

[<img src="/images/software/user/mesa-logo.png" style="width:40%; height:auto; margin-top:1%; margin-right:0%; margin-left:3%; margin-bottom:3%; float:right;">](https://docs.mesastar.org/en/stable/)The publicly availabe large scientific software suite [MESA](https://docs.mesastar.org/en/stable/) is widely used by astrophysicists to simulate the evolution (life) of a star, and enables the user to specify a large variety of different hooks (that make a [MESA](https://docs.mesastar.org/en/stable/) run very customizable).
It assumes certain widely used simplifications (for example, spherical symmetry) to be able to simulate how a star evolves from its birth to its death.
I have used [MESA](https://docs.mesastar.org/en/stable/) to generate baseline models of the stellar structure at various moments throughout the evolution of star models of specific mass at starbirth.

[<img src="/images/software/user/gyre-logo.png" style="width:40%; height:auto; margin-top:1%; margin-right:3%; margin-left:0%; margin-bottom:0%; float:left;">](https://gyre.readthedocs.io/en/stable/)Such baseline models were then employed as input for the publicly available [GYRE](https://gyre.readthedocs.io/en/stable/) stellar oscillation code to simulate waves propagating throughout the stellar interior. 
[GYRE](https://gyre.readthedocs.io/en/stable/) can simulate non-interacting (linear) standing and tidal waves. 
The models of these standing waves formed the input for the code suite that I developed, [AESolver](https://github.com/JVB11/AESolver/), which simulates non-linear interactions between oscillations. <br>

## Wolfram [Mathematica](https://www.wolfram.com/mathematica/)

[<img src="/images/software/user/wolfram.png" style="width:14%; height:auto; margin-top:1%; margin-right:0%; margin-left:3%; margin-bottom:1%; float:right;">](https://www.wolfram.com/mathematica/)Described on their website as *the world's definitive system for modern technical computing*, [Mathematica](https://www.wolfram.com/mathematica/) aids (typically theoretically-inclined) astrophysicists and scientists from other disciplines in the development of mathematical/theoretical frameworks.
I have used it to check my own work (derivations written on paper) while developing the theoretical framework that forms the basis for my computational frameworks [AESolver](https://github.com/JVB11/AESolver/) and [dervish](https://github.com/JVB11/dervish).
