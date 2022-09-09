import pandas as pd
    
class BankStates():
    def __init__(self):
        self.states = pd.read_csv("50_states.csv")
        self.answer_state = ''


    def check_name(self):
        return self.answer_state in set(self.states['state'])
        
    def get_position(self):
        if self.check_name():
            state = self.states[self.states.state == self.answer_state].values.tolist()
            x_pos = state[0][1]
            y_pos = state[0][2]
            return (x_pos, y_pos)

teste = BankStates()

x = teste.get_position("Ohio")
print(x)


