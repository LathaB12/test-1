import random
from datetime import datetime


# -------------------- TRAIN CLASS --------------------

class Train:
    def __init__(self, train_num, source, destination, seats):
        self.train_num = train_num
        self.source = source
        self.destination = destination
        self.seats = seats

        
        self.berths = {
            "SL": ["S1", "S2", "S3"],
            "SU": ["S1", "S2", "S3"],
            "U": ["U1", "U2", "U3"],
            "M": ["M1", "M2", "M3"],
            "L": ["L1", "L2", "L3"]
        }

        # Waiting list
        self.waiting_list = []

    def display_info(self):
        print(f"Train Number: {self.train_num}")
        print(f"Source: {self.source}")
        print(f"Destination: {self.destination}")
        print(f"Available Seats: {self.seats}")
        print()

    def book_tickets(self, num_tickets):
        if num_tickets > self.seats:
            return None

        pnr_list = []

        for i in range(num_tickets):
            pnr = random.randint(100000, 999999)
            pnr_list.append(pnr)

        self.seats -= num_tickets

        return pnr_list

    def allocate_berth(self):
        """
        Allocate berth in the order:
        Lower -> Middle -> Upper -> Side Lower -> Side Upper
        """

        berth_order = ["L", "M", "U", "SL", "SU"]

        for berth_type in berth_order:
            if self.berths[berth_type]:
                berth = self.berths[berth_type].pop(0)
                return berth

        return "WL"


# -------------------- PASSENGER CLASS --------------------

class Passenger:
    def __init__(self, name, age, gender, phone):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone

        self.berth = None

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Phone Number: {self.phone}")
        print(f"Berth: {self.berth}")


# -------------------- TICKET CLASS --------------------

class Ticket:
    def __init__(
        self,
        train,
        source,
        destination,
        passenger,
        pnr,
        journey_date,
        booking_time,
        travel_class
    ):
        self.train = train
        self.source = source
        self.destination = destination
        self.passenger = passenger
        self.pnr = pnr
        self.journey_date = journey_date
        self.booking_time = booking_time
        self.travel_class = travel_class

    def display_info(self):
        print("\n====================================")
        print("          RAILWAY TICKET")
        print("====================================")

        print(f"Train Number : {self.train.train_num}")
        print(f"From         : {self.source}")
        print(f"To           : {self.destination}")
        print(f"Journey Date : {self.journey_date}")
        print(f"Booking Time : {self.booking_time}")
        print(f"Class        : {self.travel_class}")
        print(f"PNR          : {self.pnr}")
        print(f"Berth        : {self.passenger.berth}")

        print("\nPassenger Details")
        self.passenger.display_info()

        print("====================================")


# -------------------- ACCOUNT CLASS --------------------

class Account:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, password):
        return self.password == password


# -------------------- ACCOUNTS --------------------

accounts = [
    Account("user1", "password1"),
    Account("user2", "password2")
]

logged_in_account = None


# -------------------- LOGIN / ACCOUNT --------------------

while True:

    print("\n1. Create an Account")
    print("2. Login")

    choice = input("Enter choice: ")

    if choice == "1":

        username = input("Enter username: ")
        password = input("Enter password: ")

        accounts.append(Account(username, password))

        print("Account created successfully!")

    elif choice == "2":

        username = input("Enter username: ")
        password = input("Enter password: ")

        for account in accounts:

            if (
                account.username == username
                and account.check_password(password)
            ):
                logged_in_account = account
                break

        if logged_in_account is None:
            print("Invalid username or password.")

        else:
            print(
                f"\nLogged in as {logged_in_account.username}"
            )
            break

    else:
        print("Invalid choice.")


# -------------------- TRAIN DETAILS --------------------

trains = [
    Train("12737", "Tadepalligudem", "Secunderabad", 40),
    Train("12728", "Tadepalligudem", "Visakhapatnam", 50),
    Train("22863", "Vijayawada", "Bangalore", 1)
]

print("\n----- AVAILABLE TRAIN DETAILS -----\n")

for train in trains:
    train.display_info()


