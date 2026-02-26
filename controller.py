def event_registration(capacity, registrations):
    if registrations > capacity:
        waitlist = registrations - capacity
        confirmed = capacity
        status = "Closed"
    else:
        confirmed = registrations
        waitlist = 0
        status = "Open"

    print("Confirmed Registrations:", confirmed)
    print("Waitlisted Users:", waitlist)
    print("Registration Status:", status)