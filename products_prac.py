store = [
  {
    "name": "Electronics",
    "products": [
      {
        "name": "Smartphone",
        "variants": [
          { "name": "64GB", "price": 300, "qty": 0 },
          { "name": "128GB", "price": 400, "qty": 3 },
          { "name": "256GB", "price": 500, "qty": 0 },
        ],
      },
      {
        "name": "Laptop",
        "variants": [
          { "name": "i3", "price": 600, "qty": 4 },
          { "name": "i5", "price": 800, "qty": 6 },
          { "name": "i7", "price": 1000, "qty": 2 },
        ],
      },
      {
        "name": "Headphones",
        "variants": [
          { "name": "Wired", "price": 50, "qty": 10 },
          { "name": "Wireless", "price": 100, "qty": 8 },
          { "name": "Noise Cancelling", "price": 150, "qty": 5 },
        ],
      },
    ],
  },
  {
    "name": "Clothing",
    "products": [
      {
        "name": "T-Shirt",
        "variants": [
          { "name": "Small", "price": 10, "qty": 12 },
          { "name": "Medium", "price": 12, "qty": 15 },
          { "name": "Large", "price": 15, "qty": 9 },
        ],
      },
      {
        "name": "Jacket",
        "variants": [
          { "name": "Leather", "price": 100, "qty": 4 },
          { "name": "Denim", "price": 70, "qty": 7 },
          { "name": "Bomber", "price": 80, "qty": 6 },
        ],
      },
    ],
  },
  {
    "name": "Groceries",
    "products": [
      {
        "name": "Rice",
        "variants": [
          { "name": "1kg", "price": 2, "qty": 20 },
          { "name": "5kg", "price": 8, "qty": 15 },
          { "name": "10kg", "price": 15, "qty": 10 },
        ],
      },
      {
        "name": "Milk",
        "variants": [
          { "name": "500ml", "price": 1, "qty": 25 },
          { "name": "1L", "price": 2, "qty": 18 },
          { "name": "2L", "price": 3, "qty": 12 },
        ],
      },
      {
        "name": "Bread",
        "variants": [
          { "name": "White", "price": 1.5, "qty": 14 },
          { "name": "Brown", "price": 2, "qty": 11 },
          { "name": "Multigrain", "price": 2.5, "qty": 9 },
        ],
      },
    ],
  },
]


basket = []

while True:
    print("\n=== Categories ===") 

    for i in range(len(store)):
        print(f"{i+1}. {store[i]['name']}")

    cat_choice = int(input("Select a category (0 to checkout): ")) - 1

    if cat_choice == -1:
        break

    print(f"\n=== Products in {store[cat_choice]['name']} ===")

    for i in range(len(store[cat_choice]["products"])):
        print(f"{i+1}. {store[cat_choice]['products'][i]['name']}")

    prod_choice = int(input("Select a product: ")) - 1

    print(f"\n=== Variants of {store[cat_choice]['products'][prod_choice]['name']} ===")

    for i in range(len(store[cat_choice]["products"][prod_choice]["variants"])):
        if(store[cat_choice]["products"][prod_choice]["variants"][i]["qty"]!=0):
            v = store[cat_choice]["products"][prod_choice]["variants"][i]
            print(f"{i+1}. {v['name']} - PKR : {v['price']} QTY : {v['qty']}")  

    var_choice = int(input("Select a variant: ")) - 1

    chosen_variant = store[cat_choice]["products"][prod_choice]["variants"][var_choice]

    if(store[cat_choice]["products"][prod_choice]["variants"][var_choice]["qty"] != 0):

        basket.append({
            "category": store[cat_choice]["name"],
            "product": store[cat_choice]["products"][prod_choice]["name"],
            "variant": chosen_variant["name"],
            "price": chosen_variant["price"]
        })
        store[cat_choice]["products"][prod_choice]["variants"][var_choice]['qty'] = store[cat_choice]["products"][prod_choice]["variants"][var_choice]['qty']-1
        print("\nAdded to basket!")
        print("Current Basket:", basket)
    else:
        print(f"{store[cat_choice]["products"][prod_choice]["variants"][var_choice]['name']} OUT OF STOCK")    

print("\nFinal Basket:", basket)
