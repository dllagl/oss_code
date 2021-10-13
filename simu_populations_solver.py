



def solver(method,sys,initial_pop,time_vec,doping,pump_fluence,
    sample_arr,molecule_arr,rates_arr,output_file) :



    # integrating the ODE system with odeint
    sol = method(sys,initial_pop,time_vec, args=(doping, pump_fluence,
        sample_arr,molecule_arr,rates_arr)
        )



    # write data on output txt file 
    ofile = open(output_file,'a+')
    for ii in range(len(sol)) :
        ofile.write('%.3e\t%.3e\t%.3e\t%.3e\n' 
        % (time_vec[ii],sol[ii,0],sol[ii,1],sol[ii,2]))
    ofile.close()

    return 0