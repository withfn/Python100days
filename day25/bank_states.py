import pandas as pd
    
class BankStates():
    def __init__(self):
        self.states = pd.read_csv("50_states.csv")
        self.answer_state = ''
        self.position = ()
        self.score = 0
        self.all_states = len(self.states)
        self.guessed_states = []
        self.missing_states = []

    def check_name(self):
        return self.answer_state in set(self.states['state'])
    
    def get_position(self):
        if self.check_name():
            if self.answer_state not in self.guessed_states:
                state = self.states[self.states.state == self.answer_state]
                self.position = (int(state.x), int(state.y))
                self.score += 1
                self.guessed_states.append(self.answer_state)
                return True
        else:
            return False
    
    #create a csv of missing states
    def states_to_learn(self):
        for state in self.states.state:
            if state not in self.guessed_states:
                self.missing_states.append(state)
        new_data = pd.DataFrame(self.missing_states)
        new_data.to_csv("states_to_learn.csv")