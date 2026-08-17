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

{% include software-suite-links.html
  repo_url="https://github.com/JVB11/NTSA"
  repo_hover="GitHub repository of NTSA (work in progress)"
  doc_url="https://jvb11.github.io/NTSA"
  doc_hover="Documentation of NTSA (work in progress)" %}

{% include work-in-progress-warning-links.html
   type="warning"
   title="Work in Progress"
   text="Please note that some of the links above may not be fully functional yet because NTSA is under active development." %}

_**Context**_

[Photometric light curves](https://en.wikipedia.org/wiki/Photometry_(astronomy)) measure the total brightness variation of a star over time.
In order to extract information on these periodic brightness variations (i.e., the variability of a [variable star](https://en.wikipedia.org/wiki/Variable_star)) from this data product, various software suites can be used (which typically employ [harmonic analysis](https://en.wikipedia.org/wiki/Harmonic_analysis)).
One such suite is the computational framework described on this page, [NTSA](https://github.com/JVB11/NTSA), which I started developing during my PhD.

_**Purpose**_

The main purpose of this framework is to detect [resonances](https://en.wikipedia.org/wiki/Resonance) (i.e., resonant combination frequencies) among the frequencies of stellar oscillations.
[Variable stars](https://en.wikipedia.org/wiki/Variable_star) whose light curves display such resonances were considered (high) priority targets for the theoretical modeling of (non-linear) mode energy exchange.

_**Applications**_

How [NTSA](https://github.com/JVB11/NTSA) is used for the detection of resonant combination frequencies is described in [Van Beeck et al. (2021)](https://www.aanda.org/articles/aa/full_html/2021/11/aa41572-21/aa41572-21.html).
In that article we specifically searched for three-mode resonances in light curves of variable stars of spectral type B[^1] that fuse hydrogen isotopes in their cores (i.e., stars on the [main sequence](https://en.wikipedia.org/wiki/Main_sequence)), which are the so-called [slowly pulsating B (SPB) stars](https://en.wikipedia.org/wiki/Slowly_pulsating_B-type_star).

_**Citations/using this code**_

An article describing the generic computational framework is still in development.
When using (part of) this code, you should therefore cite the application article, [Van Beeck et al. (2021)](https://www.aanda.org/articles/aa/full_html/2021/11/aa41572-21/aa41572-21.html).

[^1]: See for example [this wikipedia page](https://en.wikipedia.org/wiki/Stellar_classification) to learn more about stellar classification.

<!-- {% include gallery %} -->
