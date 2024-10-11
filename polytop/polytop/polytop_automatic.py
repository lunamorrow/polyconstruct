from __future__ import annotations

import json
import random
import re
from typing import Dict, List, Optional, Tuple, Union
from polytop.bonds import Bond
from polytop.junction import Junction, Junctions
from polytop.topology import Topology
from polytop.polymer import Polymer
from polytop.atoms import Atom
from polytop.monomer import Monomer
import datetime
import copy


class Automatic:
    """
    doctrings go brr
    """
    def __init__(self, orderedList, numMonomers, monomerList) -> None:
        self.directions = orderedList
        self.sizeOfPolymer = numMonomers
        self.monomers = monomerList

    def build(self, outputName = 'polymer'):
        for monomer in self.directions:
            print(monomer)
            m = Topology.from_ITP(monomer)
            # specify junctions
            # create monomers

        # arg = Topology.from_ITP(data_dir/"arginine.itp")
        # arg_a1 = arg.junction('N3','H20').named("N")
        # arg_a2 = arg.junction('N6','H23').named("N-side-chain")
        # arg_c = arg.junction('C11','O1').named("C")

    
        # glu = Topology.from_ITP(data_dir/"glutamine.itp")
        # glu_N = glu.junction('N1','H6').named("N")
        # glu_C = glu.junction('C4','O1').named("C")
        
        # arg_monomer = Monomer(arg, [arg_a1, arg_a2, arg_c]) # arginine monomer with 3 junctions
        # glu_monomer = Monomer(glu, [glu_N, glu_C]) # glutamine monomer with 2 junctions

        # # create a bond length function that returns 10x the average length of the two bonds to the leaving groups
        # def long_junction_bonds(bond1, bond2):
        #     return (bond1.bond_length + bond2.bond_length)*5

        # # set random seed for reproducibility
        # random.seed(42)
        
        # # start with a randomly selected monomer, 20:80::GLU:ARG
        # if random.random() < 0.2:
        #     polymer = Polymer(glu_monomer)
        #     last_monomer = "glutamine"
        # else:
        #     polymer = Polymer(arg_monomer)
        #     last_monomer = "arginine"
            
        # # add 12 monomers to the polymer backbone alternating         
        # for i in range(12):
        #     if last_monomer == "arginine":
        #         polymer.extend(glu_monomer, from_junction_name= 'N', to_junction_name= 'C', bond_length_func=long_junction_bonds)
        #         last_monomer = "glutamine"
        #     else:
        #         polymer.extend(arg_monomer, from_junction_name= 'N', to_junction_name= 'C', bond_length_func=long_junction_bonds)
        #         last_monomer = "arginine"
        
        # # extend the backbone in both directions with 2 more arginines
        # for i in range(2):
        #     polymer.extend(arg_monomer, from_junction_name= 'N', to_junction_name= 'C', bond_length_func=long_junction_bonds)
        #     polymer.extend(arg_monomer, from_junction_name= 'C', to_junction_name= 'N', bond_length_func=long_junction_bonds)
                    
        # # add another monomer (80:20::GLU:ARG) to the branches of any remaining junction points 3 times
        # countdown = 3
        # while polymer.has_junction("N-side-chain") and countdown > 0:
        #     if random.random() < 0.2:
        #         polymer.extend(arg_monomer, from_junction_name= 'N-side-chain', to_junction_name= 'C', bond_length_func=long_junction_bonds)
        #     else:
        #         polymer.extend(glu_monomer, from_junction_name= 'N-side-chain', to_junction_name= 'C', bond_length_func=long_junction_bonds)            
        #     countdown -= 1
        # polymer.topology.title = "complex polymer"
        # polymer.topology.preamble = ["Generated by PolyTop","Author: Richard A. Morris","pytest: tests/test_polymer.py"]

        # bond_set = set()
        # for bond in polymer.topology.bonds:
        #     bond_set.add(bond)

        # assert len(bond_set) == len(polymer.topology.bonds) # no duplicate bonds
            

        # polymer.save_to_file(output_dir/'polymer.json')
        # polymer_topology = polymer.topology
        # polymer_topology.to_ITP(output_dir/'polymer.itp')
        # Visualize.polymer(polymer,infer_bond_order=False).draw2D(output_dir/'polymer.png',(400,200))
