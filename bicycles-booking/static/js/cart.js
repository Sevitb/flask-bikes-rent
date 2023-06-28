var cartId = "cart";


var localAdapter = {

    saveCart: function (object) {

        var stringified = JSON.stringify(object);
        localStorage.setItem(cartId, stringified);
        return true;

    },
    getCart: function () {

        return JSON.parse(localStorage.getItem(cartId));

    },
    clearCart: function () {

        localStorage.removeItem(cartId);

    }

};

var storage = localAdapter;

var helpers = {

    getHtml: function (id) {

        return document.getElementById(id).innerHTML;

    },
    setHtml: function (id, html) {

        document.getElementById(id).innerHTML = html;
        return true;

    },
    itemData: function (object) {

        var item = {

            name: object.getAttribute('data-name'),
            price: parseInt(object.getAttribute('data-price')),
            id: object.getAttribute('data-id'),
            image: object.getAttribute('data-image')

        };
        return item;

    },
    updateView: function () {


        var items = cart.getItems(),
            template = this.getHtml('cartT'),
            createdTemplate = _.template(template);
        compiledTemplate = createdTemplate({
            items: items
        })
        this.setHtml('cartItems', compiledTemplate);
        this.updateTotal();

    },
    emptyView: function () {

        this.setHtml('cartItems', '<p>Корзина пока пуста</p>');
        this.updateTotal();

    },
    updateTotal: function () {

        this.setHtml('totalPrice', cart.total + ' ₽');

    }

};

var cart = {

    count: 0,
    total: 0,
    items: [],
    getItems: function () {

        return this.items;

    },
    setItems: function (items) {

        this.items = items;
        for (var i = 0; i < this.items.length; i++) {
            var _item = this.items[i];
            this.total += _item.price;
        }

    },
    clearItems: function () {

        this.items = [];
        this.total = 0;
        storage.clearCart();
        helpers.emptyView();

    },
    addItem: function (item) {

        if (this.containsItem(item.id) === false) {

            this.items.push({
                id: item.id,
                name: item.name,
                price: item.price,
                image: item.image,
            });

            storage.saveCart(this.items);
            this.total += item.price;
            this.count += 1;

        } else {
            alert("Этот товар уже есть в корзине!");
        }
        helpers.updateView();

    },
    containsItem: function (id) {

        if (this.items === undefined) {
            return false;
        }

        for (var i = 0; i < this.items.length; i++) {

            var _item = this.items[i];

            if (id == _item.id) {
                return true;
            }

        }
        return false;

    },

};

document.addEventListener('DOMContentLoaded', function () {

    if (storage.getCart()) {

        cart.setItems(storage.getCart());
        helpers.updateView();

    } else {

        helpers.emptyView();

    }
    var products = document.querySelectorAll('.product button');
    [].forEach.call(products, function (product) {

        product.addEventListener('click', function (e) {

            var item = helpers.itemData(this.closest('.product'));
            cart.addItem(item);


        });

    });

    document.querySelector('#clear').addEventListener('click', function (e) {

        cart.clearItems();

    });


});