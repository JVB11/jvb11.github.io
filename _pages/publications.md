---
layout: archive
title: "Publications"
excerpt: "This page contains a list of my five most recent publications, and shows some key works."
permalink: /publications/
author_profile: true
---

## Check out my five most recent publications

+ Patil A. A., Aerts C., Wang N. Y. N., **Van Beeck J.**, Pedersen M. G., Beyond prewhitening: detection of gravity modes and their period spacings in slowly pulsating B stars using the multitaper F-test, December 2025, arXiv, arXiv:2512.10019 (Nr. of citations: 0)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*DOI: <a href="https://doi.org/10.48550/arXiv.2512.10019">10.48550/arXiv.2512.10019</a>, NASA ADS: <a href="https://ui.adsabs.harvard.edu/abs/2025arXiv251210019P">2025arXiv251210019P</a>, arXiv: <a href="https://arxiv.org/abs/2512.10019">2512.10019</a>*

+ Ahlborn F., Ong J. M. J., **Van Beeck J.**, Bellinger E. P., Hekker S., Basu S., Impact of near-degeneracy effects on linear rotational inversions for red-giant stars, September 2025, arXiv, arXiv:2509.26319 (Nr. of citations: 1)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*DOI: <a href="https://doi.org/10.48550/arXiv.2509.26319">10.48550/arXiv.2509.26319</a>, NASA ADS: <a href="https://ui.adsabs.harvard.edu/abs/2025arXiv250926319A">2025arXiv250926319A</a>, arXiv: <a href="https://arxiv.org/abs/2509.26319">2509.26319</a>*

+ **Van Beeck J.**, Van Hoolst T., Aerts C., Fuller J., Non-linear three-mode coupling of gravity modes in rotating slowly pulsating B stars. Stationary solutions and modeling potential, July 2024, A&A, 687, A265 (Nr. of citations: 9)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*DOI: <a href="https://doi.org/10.1051/0004-6361/202348369">10.1051/0004-6361/202348369</a>, NASA ADS: <a href="https://ui.adsabs.harvard.edu/abs/2024A&A...687A.265V">2024A&A...687A.265V</a>, arXiv: <a href="https://arxiv.org/abs/2311.02972">2311.02972</a>*

+ Fritzewski D. J., Van Reeth T., Aerts C., **Van Beeck J.**, Gossage S., Li G., Age-dating the young open cluster UBC 1 with g-mode asteroseismology, gyrochronology, and isochrone fitting, January 2024, A&A, 681, A13 (Nr. of citations: 16)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*DOI: <a href="https://doi.org/10.1051/0004-6361/202347618">10.1051/0004-6361/202347618</a>, NASA ADS: <a href="https://ui.adsabs.harvard.edu/abs/2024A&A...681A..13F">2024A&A...681A..13F</a>, arXiv: <a href="https://arxiv.org/abs/2310.18426">2310.18426</a>*

+ Van Reeth T., Johnston C., Southworth J., Fuller J., Bowman D. M., Poniatowski L., **Van Beeck J.**, Tidally perturbed gravity-mode pulsations in a sample of close eclipsing binaries, March 2023, A&A, 671, A121 (Nr. of citations: 17)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*DOI: <a href="https://doi.org/10.1051/0004-6361/202245460">10.1051/0004-6361/202245460</a>, NASA ADS: <a href="https://ui.adsabs.harvard.edu/abs/2023A&A...671A.121V">2023A&A...671A.121V</a>, arXiv: <a href="https://arxiv.org/abs/2301.08816">2301.08816</a>*


(Last update: 21 December 2025)

## Check out my key works (view the full publication list in my [ADS library](https://ui.adsabs.harvard.edu/public-libraries/mrBh0XAqRuqabcPXhidMUA))

{% include base_path %}
{% assign number_printed = 0 %}
{% for publi in site.data.publication_highlights %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <div class="well">
    <pubtit>{{ publi.title }}:<br>{{ publi.subtitle }}</pubtit>
    <figure width="75%" height="auto" style="padding: inherit; margin: auto; float: right;">
      <img src="{{ base_path }}/images/publication_highlights/{{ publi.image.name }}" class="img-responsive" width="75%" height="auto" style="padding: inherit; margin: auto; float: right;" />
      <figcaption>{{ publi.image.description | markdownify }}</figcaption>
    </figure>
    <p>{{ publi.description | markdownify }}</p>
    <p><em>{{ publi.authors }}</em></p>
    <p><strong><a href="{{ publi.link.url }}">{{ publi.link.display }}</a></strong></p>
    <p>{{ publi.news | markdownify }}</p>
  </div>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

<p> &nbsp; </p>
