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
This field aims to represent a [field of fossil origin](https://en.wikipedia.org/wiki/Fossil_stellar_magnetic_field).
It extends down to the stellar centre even though the actual magnetic field structure in the stellar core would likely be more complex due to interactions with dynamo-driven field that is likely present within the core.
Similarly, near the stellar surface, the field would also be affected by the local low (mass) density.

It is an open question how stable this magnetic field configuration is within the interiors of the intermediate-mass main sequence stars that we simulated (see e.g., [Kaufman et al. 2022](https://academic.oup.com/mnras/article/517/3/3332/6748231) for information on the stability of such fields in the interior of [red giants](https://en.wikipedia.org/wiki/Red_giant)).

{% include base_path %}

<kdb>
<div class="container">
<figure style="display:table; float:left; margin-right:20%; margin-left:20%; width:60%;">
  <a href="{{ '/images/research/magnetism/internal_magnetic_field.svg' | prepend: base_path }}" class="image-popup" title="Normalized representation of a dipolar axisymmetric magnetic field.">
    <img src="{{ '/images/research/magnetism/internal_magnetic_field.svg' | prepend: base_path }}" alt="Normalized representation of a dipolar axisymmetric magnetic field." style="width:100%; height:auto;">
  </a>
  <figcaption style="display: table-caption; caption-side: bottom;">Normalized representation of a dipolar (axisymmetric) magnetic field of a specific model of an intermediate-mass main sequence star representative for the <a href='https://en.wikipedia.org/wiki/Slowly_pulsating_B-type_star'>slowly pulsating B star</a> HD 43317. $r/R$ represents the normalized radial coordinate within the star ($r/R = 1$ is the surface coordinate, $r/R$ the center coordinate). Stream lines represent normalized poloidal field component (line width proportional to their amplitude) and the colored contours represent the normalized toroidal component. The normalized magnetic field strength shown in this figure is multiplied with a scaling factor $B_0$ before computing magnetic mode frequency shifts.</figcaption>
</figure>
</div>
</kdb>

## Magneto-Asteroseismology

We were one of the pioneers in the field of magneto-asteroseismology when we characterized the magnetic frequency shifts imparted by an internal magnetic field on the frequencies of gravity modes propagating in (rapidly) rotating intermediate-mass main sequence stars.
To compute these magnetic frequency shifts we used first-order perturbation theory (for details see [Prat et al. (2019)](https://www.aanda.org/articles/aa/full_html/2019/07/aa35462-19/aa35462-19.html))
The computed shifts are therefore only valid if the magnetic field is _'weak enough'_ to induce a perturbative shift.

Our proof-of-concept studies, [Prat et al. (2019)](https://www.aanda.org/articles/aa/full_html/2019/07/aa35462-19/aa35462-19.html) and [Prat et al. (2020)](https://www.aanda.org/articles/aa/full_html/2020/04/aa37398-19/aa37398-19.html) computed magnetically influenced period spacing patterns - the main observable for gravity modes in magnetic variable stars - for HD 43317, a rapidly rotating, magnetic B-type star with detected gravity modes.
The main effect on these patterns that we observed in these studies is the presence of a specific sawtooth pattern when they are compared to the patterns influenced by internal rotation alone.
In later works, we (and others) showed however that these sawtooth patterns are likely not physical, as the shifts imparted on the oscillation modes included in the pattern are not perturbative (and therefore our model would not hold; see e.g., [Van Beeck et al. 2020](https://www.aanda.org/articles/aa/full_html/2020/06/aa37363-19/aa37363-19.html)).
Instead, the main effect on the period spacing pattern observable (due to the magnetic field) was found to be a (mode-geometry-dependent) slope change when it is compared to its rotationally influenced equivalent.
We showed that this effect is further modified by variations in internal mixing, rotation rate, metallicity and mass of the stellar evolution/structure models.

In addition to the stability arguments raised above, it also remains an open question how more realistic magnetic field configurations change (i) the computed perturbative magnetic frequency shifts and the corresponding period spacing patterns, and (ii) the perturbative nature of these shifts (i.e., are fields weaker/stronger so that more/less magnetive frequency shifts can be described perturbatively?).
I therefore have a long-term interest in magneto-hydrodynamic simulations that improve our understanding of the magnetized stellar interior and theoretical work that computes non-perturbative magnetic frequency shifts (such as [Rui, Ong and Mathis, 2024](https://academic.oup.com/mnras/article/527/3/6346/7408611)). 

<kdb>
<div class="container">
<figure style="display:table; float:left; margin-right:20%; margin-left:20%; width:60%;">
  <a href="{{ '/images/research/magnetism/magnetic_slopes.svg' | prepend: base_path }}" class="image-popup" title="Effect of an internal (dipolar, axisymmetric) magnetic field on gravity mode period spacing patterns in a slowly pulsating B star model.">
    <img src="{{ '/images/research/magnetism/magnetic_slopes.svg' | prepend: base_path }}" alt="Effect of an internal (dipolar, axisymmetric) magnetic field on gravity mode period spacing patterns in a slowly pulsating B star model." style="width:100%; height:auto;">
  </a>
  <figcaption style="display: table-caption; caption-side: bottom;">Inferred magneto-rotationally modified period spacing pattern slopes $\Sigma$ as a function of magnetic field scaling factor $B_0$ (in G) for different nonradial mode geometry (in terms of the azimuthal wavenumber $m$) of dipole ($l=1$) modes propagating in a $3$ M$_\odot$ <a href='https://en.wikipedia.org/wiki/Slowly_pulsating_B-type_star'>slowly pulsating B star</a> model. Dashed and solid lines indicate estimated slopes around the $n = −30$ and $n = −40$ mode (where $n$ is the radial order), and the shaded bands indicate $95$% confidence intervals. Check out section 1.2 of <a href='https://fys.kuleuven.be/ster/pub/phd-thesis-jordan-van-beeck/PhD_Thesis_Jordan_Van_Beeck_Digital_Version.pdf'>my PhD thesis</a> for more information on quantum numbers that are used to label oscillation modes.</figcaption>
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
