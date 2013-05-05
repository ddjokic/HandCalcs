#!/usr/bin/env python

# calculates centifugal fan characteristics

def fan (Flow, diff_pressure, temperature, density, motor_rpm, efficiency, fan_pulley, motor_pulley, rotor_dia):
    shaft_power = Flow/3600*diff_pressure
    motor_power = shaft_power/efficiency*100
    drive_ratio = motor_pulley/fan_pulley
    fan_rpm = motor_rpm*drive_ratio
    tip_speed = 3.14*rotor_dia/1000*fan_rpm/60
    return shaft_power, motor_power, drive_ratio, fan_rpm, tip_speed

def write_table2 (fn, v1, v2):
    fn.write("\n")
    fn.write(v1)
    fn.write("\t")
    fn.write(v2)
    return

# input block
pname = raw_input ("Project name: ")
Flow = float(input("Enter Flow in cum/h: "))
diff_pressure = float(input("Enter Diff. Pressure in kPa: "))
temperature = float(input("Enter Temperature in degC: "))
density = float(input("Enter Density of air in kg/cum: "))
motor_rpm = float(input("Enter RPM of the motor: "))
efficiency = float(input("Enter efficiency of the system in '%' - usually approx. 30%: "))
fan_pulley = float(input("Enter Fan Pulley Kinematic Diameter in mm: "))
motor_pulley = float(input("Enter Motor Pulley Kinematic Diameter in mm: "))
rotor_dia = float(input("Enter Fan Rotor Diameter in mm: "))



s=fan(Flow, diff_pressure, temperature, density, motor_rpm, efficiency, fan_pulley, motor_pulley, rotor_dia)

fname = pname+".out"
fn=open(fname, 'a')
write_table2(fn, "Flow [cum/h]: ", str(round(Flow,3)))
write_table2(fn, "Diff. Pressure [kPa]: ", str(round(diff_pressure,3)))
write_table2(fn, "Temperature [degC]: ", str(round(temperature,3)))
write_table2(fn, "Density [kg/cum]: ", str(round(density,3)))
write_table2(fn, "Motor RPM: ", str(round(motor_rpm,3)))
write_table2(fn, "Efficiency [%]: ", str(round(efficiency,3)))
write_table2(fn, "Fan Pulley Kinematic Diameter [mm]: ", str(round(fan_pulley,3)))
write_table2(fn, "Motor Pulley Kinematic Diameter [mm]: ", str(round(motor_pulley,3)))
write_table2(fn, "Fan Rotor Diameter [mm]: ", str(round(rotor_dia,3)))
fn.write("\n\nCalculation Results:")
write_table2(fn, "Shaft Power [kW]: ", str(round(s[0],3)))
write_table2(fn, "Motor Power [kW]: ", str(round(s[1],3)))
write_table2(fn, "Drive Ratio [-]: ", str(round(s[2],3)))
write_table2(fn, "Fan RPM: ", str(round(s[3],3)))
write_table2(fn, "Tip Speed [m/s]: ", str(round(s[4],3)))
print("Results are written in project.out file!")