# Parking Lot Class
class ParkingLot:
    def __init__(self):
        self.levels = {
            'A': [None] * 20,
            'B': [None] * 20
        }
        self.vehicle_mapping = {}  # Vehicle number to (level, spot) mapping

    def assign_parking_space(self, vehicle_number):
        for level in ['A', 'B']:
            for spot in range(20):
                if self.levels[level][spot] is None:
                    self.levels[level][spot] = vehicle_number
                    self.vehicle_mapping[vehicle_number] = {'level': level, 'spot': spot}
                    return {'level': level, 'spot': spot}
        return 'Parking is full'

    def retrieve_parking_spot(self, vehicle_number):
        if vehicle_number in self.vehicle_mapping:
            return self.vehicle_mapping[vehicle_number]
        return 'Vehicle not found in the parking lot'

    def display_parking_lot_status(self):
        for level, spots in self.levels.items():
            print(f'Level {level}:')
            for spot, vehicle in enumerate(spots):
                if vehicle:
                    print(f'Spot {spot + 1}: {vehicle}')
                else:
                    print(f'Spot {spot + 1}: Empty')
            print()

# Main application
if __name__ == '__main__':
    parking_lot = ParkingLot()
    
    while True:
        print('Options:')
        print('1. Assign Parking Space')
        print('2. Retrieve Parking Spot')
        print('3. Exit')
        
        choice = input('Enter your choice: ')
        
        if choice == '1':
            vehicle_number = input('Enter vehicle number: ')
            result = parking_lot.assign_parking_space(vehicle_number)
            if result == 'Parking is full':
                print(result)
            else:
                print(f'Assigned Parking: {result}')
        
        elif choice == '2':
            vehicle_number = input('Enter vehicle number: ')
            result = parking_lot.retrieve_parking_spot(vehicle_number)
            print(f'Parking Spot: {result}')
        
        elif choice == '3':
            break
        
        else:
            print('Invalid option. Please choose again.')
    
    parking_lot.display_parking_lot_status()
