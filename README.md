# HARDWARE API (HAPI) - DES: PYNQ Z1 Custom Hardware Overlay

Package Installation

from terminal via: sudo -H pip install --upgrade 'git+https://github.com/IamVNIE/hapi-des'
by running the example notebook provided in the 'notebooks' folder.

This DES can be used as HARDWARE API (HAPI)

Custom PYNQ Hardware Overlay Creation Testing  

# Software Interface to Hardware

hapiDES() - Programs the bit file to FPGA
 - Usage: 
 
	from hapiDES import hapiDES
	
	des=hapiDES()

Available functions:

 - des_status() - Tells the status of DES Accelerator

 - reset_des_accel() - resets the hardware

 - set_oper_encrypt() - Sets the hardware operation mode to encryption

 - set_oper_decrypt() - Sets the hardware operation mode to decryption

 - set_key(ukey) - Sets the cipher key (Key needs to be sent as a list of 2 elements - MSB 32 bits first and LSB 32 bits.

 - encrypt(data) - Perform encryption (Data needs to be sent as a list of 2 elements - MSB 32 bits first and LSB 32 bits)

 - decrypt(data) - Perform decryption (Data needs to be sent as a list of 2 elements - MSB 32 bits first and LSB 32 bits)

 - result - shows result of operation. encrypt and decrypt function return the result of the operation.
