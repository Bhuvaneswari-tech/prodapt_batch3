//Load JSON data

const products = require('./products.json')

//Activity 1

console.log('\nActivity1 - Display Product names')

products.forEach(product=>{
    console.log(`${product.name} - ₹${product.price}`)
})


//Activity 2 - Calculate Total Price(map)
console.log('\nActivity2 - Calculate Total Price')

const totalPrice = products.map(product=>({
    name: product.name,
    total: product.price * product.quantity
}))

console.log(totalPrice)

//Activity3 - Find Available products
console.log('\nActivity3 - Find Available Products')

const availableProducts = products.filter(product=>product.inStock)

console.log(availableProducts)

//Activity4 - Find Expensive product >5000
console.log('\nActivity4 - Expensive product >5000')
const expensiveProduct = products.filter(product=>product.price>5000)

console.log(expensiveProduct)

//Activity5 - Search for a Product (find - 103)
console.log("\nActivity4 - Search for a Product")
const searchProduct = products.find(product=>product.id==103)

console.log(searchProduct)

//Activity6 - Check Product Availability (some)
console.log("\nActivity6 - Check Product Availability")
const checkAvailable = products.some(product => !product.inStock)
console.log(checkAvailable)

//Activity7 - Verify Stock Status (every)
console.log("\nActivity7 - Verify Stock Status")
const allavailable =  products.every(product => product.inStock)

console.log(allavailable)

//Activity 8 - Calculate Grand Total (reduce)
console.log("\nActivity8 - Calculate Grand Total")
const grandTotal = products.reduce((total,product) =>{
    return total + (product.price * product.quantity)
}, 0)

console.log(grandTotal)

//Activity 9 - Sort Products by Price (sort)
console.log("\nActity 9 - Sort Products by Price")
const sortProduct = [...products].sort((a,b)=>a.price-b.price)

sortProduct.forEach(product=>{
    console.log(product.name)
})

//Activity 10 - Display Only Product Names (map)
console.log("\nActity 10 - Display Only Product Names")
const displayProduct = products.map(product=>product.name)
console.log(displayProduct)

//Activity 11 - Find Product(Office Chair) Position (findIndex)
console.log("\nActity 11 - Find Product(Office Chair) Position")
const index = products.findIndex(product => product.name === "Office Chair")
console.log(index)

//Activity 12 - Remove Out-of-Stock Products (filter)
console.log("\nActity 12 - Remove Out-of-Stock Products")
const removeProducts = products.filter(product=>product.inStock)

console.log(removeProducts)

//Activity 13 – Add GST (map) - 18%
console.log("\nActity 13 - Add GST (map) - 18%")
const productWithGST = products.map(product=>({
    ...product,
    gst: product.price * 0.18
}))

console.log(productWithGST)

//Activity 14 – Top 3 Cheapest Products
console.log("\nActity 14 - Top 3 Cheapest Products")
const cheapestProduct = [...products]
.sort((a,b)=>a.price-b.price)
.slice(0,3)

cheapestProduct.forEach(product=>{
    console.log(`${product.name} - ₹${product.price}`)
})

//Activity 15 – Generate Bill Summary (reduce)
console.log("\nActity 15 - Generate Bill Summary")
const billSummary = products.reduce(
    (summary,product)=>{
        summary.totalProducts++,
        summary.totalPrice += product.price,
        summary.totalAmount += product.price * product.quantity
        return summary
    },
    {
        totalProducts: 0,
        totalPrice: 0,
        totalAmount: 0
    }
)

console.log(billSummary)