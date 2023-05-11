from metadata.models import Location, Department, Category, SubCategory, SKU

# metadata_string = """Perimeter,Bakery,Bakery Bread,Bagels
# Perimeter,Bakery,Bakery Bread,Baking or Breading Products
# Perimeter,Bakery,Bakery Bread,English Muffins or Biscuits
# Perimeter,Bakery,Bakery Bread,Flatbreads
# Perimeter,Bakery,In Store Bakery,Breakfast Cake or Sweet Roll
# Perimeter,Bakery,In Store Bakery,Cakes
# Perimeter,Bakery,In Store Bakery,Pies
# Perimeter,Bakery,In Store Bakery,Seasonal
# Center,Dairy,Cheese,Cheese Sauce
# Center,Dairy,Cheese,Specialty Cheese
# Center,Dairy,Cream or Creamer,Dairy Alternative Creamer
# Center,Dairy,Cream or Creamer,Whipping Creams
# Center,Dairy,Cultured,Cottage Cheese
# Center,Dairy,Refrigerated Baking,Refrigerated Breads
# Center,Dairy,Refrigerated Baking,Refrigerated English Muffins and Biscuits
# Center,Dairy,Refrigerated Baking,Refrigerated Hand Held Sweets
# Center,Dairy,Refrigerated Baking,Refrigerated Pie Crust
# Center,Dairy,Refrigerated Baking,Refrigerated Sweet Breakfast Baked Goods
# Perimeter,Deli and Foodservice,Self Service Deli Cold,Beverages
# Perimeter,Deli and Foodservice,Service Deli,Cheese All Other
# Perimeter,Deli and Foodservice,Service Deli,Cheese American
# Perimeter,Floral,Bouquets and Cut Flowers,Bouquets and Cut Flowers
# Perimeter,Floral,Gifts,Gifts
# Perimeter,Floral,Plants,Plants
# Center,Frozen,Frozen Bake,Bread or Dough Products Frozen
# Center,Frozen,Frozen Bake,Breakfast Cake or Sweet Roll Frozen
# Center,Frozen,Frozen Breakfast,Frozen Breakfast Entrees
# Center,Frozen,Frozen Breakfast,Frozen Breakfast Sandwich
# Center,Frozen,Frozen Breakfast,Frozen Egg Substitutes
# Center,Frozen,Frozen Breakfast,Frozen Syrup Carriers
# Center,Frozen,Frozen Desserts or Fruit and Toppings,Pies Frozen
# Center,Frozen,Frozen Juice,Frozen Apple Juice
# Center,Frozen,Frozen Juice,Frozen Fruit Drink Mixers
# Center,Frozen,Frozen Juice,Frozen Fruit Juice All Other
# Center,GM,Audio Video,Audio
# Center,GM,Audio Video,Video DVD
# Center,GM,Audio Video,Video VHS
# Center,GM,Housewares,Bedding
# Center,GM,Housewares,Candles
# Center,GM,Housewares,Collectibles and Gifts
# Center,GM,Housewares,Flashlights
# Center,GM,Housewares,Frames
# Center,GM,Insect and Rodent,Indoor Repellants or Traps
# Center,GM,Insect and Rodent,Outdoor Repellants or Traps
# Center,GM,Kitchen Accessories,Kitchen Accessories
# Center,GM,Laundry,Bleach Liquid"""
#
#
# def a():
#     metadata_list = [line.split(",") for line in metadata_string.split("\n")]
#     for each in metadata_list:
#         print(each)
#         lo, created = Location.objects.get_or_create(name=each[0])
#         do, created = Department.objects.get_or_create(name=each[1], location=lo)
#         co, created = Category.objects.get_or_create(name=each[2], department=do)
#         so, created = SubCategory.objects.get_or_create(name=each[3], category=co)


data = [
    [1, "SKUDESC1", "Permiter", "Bakery", "Bakery Bread", "Bagels"],
    [
        2,
        "SKUDESC2",
        "Permiter",
        "Deli and Foodservice",
        "Self Service Deli Cold",
        "Beverages",
    ],
    [
        3,
        "SKUDESC3",
        "Permiter",
        "Floral",
        "Bouquets and Cut Flowers",
        "Bouquets and Cut Flowers",
    ],
    [4, "SKUDESC4", "Permiter", "Deli and Foodservice", "Service Deli", "All Other"],
    [
        5,
        "SKUDESC5",
        "Center",
        "Frozen",
        "Frozen Bake",
        "Bread or Dough Products Frozen",
    ],
    [6, "SKUDESC6", "Center", "Grocery", "Crackers", "Rice Cakes"],
    [7, "SKUDESC7", "Center", "GM", "Audio Video", "Audio"],
    [8, "SKUDESC8", "Center", "GM", "Audio Video", "Video DVD"],
    [9, "SKUDESC9", "Permiter", "GM", "Housewares", "Beeding"],
    [10, "SKUDESC10", "Permiter", "Seafood", "Frozen Shellfish", "Frozen Shellfish"],
    [11, "SKUDESC11", "Permiter", "Seafood", "Other Seafood", "All Other Seafood"],
    [
        12,
        "SKUDESC12",
        "Permiter",
        "Seafood",
        "Other Seafood",
        "Prepared Seafood Entrees",
    ],
    [13, "SKUDESC13", "Permiter", "Seafood", "Other Seafood", "Salads"],
    [14, "SKUDESC14", "Permiter", "Bakery", "Bakery Bread", "Bagels"],
    [
        15,
        "SKUDESC15",
        "Permiter",
        "Deli and Foodservice",
        "Self Service Deli Cold",
        "Beverages",
    ],
    [
        16,
        "SKUDESC16",
        "Permiter",
        "Floral",
        "Bouquets and Cut Flowers",
        "Bouquets and Cut Flowers",
    ],
    [17, "SKUDESC17", "Permiter", "Deli and Foodservice", "Service Deli", "All Other"],
    [
        18,
        "SKUDESC18",
        "Center",
        "Frozen",
        "Frozen Bake",
        "Bread or Dough Products Frozen",
    ],
]


def b():
    for each in data:
        print(each)
        sku = SKU.objects.get_or_create(
            sku=each[0],
            name=each[1],
            location=each[2],
            department=each[3],
            category=each[4],
            subcategory=each[5],
        )
