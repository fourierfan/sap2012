# -*- coding: utf-8 -*-


def Utilisation_factor_for_heating(
        heat_transfer_coefficient,
        total_internal_and_solar_gains,
        temperature_during_heating_living_room,
        heating_controls,
        monthly_external_temperature_table_U1,
        thermal_mass_parameter,
        heat_loss_parameter
        ):
    
    time_constant = []
    for i in range(12):
        time_constant.append(thermal_mass_parameter/
                             (3.6 * heat_loss_parameter[i]))

    a = []
    for i in range(12):
        a.append(1 + time_constant[i]/15)
        
    heat_loss_rate_living_room = []
    for i in range(12):
        heat_loss_rate_living_room.append(heat_transfer_coefficient[i] * 
                              (temperature_during_heating_living_room - monthly_external_temperature_table_U1[i]))
        
    y_living_room = []
    for i in range(12):
        if heat_loss_rate_living_room[i] == 0:
            y_living_room.append(10^6)
            
        else:
            y_living_room.append(total_internal_and_solar_gains[i] / heat_loss_rate_living_room[i])
            
            
    utilisation_factor_for_heating_living_room = []
    for i in range(12):
        if y_living_room[i] ==1:
            utilisation_factor_for_heating_living_room.append(a[i] / 
                                                  (a[i] + 1))
            
        if y_living_room[i] > 0:
            utilisation_factor_for_heating_living_room.append((1-y_living_room[i]**a[i]) / (1 - y_living_room[i]**(a[i] + 1)))
                
        else:
            utilisation_factor_for_heating_living_room.append(1)
            
            
            
            
            
            
    temperature_during_heating_rest_of_dwelling = []
    for i in range(12):
        if heating_controls == 1:
            temperature_during_heating_rest_of_dwelling.append(temperature_during_heating_living_room - 0.5 * heat_loss_parameter[i])
            
        else:
            temperature_during_heating_rest_of_dwelling.append(temperature_during_heating_living_room - (heat_loss_parameter[i] + heat_loss_parameter[i]**2 / 12))
    
    heat_loss_rate_rest_of_dwelling = []
    for i in range(12):
        heat_loss_rate_rest_of_dwelling.append(heat_transfer_coefficient[i] * 
                              (temperature_during_heating_rest_of_dwelling[i] - monthly_external_temperature_table_U1[i]))
        
    y_rest_of_dwelling = []
    for i in range(12):
        if heat_loss_rate_rest_of_dwelling[i] == 0:
            y_rest_of_dwelling.append(10^6)
            
        else:
            y_rest_of_dwelling.append(total_internal_and_solar_gains[i] / heat_loss_rate_rest_of_dwelling[i])
            
            
    utilisation_factor_for_heating_rest_of_dwelling = []
    for i in range(12):
        if y_rest_of_dwelling[i] ==1:
            utilisation_factor_for_heating_rest_of_dwelling.append(a[i] / 
                                                  (a[i] + 1))
            
        if y_rest_of_dwelling[i] > 0:
            utilisation_factor_for_heating_rest_of_dwelling.append((1-y_rest_of_dwelling[i]**a[i]) / (1 - y_rest_of_dwelling[i]**(a[i] + 1)))
                
        else:
            utilisation_factor_for_heating_rest_of_dwelling.append(1)
            
    
    
    return(
            time_constant,
            a,
            heat_loss_rate_living_room,
            y_living_room,
            utilisation_factor_for_heating_living_room,
            temperature_during_heating_rest_of_dwelling,
            heat_loss_rate_rest_of_dwelling,
            y_rest_of_dwelling,
            utilisation_factor_for_heating_rest_of_dwelling,
            
            )
            
            
            
            
            
            
            