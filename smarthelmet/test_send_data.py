"""
test_send_data.py
==================
Simulates Smart Helmet sensor data
for multiple helmets.
"""

import requests
import time
import random

BASE_URL = "http://127.0.0.1:8000"

# List of helmet IDs
HELMETS = ["H001", "H002", "H003", "H004", "H005"]


def send_normal_data(helmet_id):
    """Simulate normal riding"""

    data = {
        "helmet_id": helmet_id,
        "acceleration": round(random.uniform(0.5, 3.0), 2),
        "tilt": round(random.uniform(-5, 5), 2),

        # Random Kathmandu coordinates
        "latitude": 27.7172 + random.uniform(-0.02, 0.02),
        "longitude": 85.3240 + random.uniform(-0.02, 0.02),

        "helmet_worn": True,
        "accident": False,
        "battery": random.randint(70, 100),
    }

    response = requests.post(
        f"{BASE_URL}/api/data/",
        json=data
    )

    print(f"✅ {helmet_id} normal data sent")


def send_accident_data(helmet_id):
    """Simulate accident"""

    locations = [
        "Thamel",
        "Baneshwor",
        "Koteshwor",
        "Maitighar",
        "Kalanki"
    ]

    data = {
        "helmet_id": helmet_id,
        "acceleration": random.uniform(20, 35),
        "tilt": random.uniform(70, 95),

        "latitude": 27.7172 + random.uniform(-0.02, 0.02),
        "longitude": 85.3240 + random.uniform(-0.02, 0.02),

        "helmet_worn": True,
        "accident": True,

        "battery": random.randint(40, 90),

        "severity": random.choice([
            "low",
            "medium",
            "high"
        ]),

        "location": random.choice(locations),
    }

    response = requests.post(
        f"{BASE_URL}/api/data/",
        json=data
    )

    print(f"🚨 {helmet_id} accident data sent")


# =====================================================
# MAIN PROGRAM
# =====================================================

if __name__ == "__main__":

    print("\nSMART HELMET SIMULATOR")
    print("=" * 40)

    print("1. Send normal data")
    print("2. Send accident data")
    print("3. Continuous random data")
    print("4. Random accidents for all helmets")

    choice = input("\nEnter choice: ").strip()

    # -------------------------------------------------

    if choice == "1":

        for helmet in HELMETS:
            send_normal_data(helmet)

    # -------------------------------------------------

    elif choice == "2":

        helmet = input("Enter helmet ID: ").strip().upper()

        send_accident_data(helmet)

    # -------------------------------------------------

    elif choice == "3":

        print("\nSending live random data...")
        print("Press CTRL + C to stop.\n")

        while True:

            helmet = random.choice(HELMETS)

            # 80% normal data
            # 20% accident data
            if random.randint(1, 10) <= 8:
                send_normal_data(helmet)
            else:
                send_accident_data(helmet)

            time.sleep(3)

    # -------------------------------------------------

    elif choice == "4":

        for helmet in HELMETS:
            send_accident_data(helmet)
            time.sleep(1)

    # -------------------------------------------------

    else:
        print("Invalid choice")