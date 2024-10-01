---
title: "Non-linear Coupling of Oscillation Modes"
layout: single-portfolio
collection: research
order_number: 30
img: "coupling_triads_dark_mode.svg"
header:
    og_image: "research/coupling_triads_dark_mode.svg"
---

## Non-linear Resonant Coupling & Modeling potential

Asteroseismic analyses of variable stars are mostly performed in a linear setting, in which mode frequencies/periods and their patterns are the primary observables to constrain stellar structure and evolution models.
Mode amplitude predictions cannot be made within a linear framework.
The combination frequencies that are frequently detected when generating mode frequencies lists with harmonic analyses also cannot be accomodated within such a linear framework.
The presence of some of these combination frequencies can be explained by non-linear mode coupling/energy exchange processes among the oscillation modes.
Strongest among the possible non-linear couplings are the resonant couplings.

We therefore examined how the lowest-order (three-mode) non-linear resonant couplings implicate that amplitude equations can be used to predict mode amplitudes, which could subsequently be compared to the observed variability amplitudes.
In [Van Beeck et al. 2024](https://www.aanda.org/articles/aa/full_html/2024/07/aa48369-23/aa48369-23.html) we showed that the ratios of stationary amplitudes of 3 resonantly interacting modes could aid future (non-linear) asteroseismic modeling, serving as a constraint additional to the (linear) pulsation frequencies/periods.
Non-stationary amplitudes could also be simulated using our framework.
Higher-order coupling networks and inter-mode coupling (e.g., coupling between rossby and gravity modes) should be explored in the future to assess the effect self-saturation will have.
Wave-driven angular momentum transport is also affected by non-linear mode coupling, which we have not yet considered in our current models.
There's plenty of work left to do!

{% include base_path %}

<kdb>
<div class="container">
<figure style="display:table; float:left; margin-right:6%; width:47%;">
  <a href="{{ '/images/research/coupling_triads_dark_mode.svg' | prepend: base_path }}" class="image-popup" title="Schematic overview of triads of interacting oscillation modes.">
    <img src="{{ '/images/research/coupling_triads_dark_mode.svg' | prepend: base_path }}" alt="Schematic overview of triads of interacting oscillation modes." style="width:100%; height:auto;">
  </a>
  <figcaption style="display: table-caption; caption-side: bottom;">Schematic overview of triads of interacting oscillation modes. Orange circles indicate oscillation modes that naturally occur (i.e., are linearly driven) within the star (model). Purple squares indicate oscillation modes that would not be sustained (i.e., linearly damped) within the star without non-linear energy exchange among the modes in the triad.</figcaption>
</figure>
<figure style="display:table; float:left; margin-right:auto; width:47%;">
  <a href="{{ '/images/research/mode_coupling/coupling_profile.svg' | prepend: base_path }}" class="image-popup" title="Example of a profile of the mode coupling coefficient in the stellar model interior.">
    <img src="{{ '/images/research/mode_coupling/coupling_profile.svg' | prepend: base_path }}" alt="Example of a profile of the mode coupling coefficient in the stellar model interior." style="width:100%; height:auto;">
  </a>
  <figcaption style="display: table-caption; caption-side: bottom;">Mode energy exchange efficiency/mode coupling coefficient $\eta$ of a specific gravity mode triad in the interior of a slowly pulsating B star model (blue) vs. the squared <a href='https://en.wikipedia.org/wiki/Brunt–Väisälä_frequency'>buoyancy frequency</a> $N^2$ (a measure of the stability of a fluid to vertical displacements; it is a measure of stratification). On the x-axis we show the radial coordinate $r$ divided by the stellar model radius $R$ (i.e., $r/R = 1$ is the location of the stellar surface, and $r/R = 0$ is the center of the model). Most of the coupling for this triad occurs just above the stellar core, which is denoted by the large jump in buoyancy frequency near $r/R \approx 0.1$.</figcaption>
</figure>
</div>
</kdb>

## Relevant Publications & Software

### Software

Check out the [AESolver](https://github.com/JVB11/AESolver) computational framework that we developed for the purpose of simulating (resonant) non-linear mode three-mode coupling in rotating stars.
A succinct description of this software suite is given on the [relevant software page](https://jvb11.github.io/software/AESolver/).

The framework we developed currently only considers 1-dimensional ([MESA](https://docs.mesastar.org/en/stable/)) stellar structure models as input.
Any improvements in the description of opacity in the stellar interior will affect linear excitation properties of oscillation modes, which also is translated in the non-linear coupling properties and transport of angular momentum.
Multi-dimensional magneto-hydrodynamic (or hydrodynamic) simulations of the stellar interior could therefore be very beneficial in proving that our coupling results hold for more intricate stellar structures (and different opacity profiles).
It is my goal to adapt the [AESolver](https://github.com/JVB11/AESolver) software suite to use such simulation input to validate (or disprove) our conclusions.

<figure>
  <a href="{{ '/images/software/aesolver/AE_solver_logo.png' | prepend: base_path }}" class="image-popup">
    <img src="{{ '/images/software/aesolver/AE_solver_logo.png' | prepend: base_path }}" alt="Logo of the AESolver software suite">
  </a>
</figure>

### Publications

**Van Beeck J.**, Van Hoolst T., Aerts C., Fuller J.; Non-linear three-mode coupling of gravity modes in rotating slowly pulsating B stars. Stationary solutions and modeling potential. July 2024, Astronomy & Astrophysics, Vol. 687, A265. [HTML](https://www.aanda.org/articles/aa/full_html/2024/07/aa48369-23/aa48369-23.html) [PDF](https://www.aanda.org/articles/aa/pdf/2024/07/aa48369-23.pdf)

