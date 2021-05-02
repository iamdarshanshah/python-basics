"""
Three class -
    - Event (startTime, endTime, venue)
    - Venue (name, address)
    - Address (street, city, state, country)
"""
import datetime


class Event:
    def __init__(self, name, startTime, endTime):
        self.name = name
        self.startTime = startTime
        self.endTime = endTime
        self.venue = []

    def addVenue(self, venue):
        self.venue.append(venue)


class Venue:
    def __init__(self, name):
        self.name = name
        self.address = ""

    def addAddress(self, address):
        self.address = address


class Address:
    def __init__(self, street, city, state, country, zipcode):
        self.street = street
        self.city = city
        self.state = state
        self.country = country
        self.zipcode = zipcode


event = Event("Pushpa Movie Premire", datetime.datetime(2021, 5, 23, 12, 0, 0, 0),
              datetime.datetime(2021, 5, 23, 15, 0, 0, 20))

venue = Venue("PVR Cinemas")

address = Address("Race course road", "Indore", "M.P.", "India", 452001)

venue2 = Venue("Velocity Cinemas")

address2 = Address("MR-10 raod", "Indore", "M.P.", "India", 452001)

venue.addAddress(address)

venue2.addAddress(address2)

event.addVenue(venue)

event.addVenue(venue2)

for eachVenue in event.venue:
    print("Event Name :: {}, start :: {} end :: {}".format(event.name, event.startTime, event.endTime))
    print("Venue Name :: {} - Address :: {}".format(eachVenue.name,
                                                    {"street": eachVenue.address.street, "city": eachVenue.address.city,
                                                     "state": eachVenue.address.state,
                                                     "country": eachVenue.address.country,
                                                     "zipcode": eachVenue.address.zipcode}))
