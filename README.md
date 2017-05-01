PRISM
=====

This is a Tor bridge passive scanning mechanism.

In order to collect more expressive and expansive passive reporting from Tor bridges approximately 500 LOC was added to the existing Tor source code. Most of the modifications were done in the geoip.c file which was already designed to dump the country of origin of bridge users. In order to maintain consistency with the Tor source code, existing data structure, procedural, and code formatting rules were followed. Three different bridges were run, including: one on a machine on campus which was a regular bridge with the modified code to collect passive info; second, an obfs-proxy enabled bridge run in the cloud with the modified code to collect passive info; finally, a regular bridge with the modified code to collect passive info and capable of auto blocking IP addresses which are determined to be adversarial. The blocking process in the third bridge consisted of adding a Linux IP-Table rule to drop all outgoing traffic to the specified adversary IP.


This is a project by Tarek Chammah, Behrooz Shafiee, and Sukhbir Singh.
