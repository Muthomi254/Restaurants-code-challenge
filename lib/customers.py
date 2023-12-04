

# # customer.py

# from review import Review  

# class Customer:
#     all_customers = []

#     def __init__(self, given_name, family_name):
#         self.given_name = given_name
#         self.family_name = family_name
#         self.reviews = []
#         Customer.all_customers.append(self)

#     def get_given_name(self):
#         return self.given_name

#     def get_family_name(self):
#         return self.family_name

#     def full_name(self):
#         return f"{self.given_name} {self.family_name}"

#     @classmethod
#     def all(cls):
#         return cls.all_customers

#     def restaurants(self):
#         return list(set([review.restaurant.get_name() for review in self.reviews]))

#     def add_review(self, restaurant, rating):
#         review = Review(self, restaurant, rating)
#         self.reviews.append(review)
#         restaurant.add_review(review)

#     def __str__(self):
#         return f"Customer(Name: {self.full_name()}, Reviews: {len(self.reviews)})"

#     def display_reviews(self):
#         if self.reviews:
#             print(f"{self.full_name()} has reviewed the following restaurants:")
#             for review in self.reviews:
#                 print(f"  - {review.restaurant.get_name()}: Rating - {review.get_rating()}")
#         else:
#             print(f"{self.full_name()} has not reviewed any restaurants yet.")

# customer.py
# customer.py

from lib.review import Review  

class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []
        Customer.all_customers.append(self)

    def get_given_name(self):
        return self.given_name

    def get_family_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def all(cls):
        return cls.all_customers

    def restaurants(self):
        return list(set([review.restaurant.get_name() for review in self.reviews]))

    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self.reviews.append(review)
        restaurant.add_review(review)

    def __str__(self):
        return f"{self.full_name()} has reviewed the following restaurants: {self.restaurants()}"

    def display_reviews(self):
        if self.reviews:
            print(f"{self.full_name()} has reviewed the following restaurants:")
            for review in self.reviews:
                print(f"  - {review.restaurant.get_name()}: Rating - {review.get_rating()}")
        else:
            print(f"{self.full_name()} has not reviewed any restaurants yet.")
