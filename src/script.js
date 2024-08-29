document.title = data.title;
let bookshelf = document.querySelector("#bookshelf");
let list_elements = "";
for (const book_code in data.books) {
    list_elements += `<a class="book" href="${data.books[book_code].path}/index.html">
            <img src="covers/${book_code}.png" alt="${data.books[book_code].title}">
            <h3>${data.books[book_code].title}</h3>
        </a>
        `;
}
bookshelf.innerHTML = list_elements;