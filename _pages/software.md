---
layout: archive
permalink: /software/
title: "Software"
author_profile: true
---

Throughout the course of my academic career I have worked with different scientific software suites to interpret observed astronomical data and generate theoretical models that describe the life of a (variable) star that vibrates in its natural frequencies.
Such vibrations cause the star to periodically dim and brighten, which can be observed in astronomical data products, such as the photometric light curves (of specific variable stars) that I have studied in my doctoral dissertation.

I regularly use the [Modules for Experiments in Stellar Astrophysics (MESA)](https://docs.mesastar.org/en/stable/) stellar evolution code, the [GYRE](https://gyre.readthedocs.io/en/stable/) stellar oscillation code and [Wolfram Mathematica](https://www.wolfram.com/mathematica/) in my scientific endeavors.
A succinct description of these computational frameworks is given below.

I am also a developer of computational frameworks/scientific software suites.
Most of my coding efforts for the development of these frameworks have been made in the [Python](https://www.python.org) language, although parts of my frameworks have been written in [C++](https://isocpp.org/), [Fortran](https://fortran-lang.org/) and [Cython](https://cython.org).
More recently, I started exploring the capabilities of the [Rust language](https://www.rust-lang.org) for future scientific projects.
Although the Rust language looks promising for the development of scientific software suites, I do not yet have any publicly available (large) computational frameworks written predominantly in this language.

> I am always actively seeking for (and passionate about) opportunities to learn more about other astrophysical (or non-astrophysical) code suites/using different computer languages for my work. 
> *Please reach out if you have interesting ideas to do so.*
> *If you think my software could be beneficial to you, I also encourage you to contact me.*

## Scientific Software Suites I Like to Use

> *Additional information on these scientific software suites can be found on their respective websites, whose hyperlinks are provided below the succinct descriptions in the form of clickable logos.*

### Modules for Experiments in Stellar Astrophysics ([MESA](https://docs.mesastar.org/en/stable/)) + [GYRE](https://gyre.readthedocs.io/en/stable/) stellar oscillation code

The large scientific software suite [MESA](https://docs.mesastar.org/en/stable/) is widely used by astrophysicists to simulate the evolution (life) of a star, and enables the user to specify a large variety of different hooks (that make a [MESA](https://docs.mesastar.org/en/stable/) run very customizable).
It assumes certain widely used simplifications (for example, spherical symmetry) to be able to simulate how a star evolves from its birth to its death.

I have used it to generate baseline models of the stellar structure at various moments throughout the evolution of star models of specific mass at starbirth.
These baseline models were then employed in the [GYRE](https://gyre.readthedocs.io/en/stable/) oscillation code to simulate waves propagating throughout the stellar interior.
[GYRE](https://gyre.readthedocs.io/en/stable/) can simulate non-interacting (linear) waves.
The models of these waves formed the input for the code suite that I developed, [AE Solver](https://github.com/JVB11/AESolver/), which simulates non-linear interactions between oscillations.

[<img src="/images/software/user/mesa-logo.png" style="width:40%; height:auto; margin-right:4%; margin-left:5%;">](https://docs.mesastar.org/en/stable/)
[<img src="/images/software/user/gyre-logo.png" style="width:40%; height:auto; margin-left:4%; margin-right:5%;">](https://gyre.readthedocs.io/en/stable/)

### Wolfram [Mathematica](https://www.wolfram.com/mathematica/)

Described on their website as *the world's definitive system for modern technical computing*, [Mathematica](https://www.wolfram.com/mathematica/) aids (typically theoretically-inclined) astrophysicists and scientists from other disciplines in the development of mathematical/theoretical frameworks.
I have used it extensively to check my own work (written on paper) while developing the theoretical framework that forms the basis for my computational framework [AESolver](https://github.com/JVB11/AESolver/).

[<img src="/images/software/user/wolfram.png" style="width:20%; height:auto; margin-left:40%;">](https://www.wolfram.com/mathematica/)

## Computational Frameworks I developed

<nbsp>

{% include base_path %}

{% assign ordered_pages = site.software | sort:"order_number" %}

{% for post in ordered_pages %}
  {% include archive-single.html type="grid" %}
{% endfor %}
