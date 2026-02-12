"""
PRAGYAN-NETRA - Path Guidance Module
Navigation and route planning
"""

class PathGuide:
    def __init__(self):
        self.current_path = []
        self.obstacles = []
        
    def plan_path(self, start, destination, obstacles=[]):
        """Plan a safe path avoiding obstacles"""
        self.obstacles = obstacles
        
        # Simplified path planning
        # In real implementation, use A* or Dijkstra algorithm
        path = [start]
        
        if not obstacles:
            path.append("STRAIGHT_FOR_10M")
        elif "LEFT" in [o['position'] for o in obstacles]:
            path.append("TURN_RIGHT")
            path.append("STRAIGHT_FOR_5M")
        elif "RIGHT" in [o['position'] for o in obstacles]:
            path.append("TURN_LEFT")
            path.append("STRAIGHT_FOR_5M")
        else:
            path.append("PROCEED_WITH_CAUTION")
        
        path.append(destination)
        self.current_path = path
        return path
    
    def get_next_instruction(self):
        """Get next navigation instruction"""
        if self.current_path:
            return self.current_path.pop(0)
        return "DESTINATION_REACHED"
    
    def calculate_safety_score(self, obstacles):
        """Calculate how safe the current path is"""
        if not obstacles:
            return 100
        
        close_obstacles = sum(1 for o in obstacles if o.get('distance') in ['CLOSE', 'VERY_CLOSE'])
        score = 100 - (close_obstacles * 20)
        
        return max(0, score)