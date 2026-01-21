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

+ Ahlborn F., Joel Ong J. M., **Van Beeck J.**, Bellinger E. P., Hekker S., Basu S., Impact of near-degeneracy effects on linear rotational inversions for red giant stars, December 2025, A&A, 704, A230 (Nr. of citations: 1)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*DOI: <a href="https://doi.org/10.1051/0004-6361/202555537">10.1051/0004-6361/202555537</a>, NASA ADS: <a href="https://ui.adsabs.harvard.edu/abs/2025A&A...704A.230A">2025A&A...704A.230A</a>, arXiv: <a href="https://arxiv.org/abs/2509.26319">2509.26319</a>*

+ **Van Beeck J.**, Van Hoolst T., Fuller J., Aerts C., Resonant Amplitude Equations for Gravito-Inertial Modes: Non-linear mode coupling in a slowly pulsating B star, October 2025, tasc.conf, 70 (Nr. of citations: 0)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*DOI: <a href="https://doi.org/10.5281/zenodo.17241657">10.5281/zenodo.17241657</a>, NASA ADS: <a href="https://ui.adsabs.harvard.edu/abs/2025tasc.confE..70V">2025tasc.confE..70V</a>, arXiv: https://arxiv.org/abs/*

+ Ahlborn F., Ong J., **Van Beeck J.**, Bellinger E., Hekker S., Basu S., Estimating internal rotation rates of red giants in the presence of interacting mixed modes, October 2025, tasc.conf, 94 (Nr. of citations: 0)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*DOI: <a href="https://doi.org/10.5281/zenodo.17432360">10.5281/zenodo.17432360</a>, NASA ADS: <a href="https://ui.adsabs.harvard.edu/abs/2025tasc.confE..94A">2025tasc.confE..94A</a>, arXiv: https://arxiv.org/abs/*

+ **Van Beeck J.**, Van Hoolst T., Aerts C., Fuller J., Non-linear three-mode coupling of gravity modes in rotating slowly pulsating B stars. Stationary solutions and modeling potential, July 2024, A&A, 687, A265 (Nr. of citations: 9)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*DOI: <a href="https://doi.org/10.1051/0004-6361/202348369">10.1051/0004-6361/202348369</a>, NASA ADS: <a href="https://ui.adsabs.harvard.edu/abs/2024A&A...687A.265V">2024A&A...687A.265V</a>, arXiv: <a href="https://arxiv.org/abs/2311.02972">2311.02972</a>*


(Last update: 21 January 2026)

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
