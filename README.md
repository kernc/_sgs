Installation
------------
1. Python: https://www.python.org/downloads
2. Git: https://git-scm.com/downloads
3. `git clone this repo && cd workdir`
4. `pip install -r requirements.txt`
5. `git clone --depth 1 --recursive https://github.com/getpelican/pelican-plugins`
6. To rebuild: `pelican -v`


Content layout
--------------
```
$ tree content

content
├── images
│   └── objave
│       └── (images for news)
├── objave
│   ├── (Slovene news)
│   ├── 2020-06-13-nova-spletna-stran.md
│   ├── YYYY-MM-DD-short-url-slug.md       (required filename format)
│   ├── ...
│   └── en
│       ├── (English news; filenames must match Slovene news)
│       ├── 2020-06-13-nova-spletna-stran.md
│       └── ...
├── pages
│   ├── (Slovene pages)
│   ├── about.md
│   ├── ...
│   └── en
│       ├── (English pages; filenames must match Slovene pages)
│       ├── about.md
│       └── ...
└── static
    └── (files served at document root /)
```


Document metadata
-----------------
First lines of file, before any empty line.
```
(required)
title: Clear, Formatted Document Title

(optional)
slug: short clean URL part, see: https://en.wikipedia.org/wiki/Clean_URL#Slug
date: YYYY-MM-DD
author: Firstname Lastname, ...
description: Short document description

(additional, see: https://docs.getpelican.com/en/stable/content.html#file-metadata)
```


Writing content
---------------
Write content in [Markdown]. Review the [cheat sheet][Markdown].

[Markdown]: https://guides.github.com/features/mastering-markdown/

Referencing images in news:
```md
![alternative text for screen readers]({static}/images/objave/filename.jpg){:.float-right}

![alt text description]({static}/images/objave/filename2.jpg){:.float-left}
```

~ HTH
