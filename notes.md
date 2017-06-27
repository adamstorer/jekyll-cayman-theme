---
layout: default
title: notes
permalink: /notes/
sitemap: false
---



You can browse all of my reading notes here. I am saving these mostly for my own good as I prepare for Qualifying Exams. You can search for specific keywords by typing them in here:

<form action="/search.html" method="get">
  <label for="search-box"></label>
  <input type="text" id="search-box" name="query">
  <input type="submit" value="search">
</form>

You can also browse by category below.

#### Categories
<div>
   {% assign categories = site.categories | sort %}
   {% for category in categories %}
    <span class="tag">
       <a href="/category/{{ category | first }}">
               #{{ category[0] | replace:'-', ' ' }} ({{ category | last | size }})
       </a>
   </span>
   {% endfor %}
   </div>

Or you can browse the latest posts below.

#### Notes
<div id="home">
  <ul class="posts">
    {% for post in site.posts %}
      <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
</div>
