


# molecule name/unit array
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


# sample name/unit array
name_arr_sample = [
    'doping',
    'sigma_abs_pump',
    'neff',
    'nbr_active_mol'
]
unit_arr_sample = [
    '',
    'm2',
    '',
    'm-3',
]


# rates name/unit array
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


# resonator name/unit array
name_arr_struct = [
    'gamma',
    'Q-factor',
    'nu_lasing',
    'tau_cav',
    'pump_area',
    'spont'
]
unit_arr_struct = [
    '',
    '',
    's-1',
    's',
    'm2',
    'W/m2'
]


# pump name/unit array
name_arr_pump = [
    'pump_fluence'
]
unit_arr_pump = [
    'W.m-2'
]









# config file for populations and laser simulations
def output_file_init_simu_laser(arr_global,arr_pump,tmin,tmax,file,bool_laser) : 

    # extract different parameters arrays from arr_global
    arr_sample = arr_global[0:4]
    arr_mol    = arr_global[4:15] 
    arr_rates  = arr_global[15:19] 
    if bool_laser : arr_struct = arr_global[19:25] 

    ofile = open(file,'a+')

    # write on file each parameter of an array
    def write_params(title,name_arr,arr,unit_arr) : 
        
        ofile.write(f'@{title}\n')
        ofile.write('-------------------------\n')

        if len(arr) > 1 : 
            for ii in range(len(name_arr)) : 
                ofile.write('%s = %.3e %s\n' 
                % (name_arr[ii],arr[ii],unit_arr[ii]))
        
        # Exception handling (ex: arr_pump)
        else : 
            ofile.write('%s = %.3e %s\n' 
                % (name_arr[0],arr[0],unit_arr[0]))

        ofile.write('-------------------------\n')
        ofile.write('\n\n')

        return 0

    # write user's computer informations
    def write_user_infos() : 

        # print current day and time 
        from datetime import datetime
        ofile.write('@date : %s\n\n' % datetime.now())

        # print computer's infos
        import platform
        uname = platform.uname()
        ofile.write('@System: %s\n' % uname.system)
        ofile.write('@Computer name: %s\n' % uname.node)
        ofile.write('@Release: %s\n' % uname.release)
        ofile.write('@Version: %s\n' % uname.version)
        ofile.write('@Machine: %s\n' % uname.machine)
        ofile.write('@Processor: %s\n' % uname.processor)

        return 0



    ofile.write('\n\n')

    write_user_infos()

    ofile.write('\n\n')

    write_params('molecule parameters',name_arr_mol,arr_mol,unit_arr_mol)
    write_params('sample parameters',name_arr_sample,arr_sample,unit_arr_sample)
    write_params('rates parameters',name_arr_rates,arr_rates,unit_arr_rates)
    if bool_laser : write_params('cavity parameters',name_arr_struct,arr_struct,unit_arr_struct)
    write_params('pump parameters',name_arr_pump,arr_pump,unit_arr_pump)




    ofile.write('@time parameters\n')
    ofile.write('-------------------------\n')
    ofile.write('Starting time : %.3e s\n' % tmin)
    ofile.write('Ending time   : %.3e s\n' % tmax)
    ofile.write('-------------------------\n')
    ofile.write('\n\n')


    ofile.close()
    return 0

