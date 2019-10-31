$(document).ready(function () {
    var counters = {};

    function addRow(name) {
        counters[name] += 1;
        const row = $(`.${name}`);
        const form = `
        <div class="form-row">
            <div class="col-4">
                <label for="${name}-last-name-${counters[name]}">Прізвище</label>
                <input id="${name}-last-name-${counters[name]}" class="form-control" type="text">
            </div>
            <div class="col-4">
                <label for="${name}-first-name-${counters[name]}">Ім'я</label>
                <input id="${name}-first-name-${counters[name]}" class="form-control" type="text">
            </div>
            <div class="col-4">
                <label for="${name}-surname-${counters[name]}">По батькові</label>
                <input id="${name}-surname-${counters[name]}" class="form-control" type="text">
            </div>
        </div>`;

        row.append(form);
    }

    $('#add-author-button').on('click', function () { addRow('authors')});
    $('#add-editor-button').on('click', function () { addRow('editors') });
    $('#add-interpreter-button').on('click', function () { addRow('interpreters') });

    $('.number').on('keypress' , function (evt) {
        if (evt.which < 48 || evt.which > 57) {
            evt.preventDefault();
        }
    });

    $('#add-book').on('click', function () {
        const data = {};
        data.authors = [];

        const fields = ['authors', 'editors', 'interpreters'];
        const properties = ['first-name', 'last-name'];

        for (field of fields) {
            let author = {};
            author.first_name = $(`#${field}-first-name-0`).val() || null;
            author.last_name = $(`#${field}-last-name-0`).val() || null;
            author.patronymic = $(`#${field}-surname-0`).val() || null;
            if (field === 'authors' && author.first_name) {
                author._type = 'au';
            } else if (field === 'editors'  && author.first_name) {
                author._type = 'ed';
            } else if (field === 'interpreters' && author.first_name) {
                author._type = 'tr';
                author.lang = $(`#language`).val() || null;
            }

            if (author.first_name && author.last_name && author.patronymic) {
                data.authors.push(author);
            }
        }

        data.name = $(`#book-name`).val();
        data.book_type = $(`#book-type`).val() || null;
        data.number = $(`#edition-number`).val() || null;
        data.extra_info = $(`#additional-inform`).val() || null;
        data.city = $(`#edition-city`).val() || null;
        data.publisher = $(`#edition-house`).val() || null;
        data.year = $(`#edition-year`).val() || null;
        data.number_of_pages = $(`#number-pages`).val() || null;

        console.log(JSON.stringify(data));

        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:8000/books/",
            dataType: 'json',
            contentType: 'application/json',
            data: JSON.stringify(data),
            success: function (data) {
                console.log(data);
                alert('Відправлено');
            },
            error: function (err) {
                console.log(err);
                alert('error');
            },
          });

    })

})