



def output_file_init_simu_pop(
    arr_mol,arr_sample,arr_rates,arr_pump,tmin,tmax,file) : 

    name_arr_mol = [
        'molar_mass',
        'lambda_abs',
        'lambda_fluo',
        'tau_f',
        'tau_t',
        'sigma_em',
        'sigma_S1S2_pump',
        'sigma_S1S2_laser',
        'sigma_T1T2_pump',
        'sigma_T1T2_laser',
        'kSI'
    ]
    unit_arr_mol = [
        'g/m3',
        'm',
        'm',
        's',
        's',
        'm2',
        'm2',
        'm2',
        'm2',
        'm2',
        ''
    ]



    name_arr_sample = [
        'doping',
        'nbr_active_mol',
        'sigma_abs_pump',
        'neff'
    ]
    unit_arr_sample = [
        '',
        'm-3',
        'm2',
        '',
    ]



    name_arr_rates = [
        'kisc',
        'ksta',
        'kssa',
        'ktta'
    ]
    unit_arr_rates = [
        's-1',
        'cm3.s-1',
        'cm3.s-1',
        'cm3.s-1',
    ]



    name_arr_pump = [
        'pump_fluence'
    ]
    unit_arr_pump = [
        'W.m-2'
    ]



    ofile = open(file,'a+')
    ofile.write('\n\n')


    ofile.write('-------------------------\n')
    ofile.write('   molecule parameters   \n\n')
    for ii in range(len(name_arr_mol)) : 
        ofile.write('%s = %.3e %s\n' 
        % (name_arr_mol[ii],arr_mol[ii],unit_arr_mol[ii]))
    ofile.write('-------------------------\n')
    ofile.write('\n\n')


    ofile.write('-------------------------\n')
    ofile.write('    sample parameters    \n\n')
    for ii in range(len(name_arr_sample)) : 
        ofile.write('%s = %.3e %s\n' 
        % (name_arr_sample[ii],arr_sample[ii],unit_arr_sample[ii]))
    ofile.write('-------------------------\n')
    ofile.write('\n\n')


    ofile.write('-------------------------\n')
    ofile.write('    rates parameters    \n\n')
    for ii in range(len(name_arr_rates)) : 
        ofile.write('%s = %.3e %s\n' 
        % (name_arr_rates[ii],arr_rates[ii],unit_arr_rates[ii]))
    ofile.write('-------------------------\n')
    ofile.write('\n\n')


    ofile.write('-------------------------\n')
    ofile.write('     pump parameters    \n\n')
    ofile.write('%s = %.3e %s\n' 
        % (name_arr_pump[0],arr_pump[0],unit_arr_pump[0]))
    ofile.write('-------------------------\n')
    ofile.write('\n\n')




    ofile.write('-------------------------\n')
    ofile.write('     time parameters    \n\n')
    ofile.write('Starting time : %.3e s\n' % tmin)
    ofile.write('Ending time   : %.3e s\n' % tmax)
    # ofile.write('Number of points : %d\n' % len(vec_time))
    ofile.write('-------------------------\n')
    ofile.write('\n\n')


    ofile.close()
    return 0