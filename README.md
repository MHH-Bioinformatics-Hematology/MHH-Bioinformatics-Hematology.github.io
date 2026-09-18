# MHH-Bioinformatics-Hematology.github.io

Website of the bioinformatics work in AG Heidel, Hannover Medical School.
Built by GitHub Pages with Jekyll; pushing to the default branch publishes it.

## Layout

- `index.html`, `research.html`, `teaching.html`, `publications.html`, `contact.html`, `legal.html` (Impressum), `privacy.html`: the pages
- `_layouts/`: shared header, navigation and footer (`default.html`), course page (`course.html`)
- `_courses/`: one Markdown file per course or lecture series
- `materials/<course-file-name>/`: files offered for download on that course page
- `_data/publications.yml`: publication list
- `assets/style.css`: styling

## Add a course

Copy a file in `_courses/`, rename it (the file name becomes the URL,
`_courses/2027-ss-example.md` is served at `/teaching/2027-ss-example/`) and edit the header:

- `term`: heading the course is grouped under on the Teaching page
- `term_order`: sort key, year for summer terms (2027.0), year + 0.5 for winter terms (2027.5)
- `order`: position within the term
- `upcoming: true`: optional tag
- `modules`: optional, course material as a list of blocks from `_data/modules.yml`
  (Galaxy Training Network slides and hands-on links), in teaching order
- `links`: optional list of external links (`title`, `url`)

The text below the header is the course description and may use Markdown
(headings, lists, a lecture schedule, links).

## Publish course material

Put slides, PDFs, notebooks or data into `materials/<course-file-name>/`.
Every file in that folder is listed automatically under "Course material"
on the course page. Large datasets are better hosted elsewhere (for example Zenodo)
and added under `links`.

## Preview locally

    docker run --rm -v "$PWD":/srv/jekyll -p 4000:4000 jekyll/jekyll:3.8 jekyll serve
