---
layout: archive
title: "Sitemap"
permalink: /sitemap/
author_profile: true
my_pages_include:
    - name: "Welcome to my personal space on the web!"
    - name: "Curriculum Vitae"
    - name: "Publications"
    - name: "Research"
    - name: "Software"
    - name: "Teaching"
---

{% include base_path %}

This page contains a list of all the pages found on the site.

<!-- <h2>Pages</h2> -->
{% for post in site.pages %}
  {% for accepted_page in page.my_pages_include %}
    {% if post.title == accepted_page.name %}
      {% include archive-single.html %}
    {% endif %}
  {% endfor %}
{% endfor %}

<!-- <h2>Posts</h2>
{% for post in site.posts %}
  {% include archive-single.html %}
{% endfor %}

{% capture written_label %}'None'{% endcapture %}

{% for collection in site.collections %}
{% unless collection.output == false or collection.label == "posts" %}
  {% capture label %}{{ collection.label }}{% endcapture %}
  {% if label != written_label %}
  <h2>{{ label }}</h2>
  {% capture written_label %}{{ label }}{% endcapture %}
  {% endif %}
{% endunless %}
{% for post in collection.docs %}
  {% unless collection.output == false or collection.label == "posts" %}
  {% include archive-single.html %}
  {% endunless %}
{% endfor %}
{% endfor %} -->
