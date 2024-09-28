---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

## Highlights

{% include base_path %}
{% assign number_printed = 0 %}
{% for publi in site.data.publication_highlights %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <div class="well">
    <pubtit>{{ publi.title }}</pubtit>
    <p>{{ publi.subtitle }}</p>
    <img src="{{ base_path }}/images/publication_highlights/{{ publi.image }}" class="img-responsive" width="33%" style="float: left" />
    <p>{{ publi.description }}</p>
    <p><em>{{ publi.authors }}</em></p>
    <p><strong><a href="{{ publi.link.url }}" target="_blank">{{ publi.link.display }}</a></strong></p>
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

## Check out my five most recent publications

+ **Van Beeck J.**, Van Hoolst T., Aerts C., Fuller J., Non-linear three-mode coupling of gravity modes in rotating slowly pulsating B stars. Stationary solutions and modeling potential, July 2024, A&A, 687, A265 (Nr. of citations: 4)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*DOI: <a href="https://doi.org/10.1051/0004-6361/202348369">10.1051/0004-6361/202348369</a>, NASA ADS: <a href="https://ui.adsabs.harvard.edu/abs/2024A&A...687A.265V">2024A&A...687A.265V</a>, arXiv: <a href="https://arxiv.org/abs/2311.02972">2311.02972</a>*

+ Fritzewski D. J., Van Reeth T., Aerts C., **Van Beeck J.**, Gossage S., Li G., Age-dating the young open cluster UBC 1 with g-mode asteroseismology, gyrochronology, and isochrone fitting, January 2024, A&A, 681, A13 (Nr. of citations: 7)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*DOI: <a href="https://doi.org/10.1051/0004-6361/202347618">10.1051/0004-6361/202347618</a>, NASA ADS: <a href="https://ui.adsabs.harvard.edu/abs/2024A&A...681A..13F">2024A&A...681A..13F</a>, arXiv: <a href="https://arxiv.org/abs/2310.18426">2310.18426</a>*

+ Van Reeth T., Johnston C., Southworth J., Fuller J., Bowman D. M., Poniatowski L., **Van Beeck J.**, Tidally perturbed gravity-mode pulsations in a sample of close eclipsing binaries, March 2023, A&A, 671, A121 (Nr. of citations: 7)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*DOI: <a href="https://doi.org/10.1051/0004-6361/202245460">10.1051/0004-6361/202245460</a>, NASA ADS: <a href="https://ui.adsabs.harvard.edu/abs/2023A&A...671A.121V">2023A&A...671A.121V</a>, arXiv: <a href="https://arxiv.org/abs/2301.08816">2301.08816</a>*

+ Van Reeth T., De Cat P., **Van Beeck J.**, et al., The near-core rotation of HD 112429. A γ Doradus star with TESS photometry and legacy spectroscopy, June 2022, A&A, 662, A58 (Nr. of citations: 6)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*DOI: <a href="https://doi.org/10.1051/0004-6361/202142921">10.1051/0004-6361/202142921</a>, NASA ADS: <a href="https://ui.adsabs.harvard.edu/abs/2022A&A...662A..58V">2022A&A...662A..58V</a>, arXiv: <a href="https://arxiv.org/abs/2203.11071">2203.11071</a>*

+ Van Reeth T., Southworth J., **Van Beeck J.**, Bowman D. M., V456 Cyg: An eclipsing binary with tidally perturbed g-mode pulsations, March 2022, A&A, 659, A177 (Nr. of citations: 10)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*DOI: <a href="https://doi.org/10.1051/0004-6361/202142833">10.1051/0004-6361/202142833</a>, NASA ADS: <a href="https://ui.adsabs.harvard.edu/abs/2022A&A...659A.177V">2022A&A...659A.177V</a>, arXiv: <a href="https://arxiv.org/abs/2201.05359">2201.05359</a>*


(Last update: 21 September 2024)

## View the full publication list in my [ADS library](https://ui.adsabs.harvard.edu/public-libraries/mrBh0XAqRuqabcPXhidMUA).

<!-- {% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %} -->
