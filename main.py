



import user_interface as ui
import user_choice as uc
import simu_populations as spop
import simu_laser as slas
import plot_fct as pl


# terminal message when the program gets executed
ui.welcome()


# ask user which system to work on 
ui.print_available_systems()
user_sys_choice = eval(input('Which system (1,2,3,4) ? '))






# simulations without lasing 
if (user_sys_choice==1) or (user_sys_choice==2) :

    # choice of the simulation to run (single or multiple set of parameters)
    user_simu_choice = uc.user_type_choice()

    # one simulation with one set of parameters from imp_param.py
    if user_simu_choice == 1 : 

        data_file = spop.simu_fixed_params(user_sys_choice)
        if (uc.ask_plot() == 'y') :  pl.main_plot_fixed_params(user_sys_choice,data_file)

    # simulations for several values of one parameter chosen by the user
    elif user_simu_choice == 2 : 

        idx     = uc.choose_param_populations()
        idx_arr = uc.choose_param_values()
        name,nbr = spop.simu_multiple_params(user_sys_choice,idx,idx_arr)
        if (uc.ask_plot() == 'y') :  pl.main_plot_multiple_params(user_sys_choice,name,nbr)

    # error handling
    else : 
        print('Corresponding simulations not available. Please restart.')









# lasing simulations (to do)
if (user_sys_choice==3) or (user_sys_choice==4) :

    # choice of the simulation to run (single or multiple set of parameters)
    user_simu_choice = uc.user_type_choice()

    # one simulation with one set of parameters from imp_param.py
    if user_simu_choice == 1 : 
        data_file = slas.simu_fixed_params(user_sys_choice)
        if (uc.ask_plot() == 'y') :  pl.main_plot_fixed_params(user_sys_choice,data_file)

    # simulations for several values of one parameter chosen by the user
    elif user_simu_choice == 2 : 
        idx     = uc.choose_param_laser()
        idx_arr = uc.choose_param_values()
        name, nbr = slas.simu_multiple_params(user_sys_choice,idx,idx_arr)
        if (uc.ask_plot() == 'y') :  pl.main_plot_multiple_params(user_sys_choice,name,nbr)

    # error handling
    else : 
        print('Corresponding simulations not available. Please restart.')

