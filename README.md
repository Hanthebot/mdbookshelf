# mdBookShelf

A wrapper to grab multiple mdBook together, and serve them altogether on a static site.

## Usage
### Structure
```md
.
├── src
│   ├── cover.png  # default cover for your books
│   ├── data.js    # data wrapped by `manager.py`
│   ├── data.json  # CONFIGURATION where you specify list of books and their directory
│   ├── script.js  # JS for formatting the page
│   └── ...
├── index.html     # Homepage / Bookshelf
├── manager.py     # Manager to clear / export / serve books
└── ...
```
```json
// src/data.json
{
    "book_code_1": {
        "title": "Awesome Title 1", 
        "path": "absolute_dir_to_mdbook/book"
    },
    "book_code_2": {
        "title": "Awesome Title 2", 
        "path": "absolute_dir_to_mdbook2/book"
    },
    ...
}
```
```md
absolute_dir_to_mdbook/book
├── cover.png      # Book cover, automatically generated if needed
├── index.html     # Home page for the book
└── ...
```


### Commands
1. Clearing all subdirectories
   ```py
   python manager.py clear
   ```
   - deletes / unlinks all subdirectories except `src`
   - this operation is done before `serve` and `export` command as well
   - ⚠️don't leave any valuable files in subdirectories!
2. Serving mdBooks
   ```py
   python manager.py serve
   ```
   - creates junction (`mklink /J`) to book directory
   - all book data can be accessed from `index.html` 
3. Exporting mdBooks
   ```py
   python manager.py export
   ```
   - copies all books into subdirectory
   - modifies path from `data.js` accordingly
   - this folder can now be uploaded online for perfectly static service 



## Remarks
- While it was designed for mdBook, it can serve as a bookshelf for any con
- For the spirit of [mdBook](https://github.com/rust-lang/mdBook), `manager.py` will ~~hopefully~~ be rewritten in Rust. 
- Features to add
  - editing `data.json` through `manager.py`
    - adding new books
    - editing book information
    - deleting books
  - Some customization option (e.g. title, theme change) for `index.html`
- I'm open for collaboration || suggestions

## Thanks to
- [mdBook](https://github.com/rust-lang/mdBook)
- Arthur's work on [O'Really-like cover generator](https://github.com/ArthurBeaulieu/ORlyGenerator)