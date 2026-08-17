---
title: "jackHI"
layout: single-portfolio
excerpt: "<img src='/images/software/jackhi/jack_hi_logo.png' alt=''>"
collection: software
order_number: 40
header:
    og_image: "software/jackhi/jack_hi_logo.png"
---

{% include software-suite-links.html
  repo_url="https://github.com/JVB11/jackHI"
  repo_hover="GitHub repository of jackHI"
  doc_url="https://jvb11.github.io/jackHI/"
  doc_hover="Documentation of jackHI" %}

{% include work-in-progress-warning-links.html
   type="info"
   text="The current public version is an &alpha; version." %}

_**Context**_

Histograms are a commonly used data representation method that can be thought of as a (non-parametric) estimate of the probability distribution function of the data-generating process.
They are also frequently used to determine summary quantities of this function.
The values of such summary quantities, however, depend strongly on the way the bins are chosen.

_**Purpose**_

jackHI is a software suite that contains functions that help a user generate a histogram based on a non-arbitrary, data-based optimal choice of bin width.
The idea is that one samples the underlying probability distribution function sufficiently to capture the data features, whereas *fine details* due to `random noise' (caused by empty too-finely sampled bins) are ignored.
This sampling is effected by a "jackknife" (or cross-validation) method (see [Hogg (2008)](https://arxiv.org/abs/0807.4820))[^1].

_**Applications**_

Work in progress.

_**Citations/using this code**_

Work in progress.

[^1]: This is not the only way to construct a data-driven optimal histogram. See for example [Knuth (2006)](https://arxiv.org/abs/physics/0605197) for other ways to do so.
