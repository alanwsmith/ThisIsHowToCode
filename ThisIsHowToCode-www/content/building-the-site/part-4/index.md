---
title: Building The Site (Part 4)
---

The Plan
--------

- Finish moving in content to be served by Hugo

The Result
----------

- Got stuck working with sub directories. Files wouldn't output where expected. 
- Did some troubleshooting by switching Hugo to actually build the site with the plain `hugo` command instead of serving it from memory with `hugo server`. This let me look in the `public` directory at the files that were actually output.
- Finally figured out that if there's a subfolder that you want content rendered it, the folder above has to contain and `_index.md` file. 
- You can't have an `index.md` and an `_index.md` at the same time though
- In order to display content from the `_index.md` file, I added `layout: single` to it's YAML header.


Links
-----

- [Content Organization | Hugo](https://gohugo.io/content-management/organization/)
- [devcows/hugo-universal-theme: Port of the Universal theme to Hugo](https://github.com/devcows/hugo-universal-theme)
- [Directory Structure | Hugo](https://gohugo.io/getting-started/directory-structure/)
- [EmielH/tale-hugo: A port of the Tale theme for Hugo. Tale is a minimal theme...](https://github.com/EmielH/tale-hugo)
- [hugo directory structure - Google Search](https://www.google.com/search?client=safari&rls=en&q=hugo+directory+structure&ie=UTF-8&oe=UTF-8)
- [hugo lower level pages not showing up - Google Search](https://www.google.com/search?client=safari&rls=en&q=hugo+lower+level+pages+not+showing+up&ie=UTF-8&oe=UTF-8)
- [hugo themes - Google Search](https://www.google.com/search?client=safari&rls=en&q=hugo+themes&ie=UTF-8&oe=UTF-8)
- [Multi-level sections (tree) · Issue #465 · gohugoio/hugo](https://github.com/gohugoio/hugo/issues/465)
- [nvALT - BrettTerpstra.com](https://brettterpstra.com/projects/nvalt/)
- [Some pages not showing up - support - HUGO](https://discourse.gohugo.io/t/some-pages-not-showing-up/8118/4)


