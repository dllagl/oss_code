



import user_interface as ui
import user_choice as uc
import simu_populations as spop

# terminal message when the program gets executed
ui.welcome()


# ask user which system to work on 
ui.print_available_systems()
user_sys_choice = eval(input('Which system (1,2,3,4) ? '))



# simulations without lasing 
if (user_sys_choice==1) or (user_sys_choice==2) :

    print(
'''
1) one simulation with one set of parameters (to be customed in imp_param.py)
2) n simulations for n values of one parameter (ex : kisc = 1e6, 1e7, 1e8)
'''
)

    user_simu_choice = eval(input('Which simulation (1,2) ? '))

    # one simulation with one set of parameters from imp_param.py
    if user_simu_choice == 1 : 
        spop.simu_fixed_params(user_sys_choice)

    # simulations for several values of one parameter chosen by the user
    elif user_simu_choice == 2 : 
        idx     = uc.choose_param()
        idx_arr = uc.choose_param_values()
        spop.simu_multiple_params(user_sys_choice,idx,idx_arr)

    # error handling
    else : 
        print('Corresponding simulations not available. Please restart.')

# lasing simulations (to do)
if (user_sys_choice==3) or (user_sys_choice==4) :
    print('Currently in development, try later !')

