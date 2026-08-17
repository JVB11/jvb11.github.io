---
layout: archive
permalink: /software/develop/
title: "Software I develop"
excerpt: "This page describes which software suites I developed for advancing my research."
author_profile: true
---

To get a broad summary of the computational frameworks I developed, click on the hyperlinks or logos below.
If you think my software is interesting and could be beneficial to you, or if you have ideas on how to improve my software suites and their documentation, I encourage you to reach out/contact me.

> More information on my computational frameworks can be found by accessing their respective software documentation pages.
> The hyperlinks of those documentation pages can be found on the Github repositories and are provided for your convenience as clickable icons on the summary pages of this website.

<nbsp>

{% include base_path %}

{% assign ordered_pages = site.software | sort:"order_number" %}

{% for post in ordered_pages %}
  {% include archive-single.html type="grid" %}
{% endfor %}
