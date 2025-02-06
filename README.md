# "Build a Static Site Generator" project

-   https://www.boot.dev/
-   https://github.com/scGetStuff/sitegen.git

# structure

-   input markdown in `content/`
-   output HTML in `public/`

# run

-   `./main.sh`
-   this is suposed to be usefull somehow, I don't see it yet

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
