



import user_interface as ui
import simu_populations as spop


# terminal message when the program gets executed
ui.welcome()


# ask user which simulations to run 
user_choice = eval(input('Which simulations ? (1,2,3,4) '))

if (user_choice == 1) or (user_choice == 2)  : 
    spop.simu_fixed_params(user_choice)

elif (user_choice == 3) or (user_choice == 4) : 
    idx     = ui.choose_param()
    idx_arr = ui.choose_param_values()
    spop.simu_multiple_params(user_choice,idx,idx_arr)

else : 
    print('Error, please try again !')
    pass


