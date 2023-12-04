from lib.customers import Customer
from lib.restaurant import Restaurant
from lib.review import Review

# Example usage:
customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")

restaurant1 = Restaurant("Cafe XYZ")
restaurant2 = Restaurant("Pizza Palace")

customer1.add_review(restaurant1, 4)
customer1.add_review(restaurant2, 5)
customer2.add_review(restaurant1, 3)

print(customer1.full_name())
print(customer1.restaurants())

print(restaurant1.customers())
print(restaurant1.reviews())
