from silver_service_taxi import SilverServiceTaxi

def main():
    taxi = SilverServiceTaxi("Test taxi", 100, 2)
    taxi.drive(18)

    print(f"Total fare is: {taxi.get_fare():.2f}")

    # get a result rounded
    assert round(taxi.get_fare(), 1) == 48.80, "Calculation is not correct"

main()