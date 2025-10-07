from mcp.server.fastmcp import FastMCP
mcp = FastMCP('search_flights')

@mcp.tool()
def search_flights(type, origin, destination, departure_date, return_date, cabin_class) -> str:
    '''"""
Search for flights based on the specified parameters.

Supports `one_way`, `round_trip`, and `multi_city` flight types.  
Dates must be provided in the `MM/DD` format.  
Origin and destination must be valid IATA airport codes (e.g., `"SFO"`).  
For `round_trip` flights, both `departure_date` and `return_date` are required.  
Do not generate or assume dates that are not explicitly provided.

Args:
    type (str): The type of flight. One of `"one_way"`, `"round_trip"`, or `"multi_city"`.
    origin (str): IATA code of the departure airport (e.g., `"SFO"`). Set origin to "JFK" if the user departs from New York.
    destination (str): IATA code of the arrival airport (e.g., `"JFK"`). Set destination to "JFK" if the user arrives in New York.
    departure_date (str): Departure date in `MM/DD` format.
    return_date (str): Return date in `MM/DD` format. Required for `round_trip` flights; ignored for `one_way` and `multi_city`.
    cabin_class (str): Cabin class for the flight (e.g., `"economy"`, `"business"`).

Returns:
    str: A message indicating either the matching flights found or an error/empty result message.
"""'''
    flights_db = [{'origin': 'SFO', 'destination': 'YYZ', 'departure_date': '10/01', 'return_date': '10/05', 'cabin_class': 'economy', 'type': 'round_trip', 'flights': [{'flight_no': 'AC123', 'departure_time': '10/01T18:00', 'arrival_time': '10/02T02:00', 'connections': 0}, {'flight_no': 'AC456', 'departure_time': '10/05T12:00', 'arrival_time': '10/05T20:00', 'connections': 0}]}, {'origin': 'SEA', 'destination': 'PHX', 'departure_date': '03/05', 'return_date': '03/07', 'cabin_class': 'economy', 'type': 'round_trip', 'flights': [{'flight_no': 'DL789', 'departure_time': '03/05T08:00', 'arrival_time': '03/05T11:00', 'connections': 0}, {'flight_no': 'DL012', 'departure_time': '03/07T14:00', 'arrival_time': '03/07T17:00', 'connections': 0}]}, {'origin': 'PHX', 'destination': 'JFK', 'departure_date': '10/07', 'return_date': '10/14', 'cabin_class': 'economy', 'type': 'round_trip', 'flights': [{'flight_no': 'AA345', 'departure_time': '10/07T15:00', 'arrival_time': '10/07T23:00', 'connections': 0}, {'flight_no': 'AA678', 'departure_time': '10/14T09:00', 'arrival_time': '10/14T17:00', 'connections': 0}]}, {'origin': 'SEA', 'destination': 'SAN', 'departure_date': '03/04', 'return_date': '03/06', 'cabin_class': 'economy', 'type': 'round_trip', 'flights': [{'flight_no': 'UA234', 'departure_time': '03/04T07:00', 'arrival_time': '03/04T10:00', 'connections': 0}, {'flight_no': 'UA567', 'departure_time': '03/06T18:00', 'arrival_time': '03/06T21:00', 'connections': 0}]}, {'origin': 'LAX', 'destination': 'SFO', 'departure_date': '03/03', 'return_date': '03/12', 'cabin_class': 'economy', 'type': 'round_trip', 'flights': [{'flight_no': 'UA234', 'departure_time': '03/03T08:00', 'arrival_time': '03/03T09:30', 'connections': 0}, {'flight_no': 'UA567', 'departure_time': '03/12T18:00', 'arrival_time': '03/12T19:30', 'connections': 0}]}]
    if type not in ['one_way', 'round_trip', 'multi_city']:
        return 'Error: Invalid flight type.'
    if not origin or not destination:
        return 'Error: Origin and destination must be provided.'
    if not departure_date:
        return 'Error: Departure date must be provided.'
    if type == 'round_trip' and (not return_date):
        return 'Error: Return date must be provided for round-trip flights.'
    matching_flights = [flight for flight in flights_db if flight['origin'] == origin and flight['destination'] == destination and (flight['departure_date'] == departure_date) and (flight['return_date'] == return_date if type == 'round_trip' else True) and (flight['cabin_class'].lower() == cabin_class.lower() if cabin_class else True)]
    if not matching_flights:
        return 'No flights found for the given parameters.'
    return 'Found the following flights: ' + '\n'.join(['Departure Flight: ' + flight['flights'][0]['flight_no'] + '; Return Flight: ' + flight['flights'][1]['flight_no'] for flight in matching_flights])
if __name__ == '__main__':
    mcp.run(transport='stdio')