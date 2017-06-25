---
layout: default
title: cards
permalink: /cards/
sitemap: false
---

### This should be a list of all definitions

<div id="home">
  <ul class="posts">
    {% for post in site.posts %}
      <li><span>{{ post.content | jsonify}}</span></li>
    {% endfor %}
  </ul>
</div>
