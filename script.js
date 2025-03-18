// JavaScript for handling "Add to Cart" functionality
let cart = [];

function addToCart(product) {
    cart.push(product);
    alert(product + " has been added to your cart!");
}

// Example usage for adding products
document.querySelectorAll('.product button').forEach(button => {
    button.addEventListener('click', () => {
        const productName = button.parentElement.querySelector('h3').innerText;
        addToCart(productName);
    });
});
