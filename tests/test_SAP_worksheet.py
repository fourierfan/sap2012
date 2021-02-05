# -*- coding: utf-8 -*-

import unittest

from sap2012 import SAP_worksheet, SAP_appendices, SAP_tables
import sap2012

class Test_SAP_worksheet(unittest.TestCase):
    "Test for the SAP_worksheet subpackage"
    
    def test_overall_dwelling_dimensions(self):
        ""
        result=SAP_worksheet.overall_dwelling_dimensions(area=[0,63,63],
                                                         average_storey_height=[0,2.5,2.75])
        #print(result)
        self.assertEqual(result,
                         {'volume': [0, 157.5, 173.25], 
                          'total_floor_area': 126, 
                          'dwelling_volume': 330.75})
    
        
    def test_ventilation_rates(self):
                
        result=SAP_worksheet.ventilation_rates(
            number_of_chimneys_main_heating=0,
            number_of_chimneys_secondary_heating=0,
            number_of_chimneys_other=0,
            number_of_open_flues_main_heating=0,
            number_of_open_flues_secondary_heating=0,
            number_of_open_flues_other=0,
            number_of_intermittant_fans_total=0,
            number_of_passive_vents_total=0,
            number_of_flueless_gas_fires_total=0,
            dwelling_volume=330.75,
            air_permeability_value_q50=11.78,
            number_of_storeys_in_the_dwelling=2,
            structural_infiltration=0,
            suspended_wooden_ground_floor_infiltration=0,
            no_draft_lobby_infiltration=0,
            percentage_of_windows_and_doors_draught_proofed=0,
            number_of_sides_on_which_dwelling_is_sheltered=2,
            monthly_average_wind_speed=[4.5,4.5,4.4,3.9,3.8,3.4,3.3,3.3,3.5,3.8,3.9,4.1],
            applicable_case='natural ventilation or whole house positive input ventilation from loft',
            mechanical_ventilation_air_change_rate_through_system=0.5,
            exhaust_air_heat_pump_using_Appendix_N=False,
            mechanical_ventilation_throughput_factor=None,
            efficiency_allowing_for_in_use_factor=None,
            )
        
        self.assertEqual(result,
                         {'number_of_chimneys_total': 0, 
                          'number_of_chimneys_m3_per_hour': 0.0, 
                          'number_of_open_flues_total': 0, 
                          'number_of_open_flues_m3_per_hour': 0.0, 
                          'number_of_intermittant_fans_m3_per_hour': 0.0, 
                          'number_of_passive_vents_m3_per_hour': 0.0, 
                          'number_of_flueless_gas_fires_m3_per_hour': 0.0, 
                          'infiltration_due_to_chimneys_flues_fans_PSVs': 0.0, 
                          'additional_infiltration': None, 
                          'window_infiltration': None, 
                          'infiltration_rate': None, 
                          'infiltration_rate2': 0.589, 
                          'shelter_factor': 0.85, 
                          'infiltration_rate_incorporating_shelter_factor': 0.5006499999999999, 
                          'wind_factor': [1.125, 1.125, 1.1, 0.975, 0.95, 0.85, 0.825, 0.825, 0.875, 0.95, 0.975, 1.025], 
                          'adjusted_infiltration_rate_allowing_for_shelter_and_wind_speed': [0.56323125, 0.56323125, 0.550715, 0.4881337499999999, 0.4756174999999999, 0.42555249999999994, 0.41303624999999994, 0.41303624999999994, 0.43806874999999995, 0.4756174999999999, 0.4881337499999999, 0.5131662499999999], 
                          'exhaust_air_heat_pump_air_change_rate_through_system': None, 
                          'effective_air_change_rate': [0.6586147204882813, 0.6586147204882813, 0.6516435056125, 0.6191372789445312, 0.6131060031531249, 0.590547465128125, 0.5852994719070312, 0.5852994719070312, 0.5959521148632813, 0.6131060031531249, 0.6191372789445312, 0.6316698000695312]
                          }
                         )
    
    
    def test_heat_losses_and_heat_loss_parameter(self):
        
        result=SAP_worksheet.heat_losses_and_heat_loss_parameter(
            solid_door_net_area = 1.5,
            solid_door_u_value = 3,
            semi_glazed_door_net_area = 10.6,
            semi_glazed_door_u_value = 1.4,
            window_net_area = 23,
            window_u_value = 2,
            roof_window_net_area = 0,
            roof_window_u_value = None,
            basement_floor_net_area = 0,
            basement_floor_u_value = None,
            basement_floor_heat_capacity = None,
            ground_floor_net_area = 63,
            ground_floor_u_value = 0.63,
            ground_floor_heat_capacity = 20,
            exposed_floor_net_area = 0,
            exposed_floor_u_value = None,
            exposed_floor_heat_capacity = None,
            basement_wall_gross_area = 0,
            basement_wall_opening = 0,
            basement_wall_u_value = None,
            basement_wall_heat_capacity = None,
            external_wall_gross_area = 120,
            external_wall_opening = 35.1,
            external_wall_u_value = 1.5,
            external_wall_heat_capacity = 190,
            roof_gross_area = 63,
            roof_opening = 0,
            roof_u_value = 0.14,
            roof_heat_capacity = 9,
            party_wall_net_area = 47,
            party_wall_u_value = 0.5,
            party_wall_heat_capacity = 180,
            party_floor_net_area = 0,
            party_floor_heat_capacity = None,
            party_ceiling_net_area = 39,
            party_ceiling_heat_capacity = 100,
            internal_wall_net_area = 131,
            internal_wall_heat_capacity = 9,
            internal_floor_net_area = 63,
            internal_floor_heat_capacity = 18,
            internal_ceiling_net_area = 63,
            internal_ceiling_heat_capacity = 9,
            total_floor_area = 126,
            thermal_bridges_appendix_k = 36.9,
            effective_air_change_rate = [0.6586147204882813, 0.6586147204882813, 0.6516435056125, 0.6191372789445312, 0.6131060031531249, 0.590547465128125, 0.5852994719070312, 0.5852994719070312, 0.5959521148632813, 0.6131060031531249, 0.6191372789445312, 0.6316698000695312],
            dwelling_volume = 330.75
            )
        
        self.assertEqual(result,
                         {'solid_floor_UA': 4.5, 
                          'semi_glazed_door_UA': 14.839999999999998, 
                          'window_UA': 46, 
                          'roof_window_UA': 0, 
                          'basement_floor_UA': 0, 
                          'basement_floor_Ak': 0, 
                          'ground_floor_UA': 39.69, 
                          'ground_floor_Ak': 1260, 
                          'exposed_floor_UA': 0, 
                          'exposed_floor_Ak': 0, 
                          'basement_wall_net_area': 0, 
                          'basement_wall_UA': 0, 
                          'basement_wall_Ak': 0, 
                          'external_wall_net_area': 84.9, 
                          'external_wall_UA': 127.35000000000001, 
                          'external_wall_Ak': 16131.000000000002, 
                          'roof_net_area': 63, 
                          'roof_UA': 8.82, 
                          'roof_Ak': 567, 
                          'total_area_of_external_elements': 246.0, 
                          'party_wall_UA': 23.5, 
                          'party_wall_Ak': 8460, 
                          'party_floor_Ak': 0, 
                          'party_ceiling_Ak': 3900, 
                          'internal_wall_Ak': 1179, 
                          'internal_floor_Ak': 1134, 
                          'internal_ceiling_Ak': 567, 
                          'fabric_heat_loss': 264.7, 
                          'heat_capacity': 33198.0, 
                          'thermal_mass_parameter': 263.4761904761905, 
                          'thermal_bridges': 36.9, 
                          'total_fabric_heat_loss': 301.59999999999997, 
                          'ventilation_heat_loss_calculated_monthly': [71.88615020449468, 71.88615020449468, 71.12525952884035, 67.57728615359822, 66.9189874791557, 64.45677945007202, 63.8839741099727, 63.8839741099727, 65.04668345703999, 66.9189874791557, 67.57728615359822, 68.94517950308916], 
                          'heat_transfer_coefficient': [373.48615020449466, 373.48615020449466, 372.7252595288403, 369.1772861535982, 368.51898747915567, 366.056779450072, 365.4839741099727, 365.4839741099727, 366.64668345703996, 368.51898747915567, 369.1772861535982, 370.5451795030891], 
                          'average_heat_transfer_coefficient': 369.1088914861237, 
                          'heat_loss_parameter': [2.9641757952737673, 2.9641757952737673, 2.9581369803876214, 2.9299784615364937, 2.924753868882188, 2.905212535318032, 2.9006664611902595, 2.9006664611902595, 2.909894313151111, 2.924753868882188, 2.9299784615364937, 2.940834757961025], 
                          'average_heat_loss_parameter': 0.27899387111573976}
                         )
    
    
    def test_water_heating_requirement(self):
                
        result=SAP_worksheet.water_heating_requirement(
            assumed_occupancy=2.88,
            V_dm_table_1c=[1.1,1.06,1.02,0.98,0.94,0.9,0.9,0.94,0.98,1.02,1.06,1.1],
            days_in_month=[31,28,31,30,31,30,31,31,30,31,30,31],
            T_table_1d=[41.2,41.4,40.1,37.6,36.4,33.9,30.4,33.4,33.5,36.3,39.4,39.9],
            water_storage_loss_manufacturer=0,
            temperature_factor_table_2b=0,
            storage_volume_litres=0,
            hot_water_storage_loss_table_2=0,
            volume_factor_table_2a=0,
            Vs_appendix_G3=0,
            solar_storage_WWHRS_factor=0,
            primary_circuit_loss_table_3=[0,0,0,0,0,0,0,0,0,0,0,0],
            combi_loss_table_3=[0,0,0,0,0,0,0,0,0,0,0,0],
            solar_DHW_input_appendix_G=[0,0,0,0,0,0,0,0,0,0,0,0]    
            )

        #print(result); return        
        self.assertEqual(result,
                         {'annual_hot_water_usage_litres_per_day': 108.0, 
                          'hot_water_usage_in_litres_per_day_monthly': [118.80000000000001, 114.48, 110.16, 105.84, 101.52, 97.2, 97.2, 101.52, 105.84, 110.16, 114.48, 118.80000000000001], 
                          'energy_content_of_water_used': [176.17696800000002, 154.0855008, 159.00243479999997, 138.622176, 133.01127839999998, 114.77861999999999, 106.35926399999998, 122.04881039999998, 123.50646, 143.93487239999996, 157.116168, 170.617986], 
                          'distribution_loss': [26.426545200000003, 23.11282512, 23.850365219999997, 20.793326399999998, 19.951691759999996, 17.216793, 15.953889599999997, 18.307321559999995, 18.525969, 21.590230859999995, 23.5674252, 25.5926979], 
                          'energy_lost_from_water_storage': 0, 
                          'water_storage_loss_monthly': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                          'total_heat_required_for_water_heating': [176.17696800000002, 154.0855008, 159.00243479999997, 138.622176, 133.01127839999998, 114.77861999999999, 106.35926399999998, 122.04881039999997, 123.50646, 143.93487239999996, 157.116168, 170.617986], 
                          'output_from_water_heater_monthly': [176.17696800000002, 154.0855008, 159.00243479999997, 138.622176, 133.01127839999998, 114.77861999999999, 106.35926399999998, 122.04881039999997, 123.50646, 143.93487239999996, 157.116168, 170.617986],
                          'heat_gains_from_water_heating_monthly': [58.57884186000001, 51.233429016, 52.868309571, 46.09187352, 44.22625006799999, 38.16389115, 35.364455279999994, 40.58122945799999, 41.06589795, 47.85834507299999, 52.24112586, 56.730480345000004]}
                         )
    
    
    def test_internal_gains_appendix_L(self):
        ""
        result=SAP_appendices.internal_gains_appendix_L(total_floor_area=126, #
                                                        assumed_occupancy=2.88, #
                                                        number_of_low_energy_light_bulbs=0, 
                                                        total_number_of_light_bulbs=10, 
                                                        frame_factor=0.7, 
                                                        window_area=23, 
                                                        light_access_factor_table_6d=0, 
                                                        light_transmittance_factor_table_6d=0, 
                                                        month_number=[1,2,3,4,5,6,7,8,9,10,11,12], 
                                                        days_in_month=[31,28,31,30,31,30,31,31,30,31,30,31], #  
                                                        heat_gains_from_water_heating_monthly=[58.57884186000001, 51.233429016, 52.868309571, 46.09187352, 44.22625006799999, 38.16389115, 35.364455279999994, 40.58122945799999, 41.06589795, 47.85834507299999, 52.24112586, 56.730480345000004] #
                                                        )
        #print(result); return        
        self.assertEqual(result,
                         {'G_L': 0.0, 
                          'C_1': 1.0, 
                          'C_2': 1.433, 
                          'E_B': 961.3129846269878, 
                          'initial_annual_lighting_demand': 1377.5615069704736, 
                          'monthly_lighting_demand': [170.44004138215163, 136.73333404409811, 123.11320471364185, 90.19801113556179, 69.67153789610578, 56.92224382365604, 63.55670774707949, 82.61341500897964, 107.30665588605414, 140.792137622484, 159.02439796754066, 175.17709717811994], 
                          'annual_lighting_demand': 1375.548784405473, 
                          'lighting_gains': [194.72316555756572, 172.9513897879217, 140.65352689058545, 106.48376314614931, 79.59785915549719, 67.19987118070505, 72.61183008738921, 94.38360585703319, 126.68146875436948, 160.85123249880564, 187.7371364894577, 200.1351244642499], 
                          'initial_annual_electrical_appliance_demand': 3344.397090331292, 
                          'monthly_electrical_appliance_demand': [324.97196609445984, 296.56891709489645, 319.84634209264283, 292.02145229267745, 278.91906038248453, 249.1509937495433, 243.11740267414316, 239.74521055639624, 240.2351871057679, 266.3338680661697, 279.8422339220502, 310.63334189407493], 
                          'annual_electrical_appliance_demand': 3341.3859759253064, 
                          'appliances_gains': [436.7902770086826, 441.32279329597685, 429.9009974363479, 405.5853504064965, 374.89121019151145, 346.0430468743657, 326.77070251900966, 322.2381862317154, 333.6599820913443, 357.9756291211959, 388.66976933618076, 417.5179326533265], 
                          'cooking_gains': [55.16, 55.16, 55.16, 55.16, 55.16, 55.16, 55.16, 55.16, 55.16, 55.16, 55.16, 55.16], 
                          'losses': [-115.19999999999999, -115.19999999999999, -115.19999999999999, -115.19999999999999, -115.19999999999999, -115.19999999999999, -115.19999999999999, -115.19999999999999, -115.19999999999999, -115.19999999999999, -115.19999999999999, -115.19999999999999], 
                          'water_heating_gains': [78.73500250000002, 76.24022175, 71.059555875, 64.016491, 59.44388449999999, 53.005404375, 47.532869999999996, 54.544663249999985, 57.035969375, 64.32573262499999, 72.55711925, 76.250645625], 
                          'metabolic_gains': [172.79999999999998, 172.79999999999998, 172.79999999999998, 172.79999999999998, 172.79999999999998, 172.79999999999998, 172.79999999999998, 172.79999999999998, 172.79999999999998, 172.79999999999998, 172.79999999999998, 172.79999999999998]}
                         )
    
    
    def test_internal_gains(self):
        ""        
        result=SAP_worksheet.internal_gains(
                metabolic_gains=[172.79999999999998, 172.79999999999998, 172.79999999999998, 172.79999999999998, 172.79999999999998, 172.79999999999998, 172.79999999999998, 172.79999999999998, 172.79999999999998, 172.79999999999998, 172.79999999999998, 172.79999999999998],
                lighting_gains=[194.72316555756572, 172.9513897879217, 140.65352689058545, 106.48376314614931, 79.59785915549719, 67.19987118070505, 72.61183008738921, 94.38360585703319, 126.68146875436948, 160.85123249880564, 187.7371364894577, 200.1351244642499], 
                appliances_gains=[436.7902770086826, 441.32279329597685, 429.9009974363479, 405.5853504064965, 374.89121019151145, 346.0430468743657, 326.77070251900966, 322.2381862317154, 333.6599820913443, 357.9756291211959, 388.66976933618076, 417.5179326533265], 
                cooking_gains=[55.16, 55.16, 55.16, 55.16, 55.16, 55.16, 55.16, 55.16, 55.16, 55.16, 55.16, 55.16], 
                pumps_and_fans_gains=[3,3,3,3,3,3,3,3,3,3,3,3],
                losses=[-115.19999999999999, -115.19999999999999, -115.19999999999999, -115.19999999999999, -115.19999999999999, -115.19999999999999, -115.19999999999999, -115.19999999999999, -115.19999999999999, -115.19999999999999, -115.19999999999999, -115.19999999999999], 
                water_heating_gains=[78.73500250000002, 76.24022175, 71.059555875, 64.016491, 59.44388449999999, 53.005404375, 47.532869999999996, 54.544663249999985, 57.035969375, 64.32573262499999, 72.55711925, 76.250645625]   
                )
        #print(result); return
        self.assertEqual(result,
                         {'total_internal_gains': [826.0084450662484, 806.2744048338986, 757.3740802019332, 691.8456045526458, 629.6929538470085, 582.0083224300707, 562.6754026063988, 586.9264553387486, 633.1374202207138, 698.9125942450014, 764.7240250756385, 809.6637027425766]}
                         )
        
    
    def test_solar_gains_appendix_U3(self):
        ""
        result=SAP_appendices.solar_gains_appendix_U3(
            solar_radiation_horizontal_plane_monthly_table_U3=[28,55,97,153,191,208,194,208,163,69,35,23],
            solar_declination_monthly_table_U3=[-20.7,-12.8,-1.8,9.8,18.8,23.1,21.2,13.7,2.9,-8.7,-18.4,-23],
            location_latitude_table_U4=53.4,
            p_tilt=90
            )
        #print(result); return
        self.assertEqual(result,
                         {'solar_flux_north': [11.436412538787879, 20.68106276617149, 34.88819996564874, 56.60050580088716, 74.37336606102218, 83.23769024974976, 76.70104638812194, 78.53644960579577, 58.8572132744309, 25.27636829258531, 13.896518711289401, 9.694808146066876], 
                          'solar_flux_north_east': [12.145680410782088, 23.390120502005598, 41.822541929590635, 69.35106310279406, 90.92010849368495, 101.33317075341961, 93.56166394939247, 96.27172344125725, 71.49571781748358, 29.345278592731244, 15.052394030804441, 10.086433192648474], 
                          'solar_flux_east': [21.134620057486963, 39.10325251255132, 63.89067906174743, 94.07548963233845, 112.45528635480359, 120.35576029517244, 113.08865238428933, 125.3690022999708, 104.24164026519922, 47.62774419378216, 25.95337911472664, 17.67550544600751], 
                          'solar_flux_south_east': [39.52445140930432, 63.67584001530772, 86.45248517226558, 108.19002478773515, 118.24508642072698, 122.75319126127208, 116.79405702599594, 138.09149868418606, 131.337465411037, 72.24114109708997, 46.62387627277164, 34.40022790846911], 
                          'solar_flux_south': [50.19978039205471, 77.74870204827221, 98.25759733263759, 112.15296767461275, 114.04561780476595, 114.77624296019953, 110.66770715027762, 138.64572001814557, 144.00160165626096, 86.0766956546692, 58.60023126922464, 44.116758929075765], 
                          'solar_flux_south_west': [39.52445140930432, 63.67584001530772, 86.45248517226558, 108.19002478773515, 118.24508642072698, 122.75319126127208, 116.79405702599594, 138.09149868418606, 131.337465411037, 72.24114109708997, 46.62387627277164, 34.40022790846911], 
                          'solar_flux_west': [21.134620057486963, 39.10325251255132, 63.89067906174743, 94.07548963233845, 112.45528635480359, 120.35576029517244, 113.08865238428933, 125.3690022999708, 104.24164026519922, 47.62774419378216, 25.95337911472664, 17.67550544600751], 
                          'solar_flux_north_west': [12.145680410782088, 23.390120502005598, 41.822541929590635, 69.35106310279406, 90.92010849368495, 101.33317075341961, 93.56166394939247, 96.27172344125725, 71.49571781748358, 29.345278592731244, 15.052394030804441, 10.086433192648474]
                          }
                          )
        
    
    
    def test_solar_gains(self):
                
        result=SAP_worksheet.solar_gains(
            access_factor_table_6d_north=0.77,
            access_factor_table_6d_north_east=0,
            access_factor_table_6d_east=0.77,
            access_factor_table_6d_south_east=0,
            access_factor_table_6d_south=0.77,
            access_factor_table_6d_south_west=0,
            access_factor_table_6d_west=0,
            access_factor_table_6d_north_west=0,
            access_factor_table_6d_roof_windows=0,
            area_north=10,
            area_north_east=0,
            area_east=4.9,
            area_south_east=0,
            area_south=11.9,
            area_south_west=0,
            area_west=0,
            area_north_west=0,
            area_roof_windows=0,
            solar_flux_north=[11.436412538787879, 20.68106276617149, 34.88819996564874, 56.60050580088716, 74.37336606102218, 83.23769024974976, 76.70104638812194, 78.53644960579577, 58.8572132744309, 25.27636829258531, 13.896518711289401, 9.694808146066876], #
            solar_flux_north_east=[12.145680410782088, 23.390120502005598, 41.822541929590635, 69.35106310279406, 90.92010849368495, 101.33317075341961, 93.56166394939247, 96.27172344125725, 71.49571781748358, 29.345278592731244, 15.052394030804441, 10.086433192648474], # 
            solar_flux_east=[21.134620057486963, 39.10325251255132, 63.89067906174743, 94.07548963233845, 112.45528635480359, 120.35576029517244, 113.08865238428933, 125.3690022999708, 104.24164026519922, 47.62774419378216, 25.95337911472664, 17.67550544600751], #
            solar_flux_south_east=[39.52445140930432, 63.67584001530772, 86.45248517226558, 108.19002478773515, 118.24508642072698, 122.75319126127208, 116.79405702599594, 138.09149868418606, 131.337465411037, 72.24114109708997, 46.62387627277164, 34.40022790846911], # 
            solar_flux_south=[50.19978039205471, 77.74870204827221, 98.25759733263759, 112.15296767461275, 114.04561780476595, 114.77624296019953, 110.66770715027762, 138.64572001814557, 144.00160165626096, 86.0766956546692, 58.60023126922464, 44.116758929075765], #
            solar_flux_south_west=[39.52445140930432, 63.67584001530772, 86.45248517226558, 108.19002478773515, 118.24508642072698, 122.75319126127208, 116.79405702599594, 138.09149868418606, 131.337465411037, 72.24114109708997, 46.62387627277164, 34.40022790846911], # 
            solar_flux_west=[21.134620057486963, 39.10325251255132, 63.89067906174743, 94.07548963233845, 112.45528635480359, 120.35576029517244, 113.08865238428933, 125.3690022999708, 104.24164026519922, 47.62774419378216, 25.95337911472664, 17.67550544600751], #
            solar_flux_north_west=[12.145680410782088, 23.390120502005598, 41.822541929590635, 69.35106310279406, 90.92010849368495, 101.33317075341961, 93.56166394939247, 96.27172344125725, 71.49571781748358, 29.345278592731244, 15.052394030804441, 10.086433192648474], #
            solar_flux_roof_windows=[0,0,0,0,0,0,0,0,0,0,0,0],
            g_table_6b_north=0.72,
            g_table_6b_north_east=0,
            g_table_6b_east=0.72,
            g_table_6b_south_east=0,
            g_table_6b_south=0.72,
            g_table_6b_south_west=0,
            g_table_6b_west=0,
            g_table_6b_north_west=0,
            g_table_6b_roof_windows=0,
            FF_table_6b_north=0.72,
            FF_table_6b_north_east=0,
            FF_table_6b_east=0.72,
            FF_table_6b_south_east=0,
            FF_table_6b_south=0.72,
            FF_table_6b_south_west=0,
            FF_table_6b_west=0,
            FF_table_6b_north_west=0,
            FF_table_6b_roof_windows=0,
            total_internal_gains=[826.0084450662484, 806.2744048338986, 757.3740802019332, 691.8456045526458, 629.6929538470085, 582.0083224300707, 562.6754026063988, 586.9264553387486, 633.1374202207138, 698.9125942450014, 764.7240250756385, 809.6637027425766] #
            )
        #print(result); return
        self.assertEqual(result,
                         {'gains_north': [41.085449282545916, 74.29696616022427, 125.33627703499268, 203.33799629575677, 267.187210054615, 299.032401074509, 275.5494295618847, 282.14313764621653, 211.44524497495226, 90.80565640753223, 49.923410228531715, 34.828714602443], 
                          'gains_north_east': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
                          'gains_east': [37.20392432426168, 68.8346629062817, 112.46873529656344, 165.60398945092524, 197.9585131896034, 211.86596143347, 199.07344696965018, 220.6909261434296, 183.4997783406816, 83.84058884905545, 45.68653469600037, 31.1147380562152], 
                          'gains_south_east': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
                          'gains_south': [214.60854301242728, 332.38264266048253, 420.0600010353155, 479.4639498259235, 487.55519810813206, 490.6786858778245, 473.1143284803312, 592.7228313674555, 615.6197035435115, 367.98555885109886, 250.52122050458306, 188.60308316603607], 
                          'gains_south_west': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
                          'gains_west': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
                          'gains_north_west': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
                          'gains_roof_windows': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
                          'solar_gains_watts': [292.8979166192349, 475.5142717269885, 657.8650133668716, 848.4059355726056, 952.7009213523504, 1001.5770483858034, 947.7372050118661, 1095.5568951571017, 1010.5647268591454, 542.6318041076865, 346.13116542911513, 254.54653582469427], 
                          'total_internal_and_solar_gains': [1118.9063616854833, 1281.788676560887, 1415.239093568805, 1540.2515401252513, 1582.393875199359, 1583.5853708158743, 1510.412607618265, 1682.4833504958503, 1643.702147079859, 1241.544398352688, 1110.8551905047536, 1064.2102385672708]
                          }
                         )
    
    
    def test_utilisation_factor_for_heating_table_9a(self):
        ""
        result=SAP_tables.utilisation_factor_for_heating_table_9a(
            heat_transfer_coefficient=[373.48615020449466, 373.48615020449466, 372.7252595288403, 369.1772861535982, 368.51898747915567, 366.056779450072, 365.4839741099727, 365.4839741099727, 366.64668345703996, 368.51898747915567, 369.1772861535982, 370.5451795030891],
            total_internal_and_solar_gains=[1118.9063616854833, 1281.788676560887, 1415.239093568805, 1540.2515401252513, 1582.393875199359, 1583.5853708158743, 1510.412607618265, 1682.4833504958503, 1643.702147079859, 1241.544398352688, 1110.8551905047536, 1064.2102385672708],
            temperature_during_heating_living_room=20,
            heating_controls=2,
            monthly_external_temperature_table_U1=[4.3,4.8,6.6,9,11.8,14.8,16.6,16.5,14,10.5,7.1,4.2],
            thermal_mass_parameter=263.4761904761905,
            heat_loss_parameter=[2.9641757952737673, 2.9641757952737673, 2.9581369803876214, 2.9299784615364937, 2.924753868882188, 2.905212535318032, 2.9006664611902595, 2.9006664611902595, 2.909894313151111, 2.924753868882188, 2.9299784615364937, 2.940834757961025]
            )
        #print(result); return
        self.assertEqual(result,
                         {'time_constant': [24.690786155303304, 24.690786155303304, 24.741190544273064, 24.97896542538086, 25.02358624652486, 25.19190241612353, 25.23138446527864, 25.23138446527864, 25.151370741219782, 25.02358624652486, 24.97896542538086, 24.886753833994458], 
                          'a': [2.646052410353554, 2.646052410353554, 2.6494127029515377, 2.6652643616920573, 2.6682390831016574, 2.679460161074902, 2.6820922976852426, 2.6820922976852426, 2.6767580494146523, 2.6682390831016574, 2.6652643616920573, 2.659116922266297], 
                          'heat_loss_rate_living_room': [5863.732558210566, 5676.989483108318, 4994.51847768646, 4060.95014768958, 3021.855697329076, 1903.495253140374, 1242.6455119739067, 1279.1939093849044, 2199.88010074224, 3500.9303810519787, 4762.386991381417, 5854.613836148808], 
                          'y_living_room': [0.19081810955357412, 0.2257866921146858, 0.28335846586443425, 0.37928353811522547, 0.5236497151726959, 0.8319355502480427, 1.2154814812947081, 1.3152684187691812, 0.747178060533969, 0.3546327013734052, 0.23325596859622907, 0.18177291762547967], 
                          'utilisation_factor_for_heating_living_room': [0.9898710602320386, 0.9848424812922535, 0.9743732827705389, 0.9517679810882888, 0.9065144344272734, 0.7913072833532275, 0.6541059073056135, 0.6227782770288123, 0.8237698575019649, 0.958475204499211, 0.9840832115221984, 0.9911951081097073], 
                          'temperature_during_heating_rest_of_dwelling': [17.768019050166806, 17.768019050166806, 17.771077552507112, 17.78541935388582, 17.788094897246257, 17.798142454296052, 17.80048903206591, 17.80048903206591, 17.79572942965799, 17.788094897246257, 17.78541935388582, 17.77987433150828], 
                          'heat_loss_rate_rest_of_dwelling': [5030.118585927595, 4843.375510825348, 4163.742779975016, 3243.377274788865, 2206.726668462289, 1097.4903711521472, 438.7595023148832, 475.30789972588104, 1391.6916066843835, 2685.8013521851917, 3944.814118480702, 5031.9569717981285], 
                          'y_rest_of_dwelling': [0.22244134856298778, 0.26464780062912374, 0.3398958985591557, 0.4748912659954175, 0.7170774241388113, 1.442915047312373, 3.4424613020330477, 3.5397756937475053, 1.181082173079907, 0.4622621838143601, 0.28159886806848744, 0.21149032961364614], 
                          'utilisation_factor_for_heating_rest_of_dwelling': [0.9853699748581132, 0.9780077699256723, 0.9614077696920973, 0.9228038974306823, 0.8347106825562942, 0.5854904937196589, 0.2829256350308353, 0.2756078214168028, 0.6650196783967307, 0.9270852526727167, 0.9752439186346192, 0.9872897632890457]
                          }
                         )
        
    
    def _test_mean_internal_temperature(self):
                
        result=SAP_worksheet.mean_internal_temperature(
            temperature_during_heating_periods_living_room =21,
            utilisation_factor_for_gains_living_room_table_9a=[0.99,0.98,0.97,0.92,0.77,0.11,-1.45,-0.9,0.64,0.93,0.98,0.99],
            mean_internal_temperature_living_room_T1_Table_9c=[17.8,18,18.5,19.2,19.7,19.8,18.6,19.2,20,19.4,18.50,17.8],
            temperature_during_heating_periods_rest_of_dwelling=21,
            utilisation_factor_for_gains_rest_of_dwelling_table_9a=[0.99,0.98,0.97,0.92,0.77,0.11,-1.45,-0.9,0.64,0.93,0.98,0.99],
            mean_internal_temperature_rest_of_dwelling_T2_table_9c=[17.7,17.9,18.5,19.2,19.7,19.7,18.5,19.1,20,19.3,18.5,17.7],
            living_room_area=30,
            total_floor_area=126,
            temperature_adjustment_table_4e=0
            )
        
        print(result)
        
        
    def test_calculate_worksheet(self):
        ""
        inputs={
            'overall_dwelling_dimensions':{'area':[0,63,63],
                                           "average_storey_height": [0,2.5,2.75]
                                           },
            'ventilation_rates':dict(number_of_chimneys_main_heating=0,
                                     number_of_chimneys_secondary_heating=0,
                                     number_of_chimneys_other=0,
                                     number_of_open_flues_main_heating=0,
                                     number_of_open_flues_secondary_heating=0,
                                     number_of_open_flues_other=0,
                                     number_of_intermittant_fans_total=0,
                                     number_of_passive_vents_total=0,
                                     number_of_flueless_gas_fires_total=0,
                                     air_permeability_value_q50=11.78,
                                     number_of_storeys_in_the_dwelling=2,
                                     structural_infiltration=0,
                                     suspended_wooden_ground_floor_infiltration=0,
                                     no_draft_lobby_infiltration=0,
                                     percentage_of_windows_and_doors_draught_proofed=0,
                                     number_of_sides_on_which_dwelling_is_sheltered=2,
                                     monthly_average_wind_speed=[4.5,4.5,4.4,3.9,3.8,3.4,3.3,3.3,3.5,3.8,3.9,4.1],
                                     applicable_case='natural ventilation or whole house positive input ventilation from loft',
                                     mechanical_ventilation_air_change_rate_through_system=0.5,
                                     exhaust_air_heat_pump_using_Appendix_N=False,
                                     mechanical_ventilation_throughput_factor=None,
                                     efficiency_allowing_for_in_use_factor=None,
                                     ),
            'heat_losses_and_heat_loss_parameter':dict(solid_door_net_area = 1.5,
                                                       solid_door_u_value = 3,
                                                       semi_glazed_door_net_area = 10.6,
                                                       semi_glazed_door_u_value = 1.4,
                                                       window_net_area = 23,
                                                       window_u_value = 2,
                                                       roof_window_net_area = 0,
                                                       roof_window_u_value = None,
                                                       basement_floor_net_area = 0,
                                                       basement_floor_u_value = None,
                                                       basement_floor_heat_capacity = None,
                                                       ground_floor_net_area = 63,
                                                       ground_floor_u_value = 0.63,
                                                       ground_floor_heat_capacity = 20,
                                                       exposed_floor_net_area = 0,
                                                       exposed_floor_u_value = None,
                                                       exposed_floor_heat_capacity = None,
                                                       basement_wall_gross_area = 0,
                                                       basement_wall_opening = 0,
                                                       basement_wall_u_value = None,
                                                       basement_wall_heat_capacity = None,
                                                       external_wall_gross_area = 120,
                                                       external_wall_opening = 35.1,
                                                       external_wall_u_value = 1.5,
                                                       external_wall_heat_capacity = 190,
                                                       roof_gross_area = 63,
                                                       roof_opening = 0,
                                                       roof_u_value = 0.14,
                                                       roof_heat_capacity = 9,
                                                       party_wall_net_area = 47,
                                                       party_wall_u_value = 0.5,
                                                       party_wall_heat_capacity = 180,
                                                       party_floor_net_area = 0,
                                                       party_floor_heat_capacity = None,
                                                       party_ceiling_net_area = 39,
                                                       party_ceiling_heat_capacity = 100,
                                                       internal_wall_net_area = 131,
                                                       internal_wall_heat_capacity = 9,
                                                       internal_floor_net_area = 63,
                                                       internal_floor_heat_capacity = 18,
                                                       internal_ceiling_net_area = 63,
                                                       internal_ceiling_heat_capacity = 9,
                                                       thermal_bridges_appendix_k = 36.9,
                                                       ),
            'water_heating_requirement':dict(assumed_occupancy=2.88,
                                             V_dm_table_1c=[1.1,1.06,1.02,0.98,0.94,0.9,0.9,0.94,0.98,1.02,1.06,1.1],
                                             days_in_month=[31,28,31,30,31,30,31,31,30,31,30,31],
                                             T_table_1d=[41.2,41.4,40.1,37.6,36.4,33.9,30.4,33.4,33.5,36.3,39.4,39.9],
                                             water_storage_loss_manufacturer=0,
                                             temperature_factor_table_2b=0,
                                             storage_volume_litres=0,
                                             hot_water_storage_loss_table_2=0,
                                             volume_factor_table_2a=0,
                                             Vs_appendix_G3=0,
                                             solar_storage_WWHRS_factor=0,
                                             primary_circuit_loss_table_3=[0,0,0,0,0,0,0,0,0,0,0,0],
                                             combi_loss_table_3=[0,0,0,0,0,0,0,0,0,0,0,0],
                                             solar_DHW_input_appendix_G=[0,0,0,0,0,0,0,0,0,0,0,0]  
                                             ),
            'internal_gains_appendix_L':dict(number_of_low_energy_light_bulbs=0, 
                                             total_number_of_light_bulbs=10, 
                                             frame_factor=0.7, 
                                             window_area=23, 
                                             light_access_factor_table_6d=0, 
                                             light_transmittance_factor_table_6d=0, 
                                             month_number=[1,2,3,4,5,6,7,8,9,10,11,12], 
                                             ),
            'internal_gains':dict(pumps_and_fans_gains=[3,3,3,3,3,3,3,3,3,3,3,3]
                                  ),
            'solar_gains_appendix_U3':dict(solar_radiation_horizontal_plane_monthly_table_U3=[28,55,97,153,191,208,194,208,163,69,35,23],
                                           solar_declination_monthly_table_U3=[-20.7,-12.8,-1.8,9.8,18.8,23.1,21.2,13.7,2.9,-8.7,-18.4,-23],
                                           location_latitude_table_U4=53.4,
                                           p_tilt=90),
            'solar_gains':dict(access_factor_table_6d_north=0.77,
                               access_factor_table_6d_north_east=0,
                               access_factor_table_6d_east=0.77,
                               access_factor_table_6d_south_east=0,
                               access_factor_table_6d_south=0.77,
                               access_factor_table_6d_south_west=0,
                               access_factor_table_6d_west=0,
                               access_factor_table_6d_north_west=0,
                               access_factor_table_6d_roof_windows=0,
                               area_north=10,
                               area_north_east=0,
                               area_east=4.9,
                               area_south_east=0,
                               area_south=11.9,
                               area_south_west=0,
                               area_west=0,
                               area_north_west=0,
                               area_roof_windows=0,
                               solar_flux_roof_windows=[0,0,0,0,0,0,0,0,0,0,0,0],
                               g_table_6b_north=0.72,
                               g_table_6b_north_east=0,
                               g_table_6b_east=0.72,
                               g_table_6b_south_east=0,
                               g_table_6b_south=0.72,
                               g_table_6b_south_west=0,
                               g_table_6b_west=0,
                               g_table_6b_north_west=0,
                               g_table_6b_roof_windows=0,
                               FF_table_6b_north=0.72,
                               FF_table_6b_north_east=0,
                               FF_table_6b_east=0.72,
                               FF_table_6b_south_east=0,
                               FF_table_6b_south=0.72,
                               FF_table_6b_south_west=0,
                               FF_table_6b_west=0,
                               FF_table_6b_north_west=0,
                               FF_table_6b_roof_windows=0,
                               ),
            'utilisation_factor_for_heating_table_9a':dict(
                temperature_during_heating_living_room=20,
                heating_controls=2,
                monthly_external_temperature_table_U1=[4.3,4.8,6.6,9,11.8,14.8,16.6,16.5,14,10.5,7.1,4.2],
                ),
                
            }
        
        #print(inputs['ventilation_rates'])
        #print(inputs['heat_losses_and_heat_loss_parameter'])
        #print(inputs['water_heating_requirement'])
        #print(inputs['internal_gains_appendix_L'])
        #print(inputs['solar_gains_appendix_U3'])
        #print(inputs['solar_gains'])
        #print(inputs['utilisation_factor_for_heating_table_9a'])
        
        result=SAP_worksheet.calculate_worksheet(inputs)
        #print(result)
        
        self.assertEqual(result['overall_dwelling_dimensions'],
                         {'volume': [0, 157.5, 173.25], 
                          'total_floor_area': 126, 
                          'dwelling_volume': 330.75})
    
        
        
if __name__=='__main__':
    
    o=unittest.main(Test_SAP_worksheet())  
    
    