
def Tax(state, gross):

    state_tax = {'NY':0.05, 'IL':0.15}

    if state in state_tax:
        net = gross-state_tax[state]*gross-10/100*gross
        print ("Income for %s is" %state + str(net) )

    #elif state == 'IL':
        #net = gross-15/100*gross - 10/100*gross
       # print ("Income for IL is" +str(net))

    else:
        print("No inc")





Tax("NY", 1000)




