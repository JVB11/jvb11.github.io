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

<figure>
  <blockquote class="big-custom-blockquote">
  <p>I highly recommend reading and applying the FAIR (Findable, Accessible, Interoperable and Reusable) principles for Research Software (FAIR4RS principles, described in <a href="https://www.nature.com/articles/s41597-022-01710-x">this Nature publication</a>) when developing your own (research) software.</p>
  </blockquote>
</figure>

Throughout the course of my academic career I have worked with different scientific software suites to interpret observed astronomical data and generate theoretical models that describe the life of a ([variable](https://en.wikipedia.org/wiki/Variable_star)) star that vibrates in its natural frequencies.
Such vibrations cause the star to periodically dim and brighten, which can be observed in astronomical data products, such as the [photometric](https://en.wikipedia.org/wiki/Photometry_(astronomy)) light curves (of specific variable stars) that I have studied in my doctoral dissertation.

I regularly use the [Modules for Experiments in Stellar Astrophysics (MESA)](https://docs.mesastar.org/en/stable/) stellar evolution code, the [GYRE](https://gyre.readthedocs.io/en/stable/) stellar oscillation code and [Wolfram Mathematica](https://www.wolfram.com/mathematica/) in my scientific endeavors.
A succinct description of these computational frameworks is given below in the '*scientific software suites I like to use*' section.

I am also a developer of computational frameworks/scientific software suites (see the '*computational frameworks I developed*' section).
When developing these frameworks, I mostly have made use of the [Python](https://www.python.org) language, although parts of my frameworks have been written in [C++](https://isocpp.org/), [Fortran](https://fortran-lang.org/) and [Cython](https://cython.org).
More recently, I started exploring the capabilities of the [Rust language](https://www.rust-lang.org) and the [Julia language](https://julialang.org) for future scientific projects. 
I do not yet have any publicly available repositories that predominantly rely upon these languages.

> I am always actively seeking for (and passionate about) opportunities to learn more about other astrophysical (or non-astrophysical) code suites and/or using different computer languages for my work. 
> If you think my software could be beneficial to you or if you have ideas on how to improve my software suites (and their documentation), I encourage you to reach out/contact me.

## Scientific Software Suites I Like to Use

> *Additional information about these scientific software suites can be found on their websites, which can be accessed by clicking on the logos.*

### Modules for Experiments in Stellar Astrophysics ([MESA](https://docs.mesastar.org/en/stable/)) + [GYRE](https://gyre.readthedocs.io/en/stable/) stellar oscillation code

The publicly availabe large scientific software suite [MESA](https://docs.mesastar.org/en/stable/) is widely used by astrophysicists to simulate the evolution (life) of a star, and enables the user to specify a large variety of different hooks (that make a [MESA](https://docs.mesastar.org/en/stable/) run very customizable).[<img src="/images/software/user/mesa-logo.png" style="width:40%; height:auto; margin:5%; float:right;">](https://docs.mesastar.org/en/stable/)
It assumes certain widely used simplifications (for example, spherical symmetry) to be able to simulate how a star evolves from its birth to its death.
I have used it to generate baseline models of the stellar structure at various moments throughout the evolution of star models of specific mass at starbirth.

[<img src="/images/software/user/gyre-logo.png" style="width:40%; height:auto; margin:5%; float:left;">](https://gyre.readthedocs.io/en/stable/)Such baseline models were then employed as input for the publicly available [GYRE](https://gyre.readthedocs.io/en/stable/) oscillation code to simulate waves propagating throughout the stellar interior. 
[GYRE](https://gyre.readthedocs.io/en/stable/) can simulate non-interacting (linear) waves. 
The models of these waves formed the input for the code suite that I developed, [AE Solver](https://github.com/JVB11/AESolver/), which simulates non-linear interactions between oscillations. 

### Wolfram [Mathematica](https://www.wolfram.com/mathematica/)

Described on their website as *the world's definitive system for modern technical computing*, [Mathematica](https://www.wolfram.com/mathematica/) aids (typically theoretically-inclined) astrophysicists and scientists from other disciplines in the development of mathematical/theoretical frameworks.[<img src="/images/software/user/wolfram.png" style="width:20%; height:auto; margin:10%; float:right;">](https://www.wolfram.com/mathematica/)
I have used it extensively to check my own work (written on paper) while developing the theoretical framework that forms the basis for my computational framework [AESolver](https://github.com/JVB11/AESolver/).

## Computational Frameworks I developed

<nbsp>

{% include base_path %}

{% assign ordered_pages = site.software | sort:"order_number" %}

{% for post in ordered_pages %}
  {% include archive-single.html type="grid" %}
{% endfor %}
