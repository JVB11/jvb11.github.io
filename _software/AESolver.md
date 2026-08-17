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

The theoretical modeling of (standing) stellar vibrations - also known as stellar oscillation modes - has been the focus of my work for a large part of my (short) academic career.
It is quite commonly performed in the linear approximation, which neglects energy exchange among the oscillation modes.
To model the (non-linear) energy exchange among oscillation modes, I developed a computational framework called [AESolver](https://github.com/JVB11/AESolver).

_**Purpose**_

Modeling within the linear approximation offers the asteroseismologist theoretically predicted observables - oscillation mode frequencies - that are to be compared to the observed variability frequencies.
This computational framework simulates the non-linear energy exchange among oscillation modes, so that mode amplitudes can be modeled.
If we account for the projection of the stellar surface onto a telescope, the computed amplitudes (more specifically, their ratios in resonant triads) can be contrasted with the variability amplitudes detected in photometric light curves of variable stars suing that telescope.

_**Applications**_

In [Van Beeck et al. (2024)](https://www.aanda.org/articles/aa/full_html/2024/07/aa48369-23/aa48369-23.html) we use [AESolver](https://github.com/JVB11/AESolver) to compute amplitudes of gravity modes in a small model grid representative for slowly pulsating B stars.
We found that the ratios of amplitudes of modes in a resonant triad that fulfill certain (angular momentum conservation) selection rules (see [Van Beeck et al. (2024)](https://www.aanda.org/articles/aa/full_html/2024/07/aa48369-23/aa48369-23.html) for details) are the most promising non-linear theoretically predicted observables for constraining the models of stellar interiors.

_**Citations/using this code**_

The theoretical formalism that forms the basis for this computational framework is described in [Van Beeck et al. (2024)](https://www.aanda.org/articles/aa/full_html/2024/07/aa48369-23/aa48369-23.html).
When using (part of) this code, you should therefore cite that article.
