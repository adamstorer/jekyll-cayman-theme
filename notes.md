---
layout: default
title: notes
permalink: /notes/
sitemap: false
---

You can browse all of my reading notes here. I am saving these mostly for my own good as I prepare for Qualifying Exams.

#### Categories
<div>
   {% assign categories = site.categories | sort %}
   {% for category in categories %}
    <span class="tag">
       <a href="/category/{{ category | first | slugify }}">
               #{{ category[0] | replace:'-', ' ' }} ({{ category | last | size }})
       </a>
   </span>
   {% endfor %}
   </div>




#### Notes
<div id="home">
  <ul class="posts">
    {% for post in site.posts %}
      <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
</div>
