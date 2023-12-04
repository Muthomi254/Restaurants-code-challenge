# Restaurant Review System

A Python-based system for managing restaurant reviews.

## Description

This system provides a simple framework for managing restaurant reviews. It includes classes for Customers, Restaurants, and Reviews. Customers can leave reviews for specific restaurants, and the system keeps track of this information.


## Installation

    Clone the repository:

bash/Terminal

git clone https://github.com/Muthomi254/Restaurants-code-challenge.git

    Navigate to the project directory:

bash/Terminal

cd restaurant-review-system

    Install dependencies:

bash/Terminal

pip install -r requirements.txt

Usage

    Run the main.py script:

bash/Terminal


python main.py

    The script creates customers, restaurants, and reviews based on the provided example. It displays information about customers, restaurants, and reviews.

    Explore and modify the code in main.py and other files for your specific use case.

## How to Use
  ### Usage

    Run the main.py script:

bash

python main.py

    The script creates customers, restaurants, and reviews based on the provided example. It displays information about customers, restaurants, and reviews.

    Explore and modify the code in main.py and other files for your specific use case.

 ### Customer Information

    To display information about customers:

python

print(customer1)
print(customer2)

 ### Restaurant Information

    To display information about restaurants:

python

print(restaurant1)
print(restaurant2)

  ### Reviews

    To display specific details using individual methods:

python

print(f"{customer1.full_name()} has reviewed the following restaurants: {customer1.restaurants()}")
print(f"{restaurant1.get_name()} has been reviewed by the following customers: {restaurant1.customers()}")

    To display all reviews for a specific restaurant:

python

print(f"\nReviews for {restaurant1.get_name()}:")
for review in restaurant1.get_reviews():
    print(f"  - Review by {review.get_customer().full_name()}: Rating - {review.get_rating()}")

## Contribution

Contributions are welcome! Here's how you can contribute:

    Fork the repository
    Create a new branch (git checkout -b feature/new-feature)
    Make your changes
    Commit your changes (git commit -m 'Add new feature')
    Push to the branch (git push origin feature/new-feature)
    Open a pull request

## Review

If you find any issues or have suggestions for improvement, please open an issue.
License

This project is licensed under the MIT License - see the LICENSE file for details.