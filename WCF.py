from search import Problem, breadth_first_search


class WolfGoatCabbage(Problem):
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal
        
    def actions(self, state):
        actions = []
        if 'F' in state:
            # Farmer is on the left bank
            for objects in [['F'], ['F', 'G'], ['F', 'W'], ['F', 'C']]:
                # Check if the action is valid
                if all(object in state for object in objects):
                    actions.append(set(objects))
        else:
            # Farmer is on the right bank
            for objects in [['F'], ['F', 'G'], ['F', 'W'], ['F', 'C']]:
                # Check if the action is valid
                if all(object not in state for object in objects):
                    actions.append(set(objects))
        return actions
    
    def result(self, state, action):
        new_state = set(state)
        for object in action:
            if object in state:
                # Object is moving from left to right
                new_state.remove(object)
            else:
                # Object is moving from right to left
                new_state.add(object)
        return frozenset(new_state)
    
    def goal_test(self, state):
        return state == self.goal


def main():
    initial_state = frozenset(['F', 'G', 'W', 'C'])
    goal_state = frozenset(['G', 'W', 'C'])

    problem = WolfGoatCabbage(initial_state, goal_state)
    solution = breadth_first_search(problem)

    for state in solution.path():
        print(state.action)


if __name__ == '__main__':
    main()
