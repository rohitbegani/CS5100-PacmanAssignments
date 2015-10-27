    #           S is the set of all states 
           #           A is the set of all actions 
           #           P is state transition function specifying P(s'|s,a) 
           #           R is a reward function R(s,a,s') 
           #           θ a threshold, θ>0 
           # Output
           #           π[S] approximately optimal policy 
           #          V[S] value function 
           # Local
           #           real array Vk[S] is a sequence of value functions 
           #           action array π[S] 
           # assign V0[S] arbitrarily 
           # k ←0 
           # repeat
           #           k ←k+1 
           #           for each state s do 
           #                     Vk[s] = maxa ∑s' P(s'|s,a) (R(s,a,s')+ γVk-1[s']) 
           # until ∀s |Vk[s]-Vk-1[s]| < θ 
           # for each state s do  
           #           π[s] = argmaxa ∑s' P(s'|s,a) (R(s,a,s')+ γVk[s']) 
           # return π,Vk