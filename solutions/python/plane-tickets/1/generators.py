"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    letters = "ABCD"  
    for num in range(number):
        yield letters[num % 4]
        
def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    seat_letters = generate_seat_letters(number)
    row = 1
    seats_in_row = 0
    for letter in seat_letters:
        if row == 13:
            row += 1
        yield str(row) + letter  
        seats_in_row += 1
        if seats_in_row == 4: 
            seats_in_row = 0
            row += 1

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    new_dict = {}
    seat_generator = generate_seats(len(passengers) * 4) 
    for passenger in passengers:
        new_dict[passenger] = next(seat_generator) 
    return new_dict

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    for seat_number in seat_numbers:
        base_code = seat_number + flight_id
        padding_length = 12 - len(base_code)
        if padding_length < 0:
            raise ValueError("Combined seat number and flight ID exceeds 12 characters.")
        ticket_code = base_code + "0" * padding_length
        yield ticket_code
