---
title: "Non-linear Time Series Analysis: NTSA"
layout: single-portfolio
excerpt: "<img src='/images/software/ntsa/NTSA_logo.png' alt=''>"
collection: software
order_number: 10
header:
    og_image: "software/ntsa/NTSA_logo.png"
gallery:
    - url: software/ntsa/explained_scaled_variance.svg
      image_path: software/ntsa/explained_scaled_variance.svg
      alt: ""
      title: ""
    - url: software/ntsa/nr_candidate_resonances.svg
      image_path: software/ntsa/nr_candidate_resonances.svg
      alt: ""
      title: ""
    - url: software/ntsa/properties_resonances.svg
      image_path: software/ntsa/properties_resonances.svg
      alt: ""
      title: ""
---

_**Context**_

*[Photometric light curves](https://en.wikipedia.org/wiki/Photometry_(astronomy)) measure the total brightness variation of a star over time.
In order to extract information on these periodic brightness variations (i.e., the variability of a [variable star](https://en.wikipedia.org/wiki/Variable_star)) from this data product, various software suites can be used (which typically employ [harmonic analysis](https://en.wikipedia.org/wiki/Harmonic_analysis)).
One such suite is the computational framework described on this page, [NTSA](https://github.com/JVB11/NTSA), which I started developing during my PhD.*

_**Purpose**_

Originally, the main purpose of this framework was to detect [resonances](https://en.wikipedia.org/wiki/Resonance) (i.e., resonant combination frequencies) among the frequencies of stellar oscillations.
[Variable stars](https://en.wikipedia.org/wiki/Variable_star) whose light curves display such resonances were considered (high) priority targets for the theoretical modeling of (non-linear) mode energy exchange.

_**Applications**_

Use of [NTSA](https://github.com/JVB11/NTSA) for the detection of resonant combination frequencies is highlighted in [Van Beeck et al. (2021)](https://www.aanda.org/articles/aa/full_html/2021/11/aa41572-21/aa41572-21.html), where we specifically searched for three-mode resonances in light curves of variable stars of spectral type B[^1] that fuse hydrogen isotopes in their cores (i.e., stars on the [main sequence](https://en.wikipedia.org/wiki/Main_sequence)), which are the so-called [slowly pulsating B (SPB) stars](https://en.wikipedia.org/wiki/Slowly_pulsating_B-type_star).

_**Citations/using this code**_

An article describing the generic computational framework is to be made.
When using (part of) this code, you should therefore cite the application article, [Van Beeck et al. (2021)](https://www.aanda.org/articles/aa/full_html/2021/11/aa41572-21/aa41572-21.html).[^2]

[^1]: See for example [this wikipedia page](https://en.wikipedia.org/wiki/Stellar_classification) to learn more about stellar classification.
[^2]: Check out the associated NASA ADS page for the [NTSA application article](https://ui.adsabs.harvard.edu/abs/2021A%26A...655A..59V/abstract) to easily export the data required for citing this article, which is available in different formats.

<!-- {% include gallery %} -->
