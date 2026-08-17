---
layout: archive
permalink: /software/
title: "Software"
excerpt: "This page contains a description of my view on research software. It also contains links to pages where I describe which scientific software suites I use for advancing my research, and which software suites I developed for this same purpose."
author_profile: true

feature_row:
  - title: ""
    url: "/software/use/"
    btn_class: "btn--info"
    btn_label: "Software suites I use"

  - title: ""
    url: "/software/develop/"
    btn_class: "btn--info"
    btn_label: "Software suites I develop"    
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

I use several scientific software suites for my scientific endeavors - these software suites are typically [FOSS](https://en.wikipedia.org/wiki/Free_and_open-source_software) (with the exception of [Wolfram Mathematica](https://www.wolfram.com/mathematica/)).
I also develop my own computational frameworks for research purposes.
Most of my own code has been written in the [Python](https://www.python.org) and [Fortran](https://fortran-lang.org/) languages, and some of my frameworks make use of Python-interfaced modules written in [C++](https://isocpp.org/) and [Fortran](https://fortran-lang.org/), where the interface is written in [Cython](https://cython.org).
I also enjoy exploring the capabilities of the [Rust language](https://www.rust-lang.org) and the [Julia language](https://julialang.org) for (future) scientific projects.

{% include feature_row %}

<figure>
  <blockquote class="big-custom-blockquote">
  <p>Writing (research) software is one of my passions, and I regularly like to challenge myself to learn more about different (typically astrophysical) software suites/different programming languages.</p> 
  <p>If you share this passion and want to develop your own (research) software, I highly recommend reading and applying the FAIR (Findable, Accessible, Interoperable and Reusable) principles for Research Software (FAIR4RS principles, which are described in <a href="https://www.nature.com/articles/s41597-022-01710-x">this Nature publication</a>).</p>
  </blockquote>
</figure>
