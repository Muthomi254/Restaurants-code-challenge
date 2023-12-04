# from review import Review  
# from customers import Customer
# from restaurant import Restaurant

# # Example usage:
# customer1 = Customer("John", "Doe")
# customer2 = Customer("Jane", "Smith")

# restaurant1 = Restaurant("Cafe XYZ")
# restaurant2 = Restaurant("Pizza Palace")

# customer1.add_review(restaurant1, 4)
# customer1.add_review(restaurant2, 5)
# customer2.add_review(restaurant1, 3)

# print(customer1.full_name())
# print(customer1.restaurants())

# print(restaurant1.customers())
# print(restaurant1.get_reviews)  # Remove the parentheses when accessing the attribute


from review import Review  
from customers import Customer
from restaurant import Restaurant

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
print(restaurant1.get_reviews())  
