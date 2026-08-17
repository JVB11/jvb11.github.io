---
title: "dervish"
layout: single-portfolio
excerpt: "<img src='/images/software/dervish/dervish_logo.png' alt=''>"
collection: software
order_number: 30
header:
    og_image: "software/dervish/dervish_logo.png"
---

{% include software-suite-links.html
  repo_url="https://github.com/JVB11/dervish"
  repo_hover="GitHub repository of dervish (work in progress)"
  doc_url="https://jvb11.github.io/dervish/"
  doc_hover="Documentation of dervish (work in progress)" %}

{% include work-in-progress-warning-links.html %}

_**Context**_

The theoretical modeling of a specific kind of *(mixed)* stellar vibrations in evolved [red-giant stars](https://en.wikipedia.org/wiki/Red_giant) needs to be able to explain why observed *frequency splittings* (i.e., the lifting of degeneracy due to rotation and/or other symmetry-breaking effects) are asymmetric.
Higher-order rotational effects that occur for differentially rotating red giants are typically not included.
To model these effects, I am developing a computational framework called [dervish](https://github.com/JVB11/dervish).

_**Purpose**_

Modeling higher-order effects of rotation on adiabatic linear oscillations of a rotating red-giant star offers the asteroseismologist a good first window on the importance of different contributing terms.
This computational framework revisits *(and corrects)* published theoretical frameworks, and provides the means to distinguish between different contributions to the rotational perturbation of the oscillation frequency up to second order (*for now*).
It also computes the perturbations of the eigenfunctions due to rotation, and accounts for the rotational distortion (of the star) in a perturbative manner.
This allows the user to compute asymmetric rotational splittings for the frequently observed dipole (*for now*) mixed modes in red-giant stars.

_**Applications**_

Work in progress.

_**Citations/using this code**_

Work in progress.
