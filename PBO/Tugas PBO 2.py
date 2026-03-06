class Restaurant:
    def __init__(self,restaurant_name,Cuisine_type):
        self.restaurant_name = restaurant_name
        self.Cuicine_type = Cuisine_type

    def describe_restaurant(self):
        print("nama restaurant :", self.restaurant_name)
        print("Jenis Maaakan :", self.Cuicine_type)

    def open_restaurant(self):
        print(self.restaurant_name, "sekarang buka")

restaurant1 = Restaurant("Restaurant Nusantara", "Masakan Indonesia")
restaurant2 = Restaurant("Sushi Tokyo", "Masakan Jepang")
restaurant3 = Restaurant("Pasta Italia", "Masakan Italia")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()