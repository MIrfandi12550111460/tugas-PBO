class User:
    def __init__(self, first_name, last_name, age, email, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.city = city
        self.login_attempts = 0

    def describe_user(self):
        print("Nama Depan :", self.first_name)
        print("Nama Belakang :", self.last_name)
        print("Umur :", self.age)
        print("Email :", self.email)
        print("Kota :", self.city)
        print()

    def greet_user(self):
        print("Halo", self.first_name, self.last_name, "! Selamat datang.")
        print()

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User("Muhamad", "Irfandi", 20, "irfandi@email.com", "Pekanbaru")

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print("Jumlah login attempts:", user1.login_attempts)

user1.reset_login_attempts()

print("Login attempts setelah reset:", user1.login_attempts)

#user1 = User("Muhamad", "Irfandi", 20, "irfandi@email.com", "Pekanbaru")
#user2 = User("Andi", "Saputra", 22, "andi@email.com", "Jakarta")
#user3 = User("Siti", "Rahma", 19, "siti@email.com", "Bandung")

#user1.describe_user()
#user1.greet_user()

#user2.describe_user()
#user2.greet_user()

#user3.describe_user()
#user3.greet_user()