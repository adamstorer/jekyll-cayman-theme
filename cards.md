---
layout: default
title: cards
permalink: /cards/
sitemap: false
---

### This should be a list of all definitions


<table>
  <tr>
  <th>Link</th>
  <th>Title</th>
  <th>Date</th>
  <th>Term</th>
  <th>Definition</th>
  </tr>
    {% for post in site.posts %}
      {% for def in post.defs_used %}
      <tr>
      <th>Access here[{{post.url}}]</th>
      <th>{{ post.title}}</th>
      <th>{{ post.date}}</th>
      <th>{{ def[0] }}</th>
      <th>{{ def[1] }}</th>
      </tr>
{% endfor %}
    {% endfor %}
