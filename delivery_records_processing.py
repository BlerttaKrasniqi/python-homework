deliveries = [
    {"delivery_id":1, "distance":12, "status":"completed"},
    {"delivery_id":2, "distance":-3, "status":"completed"},
    {"delivery_id":3, "distance":-8, "status":"pending"},
    {"delivery_id":4, "distance":20, "status":"completed"}
]

def get_valid_deliveries(deliveries):
    
    return [delivery for delivery in deliveries if delivery["distance"] > 0 and delivery["status"] == "completed"]

if __name__ == "__main__":
    print("Valid deliveries: ")
    res = get_valid_deliveries(deliveries)
    for d in res:
        print(
            f"Delivery ID: {d['delivery_id']} - "
            f"Distance: {d['distance']} - "
            f"Status: {d['status']}"
        )