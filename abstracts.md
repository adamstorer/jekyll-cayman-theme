---
layout: default
title: abstracts
permalink: /abstracts/
sitemap: false
---

### This should be a list of all abstracts


<table>
  <tr>
  <th>Title</th>
  <th>Date</th>
  <th>Abstract</th>
  </tr>
    {% for post in site.posts %}
      <tr>
      <th>{{ post.title}}</th>
      <th>{{ post.date}}</th>
      <th>{{ post.Abstract }}</th>
      </tr>

    {% endfor %}
