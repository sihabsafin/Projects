class Hall:
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.entry_hall()  # Automatically add this hall to Star_Cinema

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.__show_list.append(show_info)
        self.__seats[id] = [[0] * self.__cols for _ in range(self.__rows)]  # Initialize seats

    def book_seats(self, id, seats_to_book):
        if id in self.__seats:
            seat_map = self.__seats[id]
            for row, col in seats_to_book:
                if 0 <= row < self.__rows and 0 <= col < self.__cols:
                    if seat_map[row][col] == 0:
                        seat_map[row][col] = 1  # Book the seat
                    else:
                        raise ValueError(f"Seat at row {row}, col {col} is already booked.")
                else:
                    raise ValueError(f"Invalid seat at row {row}, col {col}.")
        else:
            raise ValueError(f"Show ID '{id}' not found.")

    def view_show_list(self):
        print("\nCurrent Shows:")
        for show_info in self.__show_list:
            print(f"ID: {show_info[0]}, Movie: {show_info[1]}, Time: {show_info[2]}")

    def view_available_seats(self, id):
        if id in self.__seats:
            seat_map = self.__seats[id]
            print(f"\nAvailable seats for Show ID '{id}':")
            for row in range(self.__rows):
                for col in range(self.__cols):
                    if seat_map[row][col] == 0:
                        print(f"Seat at row {row}, col {col} is available.")
        else:
            raise ValueError(f"Show ID '{id}' not found.")


class Star_Cinema(Hall):
    __hall_list = []

    def __init__(self, rows, cols, hall_no):
        super().__init__(rows, cols, hall_no)
        Star_Cinema.__hall_list.append(self)

    @classmethod
    def entry_hall(cls):
        # Append the latest hall to the hall_list
        hall = cls.__hall_list[-1]
        cls.__hall_list.append(hall)

    @classmethod
    def get_hall_list(cls):
        return cls.__hall_list


def main():
    while True:
        print("\n===== Star Cinema Management System =====")
        print("1. Add Hall")
        print("2. Add Show")
        print("3. Book Seats")
        print("4. View Show List")
        print("5. View Available Seats")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            rows = int(input("Enter number of rows for the hall: "))
            cols = int(input("Enter number of columns for the hall: "))
            hall_no = len(Star_Cinema.get_hall_list()) + 1
            Star_Cinema(rows, cols, hall_no)
            print(f"Hall {hall_no} added successfully!")

        elif choice == "2":
            hall_id = int(input("Enter Hall ID for the show: "))
            movie_name = input("Enter movie name: ")
            show_time = input("Enter show time: ")
            hall = Star_Cinema.get_hall_list()[hall_id - 1]
            hall.entry_show(f"S{len(hall._Hall__show_list) + 1}", movie_name, show_time)
            print("Show added successfully!")

        elif choice == "3":
            hall_id = int(input("Enter Hall ID for booking: "))
            show_id = input("Enter Show ID for booking: ")
            seats_to_book = []
            while True:
                seat_input = input("Enter seat (row,col) to book (e.g., 1,2) or 'done' to finish: ")
                if seat_input.lower() == "done":
                    break
                try:
                    row, col = map(int, seat_input.split(","))
                    seats_to_book.append((row, col))
                except ValueError:
                    print("Invalid input. Please try again.")
            hall = Star_Cinema.get_hall_list()[hall_id - 1]
            hall.book_seats(show_id, seats_to_book)
            print("Seats booked successfully!")

        elif choice == "4":
            hall_id = int(input("Enter Hall ID to view show list: "))
            hall = Star_Cinema.get_hall_list()[hall_id - 1]
            hall.view_show_list()

        elif choice == "5":
            hall_id = int(input("Enter Hall ID to view available seats: "))
            show_id = input("Enter Show ID: ")
            hall = Star_Cinema.get_hall_list()[hall_id - 1]
            hall.view_available_seats(show_id)

        elif choice == "6":
            print("Exiting Star Cinema Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a number between 1 and 6.")


if __name__ == "__main__":
    main()
