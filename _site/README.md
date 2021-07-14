# README

## About

 * Author: Carl Simon Adorf
 * License: Copyright reserved.

## How to preview the website locally

This is a [jekyll](https://jekyllrb.com/) powered website.

First, clone this repository, then follow these instructions:

```bash
~ $ gem install bundler jekyll
~ $ cd rosecers-website
~/rosecers-website $ bundle exec jekyll serve
```

Then open [http://localhost:4000](http://localhost:400).

## How to edit the website

Just open any of the markdown files (ending in `.md`) and edit them.
If you are running a preview server, the website will update automatically.

## How to publish the website

Execute the following commands:
```bash
bundle exec jekyll build
rsync -rvt _site/ login.itd.umich.edu:~/Public/html
```
