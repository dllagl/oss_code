#include <iostream>
#include <fstream>
#include <boost/array.hpp>
#include <boost/numeric/odeint.hpp>


using namespace std;
using namespace boost::numeric::odeint;

typedef const double cdouble;
typedef const int cint;
typedef boost::array<double,4> state_type;


#define AVOGRADRO   6.022e+23
#define SPEED_LIGHT 3.e8
#define PLANCK      6.626e-34
#define HC          (SPEED_LIGHT * PLANCK)
#define PI          3.14159




// main parameters
cdouble doping_ratio_sample = 1.;
cdouble quality_factor = 2000.;
cdouble pump_power = 10. * 1.e7;



// parameters of BSBCz
cdouble molar_mass = 689.e-3;
cdouble lambda_abs = 405.e-9;
cdouble lambda_fluo = 480.e-9;

cdouble tau_f = 1.28e-9;
cdouble tau_t = 175.e-6;

cdouble sigma_em = 2.8e-20;
cdouble sigma_triplet_pump = 0.0;

cdouble ksi = 0.9;


// parameters that depends on the sample
cdouble mol_density = 1.15e-3;
cdouble dye_density = (doping_ratio_sample * mol_density * AVOGRADRO) / molar_mass;
cdouble sigma_abs_pump = 8.5e-21;
cdouble neff = 1.7;


// photophysical interaction rates
cdouble kisc = 6.e6;
cdouble ksta = 8.e-11 * 1.e-6 * dye_density;
cdouble kssa = 0.0 * 1.e-6 * dye_density;
cdouble ktta = 0.0 * 1.e-6 * dye_density;
cdouble sigma_ta = 0.0;


// parameters of the laser device
cdouble gamma = 0.5;
cdouble nu = SPEED_LIGHT / lambda_fluo;
cdouble tau_cav = quality_factor / (2 * PI * nu);
cdouble pump_area = 4.5e-9;
cdouble spont = PLANCK*SPEED_LIGHT*SPEED_LIGHT 
                / (lambda_fluo*pow(pump_area,3./2.));




void system(const state_type &x, state_type &dxdt, double t)
{

    // S0 
    dxdt[0] = (
        (-sigma_abs_pump * lambda_abs * pump_power *x[0]/ HC)
        + ( x[1] / tau_f )
        + ( x[2] / tau_t )
        + ( ksta + x[1] * x[2] )
        + ( 1. * ktta * x[2] * x[2] )
        + ( kssa * x[1] * x[1] )
        + ( x[1] * sigma_em * x[3] * lambda_fluo / HC)
    );


    // S1
    dxdt[1] = (
        ( sigma_abs_pump * lambda_abs * pump_power * x[0] / HC )
        - ( x[1] * (1/tau_f + kisc) )
        - ( ksta * x[1] * x[2] )
        + ( 0.25 * ktta * x[2] * x[2] )
        - (kssa * x[1] * x[1] * (2-ksi) )
        - (x[1] * sigma_em * x[3] * lambda_fluo / HC )
    );


    // T1
    dxdt[2] = (
        ( x[1] * kisc )
        - ( x[2] / tau_t )
        + ( kssa * x[1] * x[1] * (1-ksi) )
        - ( 1.25 * ktta * x[2] * x[2] )
        - ( sigma_triplet_pump * lambda_abs * pump_power * x[2] / HC )
    );


    // photon density
    dxdt[3] =  (
          ( (HC/neff) * dye_density * gamma * sigma_em * x[1] * (x[3] + spont) )
        - ( (HC/neff) * dye_density * gamma * sigma_ta * x[2] * x[3] )
        - ( x[3] / tau_cav )
    );
}


void write_output(const state_type &x, const double t)
{
    const string output_path = "test.txt";
    ofstream ofile(output_path.c_str());

    ofile << t << '\t' 
          << x[0] << '\t' 
          << x[1] << '\t' 
          << x[2] << '\t' 
          << x[3] << endl;

}



int main()
{

    state_type x = {1., 0.0, 0.0, 0.0};

    return 0;
}