products = [
    {
        "category": "Electronics",
        "items": [
            {"name": "Laptop", "price": 850, "stock": 10},
            {"name": "Smartphone", "price": 600, "stock": 25},
            {"name": "Headphones", "price": 80, "stock": 50},
        ],
    },
    {
        "category": "Clothing",
        "items": [
            {"name": "T-Shirt", "price": 15, "stock": 100},
            {"name": "Jeans", "price": 40, "stock": 60},
            {"name": "Jacket", "price": 90, "stock": 20},
        ],
    },
    {
        "category": "Groceries",
        "items": [
            {"name": "Rice (5kg)", "price": 10, "stock": 200},
            {"name": "Milk (1L)", "price": 2, "stock": 300},
            {"name": "Eggs (12)", "price": 3, "stock": 150},
        ],
    },
]

for category in products:  # outer loop
    print(f"\nCategory: {category['category']}")
    for item in category["items"]:  # inner loop
        print(f" - {item['name']} ({item['price']}) | Stock: {item['stock']}")


Output :

Category: Electronics
 - Laptop (850) | Stock: 10
 - Smartphone (600) | Stock: 25
 - Headphones (80) | Stock: 50
