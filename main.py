



import user_interface as ui
import simu_populations as spop


# terminal message when the program gets executed
ui.welcome()


# ask user which simulations to run 
user_choice = eval(input('Which simulations ? (1,) '))
if user_choice == 1 : 
    spop.simu()
else : 
    print('Error, please try again !')
    pass


