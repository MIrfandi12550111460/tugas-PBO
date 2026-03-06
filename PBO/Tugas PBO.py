class Restaurant:
    def __init__(self,restaurant_name,Cuisine_type):
        self.restaurant_name = restaurant_name
        self.Cuicine_type = Cuisine_type

    def describe_restaurant(self):
        print("nama restaurant :", self.restaurant_name)
        print("Jenis Maaakan :", self.Cuicine_type)

    def open_restaurant(self):
        print(self.restaurant_name, "sekarang buka")

restaurant = Restaurant("Restaurant Nusantara", "Masakan Indonesia")

print("Nama restaurant :", restaurant.restaurant_name)
print("Jenis Masakan :", restaurant.Cuicine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()