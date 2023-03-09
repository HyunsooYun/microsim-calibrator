import sys
import os
from typing import Union, Dict, List
from xml.dom import minidom
import numpy as np
import traci
import traci.constants as tc
import sumolib


class Calibrator:
    '''
    Class containing the entire framework for managing simulations
    and calibrating them with field collected data. 
    
    Args:
        sumo_cfg (str): Path to the SUMO configuration file
        use_gui (bool): Whether to use the SUMO GUI or not. Defaults to False
        simulation_time (int): Time to run the simulation time. Defaults to 3600
    
    '''
    def __init__(self,sumo_cfg,
                 use_gui = False,
                 simulation_time = 3600):
        self.sumo_cfg = sumo_cfg
        self.simulation_time = simulation_time

        self.network_file = self.get_xml_filename('net-file')
        self.route_file = self.get_xml_filename('route-files')
        self.network = sumolib.net.readNet(self.network_file)
        self.sumo_bin = sumolib.checkBinary('sumo-gui') if use_gui else sumolib.checkBinary('sumo')

        self.current_step = 0
        
    def get_xml_filename(self,filename):
        name = self.sumo_cfg[:self.sumo_cfg.rfind("/")+1]
        name += minidom.parse(self.sumo_cfg).getElementsByTagName(filename)[0].attributes['value'].value
        
        return name
    
    def calibrate():
        pass
    