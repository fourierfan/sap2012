# -*- coding: utf-8 -*-

from . import overall_dwelling_dimensions
from . import ventilation_rates
from . import heat_losses_and_heat_loss_parameter
from . import Water_Heating_Energy_Requirement
from . import Internal_Gains
from . import Solar_gains
from . import Mean_Internal_Temperature
from . import Space_Heating_Requirement
from . import Energy_Requirements
from . import Fuel_Costs
from . import SAP_Rating
from . import CO2_emissions



def calcs(
        
        # overall_dwelling_dimensions inputs
        area,
        average_storey_height,
        
        # ventilation_rates inputs
        number_of_chimneys_main_heating,
        number_of_chimneys_secondary_heating,
        number_of_chimneys_other,
        number_of_open_flues_main_heating,
        number_of_open_flues_secondary_heating,
        number_of_open_flues_other,
        number_of_intermittant_fans_total,
        number_of_passive_vents_total,
        number_of_flueless_gas_fires_total,
        #### note that 'dwelling_volume' isn't needed as an input here because it is calculated in 'overall_dwelling_dimenstions' #### Please delete this line once read
        air_permeability_value_q50,
        number_of_storeys_in_the_dwelling,
        structural_infiltration,
        suspended_wooden_ground_floor_infiltration,
        no_draft_lobby_infiltration,
        percentage_of_windows_and_doors_draught_proofed,
        number_of_sides_on_which_dwelling_is_sheltered,
        monthly_average_wind_speed,
        applicable_case,
        mechanical_ventilation_air_change_rate_through_system,
        exhaust_air_heat_pump_using_Appendix_N,
        mechanical_ventilation_throughput_factor,
        efficiency_allowing_for_in_use_factor,
        
        # heat_losses_and_heat_loss_parameter inputs
        solid_door_net_area,
        solid_door_u_value,
        semi_glazed_door_net_area,
        semi_glazed_door_u_value,
        window_net_area,
        window_u_value,
        roof_window_net_area,
        roof_window_u_value,
        basement_floor_net_area,
        basement_floor_u_value,
        basement_floor_heat_capacity,
        ground_floor_net_area,
        ground_floor_u_value,
        ground_floor_heat_capacity,
        exposed_floor_net_area,
        exposed_floor_u_value,
        exposed_floor_heat_capacity,
        basement_wall_gross_area,
        basement_wall_opening,
        basement_wall_u_value,
        basement_wall_heat_capacity,
        external_wall_gross_area,
        external_wall_opening,
        external_wall_u_value,
        external_wall_heat_capacity,
        roof_gross_area,
        roof_opening,
        roof_u_value,
        roof_heat_capacity,
        party_wall_net_area,
        party_wall_u_value,
        party_wall_heat_capacity,
        party_floor_net_area,
        party_floor_heat_capacity,
        party_ceiling_net_area,
        party_ceiling_heat_capacity,
        internal_wall_net_area,
        internal_wall_heat_capacity,
        internal_floor_net_area,
        internal_floor_heat_capacity,
        internal_ceiling_net_area,
        internal_ceiling_heat_capacity,
        thermal_bridges_appendix_k,
        
        #water heating requirement inputs
        assumed_occupancy,
        V_dm_table_1c,
        days_in_month,
        T_table_1d,
        water_storage_loss_manufacturer,
        temperature_factor_table_2b,
        storage_volume_litres,
        hot_water_storage_loss_table_2,
        volume_factor_table_2a,
        Vs_appendix_G3,
        solar_storage_WWHRS_factor,
        primary_circuit_loss_table_3,
        combi_loss_table_3,
        solar_DHW_input_appendix_G,
        
        #internal gains inputs
        metabolic_gains,
        lighting_gains,
        appliances_gains,
        cooking_gains,
        pumps_and_fans_gains,
        losses,
        water_heating_gains,
        
        #solar gains inputs
        access_factor_table_6d_north,
        access_factor_table_6d_north_east,
        access_factor_table_6d_east,
        access_factor_table_6d_south_east,
        access_factor_table_6d_south,
        access_factor_table_6d_south_west,
        access_factor_table_6d_west,
        access_factor_table_6d_north_west,
        access_factor_table_6d_roof_windows,
        area_north,
        area_north_east,
        area_east,
        area_south_east,
        area_south,
        area_south_west,
        area_west,
        area_north_west,
        area_roof_windows,
        solar_flux_north,
        solar_flux_north_east,
        solar_flux_east,
        solar_flux_south_east,
        solar_flux_south,
        solar_flux_south_west,
        solar_flux_west,
        solar_flux_north_west,
        solar_flux_roof_windows,
        g_table_6b_north,
        g_table_6b_north_east,
        g_table_6b_east,
        g_table_6b_south_east,
        g_table_6b_south,
        g_table_6b_south_west,
        g_table_6b_west,
        g_table_6b_north_west,
        g_table_6b_roof_windows,
        FF_table_6b_north,
        FF_table_6b_north_east,
        FF_table_6b_east,
        FF_table_6b_south_east,
        FF_table_6b_south,
        FF_table_6b_south_west,
        FF_table_6b_west,
        FF_table_6b_north_west,
        FF_table_6b_roof_windows,
        
        #mean internal temperature inputs
        temperature_during_heating_periods_living_room,
        utilisation_factor_for_gains_living_room_table_9a,
        mean_internal_temperature_living_room_T1_Table_9c,
        temperature_during_heating_periods_rest_of_dwelling,
        utilisation_factor_for_gains_rest_of_dwelling_table_9a,
        mean_internal_temperature_rest_of_dwelling_T2_table_9c,
        living_room_area,
        temperature_adjustment_table_4e,
        
        #space heating requirement inputs
        utilisation_factor_for_gains_table_9a,
        total_gains_internal_and_solar,
        monthly_external_temperature_table_U1,
        mean_internal_temperature_whole_dwelling,
        
        #energy requirements inputs
        fraction_of_space_heat_secondary_system,
        fraction_of_space_heat_from_main_system_2,
        efficiency_of_main_space_heating_system_1,
        efficiency_of_main_space_heating_system_2,
        efficiency_of_secondary_space_heating_system,
        cooling_system_energy_efficiency_ratio_table_10c,
        efficiency_of_water_heater_table_4a,
        space_cooling_requirement_monthly,
        electricity_demand_mechanical_ventilation_fans_table_4f,
        electricity_demand_warm_air_heating_systems_fans_table_4f,
        electricity_demand_central_heating_pump_or_water_pump_table_4f,
        electricity_demand_oil_boiler_pump_table_4f,
        electricity_demand_boiler_flue_fan_table_4f,
        electricity_demand_keep_hot_facility_gas_combi_boiler_table_4f,
        electricity_demand_pump_for_solar_water_heating_table_4f,
        electricity_demand_pump_for_storage_WWHRS_Table_G3,
        electricity_for_lighting,
        electricity_generated_by_PV_Appendix_M,
        electricity_generated_by_wind_turbine_appendix_M,
        electricity_used_or_generated_by_micro_CHP_appendix_N,
        electricity_generated_by_hydro_electric_generator_appendix_M,
        appendix_Q_energy_saved,
        appendix_Q_energy_used,
        
        #fuel cost inputs
        space_heating_fuel_price_main_system_1,
        space_heating_fuel_price_main_system_2,
        space_heating_fuel_price_secondary,
        water_heating_high_rate_fraction_table_13,
        water_heating_low_rate_fraction_table_13,
        high_rate_fuel_price,
        low_rate_fuel_price,
        water_heating_fuel_price_other,
        space_cooling_fuel_used,
        space_cooling_fuel_price,
        electricity_for_pumps_fans_electric_keep_hot,
        fuel_price_for_pumps_fans_electric_keep_hot,
        fuel_price_for_lighting,
        additional_standing_charges_table_12,
        energy_saving_generation_technologies,
        energy_saving_generation_technologies_fuel_price,
        appendix_Q_energy_used_fuel_price,
        appendix_Q_energy_saved_fuel_price,
        
        #Sap rating inputs
        energy_cost_deflator,
        
        #CO2 emissions inputs
        space_heating_fuel_emission_factor_main_system_1,
        space_heating_fuel_emission_factor_main_system_2,
        space_heating_fuel_emission_factor_secondary,
        water_heating_fuel_emission_factor,
        space_cooling_fuel_emission_factor,
        fuel_emission_factor_for_pumps_fans_electric_keep_hot,
        fuel_emission_factor_for_lighting,
        energy_saving_generation_technologies_fuel_emission_factor,
        appendix_Q_energy_used_fuel_emission_factor,
        appendix_Q_energy_saved_fuel_emission_factor
        ):
    
    """This method runs the complete set of calculations for SAP2012
    
    """
    
    # overall_dwelling_dimensions calculations
    result=overall_dwelling_dimensions(
        area,
        average_storey_height)
    
    volume,total_floor_area,dwelling_volume=result
    
    
    # ventilation_rates calculations
    result=ventilation_rates(
        number_of_chimneys_main_heating,
        number_of_chimneys_secondary_heating,
        number_of_chimneys_other,
        number_of_open_flues_main_heating,
        number_of_open_flues_secondary_heating,
        number_of_open_flues_other,
        number_of_intermittant_fans_total,
        number_of_passive_vents_total,
        number_of_flueless_gas_fires_total,
        dwelling_volume,
        air_permeability_value_q50,
        number_of_storeys_in_the_dwelling,
        structural_infiltration,
        suspended_wooden_ground_floor_infiltration,
        no_draft_lobby_infiltration,
        percentage_of_windows_and_doors_draught_proofed,
        number_of_sides_on_which_dwelling_is_sheltered,
        monthly_average_wind_speed,
        applicable_case,
        mechanical_ventilation_air_change_rate_through_system,
        exhaust_air_heat_pump_using_Appendix_N,
        mechanical_ventilation_throughput_factor,
        efficiency_allowing_for_in_use_factor
        )
    
    (number_of_chimneys_total,
        number_of_chimneys_m3_per_hour,
        number_of_open_flues_total,
        number_of_open_flues_m3_per_hour,
        number_of_intermittant_fans_m3_per_hour,
        number_of_passive_vents_m3_per_hour,
        number_of_flueless_gas_fires_m3_per_hour,
        infiltration_due_to_chimneys_flues_fans_PSVs,
        additional_infiltration,
        window_infiltration,
        infiltration_rate,
        infiltration_rate2,
        shelter_factor,
        infiltration_rate_incorporating_shelter_factor,
        wind_factor,
        adjusted_infiltration_rate_allowing_for_shelter_and_wind_speed,
        exhaust_air_heat_pump_air_change_rate_through_system,
        effective_air_change_rate) = result
    
     
    # heat_losses_and_heat_loss_parameter calculations
    result=heat_losses_and_heat_loss_parameter(
        solid_door_net_area,
        solid_door_u_value,
        semi_glazed_door_net_area,
        semi_glazed_door_u_value,
        window_net_area,
        window_u_value,
        roof_window_net_area,
        roof_window_u_value,
        basement_floor_net_area,
        basement_floor_u_value,
        basement_floor_heat_capacity,
        ground_floor_net_area,
        ground_floor_u_value,
        ground_floor_heat_capacity,
        exposed_floor_net_area,
        exposed_floor_u_value,
        exposed_floor_heat_capacity,
        basement_wall_gross_area,
        basement_wall_opening,
        basement_wall_u_value,
        basement_wall_heat_capacity,
        external_wall_gross_area,
        external_wall_opening,
        external_wall_u_value,
        external_wall_heat_capacity,
        roof_gross_area,
        roof_opening,
        roof_u_value,
        roof_heat_capacity,
        party_wall_net_area,
        party_wall_u_value,
        party_wall_heat_capacity,
        party_floor_net_area,
        party_floor_heat_capacity,
        party_ceiling_net_area,
        party_ceiling_heat_capacity,
        internal_wall_net_area,
        internal_wall_heat_capacity,
        internal_floor_net_area,
        internal_floor_heat_capacity,
        internal_ceiling_net_area,
        internal_ceiling_heat_capacity,
        total_floor_area,
        thermal_bridges_appendix_k,
        effective_air_change_rate,
        dwelling_volume
        )     
    
    (solid_floor_UA,
        semi_glazed_door_UA,
        window_UA,
        roof_window_UA,
        basement_floor_UA,
        basement_floor_Ak,
        ground_floor_UA,
        ground_floor_Ak,
        exposed_floor_UA,
        exposed_floor_Ak,
        basement_wall_net_area,
        basement_wall_UA,
        basement_wall_Ak,
        external_wall_net_area,
        external_wall_UA,
        external_wall_Ak,
        roof_net_area,
        roof_UA,
        roof_Ak,
        total_area_of_external_elements,
        party_wall_UA,
        party_wall_Ak,
        party_floor_Ak,
        party_ceiling_Ak,
        internal_wall_Ak,
        internal_floor_Ak,
        internal_ceiling_Ak,
        fabric_heat_loss,
        heat_capacity,
        thermal_mass_parameter,
        thermal_bridges,
        total_fabric_heat_loss,
        ventilation_heat_loss_calculated_monthly,
        heat_transfer_coefficient,
        average_heat_transfer_coefficient,
        heat_loss_parameter,
        average_heat_loss_parameter) = result
     
     
     
    # Water heating requirement calculations 
    result = Water_Heating_Energy_Requirement(
        assumed_occupancy,
        V_dm_table_1c,
        days_in_month,
        T_table_1d,
        water_storage_loss_manufacturer,
        temperature_factor_table_2b,
        storage_volume_litres,
        hot_water_storage_loss_table_2,
        volume_factor_table_2a,
        Vs_appendix_G3,
        solar_storage_WWHRS_factor,
        primary_circuit_loss_table_3,
        combi_loss_table_3,
        solar_DHW_input_appendix_G
        )
    
    (annual_hot_water_usage_litres_per_day,
         hot_water_usage_in_litres_per_day_monthly,
         energy_content_of_water_used,
         distribution_loss,
         energy_lost_from_water_storage,
         water_storage_loss_monthly,
         total_heat_required_for_water_heating,
         output_from_water_heater_monthly,
         heat_gains_from_water_heating_monthly) = result
     
    #Internal gains inputs
    result = Internal_Gains(
        metabolic_gains,
        lighting_gains,
        appliances_gains,
        cooking_gains,
        pumps_and_fans_gains,
        losses,
        water_heating_gains
        )
    
    (total_internal_gains) = result
    
    # Solar gains calculations
    
    result = Solar_gains(
        access_factor_table_6d_north,
        access_factor_table_6d_north_east,
        access_factor_table_6d_east,
        access_factor_table_6d_south_east,
        access_factor_table_6d_south,
        access_factor_table_6d_south_west,
        access_factor_table_6d_west,
        access_factor_table_6d_north_west,
        access_factor_table_6d_roof_windows,
        area_north,
        area_north_east,
        area_east,
        area_south_east,
        area_south,
        area_south_west,
        area_west,
        area_north_west,
        area_roof_windows,
        solar_flux_north,
        solar_flux_north_east,
        solar_flux_east,
        solar_flux_south_east,
        solar_flux_south,
        solar_flux_south_west,
        solar_flux_west,
        solar_flux_north_west,
        solar_flux_roof_windows,
        g_table_6b_north,
        g_table_6b_north_east,
        g_table_6b_east,
        g_table_6b_south_east,
        g_table_6b_south,
        g_table_6b_south_west,
        g_table_6b_west,
        g_table_6b_north_west,
        g_table_6b_roof_windows,
        FF_table_6b_north,
        FF_table_6b_north_east,
        FF_table_6b_east,
        FF_table_6b_south_east,
        FF_table_6b_south,
        FF_table_6b_south_west,
        FF_table_6b_west,
        FF_table_6b_north_west,
        FF_table_6b_roof_windows
        )
    
    (gains_north,
         gains_north_east,
         gains_east,
         gains_south_east,
         gains_south,
         gains_south_west,
         gains_west,
         gains_north_west,
         gains_roof_windows,
         solar_gains_watts) = result
     
    # Mean internal temperature calculations
    
    result = Mean_Internal_Temperature(
        temperature_during_heating_periods_living_room,
        utilisation_factor_for_gains_living_room_table_9a,
        mean_internal_temperature_living_room_T1_Table_9c,
        temperature_during_heating_periods_rest_of_dwelling,
        utilisation_factor_for_gains_rest_of_dwelling_table_9a,
        mean_internal_temperature_rest_of_dwelling_T2_table_9c,
        living_room_area,
        total_floor_area,
        temperature_adjustment_table_4e
        )
    
    (living_area_fraction,
         mean_internal_temp_whole_dwelling) = result
     
    # Space heating requirement calculations
    
    result = Space_Heating_Requirement(
        utilisation_factor_for_gains_table_9a,
        total_gains_internal_and_solar,
        monthly_external_temperature_table_U1,
        mean_internal_temperature_whole_dwelling,
        heat_transfer_coefficient,
        days_in_month,
        total_floor_area
        )
    
    (useful_gains,
        heat_loss_rate_for_mean_internal_temperature,
        space_heating_requirement_monthly,
        space_heating_requirement_yearly,
        space_heating_requirement_yearly_per_m2) = result
     
     
    # Energy requirements calculations 
    
    result = Energy_Requirements(
        fraction_of_space_heat_secondary_system,
        fraction_of_space_heat_from_main_system_2,
        efficiency_of_main_space_heating_system_1,
        efficiency_of_main_space_heating_system_2,
        efficiency_of_secondary_space_heating_system,
        cooling_system_energy_efficiency_ratio_table_10c,
        space_heating_requirement_monthly,
        output_from_water_heater_monthly,
        efficiency_of_water_heater_table_4a,
        space_cooling_requirement_monthly,
        electricity_demand_mechanical_ventilation_fans_table_4f,
        electricity_demand_warm_air_heating_systems_fans_table_4f,
        electricity_demand_central_heating_pump_or_water_pump_table_4f,
        electricity_demand_oil_boiler_pump_table_4f,
        electricity_demand_boiler_flue_fan_table_4f,
        electricity_demand_keep_hot_facility_gas_combi_boiler_table_4f,
        electricity_demand_pump_for_solar_water_heating_table_4f,
        electricity_demand_pump_for_storage_WWHRS_Table_G3,
        electricity_for_lighting,
        electricity_generated_by_PV_Appendix_M,
        electricity_generated_by_wind_turbine_appendix_M,
        electricity_used_or_generated_by_micro_CHP_appendix_N,
        electricity_generated_by_hydro_electric_generator_appendix_M,
        appendix_Q_energy_saved,
        appendix_Q_energy_used
        )
    
    (fraction_of_space_heat_from_main_systems,
        fraction_of_total_space_heat_from_main_system_1,
        fraction_of_total_space_heat_from_main_system_2,
        space_heating_fuel_main_system_1,
        space_heating_fuel_main_system_2,
        space_heating_fuel_secondary_system,
        fuel_for_water_heating_monthly,
        space_cooling_fuel_monthly,
        space_heating_fuel_used_main_system_1,
        space_heating_fuel_used_main_system_2,
        space_heating_fuel_used_secondary,
        water_fuel_used,
        space_cooling_fuel_used,
        electricity_for_pumps_fans_electric_keep_hot,
        energy_saving_generation_technologies,
        appendix_Q_energy_total,
        total_energy_used) = result
     
     
     # Fuel cost calculations
     
    result = Fuel_Costs(
        space_heating_fuel_main_system_1,
        space_heating_fuel_main_system_2,
        space_heating_fuel_secondary_system,
        space_heating_fuel_price_main_system_1,
        space_heating_fuel_price_main_system_2,
        space_heating_fuel_price_secondary,
        water_heating_high_rate_fraction_table_13,
        water_heating_low_rate_fraction_table_13,
        high_rate_fuel_price,
        low_rate_fuel_price,
        water_fuel_used,
        water_heating_fuel_price_other,
        space_cooling_fuel_used,
        space_cooling_fuel_price,
        electricity_for_pumps_fans_electric_keep_hot,
        fuel_price_for_pumps_fans_electric_keep_hot,
        electricity_for_lighting,
        fuel_price_for_lighting,
        additional_standing_charges_table_12,
        energy_saving_generation_technologies,
        energy_saving_generation_technologies_fuel_price,
        appendix_Q_energy_used,
        appendix_Q_energy_used_fuel_price,
        appendix_Q_energy_saved,
        appendix_Q_energy_saved_fuel_price
        )
    
    (space_heating_main_system_1_fuel_cost,
        space_heating_main_system_2_fuel_cost,
        space_heating_secondary_fuel_cost,
        water_heating_high_rate_fuel_cost,
        water_heating_low_rate_fuel_cost,
        water_heating_cost_other,
        space_cooling_cost,
        pumps_fan_keep_hot_cost,
        lighting_cost,
        appendix_Q_fuel_cost,
        energy_saving_total_fuel_cost,
        additional_standing_charges_table_12,
        total_fuel_cost) = result
     
     # SAP rating calculations
     
    result = SAP_Rating(
        energy_cost_deflator,
        total_fuel_cost,
        total_floor_area
        )
     
    (SAP_rating) = result
    
    # CO2 emissions calculations
    
    result = CO2_emissions(
        space_heating_fuel_main_system_1,
        space_heating_fuel_main_system_2,
        space_heating_fuel_secondary_system,
        space_heating_fuel_emission_factor_main_system_1,
        space_heating_fuel_emission_factor_main_system_2,
        space_heating_fuel_emission_factor_secondary,
        water_fuel_used,
        water_heating_fuel_emission_factor,
        space_cooling_fuel_used,
        space_cooling_fuel_emission_factor,
        electricity_for_pumps_fans_electric_keep_hot,
        fuel_emission_factor_for_pumps_fans_electric_keep_hot,
        electricity_for_lighting,
        fuel_emission_factor_for_lighting,
        energy_saving_generation_technologies,
        energy_saving_generation_technologies_fuel_emission_factor,
        appendix_Q_energy_used,
        appendix_Q_energy_used_fuel_emission_factor,
        appendix_Q_energy_saved,
        appendix_Q_energy_saved_fuel_emission_factor,
        total_floor_area
        )
    (space_heating_main_system_1_emissions,
        space_heating_main_system_2_emissions,
        space_heating_secondary_emissions,
        water_used_emissions,
        space_cooling_used_emissions,
        pumps_fans_electric_keep_hot_emissions,
        lighting_emissions,
        appendix_Q_used_emissions,
        appendix_Q_saved_emissions,
        energy_saving_generation_technologies_emissions,
        space_and_water_heating_emissions,
        appendix_Q_total_used_emissions,
        appendix_Q_total_saved_emissions,
        energy_saving_generation_technologies_total_emissions,
        total_CO2_emissions_yearly,
        dwelling_CO2_emission_rate,
        CF,
        EI_rating) = result
    
    
     
     
     
     
     
     
     
     
     
     
     
    return (
            
        # overall_dwelling_dimensions results
        volume,
        total_floor_area,
        dwelling_volume,
        
        # ventilation_rates results
        number_of_chimneys_total,
        number_of_chimneys_m3_per_hour,
        number_of_open_flues_total,
        number_of_open_flues_m3_per_hour,
        number_of_intermittant_fans_m3_per_hour,
        number_of_passive_vents_m3_per_hour,
        number_of_flueless_gas_fires_m3_per_hour,
        infiltration_due_to_chimneys_flues_fans_PSVs,
        additional_infiltration,
        window_infiltration,
        infiltration_rate,
        infiltration_rate2,
        shelter_factor,
        infiltration_rate_incorporating_shelter_factor,
        wind_factor,
        adjusted_infiltration_rate_allowing_for_shelter_and_wind_speed,
        exhaust_air_heat_pump_air_change_rate_through_system,
        effective_air_change_rate,
        
        # heat_losses_and_heat_loss_parameter results
        solid_floor_UA,
        semi_glazed_door_UA,
        window_UA,
        roof_window_UA,
        basement_floor_UA,
        basement_floor_Ak,
        ground_floor_UA,
        ground_floor_Ak,
        exposed_floor_UA,
        exposed_floor_Ak,
        basement_wall_net_area,
        basement_wall_UA,
        basement_wall_Ak,
        external_wall_net_area,
        external_wall_UA,
        external_wall_Ak,
        roof_net_area,
        roof_UA,
        roof_Ak,
        total_area_of_external_elements,
        party_wall_UA,
        party_wall_Ak,
        party_floor_Ak,
        party_ceiling_Ak,
        internal_wall_Ak,
        internal_floor_Ak,
        internal_ceiling_Ak,
        fabric_heat_loss,
        heat_capacity,
        thermal_mass_parameter,
        thermal_bridges,
        total_fabric_heat_loss,
        ventilation_heat_loss_calculated_monthly,
        heat_transfer_coefficient,
        average_heat_transfer_coefficient,
        heat_loss_parameter,
        average_heat_loss_parameter,
        
        #water heating requirements results
        annual_hot_water_usage_litres_per_day,
        hot_water_usage_in_litres_per_day_monthly,
        energy_content_of_water_used,
        distribution_loss,
        energy_lost_from_water_storage,
        water_storage_loss_monthly,
        total_heat_required_for_water_heating,
        output_from_water_heater_monthly,
        heat_gains_from_water_heating_monthly,
        
        #internal gains results
        total_internal_gains,
        
        #solar gains results
        gains_north,
        gains_north_east,
        gains_east,
        gains_south_east,
        gains_south,
        gains_south_west,
        gains_west,
        gains_north_west,
        gains_roof_windows,
        solar_gains_watts,
        
        #mean internal temperature results
        living_area_fraction,
        mean_internal_temp_whole_dwelling,
        
        #space heating requirements results
        useful_gains,
        heat_loss_rate_for_mean_internal_temperature,
        space_heating_requirement_monthly,
        space_heating_requirement_yearly,
        space_heating_requirement_yearly_per_m2,
        
        #energy requirements results
        fraction_of_space_heat_from_main_systems,
        fraction_of_total_space_heat_from_main_system_1,
        fraction_of_total_space_heat_from_main_system_2,
        space_heating_fuel_main_system_1,
        space_heating_fuel_main_system_2,
        space_heating_fuel_secondary_system,
        fuel_for_water_heating_monthly,
        space_cooling_fuel_monthly,
        space_heating_fuel_used_main_system_1,
        space_heating_fuel_used_main_system_2,
        space_heating_fuel_used_secondary,
        water_fuel_used,
        space_cooling_fuel_used,
        electricity_for_pumps_fans_electric_keep_hot,
        energy_saving_generation_technologies,
        appendix_Q_energy_total,
        total_energy_used,
        
        #fuel cost results
        space_heating_main_system_1_fuel_cost,
        space_heating_main_system_2_fuel_cost,
        space_heating_secondary_fuel_cost,
        water_heating_high_rate_fuel_cost,
        water_heating_low_rate_fuel_cost,
        water_heating_cost_other,
        space_cooling_cost,
        pumps_fan_keep_hot_cost,
        lighting_cost,
        appendix_Q_fuel_cost,
        energy_saving_total_fuel_cost,
        additional_standing_charges_table_12,
        total_fuel_cost,
        
        #SAP rating result
        SAP_rating,
        
        #CO2 emissions result
        space_heating_main_system_1_emissions,
        space_heating_main_system_2_emissions,
        space_heating_secondary_emissions,
        water_used_emissions,
        space_cooling_used_emissions,
        pumps_fans_electric_keep_hot_emissions,
        lighting_emissions,
        appendix_Q_used_emissions,
        appendix_Q_saved_emissions,
        energy_saving_generation_technologies_emissions,
        space_and_water_heating_emissions,
        appendix_Q_total_used_emissions,
        appendix_Q_total_saved_emissions,
        energy_saving_generation_technologies_total_emissions,
        total_CO2_emissions_yearly,
        dwelling_CO2_emission_rate,
        CF,
        EI_rating
        )
    
    
    
    
    
    
    
    
    
    
    
    