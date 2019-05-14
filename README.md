# linuxandchill-src
source code for linux and chill

## How To

```
git clone git@github.com:Timothy-Pulliam/linuxandchill-src.git
cd linuxandchill-src
```

Create virtual environment
```
python3 -m venv venv
. venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```

Clone content (HTML, CSS, Themes and posts)
```
git clone git@github.com:Timothy-Pulliam/Timothy-Pulliam.github.io.git output/.
```

Generate HTML from markdown
```
make html
make serve
```

Visit localhost:8000

