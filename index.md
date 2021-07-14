---
# You don't need to edit this file, it's empty on purpose.
# Edit theme's home layout instead if you wanna make some changes
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: default
title: Home

---
<img style="float:right;padding:10px;" src="{{ site.baseurl }}/assets/gallery/rosecers.jpg">
Hi!

My name is Rose Cersonsky and I am a Postdoctoral Researcher in the <a href="https://www.epfl.ch/labs/cosmo/"> {{"Laboratory of Computational Science and Modelling (COSMO)"}}</a> at the Ecol&eacute; Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL) in Lausanne, Switzerland.

My research is largely focused on computer-aided materials design. In my doctoral research, I ran simulations using statistical mechanics to understand the role that particle shape has in predicting colloidal self-assembly. This included a lot of geometry, physics, computer science, and mathematics (to my delight). I've also taken an interest into the field of photonic crystals, and how we can use crystallographic analysis to understand them.

At EPFL, I work with Prof. Michele Ceriotti to develop machine learning methods and approaches for atomistic simulations. Specifically, I focus on the role of materials featurization in machine learning models. Using these techniques, we can better understand the relationship between crystal structure and behavior across many length scales.

In my spare time, I conduct [community outreach](outreach), run, travel, and search for delicious food.

For an up-to-date list of publications and software, please refer to [Google Scholar](https://scholar.google.com/citations?user=B2cyV70AAAAJ&hl=en) and [GitHub](https://github.com/rosecers). 





**Recent News**:

<div style="height:200px;width:800px;border:1px solid #ccc;font:16px/26px Georgia, Garamond, Serif;overflow-x:hidden;overflow-y:scroll">
<style> .indented { padding-left: 16pt; padding-right: 50pt; }
</style>

{% assign now = site.time | date: '%Y' %}
{% assign total_count = 0 %}
{% for i in (0..10) %}
    {% if total_count < 5 %}
        {% assign this_year = now | minus: i %}
        {% assign count = 0 %}
        {% for post in site.posts %}
             {% assign year = post.date  | date: "%Y" | times: 1 %}
             {% if year == this_year %}
                 {% assign count = count | plus: 1 %}
                 {% assign total_count = total_count | plus: 1 %}
                 <p><b><time datetime="{{ post.date | date: "%Y-%m-%d" }}">{{ post.date | date_to_long_string }}</time></b><br>{{ post.excerpt }}</p>
             {% endif %}
        {% endfor %}
    {% endif %}
{% endfor %}

</div>

For more news items, check out the [news page](news)!
