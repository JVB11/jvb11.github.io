---
permalink: /software/
title: "Software"
---

Throughout the course of my academic career I have worked with different scientific software suites to interpret observed astronomical data and generate theoretical models that describe the life of a (variable) star that vibrates in its natural frequencies.
Such vibrations cause the star to periodically dim and brighten, which can be observed in astronomical data products, such as photometric light curves.

These light curves measure the total brightness of a star over time, and in order to extract the periodic variations from this data product various software suites can be used.
One such suite is the computational framework I developed for my doctoral dissertation, [NTSA](https://github.com/JVB11/NTSA), which is described in more detail below.

The theoretical modeling of these vibrations - also known as stellar oscillations - has been the focus of my work for a large part of my (short academic) career.
To perform this theoretical modeling I developed a computational framework, [AE Solver](https://github.com/JVB11/AESolver), that aims to simulate the (non-linear) energy exchange among different stellar oscillations in order to model their amplitudes in, for example, observed stellar light curves.

## Non-linear Time Series Analysis (NTSA) <a href="https://github.com/JVB11/NTSA"><img align="right" width="300" height="200" src="/images/software/NTSA_logo.png"></a>

This computational framework was originally developed to detect resonances among the frequencies of stellar oscillations, in order to select targets for theoretical modeling.
Its use for this application is highlighted in [Van Beeck et al. (2021)](https://www.aanda.org/articles/aa/full_html/2021/11/aa41572-21/aa41572-21.html), where we specifically looked for three-oscillation resonances in variable stars of spectral type B[^1] that fuse hydrogen isotopes in their cores.

An article describing the generic computational framework is to be made.
When using (part of) this code, you should therefore cite the application article, [Van Beeck et al. (2021)](https://www.aanda.org/articles/aa/full_html/2021/11/aa41572-21/aa41572-21.html).[^2]

## Amplitude Equations Solver (AE Solver) <a href="https://github.com/JVB11/AESolver"><img align="right" width="240" height="176" src="/images/software/AE_solver_logo.png"></a>

The theoretical formalism that forms the basis for this computational framework is described in [Van Beeck et al. (2024)](https://www.aanda.org/articles/aa/full_html/2024/07/aa48369-23/aa48369-23.html).
When using (part of) this code, you should therefore cite that article.[^2]

[^1]: See for example [this wikipedia page](https://en.wikipedia.org/wiki/Stellar_classification) to learn more about stellar classification.
[^2]: Check out the associated NASA ADS pages for the [NTSA application article](https://ui.adsabs.harvard.edu/abs/2021A%26A...655A..59V/abstract) and the [AE Solver formalism article](https://ui.adsabs.harvard.edu/abs/2024A%26A...687A.265V/abstract) to easily export the data required for citing these articles, which is available in different formats.
