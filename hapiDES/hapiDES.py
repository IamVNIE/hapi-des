from pynq import PL
from pynq import MMIO
from pynq import Overlay
from hapiDES import general_const
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

    
from pynq import PL
from pynq import MMIO
from pynq import Overlay
from hapiDES import general_const
DES_overlay = None
mmio = MMIO(0x43C40000,0x00010000)
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
        if PL.bitfile_name != self.bitfile:
                self.download_bitstream()

    def download_bitstream(self):
        global DES_overlay
        DES_overlay = Overlay(self.bitfile)
        DES_overlay.download()
        #DES_overlay.ip_dict

    def reset_des_accel(self):
        global mmio
        config_reg=0x80000001
        self.mmio.write(0,config_reg)
        print("DES ACCELERATOR RESET")
        config_reg=0x80000001
        self.mmio.write(0,config_reg)