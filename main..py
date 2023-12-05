from review import Review  
from customers import Customer
from restaurant import Restaurant

# Example usage:
customer1 = Customer("Kamande","Wa Kioi")
customer2 = Customer("Nganga", "Duma")

restaurant1 = Restaurant("Base ya Mutura")
restaurant2 = Restaurant("Kwa Mathee")

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
print(f"{restaurant1.get_name()} has been reviewed by the following customers: {[restaurant1.customers()]}")

print(f"\n{customer2.full_name()} has reviewed the following restaurants: {customer2.restaurants()}")
print(f"{restaurant2.get_name()} has been reviewed by the following customers: {restaurant2.customers()}")


# Display all reviews for a specific restaurant
print(f"\nReviews for {restaurant1.get_name()}:")
for review in restaurant1.get_reviews():
    print(f"  - Review by {review.get_customer().full_name()}: Rating - {review.get_rating()}")

print(f"\nReviews for {restaurant2.get_name()}:")
for review in restaurant2.get_reviews():
    print(f"  - Review by {review.get_customer().full_name()}: Rating - {review.get_rating()}")

