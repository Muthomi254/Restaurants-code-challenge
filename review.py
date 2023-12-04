class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating_value = rating
        Review.all_reviews.append(self)

    def get_rating(self):
        return self.rating_value

    @classmethod
    def all(cls):
        return cls.all_reviews

    def get_customer(self):
        return self.customer

    def get_restaurant(self):
        return self.restaurant

    def __str__(self):
        return f"Review(Customer: {self.customer.full_name()}, Restaurant: {self.restaurant.get_name()}, Rating: {self.rating_value})"