Title: Static Websites With Pelican
Date: 2010-12-03 10:20
Modified: 2010-12-05 19:30
Category: Python
Tags: pelican, python
Slug: static-websites-with-pelican
Authors: Timothy Pulliam
Summary: Set up your own blog with Python and Pelican
Status: published

## Python, Pelican, and Static Websites

Static webpages are websites that use static assets. HTML, CSS and Javascript. If you are writing a humble blog, you don't need any fancy database backend stuff, or server end daemon thingys like that.

That's where [Pelican](https://blog.getpelican.com/) comes in. It manages HTML/CSS for you so can stick to writing content.

## Installation

If you are familiar with Python, you install Pelican the same way you install other Python packages, using PIP.

First, create a virtual environment

    $ cd ~/code/blog
    $ python3 -m venv venv
    $ . venv/bin/activate
    $ pip install -U pip

Install the requisite packages

    $ pip install pelican Markdown tzlocal typogrify
    $ pip freeze > requirements.txt

Quickstart a pelican project with the following command

    $ pelican-quickstart --title linuxandchill --author "Timothy Pulliam"

You will be prompted to answer the following questions

```
> Where do you want to create your new web site? [.]
> What will be the title of this web site? [linuxandchill]
> Who will be the author of this web site? [Timothy Pulliam]
> What will be the default language of this web site? [en]
> Do you want to specify a URL prefix? e.g., https://example.com   (Y/n)
> What is your URL prefix? (see above example; no trailing slash) http://linuxandchill.xyz
> Do you want to enable article pagination? (Y/n)
> How many articles per page do you want? [10]
> What is your time zone? [America/New_York]
> Do you want to generate a tasks.py/Makefile to automate generation and publishing? (Y/n)
> Do you want to upload your website using FTP? (y/N)
> Do you want to upload your website using SSH? (y/N)
> Do you want to upload your website using Dropbox? (y/N)
> Do you want to upload your website using S3? (y/N)
> Do you want to upload your website using Rackspace Cloud Files? (y/N)
> Do you want to upload your website using GitHub Pages? (y/N) y
> Is this your personal page (username.github.io)? (y/N) y
Done. Your new project is available at /home/tpulliam/code/blog
```

After that, you should have a directory structure similar to the one below

    blog/
    ├── content
    │    ├──article.md
    |    ├── images/
    |         └── picture.png       
    |     
    ├── output
    ├── tasks.py
    ├── Makefile
    ├── pelicanconf.py       # Main settings file
    └── publishconf.py       # Settings to use when ready to publish

Your articles will be written in markdown files. A minimum article.md will contain the following


Title: My super title
Date: 2010-12-03 10:20
Modified: 2010-12-05 19:30
Category: Python
Tags: pelican, publishing
Slug: my-super-post
Authors: Alexis Metaireau, Conan Doyle
Summary: Short version for index and feeds

This is the content of my super blog post.


If you are going to include images in your articles (most likely), you can include them in a blog/content/images/ directory and reference them by adding the following line in pelicanconf.py

    STATIC_PATHS = ['images']

When you write an article, you can include an image like this

    ![Alt text]({static}/images/picture.png)

### Python Syntax Highlighting

If you want to have your python code to be syntax highlighted like this

    :::python
    print("The triple-colon syntax will *not* show line numbers.")

To display line numbers, use a path-less shebang instead of colons:

    #!python
    print("The path-less shebang syntax *will* show line numbers.")
