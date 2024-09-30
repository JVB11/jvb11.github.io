---
title: "Amplitude equations solver: AESolver"
layout: single-portfolio
excerpt: "<img src='/images/software/aesolver/AE_solver_logo.png' alt=''>"
collection: software
order_number: 20
header:
    og_image: "software/aesolver/AE_solver_logo.png"
---

_**Context**_

The theoretical modeling of stellar vibrations - also known as stellar oscillation modes - has been the focus of my work for a large part of my (short) academic career.
It is quite commonly performed in the linear approximation, which neglects energy exchange among the oscillation modes.
To model the (non-linear) energy exchange among oscillation modes, I developed a computational framework called [AESolver](https://github.com/JVB11/AESolver).

_**Purpose**_

Modeling within the linear approximation offers the asteroseismologist theoretically predicted observables - oscillation mode frequencies - that are to be compared to the observed variability frequencies.
Simulates the non-linear energy exchange among oscillation modes, so that mode amplitudes can be modelled (and compared to observed amplitudes).
The computed amplitudes (more specifically, their ratios in resonant triads) can then be contrasted with observed variability amplitudes detected in photometric light curves of variable stars.

_**Applications**_

In [Van Beeck et al. (2024)](https://www.aanda.org/articles/aa/full_html/2024/07/aa48369-23/aa48369-23.html) we use [AESolver](https://github.com/JVB11/AESolver) to compute amplitudes of gravity modes in a small model grid representative for slowly pulsating B stars.
We found that the ratios of amplitudes of modes in a resonant triad that fulfill certain selection rules (see [Van Beeck et al. (2024)](https://www.aanda.org/articles/aa/full_html/2024/07/aa48369-23/aa48369-23.html) for details) are the most promising non-linear theoretically predicted observables for constraining the models of stellar interiors.

_**Citations/using this code**_

The theoretical formalism that forms the basis for this computational framework is described in [Van Beeck et al. (2024)](https://www.aanda.org/articles/aa/full_html/2024/07/aa48369-23/aa48369-23.html).
When using (part of) this code, you should therefore cite that article.[^1]

[^1]: Check out the associated NASA ADS page for the [AESolver formalism article](https://ui.adsabs.harvard.edu/abs/2024A%26A...687A.265V/abstract) to easily export the data required for citing this article, which is available in different formats.
