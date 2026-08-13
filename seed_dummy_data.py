import os
import django
from datetime import date, timedelta
from decimal import Decimal

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "food_delivery_system.settings")
django.setup()

from django.db import transaction
from django.utils import timezone

from users.models import User
from restaurants.models import Restaurant, MenuItem
from orders.models import Order
from delivery.models import Driver, Delivery
from feedback.models import Feedback
from promotions.models import Promotion


@transaction.atomic
def create_dummy_data():

    print("Creating anonymous test data...")

    # ---------------------------------------------------------
    # 1. USERS
    # ---------------------------------------------------------

    users = []

    for i in range(1, 6):
        user, created = User.objects.update_or_create(
            email=f"customer{i}@example.com",
            defaults={
                "full_name": f"Customer{i:03d}",
                "phone": f"+44 00000000{i:02d}",
                "address": f"Test Address {i:03d}",
                "role": "customer",
            },
        )
        users.append(user)

    print(f"Users created/updated: {len(users)}")

    # ---------------------------------------------------------
    # 2. RESTAURANTS
    # ---------------------------------------------------------

    restaurants = []

    restaurant_data = [
        ("Restaurant001", "Test Location 001", "+44 0000000101", Decimal("4.5")),
        ("Restaurant002", "Test Location 002", "+44 0000000102", Decimal("4.2")),
        ("Restaurant003", "Test Location 003", "+44 0000000103", Decimal("4.7")),
    ]

    for name, location, phone, rating in restaurant_data:
        restaurant, created = Restaurant.objects.update_or_create(
            name=name,
            defaults={
                "location": location,
                "phone": phone,
                "rating": rating,
            },
        )
        restaurants.append(restaurant)

    print(f"Restaurants created/updated: {len(restaurants)}")

    # ---------------------------------------------------------
    # 3. MENU ITEMS
    # ---------------------------------------------------------

    menu_data = [
        (restaurants[0], "Test Burger 001", "Sample menu item for testing", Decimal("25.00")),
        (restaurants[0], "Test Pizza 001", "Sample pizza for testing", Decimal("32.00")),
        (restaurants[1], "Test Pasta 001", "Sample pasta for testing", Decimal("28.00")),
        (restaurants[1], "Test Sandwich 001", "Sample sandwich for testing", Decimal("18.00")),
        (restaurants[2], "Test Rice Bowl 001", "Sample rice bowl for testing", Decimal("22.00")),
        (restaurants[2], "Test Salad 001", "Sample salad for testing", Decimal("16.00")),
    ]

    menu_items = []

    for restaurant, food_name, description, price in menu_data:
        item, created = MenuItem.objects.update_or_create(
            restaurant=restaurant,
            food_name=food_name,
            defaults={
                "description": description,
                "price": price,
                "available": True,
            },
        )
        menu_items.append(item)

    print(f"Menu items created/updated: {len(menu_items)}")

    # ---------------------------------------------------------
    # 4. DELIVERY DRIVERS
    # ---------------------------------------------------------

    drivers = []

    driver_data = [
        ("Driver001", "+44 0000000201", "Bike-001", 2, True),
        ("Driver002", "+44 0000000202", "Bike-002", 4, True),
        ("Driver003", "+44 0000000203", "Car-001", 6, True),
    ]

    for name, phone, vehicle, experience, available in driver_data:
        driver, created = Driver.objects.update_or_create(
            name=name,
            defaults={
                "phone": phone,
                "vehicle": vehicle,
                "experience": experience,
                "available": available,
            },
        )
        drivers.append(driver)

    print(f"Drivers created/updated: {len(drivers)}")

    # ---------------------------------------------------------
    # 5. ORDERS
    # ---------------------------------------------------------

    orders = []

    order_data = [
        (users[0], restaurants[0], menu_items[0], 2, "Delivered"),
        (users[1], restaurants[1], menu_items[2], 1, "Delivered"),
        (users[2], restaurants[2], menu_items[4], 3, "Delivered"),
        (users[3], restaurants[0], menu_items[1], 1, "Preparing"),
        (users[4], restaurants[1], menu_items[3], 2, "Out for Delivery"),
    ]

    for customer, restaurant, menu_item, quantity, status in order_data:

        total_price = menu_item.price * quantity

        order, created = Order.objects.get_or_create(
            customer=customer,
            restaurant=restaurant,
            menu_item=menu_item,
            quantity=quantity,
            defaults={
                "total_price": total_price,
                "order_date": timezone.now(),
                "status": status,
            },
        )

        # Update status/price if record already existed
        order.total_price = total_price
        order.status = status
        order.save()

        orders.append(order)

    print(f"Orders created/updated: {len(orders)}")

    # ---------------------------------------------------------
    # 6. DELIVERIES
    # ---------------------------------------------------------

    delivery_data = [
        (orders[0], drivers[0]),
        (orders[1], drivers[1]),
        (orders[2], drivers[2]),
        (orders[4], drivers[0]),
    ]

    deliveries = []

    for order, driver in delivery_data:

        delivery, created = Delivery.objects.update_or_create(
            order=order,
            defaults={
                "driver": driver,
                "assigned_date": timezone.now(),
            },
        )

        deliveries.append(delivery)

    print(f"Deliveries created/updated: {len(deliveries)}")

    # ---------------------------------------------------------
    # 7. FEEDBACK
    # ---------------------------------------------------------

    feedback_data = [
        (orders[0], 5, "Test feedback: order received successfully."),
        (orders[1], 4, "Test feedback: good service and delivery."),
        (orders[2], 5, "Test feedback: sample positive feedback."),
    ]

    feedback_records = []

    for order, rating, comment in feedback_data:

        feedback, created = Feedback.objects.update_or_create(
            order=order,
            defaults={
                "rating": rating,
                "comment": comment,
                "created_at": timezone.now(),
            },
        )

        feedback_records.append(feedback)

    print(f"Feedback records created/updated: {len(feedback_records)}")

    # ---------------------------------------------------------
    # 8. PROMOTIONS
    # ---------------------------------------------------------

    today = date.today()

    promotion_data = [
        (
            "Promotion001",
            "Sample promotion for testing",
            10,
            today - timedelta(days=10),
            today + timedelta(days=20),
        ),
        (
            "Promotion002",
            "Anonymous promotional offer",
            15,
            today - timedelta(days=5),
            today + timedelta(days=25),
        ),
        (
            "Promotion003",
            "Test discount promotion",
            20,
            today,
            today + timedelta(days=30),
        ),
    ]

    promotions = []

    for title, description, discount, start_date, end_date in promotion_data:

        promotion, created = Promotion.objects.update_or_create(
            title=title,
            defaults={
                "description": description,
                "discount": discount,
                "start_date": start_date,
                "end_date": end_date,
            },
        )

        promotions.append(promotion)

    print(f"Promotions created/updated: {len(promotions)}")

    print()
    print("==========================================")
    print("ANONYMOUS TEST DATA CREATED SUCCESSFULLY")
    print("==========================================")
    print(f"Users:       {User.objects.count()}")
    print(f"Restaurants: {Restaurant.objects.count()}")
    print(f"Menu items:  {MenuItem.objects.count()}")
    print(f"Drivers:     {Driver.objects.count()}")
    print(f"Orders:      {Order.objects.count()}")
    print(f"Deliveries:  {Delivery.objects.count()}")
    print(f"Feedback:   {Feedback.objects.count()}")
    print(f"Promotions:  {Promotion.objects.count()}")
    print("==========================================")


if __name__ == "__main__":
    create_dummy_data()