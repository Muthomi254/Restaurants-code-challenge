# # class Restaurant:
# #     all_restaurants = []

# #     def __init__(self, name):
# #         self.name = name
# #         self.reviews = []
# #         Restaurant.all_restaurants.append(self)

# #     def name(self):
# #         return self.name

# #     @classmethod
# #     def all(cls):
# #         return cls.all_restaurants

# #     def reviews(self):
# #         return self.reviews

# #     def customers(self):
# #         return list(set([review.customer for review in self.reviews]))

# #     def add_review(self, review):
# #         self.reviews.append(review)
# class Restaurant:
#     all_restaurants = []

#     def __init__(self, name):
#         self.restaurant_name = name  # Changed attribute name to avoid conflict
#         self.review_list = []  # Changed attribute name to avoid conflict
#         Restaurant.all_restaurants.append(self)

#     def get_name(self):  
#         return self.restaurant_name  # Changed method name to avoid conflict

#     @classmethod
#     def all(cls):
#         return cls.all_restaurants

#     def get_reviews(self):  
#         return self.review_list  # Changed method name to avoid conflict

#     def customers(self):
#         return list(set([review.customer for review in self.review_list]))

#     def add_review(self, review):
#         self.review_list.append(review)

# restaurant.py

from lib.review import Review 
from lib.customers import Customer
 

class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.restaurant_name = name  
        self.review_list = []  
        Restaurant.all_restaurants.append(self)

    def get_name(self):  
        return self.restaurant_name  

    @classmethod
    def all(cls):
        return cls.all_restaurants

    def get_reviews(self):  
        return self.review_list  

    def add_review(self, review):
        self.review_list.append(review)

    def customers(self):
        return list(set([review.get_customer() for review in self.get_reviews()]))

    def display_info(self):
        print(f"Restaurant Name: {self.get_name()}")
        print(f"Number of Reviews: {len(self.get_reviews())}")
        print(f"Customers: {', '.join([customer.full_name() for customer in self.customers()])}")

    def __str__(self):
        return f"Restaurant(Name: {self.get_name()}, Reviews: {len(self.get_reviews())}, Customers: {', '.join([customer.full_name() for customer in self.customers()])})"
