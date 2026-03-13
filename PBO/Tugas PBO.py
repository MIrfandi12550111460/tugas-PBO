class Restaurant:
    def __init__(self,restaurant_name,Cuisine_type,):
        self.restaurant_name = restaurant_name
        self.Cuicine_type = Cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("nama restaurant :", self.restaurant_name)
        print("Jenis Maaakan :", self.Cuicine_type)

    def open_restaurant(self):
        print(self.restaurant_name, "sekarang buka")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, additional):
        self.number_served += additional

restaurant = Restaurant("Restaurant Nusantara", "Masakan Indonesia")
restaurant.describe_restaurant()

print("Jumlah pelanggan dilayani:", restaurant.number_served)
restaurant.number_served =15
print("Jumlah pelanggan sekarang:", restaurant.number_served)
restaurant.set_number_served(35)
print("Jumlah pelanggan setelah diubah:", restaurant.number_served)
restaurant.increment_number_served(15)
print("Jumlah pelanggan setelah penambahan:", restaurant.number_served)


#print("Nama restaurant :", restaurant.restaurant_name)
#print("Jenis Masakan :", restaurant.Cuicine_type)

#restaurant.describe_restaurant()
#restaurant.open_restaurant()
#restaurant.set_number_served(15)
#restaurant.increment_number_served(20)