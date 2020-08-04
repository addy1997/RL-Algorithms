#!/usr/bin/env python
# coding: utf-8

# In[15]:


import random

class Sarsa:
    
    def __init__(self, action, gamma=0.642, alpha=0.124):
        
        self.action = action
        self.alpha  = alpha
        self.gamma  = gamma
        self.terminal_state = s_term
        
    def Calculate_Q_values(self, state, action):
        """
        This function estimates the value for the action value function
        """
        self.Qvalue = Q(state, action)
        
        #condition for terminal state Q(s,a) = 0.0
        
        if (state==s_term):
            
            return 0.0
        else:
            return Q_value
        
    def action_selection(self, epsilon=0.9):
        
        """
        this function select action for a particular state
        """
        #the probability condition 
        if random.random() < 0.9:
            
            action = random.choice(self.action)
        else:
        #selecting the action that maximizes the Q_value
        
            Q_values = [self.Calculate_Q_values(state, action) for action in self.action]
            
            #find the max Q value
            Q_max = max(Q_values)
            
            #estimate the count of Q values where it is max
            count_Q_max = Q_values.count(Q_max)
            
            #condition for identical Q_max values for many actions
            if (count_Q_max > 1):
                
                for i in range(len(self.action)):
                    #track the indices of the 
                    if Q_values[i] == Q_max:
                        
                        best_action_idxs = i
                        
                        action_idx = random.choice(best_action_idxs)
                    else:
                        
                        action_idx = Q_values.index(Q_max)
                
                        return self.action[best_action_idx], self.action[action_idx]
                
                
    def update(self, state, action, reward, s_next):
        """
        this function updates the Qvalue
        """
        Q_prime = self.Calculate_Q_values(state=s_next
                , action=self.select_greedy_action(s_next))
        
        
        Q_current = self.Q_value((state, action), None)
        
        if Q_current:
            self.Q_value[(state, action)] = self.reward
        else:
            self.Q_value[(state, action)] = Q_current + (self.alpha*(self.reward + self.gamma*Q_prime-Q_current))
               


# In[ ]:




