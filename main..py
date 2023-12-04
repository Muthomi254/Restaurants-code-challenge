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

# Display information about customers and restaurants
print("Customer Information:")
print(customer1)
print(customer2)
print("\nRestaurant Information:")
print(restaurant1)
print(restaurant2)

# Print specific details using individual methods
print(f"\n{customer1.full_name()} has reviewed the following restaurants: {customer1.restaurants()}")

# Display all reviews for a specific restaurant
print(f"\nReviews for {restaurant2.get_name()}:")
for review in restaurant1.get_reviews():
    print(f"  - Review by {review.get_customer().full_name()}: Rating - {review.get_rating()}")
