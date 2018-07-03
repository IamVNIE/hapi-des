# HARDWARE API (HAPI) - DES: PYNQ Z1 Custom Hardware Overlay

Building application software became seamlessly easy with the advent of application programming interfaces (API), which are a set of subroutine definitions, protocols, and tools for building application software. By abstracting the underlying implementation and only exposing objects or actions the developer needs, an API reduces the cognitive load on a programmer and inherently reduces the development life cycle. However, accelerating applications using FPGAs require considerable expertise in hardware design and digital logic.

This project aims at advancing hardware acceleration programming interface (HAPI) for All Programmable System on Chip (APSoC) such as PYNQ. HAPI can provide on-demand hardware acceleration to developers for improving the performance of applications. As a case study, we explore the design space area of accelerating crypto-systems such as DES and AES which play a critical role in security. The goal is to develop hardware libraries required for the application using digital logic design and/or hardware description language.

HAPI will provide seamless interface to the underlying hardware libraries to be accessed using software. Once developed, applications can be accelerated using FPGAs even by a person without the knowledge/expertise of hardware design or digital logic. 

Package Installation

from terminal via: sudo -H pip install --upgrade 'git+https://github.com/IamVNIE/hapi-des'
or by running the example notebook provided in the 'notebook' folder.

This DES can be used as HARDWARE API (HAPI)

Custom PYNQ Hardware Overlay Creation Testing  

# Software Interface to Hardware

	hapiDES() - Programs the bit file to FPGA
 	- Usage: 
		from hapiDES import hapiDES	
		des=hapiDES()

Available functions:

 	des_status() - Tells the status of DES Accelerator

	reset_des_accel() - resets the hardware

	set_oper_encrypt() - Sets the hardware operation mode to encryption

	set_oper_decrypt() - Sets the hardware operation mode to decryption

	set_key(ukey) - Sets the cipher key (Key needs to be sent as a list of 2 elements - MSB 32 bits first and LSB 32 bits.

	encrypt(data) - Perform encryption (Data needs to be sent as a list of 2 elements - MSB 32 bits first and LSB 32 bits)

	decrypt(data) - Perform decryption (Data needs to be sent as a list of 2 elements - MSB 32 bits first and LSB 32 bits)

	result - shows result of operation. encrypt and decrypt function return the result of the operation.
 
# Coming soon.. MultiCore DES Accelerator with 5 Cores  
