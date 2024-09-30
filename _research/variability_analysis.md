---
title: "Variability Analysis of Stars"
layout: single-portfolio
collection: research
order_number: 10
img: "explained_scaled_variance.svg"
header:
    og_image: "research/explained_scaled_variance.svg"
---

## Harmonic Analysis (Asteroseismology)

To describe the variability in brightness of a variable star it is quite common that harmonic analysis is used.
This harmonic analysis consists of a (iterative) Fourier decomposition of the observed signal, resulting in parameters that describe the variability using a sum-of-sines or variability model $F(t_i)$ for the observed (photometric) light curve:

$$ F(t_i) = \beta_0 + \sum_{j=1}^{n_{\rm f}} A_j \sin\left[2\pi\nu_jt_i + \phi_j\right] $$

where $\beta_0$ is a parameter that corrects for a detrending offset, and the parameters with subscript $j$ relate to the amplitudes ($A_j$), (temporal) frequencies ($\nu_j$) and phases ($\phi_j$) at a specific time $t_i$ for which the stellar brightness was observed.

_For technical details on harmonic analysis, I refer the interested reader towards section 2 of [Van Beeck et al. (2021)](https://www.aanda.org/articles/aa/full_html/2021/11/aa41572-21/aa41572-21.html)_

## Robust Frequency Analysis

> Several approaches to harmonic analysis (or iterative prewhitening) were taken in literature.
One often undefined source of uncertainty when performing such analysis is the lack of assessment of how various approaches systematically influence results.

We therefore employed five different strategies that emulate various approaches taken in literature and assessed their capacity for modeling the light curves.
This resulted in robust variability models (that take into account systematics) for a sample of slowly pulsating B stars in [Van Beeck et al. (2021)](https://www.aanda.org/articles/aa/full_html/2021/11/aa41572-21/aa41572-21.html).
Other works have used the same computational framework to characterize variability in the light curves of close ellipsing binaries with tidally perturbed gravity-mode oscillations, HD 112429 (where it was used to measure near-core rotation), and identified g-mode pulsators of the young open cluster UBC1 (to age-date the cluster).

## Resonant Frequency Detection

> Linear asteroseismology employs oscillation mode frequencies to model waves propagating in stellar interiors (and constrain the numerical implementations of physical laws included in these models of the stellar interior).
It is clear however that using only the variability frequencies leaves much of the information in the variability model $F(t_i)$ unused.
Moreover, linear theory cannot explain why some oscillation modes are sustained (and observed) for long periods inside stars.

To explain why some modes are excited and others are damped - the problem of mode selection - a non-linear wave formalism is required (i.e., we enter the realms of non-linear asteroseismology) as this model can explain (significant) energy exchanges/coupling between modes.
The lowest-order non-linear coupling theories describe interactions between sets of 3 modes, or triads, with resonant interactions being the strongest.

One important goal of my research is thus to identify and characterize the parameters of modes in resonance with each other.
An example of the detection of resonant triads is given in [Van Beeck et al. (2021)](https://www.aanda.org/articles/aa/full_html/2021/11/aa41572-21/aa41572-21.html).

## Relevant Publications & Software

### Software

Check out the [NTSA](https://github.com/JVB11/NTSA) computational framework that we developed for the purpose of robust frequency analysis and the detection of resonant frequencies.
A succinct description of this software suite is given on the [relevant software page](https://jvb11.github.io/software/NTSA/).

While this framework is currently limited to harmonic analysis approaches for analyzing variability, some (baby) steps have been made towards expansions that can model other types of variability.
As an example of non-harmonic variability, non-linear mode coupling theories predict time-variable mode parameters (of interacting modes) when certain conditions are fulfilled.
Other examples include various transient astronomical events (also called transients), such as various types of novas or tidal disruption events (among others).
It is therefore a long-term goal to include functionality in the [NTSA](https://github.com/JVB11/NTSA) framework that can detect such non-harmonic behavior.

### Publications

Van Beeck J., Bowman D. M., Pedersen M. G., Van Reeth T., Van Hoolst T., Aerts C.; Detection of non-linear resonances among gravity modes of slowly pulsating B stars: results from five iterative pre-whitening strategies. November 2021, Astronomy & Astrophysics, Vol. 655, A59. [HTML](https://www.aanda.org/articles/aa/full_html/2021/11/aa41572-21/aa41572-21.html) [PDF](https://www.aanda.org/articles/aa/pdf/2021/11/aa41572-21.pdf)

Van Reeth T., Southworth J., Van Beeck J., Bowman D. M.; V456 Cyg: an eclipsing binary with tidally perturbed g-mode pulsations. March 2022, Astronomy & Astrophysics, Vol. 659, A177. [HTML](https://www.aanda.org/articles/aa/full_html/2022/03/aa42833-21/aa42833-21.html) [PDF](https://www.aanda.org/articles/aa/pdf/2022/03/aa42833-21.pdf)

Van Reeth T., De Cat P., Van Beeck J., Prat V., Wright D. J., Lehmann H., Chene A.-N., Kambe E., Yang S. L. S., Gentile G., Joos M.; The near-core rotation of HD112429: A $\gamma$ Doradus star with TESS photometry and legacy spectroscopy. June 2022, Astronomy & Astrophysics, Vol. 662, A58. [HTML](https://www.aanda.org/articles/aa/full_html/2022/06/aa42921-21/aa42921-21.html) [PDF](https://www.aanda.org/articles/aa/pdf/2022/06/aa42921-21.pdf)

Van Reeth T., Johnston C., Southworth J., Fuller J., Bowman D. M., Poniatowski L., Van Beeck J.; Tidally perturbed gravity-mode pulsations in a sample of close eclipsing binaries. March 2023, Astronomy & Astrophysics, Vol. 671, A121. [HTML](https://www.aanda.org/articles/aa/full_html/2023/03/aa45460-22/aa45460-22.html) [PDF](https://www.aanda.org/articles/aa/pdf/2023/03/aa45460-22.pdf)

Fritzewski D. J., Van Reeth T., Aerts C., Van Beeck J., Gossage S., Li G.; Age-dating the young open cluster UBC1 with g-mode asteroseismology, gyrochronology, and isochrone fitting. January 2024, Astronomy & Astrophysics, Vol. 681, A13. [HTML](https://www.aanda.org/articles/aa/full_html/2024/01/aa47618-23/aa47618-23.html) [PDF](https://www.aanda.org/articles/aa/pdf/2024/01/aa47618-23.pdf)
