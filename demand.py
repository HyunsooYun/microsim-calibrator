import sys
import os
from typing import Union, Dict, List
from xml.dom import minidom
import numpy as np
import sumolib


class Demand:
    '''
    Classes responsible for generating different types of demand files that can be simulated in SUMO.
    
    Args:
        sumo_cfg (str): Path to the SUMO configuration file
    '''
    def __init__(self,sumo_cfg):
        self.sumo_cfg = sumo_cfg
        self.network_file = self.get_xml_filename('net-file')
        self.route_file = self.get_xml_filename('route-files')
        self.network = sumolib.net.readNet(self.network_file)
        
    def get_xml_filename(self,filename):
        name = self.sumo_cfg[:self.sumo_cfg.rfind("/")+1]
        name += minidom.parse(self.sumo_cfg).getElementsByTagName(filename)[0].attributes['value'].value
        
        return name
    
    def make_trips():
        pass
    
    def make_flow():
        pass
    
    def make_random_trips():
        pass
    
    def make_od_matrices():
        pass
    
    def make_detector_data():
        pass
    
    def make_population_data():
        pass
    
    
    
    
    
    
    