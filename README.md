# "Build a Static Site Generator" project

-   https://www.boot.dev/
-   https://github.com/scGetStuff/sitegen.git

# structure

-   input markdown in `content/`
-   output HTML in `public/`

# run

-   `./main.sh`
-   `./test/sh`

# serve output

```shell
cd public
python3 -m http.server 8888
```

http://localhost:8888

# main algorithim

-   `rm public/*`
-   copy static assets to `public/`
-   generate HTML file for each Markdown file in `content/`

# assumptions

-   markdown valid
-   there is no nested markdown

# type hints & mypy

-   I'm using type hints because I hate languages that are not static typed
-   but I am not using mypy yet
-   the IDE behaves better with the hints; that's good enough for me

# enhancments

-   nested markdown
    -   first pass only support a single level of nesting
    -   make this `This is an *italic and **bold** word*.` work
