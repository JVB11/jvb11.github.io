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

<style>
  [data-hover]:relative { position: relative; }
  [data-hover]::after {
    content: attr(data-hover);
    position: absolute; bottom: -35px; left: 50%; transform: translateX(-50%);
    background: #222; color: #fff; padding: 4px 8px; font-size: 0.75rem; white-space: nowrap;
    border-radius: 6px;
    opacity: 0; visibility: hidden; transition: 0.15s;
  }
  [data-hover]:hover::after { opacity: 1; visibility: visible; }
</style>

<div style="display: flex; justify-content: flex-start; align-items: center; gap: 2.5rem; margin-top: 0.5rem; margin-bottom:1.0rem; margin-left: 0.75rem;">
  <!-- GitHub Repository link -->
  <a href="https://github.com/JVB11/NTSA" target="_blank" rel="noopener" style="text-decoration: none; line-height: 1; position: relative" data-hover="GitHub repository of NTSA">
    <i class="fab fa-github" style="color: #ffffff; font-size: 2.5rem;"></i>
  </a>
  <!-- Documentation link -->
  <a href="https://github.com/JVB11/NTSA" target="_blank" rel="noopener" style="text-decoration: none; line-height: 1; display: flex; align-items: center;" title="Documentation of NTSA">
    <img src="/images/software/readme-brands-solid-full.svg" alt="" style="height: 2.9rem; width: auto; filter: brightness(0) invert(1);">
  </a>
</div>

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