# -------------------- GET TRAIN INPUT --------------------

while True:

    try:

        train_num = input("Enter Train Number: ")

        num_tickets = int(
            input("Enter Number of Tickets: ")
        )

        if num_tickets <= 0:
            raise ValueError(
                "Number of tickets should be greater than 0"
            )

        selected_train = None

        for train in trains:

            if train.train_num == train_num:
                selected_train = train
                break

        if selected_train is None:
            raise ValueError("Invalid Train Number.")

        break

    except ValueError as e:

        print(f"Invalid Input: {e}")


train = selected_train


# -------------------- JOURNEY DATE --------------------

while True:

    try:

        journey_date = input(
            "Enter Journey Date (DD-MM-YYYY): "
        )

        date_object = datetime.strptime(
            journey_date,
            "%d-%m-%Y"
        )

        if date_object.date() < datetime.now().date():
            raise ValueError(
                "Journey date cannot be in the past."
            )

        break

    except ValueError as e:

        print(f"Invalid Date: {e}")


# -------------------- BOOKING DATE & TIME --------------------

booking_time = datetime.now().strftime(
    "%d-%m-%Y %H:%M:%S"
)


# -------------------- CLASS SELECTION --------------------

print("\n----- SELECT TRAVEL CLASS -----")
print("1. SL  - Sleeper")
print("2. 3AC - AC 3 Tier")
print("3. 2AC - AC 2 Tier")
print("4. 1AC - AC First Class")

while True:

    class_choice = input("Enter class choice: ")

    if class_choice == "1":
        travel_class = "SL"
        break

    elif class_choice == "2":
        travel_class = "3AC"
        break

    elif class_choice == "3":
        travel_class = "2AC"
        break

    elif class_choice == "4":
        travel_class = "1AC"
        break

    else:
        print("Invalid class choice.")


# -------------------- PASSENGER DETAILS --------------------

passengers = []

for i in range(num_tickets):

    print(f"\nEnter details for Passenger {i + 1}")

    while True:

        try:

            name = input("Name: ")

            if not name:
                raise ValueError(
                    "Name cannot be empty"
                )

            age = int(input("Age: "))

            if age <= 0 or age > 120:
                raise ValueError("Invalid Age")

            gender = input("Gender: ")

            phone = input("Phone Number: ")

            if (
                not phone
                or len(phone) != 10
                or not phone.isdigit()
            ):
                raise ValueError(
                    "Invalid Phone Number"
                )

            passenger = Passenger(
                name,
                age,
                gender,
                phone
            )

            passengers.append(passenger)

            break

        except ValueError as e:

            print(f"Invalid Input: {e}")


# -------------------- SEAT / WAITING LIST --------------------

if num_tickets <= train.seats:

    pnr_list = train.book_tickets(num_tickets)

    print(
        "\n-------------- BOOKING SUCCESSFUL --------------"
    )

    for i in range(num_tickets):

        passengers[i].berth = train.allocate_berth()

        ticket = Ticket(
            train,
            train.source,
            train.destination,
            passengers[i],
            pnr_list[i],
            journey_date,
            booking_time,
            travel_class
        )

        ticket.display_info()

else:

    print(
        "\nNo sufficient confirmed seats available."
    )

    print(
        "Would you like to join the Waiting List?"
    )

    choice = input("Enter Y/N: ").upper()

    if choice == "Y":

        for passenger in passengers:

            waiting_number = len(train.waiting_list) + 1

            train.waiting_list.append(passenger)

            print(
                f"{passenger.name} added to Waiting List."
            )

            print(
                f"Waiting List Number: WL{waiting_number}"
            )

    else:

        print("Booking cancelled.")


# -------------------- WAITING LIST DISPLAY --------------------

print("\n----- WAITING LIST -----")

if len(train.waiting_list) == 0:

    print("No passengers in waiting list.")

else:

    for i, passenger in enumerate(
        train.waiting_list,
        start=1
    ):

        print(
            f"WL{i} - {passenger.name}"
        )


print("\n------- THANK YOU -------")
print("------ SAFE JOURNEY -----")