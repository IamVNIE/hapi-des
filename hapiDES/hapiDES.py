from pynq import PL
from pynq import MMIO
from pynq import Overlay
from hapiDES import general_const
from . import mimo
class hapiDES():
    """Class to control the custom IP hardware (HAPI)

    Attributes
    ----------
    bitfile : str
    Absolute path to bitstream
    
    data : List of size2 (int or hex values) 
       Input Data for Encryption or Decryption: data[0] is MSB 32 bits and data [1] is LSB 32 bits
    result_ENC_DEC : List of size2 (hex value) 
       Return results of Encryption or Decryption: result_ENC_DEC[0] is MSB 32 bits and result_ENC_DEC[1] is LSB 32 bits
       
   """

    
    def __init__(self):
        self.bitfile = general_const.BITFILE
        self.overlay = Overlay(self.bitfile)
        mmio = MMIO(0x43C40000,0x00010000)
    #global mmio = MMIO(0x43C40000,0x00010000)
        global result_ENC_DEC
        result_ENC_DEC=[0,0]
        if not Overlay.is_loaded(self.overlay):
            self.overlay.download()

    def reset_des_accel(self):
        config_reg=0x80000001
        mmio.write(0,config_reg)
        print("DES ACCELERATOR RESET")
        config_reg=0x80000001
        mmio.write(0,config_reg)