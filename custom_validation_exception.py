class InvalidDistanceError(Exception):
    def __init__(self, message):
        super().__init__(message)

def validate_distance(distance):
    if distance <=0:
        raise InvalidDistanceError("Distance must be greater than 0")
    if distance > 1000:
        raise InvalidDistanceError("Distance must not exceed 1000")
    return "Valid distance"

if __name__ == "__main__":
    distances = [10,-2,4,2500]
    for distance in distances:
        try:
            print(f" {distance} -> {validate_distance(distance)}")
        except InvalidDistanceError as e:
            print(f"{distance} -> Error: {e}")