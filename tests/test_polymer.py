    
from polytop.monomer import Monomer
from polytop.polymer import Polymer
from polytop.topology import Topology


def test_polymer():    
    arg = Topology.from_ITP("tests/samples/arginine.itp")
    glu = Topology.from_ITP("tests/samples/glutamine.itp")
    arg_monomer = Monomer(arg, arg.get_bond_by_name('N3','H20'), arg.get_bond_by_name('C11','O1'))
    
    glu_monomer = Monomer(glu, glu.get_bond_by_name('N1','H6'), glu.get_bond_by_name('C4','O1'))
    
    polymer = Polymer([arg_monomer,glu_monomer], [20,80], num_monomers= 12, seed= 42, start_monomer= arg_monomer)
    polymer.save_to_file('tests/samples/polymer.json')
    polymer_topology = polymer.get_topology()