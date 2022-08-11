---
layout: bytopic
title: "By Venue"
permalink: /byvenue/
---

<section class="container posts-content">
{% assign sorted_categories = site.categories | sort %}

{% assign my_array = "" | split: ',' %}

{% for c in sorted_categories %}
{% assign name = c[0] %}
{% if name contains "Venue" %}
{% assign my_array = my_array | push: c %}
{% endif %}
{% endfor %}



{% for category in my_array %}
<h3 id="{{ category[0] }}">{{ category | first }}</h3>
<ol class="posts-list">
{% for post in category.last %}
<li class="posts-list-item">
<!-- <span class="posts-list-meta">{{ post.date | date:"%Y-%m-%d" }}</span> -->
<a class="posts-list-name" href="{{ site.url }}{{ post.url }}">{{ post.title }}</a>
</li>
{% endfor %}
</ol>
{% endfor %}
</section>
