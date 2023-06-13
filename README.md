# FPGA-Pin-Delay-Generator
Converts the pin delay list returned by Vivado into a usable CSV that can be pasted into Altium

Use this TCL script to generate the package pinout list. Enter the Dvice name in the <Part> field, eg xc7a35Tfgg484-1

create_project pin_gen -in_memory -part <Part>
set_property design_mode PinPlanning [current_fileset]
open_io_design
foreach pin [get_package_pins -filter { MIN_DELAY > 0 }] {
  puts "$pin [get_property MIN_DELAY [get_package_pin $pin]]"
}
  
Copy the returned List of pins and delay numbers to a .txt file. Open the python script in the same directory as the txt file. Add the txt file name in the <FILE NAME HERE> field and change the max number of pins + 1 (A1 - AXXX) in the "MaxNumPins" Field. So for something like a FGG484 1mm package, the max number is 22 (A1 - A22), so you would make MaxNumPins 23. 
  
Run the script and you'll get a CSV with the pins organized in Alphanumeric order with any missing pins filled in with 0's and all numbers will be converted into ps. You can copy this into Altium now. 
