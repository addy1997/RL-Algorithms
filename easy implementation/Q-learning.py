import random

class Q_learning:
    def __init__(self,alpha, gamma, action):
        
        #parameter
        self.action = action
        self.alpha = alpha
        self.gamma = gamma
        
        self.s_terminal = s_
        
        
    def Calculate_Q_value(self, state, action):
        
        self.Qvalue = Q(self.state,self.action)
        
        if (self.state==s_):
            
            return 0.0 #condition if the terminal state is encountered 
        
        else:
            
            return Qvalue
        
    def act(self, epsilon=0.9):
        #condition for choosing the random action
        if random.random() < epsilon:
            action = random.choice(self.action)
        else:
        #condition for greedy action selection   
            action = self.select_greedy_action(self.state)
            return action
        
    def update(self, state, action, reward, s_next):
        
        Q_prime = self.Calculate_Q_values(state=s_next
                , action=self.select_greedy_action(s_next))
        
        
        Q_current = self.Q_value((state, action), None)
        
        if Q_current:
            self.Q_value[(state, action)] = self.reward
        else:
            self.Q_value[(state, action)] = Q_current + (self.alpha*(self.reward + self.gamma*Q_prime-Q_current))
        
        
        
    def select_greedy_action(self, state):
        
        #calculate all Q-values for all the state and action pairs
        Q_values = [self.Calculate_Q_value(state, action) for action in self.action]
        
        Q_max = max(Q_values)
        
        count_Q_max = count = Q_values.count(Q_max)
        
        if count_Q_max > 1:
            
            #all the actions which maximise the Q value
            
            best_action_idxs = [i for i in range(len(self.action)) if Q_values[i] == Q_max]
            action_idx = random.choice(best_action_idxs)
        else:
            action_idx = Q_values.index(Q_max)
            
            return self.action[action_idx]
