---
permalink: /software/
title: "Software"
gallery:
    - url: software/ntsa/explained_scaled_variance.pdf
      image_path: software/ntsa/explained_scaled_variance.pdf
      alt: ""
      title: ""
    - url: software/ntsa/nr_candidate_resonances.pdf
      image_path: software/ntsa/nr_candidate_resonances.pdf
      alt: ""
      title: ""
    - url: software/ntsa/properties_resonances.pdf
      image_path: software/ntsa/properties_resonances.pdf
      alt: ""
      title: ""
---

Throughout the course of my academic career I have worked with different scientific software suites to interpret observed astronomical data and generate theoretical models that describe the life of a (variable) star that vibrates in its natural frequencies.
Such vibrations cause the star to periodically dim and brighten, which can be observed in astronomical data products, such as photometric light curves.

These light curves measure the total brightness of a star over time, and in order to extract the periodic variations from this data product various software suites can be used.
One such suite is the computational framework I developed for my doctoral dissertation, [NTSA](https://github.com/JVB11/NTSA), which is described in more detail below.

The theoretical modeling of these vibrations - also known as stellar oscillations - has been the focus of my work for a large part of my (short academic) career.
To perform this theoretical modeling I developed a computational framework, [AE Solver](https://github.com/JVB11/AESolver), that aims to simulate the (non-linear) energy exchange among different stellar oscillations in order to model their amplitudes in, for example, observed stellar light curves.

In addition to the computational frameworks that I have developed, I regularly use the [Modules for Experiments in Stellar Astrophysics (MESA)](https://docs.mesastar.org/en/stable/) stellar evolution code, the [GYRE](https://gyre.readthedocs.io/en/stable/) stellar oscillation code and [Wolfram Mathematica](https://www.wolfram.com/mathematica/) in my scientific endeavors.
More information on those code suites can be found on their respective websites.

Most of my coding efforts have been made in the [Python]() language, although parts of my frameworks have been written in [C++](https://isocpp.org/), [Fortran](https://fortran-lang.org/) and [Cython](https://cython.org).
More recently, I started exploring the capabilities of the [Rust language](https://www.rust-lang.org) for future scientific projects.
Although it looks promising, I do not yet have any publicly available computational frameworks that were written predominantly in this language.

I am always actively seeking for (and passionate about) opportunities to learn more about other astrophysical (or non-astrophysical) code suites/using different computer languages for my work, so please reach out if you have interesting ideas to do so.
Reversely, if you think my software could be beneficial to you, I also encourage you to contact me.

## Non-linear Time Series Analysis (NTSA) <a href="https://github.com/JVB11/NTSA"><img align="right" width="200" height="133" src="/images/software/ntsa/NTSA_logo.png"></a>

This computational framework was originally developed to detect resonances among the frequencies of stellar oscillations, in order to select targets for theoretical modeling.
Its use for this application is highlighted in [Van Beeck et al. (2021)](https://www.aanda.org/articles/aa/full_html/2021/11/aa41572-21/aa41572-21.html), where we specifically looked for three-oscillation resonances in variable stars of spectral type B[^1] that fuse hydrogen isotopes in their cores.

An article describing the generic computational framework is to be made.
When using (part of) this code, you should therefore cite the application article, [Van Beeck et al. (2021)](https://www.aanda.org/articles/aa/full_html/2021/11/aa41572-21/aa41572-21.html).[^2]

{% include gallery %}

## Amplitude Equations Solver (AE Solver) <a href="https://github.com/JVB11/AESolver"><img align="right" width="180" height="132" src="/images/software/aesolver/AE_solver_logo.png"></a>

The theoretical formalism that forms the basis for this computational framework is described in [Van Beeck et al. (2024)](https://www.aanda.org/articles/aa/full_html/2024/07/aa48369-23/aa48369-23.html).
When using (part of) this code, you should therefore cite that article.[^2]

[^1]: See for example [this wikipedia page](https://en.wikipedia.org/wiki/Stellar_classification) to learn more about stellar classification.
[^2]: Check out the associated NASA ADS pages for the [NTSA application article](https://ui.adsabs.harvard.edu/abs/2021A%26A...655A..59V/abstract) and the [AE Solver formalism article](https://ui.adsabs.harvard.edu/abs/2024A%26A...687A.265V/abstract) to easily export the data required for citing these articles, which is available in different formats.
