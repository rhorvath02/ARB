# ARBCalcs
*Calculates stiffness values for bladed ARBs*

***This repo contains two separate programs.***
***One runs stiffness calculations while the other returns stiffness vs rotation graphs***

*The following applies to both programs*

***Inputs are located in Properties.json***

***All calculations are handled within CNP.py***

**Run main.py and stiffness calculations will print in console**

There are four total stiffness calculations in CNP.py: TorsionBar stiffness, 
max blade stiffness, min blade stiffness, and Combined TorsionBar/Blade stiffness


Additional Notes:
- Conversions.py processes data from the Json and returns it in an appropriate format
- CNP.py defines the torsion bar, blade, and combined torsion bar/blade
