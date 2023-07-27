const products = [
    {
        id: 0,
        image: 'images/1.jpg',
        title: 'Cappuccino',
        price: 150,
    },
    {
        id: 1,
        image: 'images/2.jpg',
        title: 'Americano',
        price: 170,
    },
    {
        id: 2,
        image: 'images/2.jpg',
        title: 'Mocha',
        price: 180,
    },
    {
        id: 3,
        image: 'images/3.jpg',
        title: 'Latte',
        price: 180,
    }
]
const categories = [...new Set(product.map((item) =>
    {return item}))]
    