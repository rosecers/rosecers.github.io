---
layout: page
title: News 
permalink: /news/
---

<article>
<style> .indented { padding-left: 16pt; padding-right: 50pt; } 
</style>

{% assign now = site.time | date: '%Y' %}
{% for i in (0..10) %}
{% assign this_year = now | minus: i %}

{% assign count = 0 %}
{% for post in site.posts %} 
    {% assign year = post.date  | date: "%Y" | times: 1 %}
    {% if year == this_year %}
	    {% if count == 0 %}
		{% if i <= 3 %}
		    <details open>
		{% else %}
			<details>
		{% endif %}
		<summary> <b> {{ this_year }} </b> </summary>
	    {% endif %}
	    {% assign count = count | plus: 1 %}
	    <p class="indented"><b><time datetime="{{ post.date | date: "%Y-%m-%d" }}">{{ post.date | date_to_long_string }}</time></b><br>{{ post.content }}</p>
    {% endif %}
{% endfor %}
{% if count > 0 %}
	</details>
{% endif %}
{% endfor %}
</article>

