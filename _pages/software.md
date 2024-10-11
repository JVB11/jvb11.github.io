---
layout: archive
permalink: /software/
title: "Software"
excerpt: "This page contains a description of my view on research software. It also describes which scientific software suites I for advancing my research, and which software suites I developed for this same purpose."
author_profile: true
---

<style>
.big-custom-blockquote {
    font-style:italic;
    font-size:20px;
    line-height:24px;
    font-weight:500;
    padding-bottom:0px;
    width: 100%!important;
    padding: 1% 1.5% 1% 1.5%!important;
    margin-bottom: 0px;
    margin-top: 0px;
    margin-left: 0px;
    border-left: 5px solid #0066b2;
    border-bottom: 5px solid #0066b2;
    position: relative;
}

.big-custom-blockquote::before {
    content: ""!important;
    position: absolute!important;
    width: 10%;
    height: 100%!important;
    top: 0;
    left: -1px;
    border-top: 5px solid #0066b2;
}

.big-custom-blockquote::after {
    content: "";
    position: absolute;
    width: 100%;
    height: 15%;
    bottom: -5px;
    left: 0;
    box-shadow: inset -5px 0 0 0 #0066b2;
}
</style>

I have worked with different scientific software suites to interpret observed astronomical data and generate theoretical models that describe the life of a ([variable](https://en.wikipedia.org/wiki/Variable_star)) star that vibrates in its natural frequencies.
Such vibrations/oscillations cause the star to periodically dim and brighten, which can be observed in astronomical data products, such as the [photometric](https://en.wikipedia.org/wiki/Photometry_(astronomy)) light curves (of specific variable stars) that I have studied in my doctoral dissertation - these were observed by the [NASA Kepler space telescope](https://en.wikipedia.org/wiki/Kepler_space_telescope).

I use several scientific software suites for my scientific endeavors - these software suites are typically [FOSS](https://en.wikipedia.org/wiki/Free_and_open-source_software) (with the exception of Wolfram [Mathematica](https://www.wolfram.com/mathematica/)).
An overview of the suites I regularly use can be found below in the [*scientific software suites I like to use* section](#scientific-software-suites-i-like-to-use).

I also develop computational frameworks for research purposes - check them out in the [*computational frameworks I developed* section](#computational-frameworks-i-developed) below.
Most of my own code has been written in the [Python](https://www.python.org) language, although parts of my frameworks make use of modules written in [C++](https://isocpp.org/), [Fortran](https://fortran-lang.org/) and [Cython](https://cython.org).
More recently, I started exploring the capabilities of the [Rust language](https://www.rust-lang.org) and the [Julia language](https://julialang.org) for future scientific projects.

<figure>
  <blockquote class="big-custom-blockquote">
  <p>Writing (research) software is one of my passions, and I regularly like to challenge myself to learn more about different (typically astrophysical) software suites/different programming languages.</p> 
  <p>If you share this passion and want to develop your own (research) software, I highly recommend reading and applying the FAIR (Findable, Accessible, Interoperable and Reusable) principles for Research Software (FAIR4RS principles, described in <a href="https://www.nature.com/articles/s41597-022-01710-x">this Nature publication</a>).</p>
  </blockquote>
</figure>

## Scientific Software Suites I Like to Use

> *Additional information about these scientific software suites can be found on their websites, which can be accessed by clicking on the logos or hyperlinks.*

### Modules for Experiments in Stellar Astrophysics ([MESA](https://docs.mesastar.org/en/stable/)) + [GYRE](https://gyre.readthedocs.io/en/stable/) stellar oscillation code

[<img src="/images/software/user/mesa-logo.png" style="width:40%; height:auto; margin-top:1%; margin-right:0%; margin-left:3%; margin-bottom:3%; float:right;">](https://docs.mesastar.org/en/stable/)The publicly availabe large scientific software suite [MESA](https://docs.mesastar.org/en/stable/) is widely used by astrophysicists to simulate the evolution (life) of a star, and enables the user to specify a large variety of different hooks (that make a [MESA](https://docs.mesastar.org/en/stable/) run very customizable).
It assumes certain widely used simplifications (for example, spherical symmetry) to be able to simulate how a star evolves from its birth to its death.
I have used [MESA](https://docs.mesastar.org/en/stable/) to generate baseline models of the stellar structure at various moments throughout the evolution of star models of specific mass at starbirth.

[<img src="/images/software/user/gyre-logo.png" style="width:40%; height:auto; margin-top:1%; margin-right:3%; margin-left:0%; margin-bottom:0%; float:left;">](https://gyre.readthedocs.io/en/stable/)Such baseline models were then employed as input for the publicly available [GYRE](https://gyre.readthedocs.io/en/stable/) stellar oscillation code to simulate waves propagating throughout the stellar interior. 
[GYRE](https://gyre.readthedocs.io/en/stable/) can simulate non-interacting (linear) waves. 
The models of these waves formed the input for the code suite that I developed, [AESolver](https://github.com/JVB11/AESolver/), which simulates non-linear interactions between oscillations. <br>

### Wolfram [Mathematica](https://www.wolfram.com/mathematica/)

[<img src="/images/software/user/wolfram.png" style="width:14%; height:auto; margin-top:1%; margin-right:0%; margin-left:3%; margin-bottom:1%; float:right;">](https://www.wolfram.com/mathematica/)Described on their website as *the world's definitive system for modern technical computing*, [Mathematica](https://www.wolfram.com/mathematica/) aids (typically theoretically-inclined) astrophysicists and scientists from other disciplines in the development of mathematical/theoretical frameworks.
I have used it to check my own work (written on paper) while developing the theoretical framework that forms the basis for my computational framework [AESolver](https://github.com/JVB11/AESolver/).

## Computational Frameworks I developed

> Click on the hyperlinks or logos below to find out more about my computational frameworks!
> If you think my software is interesting and could be beneficial to you, or if you have ideas on how to improve my software suites and their documentation, I encourage you to reach out/contact me.

<nbsp>

{% include base_path %}

{% assign ordered_pages = site.software | sort:"order_number" %}

{% for post in ordered_pages %}
  {% include archive-single.html type="grid" %}
{% endfor %}
