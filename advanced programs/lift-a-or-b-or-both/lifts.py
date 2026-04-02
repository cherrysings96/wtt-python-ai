#lift A,B, or both which one reaches first 
class Lift:
    def __init__(self, name, current_floor):
        self.name = name
        self.current_floor = current_floor
        self.direction = 0  # 0: idle, 1: up, -1: down

    def get_cost(self, call_floor, call_direction):
        # Calculate base distance
        distance = abs(self.current_floor - call_floor)
        
        # LOGIC: Is the lift already moving toward the call?
        is_moving_toward = (self.direction == 1 and self.current_floor <= call_floor) or \
                           (self.direction == -1 and self.current_floor >= call_floor)
        
        # If it's moving away or in the wrong direction, add a "penalty" cost
        if self.direction != 0 and (not is_moving_toward or self.direction != call_direction):
            return distance + 10  # Arbitrary penalty for being "off-course"
            
        return distance

def dispatch(lifts, call_floor, call_direction):
    # Find the lift with the lowest cost/ETA
    return min(lifts, key=lambda lift: lift.get_cost(call_floor, call_direction))

# Setup two lifts
lift_a = Lift("Lift A", current_floor=10)
lift_b = Lift("Lift B", current_floor=9)

# Scenario: Someone at Floor 5 wants to go Up (1)
winner = dispatch([lift_a, lift_b], call_floor=5, call_direction=1)
print(f"The best lift is: {winner.name}")
