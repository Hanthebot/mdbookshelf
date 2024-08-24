let bookshelf = document.querySelector("#bookshelf");
let list_elements = "";
for (const book_code in data) {
    list_elements += `<a class="book" href="${data[book_code].path}/index.html">
            <img src="${data[book_code].path}/cover.png" alt="${data[book_code].title}">
            <h3>${data[book_code].title}</h3>
        </a>
        `;
}
bookshelf.innerHTML = list_elements;