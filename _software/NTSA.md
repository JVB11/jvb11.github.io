---
title: "Non-linear Time Series Analysis: NTSA"
layout: single-portfolio
excerpt: "<img src='/images/software/ntsa/NTSA_logo.png' alt=''>"
collection: software
order_number: 10
header:
    og_image: "software/ntsa/NTSA_logo.png"
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

Photometric light curves measure the total brightness of a star over time, and in order to extract periodic brightness variations (as expected for a variable star) from this data product various software suites can be used.
One such suite is this computational framework, [NTSA](https://github.com/JVB11/NTSA), that I developed for my doctoral dissertation.
It was originally developed to detect resonances among the frequencies of stellar oscillations, in order to select targets for theoretical modeling.
Its use for this application is highlighted in [Van Beeck et al. (2021)](https://www.aanda.org/articles/aa/full_html/2021/11/aa41572-21/aa41572-21.html), where we specifically looked for three-oscillation resonances in variable stars of spectral type B[^1] that fuse hydrogen isotopes in their cores.

An article describing the generic computational framework is to be made.
When using (part of) this code, you should therefore cite the application article, [Van Beeck et al. (2021)](https://www.aanda.org/articles/aa/full_html/2021/11/aa41572-21/aa41572-21.html).[^2]

{% include gallery %}

[^1]: See for example [this wikipedia page](https://en.wikipedia.org/wiki/Stellar_classification) to learn more about stellar classification.
[^2]: Check out the associated NASA ADS page for the [NTSA application article](https://ui.adsabs.harvard.edu/abs/2021A%26A...655A..59V/abstract) to easily export the data required for citing this article, which is available in different formats.
