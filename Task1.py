our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

common_destinations = our_routes.intersection(competitor_routes)
print("Destinations both airlines fly to:", common_destinations)

unique_our_routes = our_routes.difference(competitor_routes)
print("Destinations unique to our airline:", unique_our_routes)

unique_routes = our_routes.symmetric_difference(competitor_routes)
print("Destinations neither airline shares:", unique_routes)
