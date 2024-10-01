---
title: "Internal Stellar Magnetism"
layout: single-portfolio
collection: research
order_number: 20
img: "magnetic_cover.png"
header:
    og_image: "research/magnetic_cover.png"
---

## Magnetic Field Model

For our work on stellar magnetism we used a model of an internal (stellar) magnetic field that is [dipolar](https://en.wikipedia.org/wiki/Dipole) and [axisymmetric](https://en.wikipedia.org/wiki/Axial_symmetry) or oblique with respect to the [axis of rotation](https://en.wikipedia.org/wiki/Rotation) (i.e., the magnetic field axis is inclined with respect to the axis of rotation).
This field aims to represent a [field with fossil origin](https://en.wikipedia.org/wiki/Fossil_stellar_magnetic_field).
It extends down to the stellar centre even though the actual magnetic field structure in the stellar core would likely be more complex due to interactions with dynamo-driven field that is likely present within the core.
Similarly, the field near the stellar surface would also be affected by the local low density.

It is an open question how stable this magnetic field configuration is within the interiors of the intermediate-mass main sequence stars that we simulated (see e.g., [Kaufman et al. 2022](https://academic.oup.com/mnras/article/517/3/3332/6748231) for information on the stability of such fields in the interior of [red giants](https://en.wikipedia.org/wiki/Red_giant)).
I therefore have a long-term interest in magneto-hydrodynamic simulations that improve our understanding of the magnetized stellar interior. 

{% include base_path %}

<kdb>
<div class="container">
<figure style="display:table; float:left; margin-right:20%; width:20%; width:60%;">
  <a href="{{ '/images/research/magnetism/internal_magnetic_field.svg' | prepend: base_path }}" class="image-popup" title="Normalized representation of a dipolar axisymmetric magnetic field.">
    <img src="{{ '/images/research/magnetism/internal_magnetic_field.svg' | prepend: base_path }}" alt="Normalized representation of a dipolar axisymmetric magnetic field." style="width:100%; height:auto;">
  </a>
  <figcaption style="display: table-caption; caption-side: bottom;">Normalized representation of a dipolar (axisymmetric) magnetic field of a specific model of an intermediate-mass main sequence star. Stream lines represent normalized poloidal field component (line width proportional to their amplitude) and the colored contours represent the normalized toroidal component. The normalized magnetic field strength shown in this figure is multiplied with a scaling factor before computing magnetic mode frequency shifts.</figcaption>
</figure>
</div>
</kdb>


## Magneto-Asteroseismology

We were one of the pioneers of this field when we characterized the magnetic frequency shifts imparted by an internal magnetic field on the frequencies of gravity modes propagating in (rapidly) rotating intermediate-mass main sequence stars.
To compute these magnetic frequency shifts we used first-order perturbation theory (for details see [Prat et al. (2019)](https://www.aanda.org/articles/aa/full_html/2019/07/aa35462-19/aa35462-19.html))
The computed shifts are therefore only valid if the magnetic field is _'weak enough'_ to induce a perturbative shift.

Our proof-of-concept studies, [Prat et al. (2019)](https://www.aanda.org/articles/aa/full_html/2019/07/aa35462-19/aa35462-19.html) and [Prat et al. (2020)](https://www.aanda.org/articles/aa/full_html/2020/04/aa37398-19/aa37398-19.html) computed magnetically influenced period spacing patterns - the main observable for gravity modes in magnetic variable stars - for HD 43317, a rapidly rotating, magnetic B-type star with detected gravity modes.
The main effect on these patterns that we observed in these studies is the presence of a specific sawtooth pattern compared to the patterns influenced by internal rotation alone.
In later works, we (and others) showed however that these sawtooth patterns are likely not physical, as the shifts imparted on the oscillation modes included in the pattern are not perturbative (and therefore our model would not hold; see e.g., [Van Beeck et al. 2020](https://www.aanda.org/articles/aa/full_html/2020/06/aa37363-19/aa37363-19.html)).
Instead, the main effect on the period spacing pattern observable (due to the magnetic field) is a (mode-dependent) slope change compared to the rotationally influenced pattern.

<kdb>
<div class="container">
<figure style="display:table; float:left; margin-right:20%; width:20%; width:60%;">
  <a href="{{ '/images/research/magnetism/magnetic_slopes.svg' | prepend: base_path }}" class="image-popup" title="Effect of an internal (dipolar, axisymmetric) magnetic field on gravity mode period spacing patterns in a slowly pulsating B star model.">
    <img src="{{ '/images/research/magnetism/magnetic_slopes.svg' | prepend: base_path }}" alt="Effect of an internal (dipolar, axisymmetric) magnetic field on gravity mode period spacing patterns in a slowly pulsating B star model." style="width:100%; height:auto;">
  </a>
  <figcaption style="display: table-caption; caption-side: bottom;">Inferred magneto-rotationally modified period spacing pattern slopes $\Sigma$ as a function of $B_0$ (in G) for different nonradial mode geometry (in terms of the azimuthal wavenumber m) of dipole modes propagating in a slowly pulsating B star model. Dashed and solid lines indicate estimated slopes around the $n = −30$ and $n = −40$ mode, and the shaded bands indicate $95%$ confidence intervals.</figcaption>
</figure>
</div>
</kdb>


## Relevant Publications & Software

### Software

Python scripts used to simulate the magnetic field and compute the magnetic frequency shifts are available upon request.
No public repository is currently available.

### Publications

Prat V., Mathis S., Buysschaert B., **Van Beeck J.**, Bowman D. M., Aerts C., Neiner C.; Period spacings of gravity modes in rapidly rotating magnetic stars. I. Axisymmetric fossil field with poloidal and toroidal components. July 2019, Astronomy & Astrophysics, Vol. 627, A64. [HTML](https://www.aanda.org/articles/aa/full_html/2019/07/aa35462-19/aa35462-19.html) [PDF](https://www.aanda.org/articles/aa/pdf/2019/07/aa35462-19.pdf)

Prat V., Mathis S., Neiner C., **Van Beeck J.**, Bowman D. M., Aerts C.; Period spacings of gravity modes in rapidly rotating magnetic stars. II. The case of an oblique dipolar fossil magnetic field. April 2020, Astronomy & Astrophysics, Vol. 636, A100. [HTML](https://www.aanda.org/articles/aa/full_html/2020/04/aa37398-19/aa37398-19.html) [PDF](https://www.aanda.org/articles/aa/pdf/2020/04/aa37398-19.pdf)

**Van Beeck J.**, Prat V., Van Reeth T., Mathis S., Bowman D. M., Neiner C., Aerts C.; Detecting axisymmetric magnetic fields using gravity modes in intermediate-mass stars. June 2020, Astronomy & Astrophysics, Vol. 638, A149. [HTML](https://www.aanda.org/articles/aa/full_html/2020/06/aa37363-19/aa37363-19.html) [PDF](https://www.aanda.org/articles/aa/pdf/2020/06/aa37363-19.pdf)

Aerts C., Augustson K., Mathis S., Pedersen M. G., Mombarg J. S. G., Vanlaer V., **Van Beeck J.**, Van Reeth T.; Rossby numbers and stiffness values inferred from gravity-mode asteroseismology of rotating F- and B-type dwarfs. Consequences for mixing, transport, magnetism, and convective penetration. December 2021, Astronomy & Astrophysics, Vol. 656, A121. [HTML](https://www.aanda.org/articles/aa/full_html/2021/12/aa42151-21/aa42151-21.html) [PDF](https://www.aanda.org/articles/aa/pdf/2021/12/aa42151-21.pdf)
