import os
import platform

class Element:
    def __init__(self, name, symbol, atomic_number, atomic_mass, group, period, state,
                 ionization_energy=None, electron_configuration=None, atomic_radius=None,
                 valence_electrons=None, reactivity=None, isotopes=None, heat_of_fusion=None,
                 heat_of_vaporization=None, crystal_structure=None, electropositivity=None,
                 oxidation_states=None, allotropes=None, color=None, natural_abundance=None,
                 toxicity=None, electronegativity=None, density=None, melting_point=None,
                 boiling_point=None, electron_affinity=None, thermal_conductivity=None,
                 specific_heat_capacity=None, magnetic_properties=None, solubility=None,
                 phase_at_stp=None, isotopic_mass=None, atomic_volume=None, 
                 standard_state=None, covalent_radius=None, atomic_weight=None,
                 lattice_structure=None, chemical_properties=None, spectral_data=None,
                 bonding_type=None, molar_mass=None, electrochemical_series_position=None,
                 acid_base_behavior=None):
        
        self.name = name
        self.symbol = symbol
        self.atomic_number = atomic_number
        self.atomic_mass = atomic_mass
        self.group = group
        self.period = period
        self.state = state
        self.number_of_protons = atomic_number
        self.number_of_electrons = atomic_number
        self.number_of_neutrons = round(atomic_mass - atomic_number)
        self.ionization_energy = ionization_energy
        self.electron_configuration = electron_configuration
        self.atomic_radius = atomic_radius
        self.valence_electrons = valence_electrons
        self.reactivity = reactivity
        self.isotopes = isotopes
        self.heat_of_fusion = heat_of_fusion
        self.heat_of_vaporization = heat_of_vaporization
        self.crystal_structure = crystal_structure
        self.electropositivity = electropositivity
        self.oxidation_states = oxidation_states
        self.allotropes = allotropes
        self.color = color
        self.natural_abundance = natural_abundance
        self.toxicity = toxicity
        self.electronegativity = electronegativity
        self.density = density
        self.melting_point = melting_point
        self.boiling_point = boiling_point
        self.electron_affinity = electron_affinity
        self.thermal_conductivity = thermal_conductivity
        self.specific_heat_capacity = specific_heat_capacity
        self.magnetic_properties = magnetic_properties
        self.solubility = solubility
        self.phase_at_stp = phase_at_stp
        self.isotopic_mass = isotopic_mass
        self.atomic_volume = atomic_volume
        self.standard_state = standard_state
        self.covalent_radius = covalent_radius
        self.atomic_weight = atomic_weight
        self.lattice_structure = lattice_structure
        self.chemical_properties = chemical_properties
        self.spectral_data = spectral_data
        self.bonding_type = bonding_type
        self.molar_mass = molar_mass
        self.electrochemical_series_position = electrochemical_series_position
        self.acid_base_behavior = acid_base_behavior

    def print_details(self):
        print(f"\nElement: {self.name} ({self.symbol})")
        print(f"Atomic Number: {self.atomic_number}")
        print(f"Atomic Mass: {self.atomic_mass}")
        print(f"Group: {self.group}")
        print(f"Period: {self.period}")
        print(f"State: {self.state}")
        print(f"Number of Protons: {self.number_of_protons}")
        print(f"Number of Electrons: {self.number_of_electrons}")
        print(f"Number of Neutrons: {self.number_of_neutrons}")
        print(f"Ionization Energy: {self.ionization_energy}")
        print(f"Electron Configuration: {self.electron_configuration}")
        print(f"Atomic Radius: {self.atomic_radius} pm")
        print(f"Valence Electrons: {self.valence_electrons}")
        print(f"Reactivity: {self.reactivity}")
        print(f"Isotopes: {self.isotopes}")
        print(f"Heat of Fusion: {self.heat_of_fusion} kJ/mol")
        print(f"Heat of Vaporization: {self.heat_of_vaporization} kJ/mol")
        print(f"Crystal Structure: {self.crystal_structure}")
        print(f"Electropositivity: {self.electropositivity}")
        print(f"Oxidation States: {self.oxidation_states}")
        print(f"Allotropes: {self.allotropes}")
        print(f"Color: {self.color}")
        print(f"Natural Abundance: {self.natural_abundance}")
        print(f"Toxicity: {self.toxicity}")
        print(f"Electronegativity: {self.electronegativity}")
        print(f"Density: {self.density} g/cm³")
        print(f"Melting Point: {self.melting_point} K")
        print(f"Boiling Point: {self.boiling_point} K")
        print(f"Electron Affinity: {self.electron_affinity} kJ/mol")
        print(f"Thermal Conductivity: {self.thermal_conductivity} W/m·K")
        print(f"Specific Heat Capacity: {self.specific_heat_capacity} J/g·K")
        print(f"Magnetic Properties: {self.magnetic_properties}")
        print(f"Solubility: {self.solubility}")
        print(f"Phase at STP: {self.phase_at_stp}")
        print(f"Isotopic Mass: {self.isotopic_mass}")
        print(f"Atomic Volume: {self.atomic_volume} cm³/mol")
        print(f"Standard State: {self.standard_state}")
        print(f"Covalent Radius: {self.covalent_radius} pm")
        print(f"Atomic Weight: {self.atomic_weight} g/mol")
        print(f"Lattice Structure: {self.lattice_structure}")
        print(f"Chemical Properties: {self.chemical_properties}")
        print(f"Spectral Data: {self.spectral_data}")
        print(f"Bonding Type: {self.bonding_type}")
        print(f"Molar Mass: {self.molar_mass} g/mol")
        print(f"Electrochemical Series Position: {self.electrochemical_series_position}")
        print(f"Acid-Base Behavior: {self.acid_base_behavior}")

    def clear_screen(self):
        # Clear the console screen
        os.system('cls' if platform.system() == 'Windows' else 'clear')

    def search(self):
        while True:
            attribute = input("\nEnter the attribute you want to search for (or 'all' to see all details, 'help' for options, 'clear' to clear the screen, or 'back' to choose another element): ").strip().lower()
            
            # Define a mapping of attribute names to the actual object attributes
            attributes_mapping = {
                "name": self.name,
                "symbol": self.symbol,
                "atomic_number": self.atomic_number,
                "atomic_mass": self.atomic_mass,
                "group": self.group,
                "period": self.period,
                "state": self.state,
                "ionization_energy": self.ionization_energy,
                "electron_configuration": self.electron_configuration,
                "atomic_radius": self.atomic_radius,
                "valence_electrons": self.valence_electrons,
                "reactivity": self.reactivity,
                "isotopes": self.isotopes,
                "heat_of_fusion": self.heat_of_fusion,
                "heat_of_vaporization": self.heat_of_vaporization,
                "crystal_structure": self.crystal_structure,
                "electropositivity": self.electropositivity,
                "oxidation_states": self.oxidation_states,
                "allotropes": self.allotropes,
                "color": self.color,
                "natural_abundance": self.natural_abundance,
                "toxicity": self.toxicity,
                "electronegativity": self.electronegativity,
                "density": self.density,
                "melting_point": self.melting_point,
                "boiling_point": self.boiling_point,
                "electron_affinity": self.electron_affinity,
                "thermal_conductivity": self.thermal_conductivity,
                "specific_heat_capacity": self.specific_heat_capacity,
                "magnetic_properties": self.magnetic_properties,
                "solubility": self.solubility,
                "phase_at_stp": self.phase_at_stp,
                "isotopic_mass": self.isotopic_mass,
                "atomic_volume": self.atomic_volume,
                "standard_state": self.standard_state,
                "covalent_radius": self.covalent_radius,
                "atomic_weight": self.atomic_weight,
                "lattice_structure": self.lattice_structure,
                "chemical_properties": self.chemical_properties,
                "spectral_data": self.spectral_data,
                "bonding_type": self.bonding_type,
                "molar_mass": self.molar_mass,
                "electrochemical_series_position": self.electrochemical_series_position,
                "acid_base_behavior": self.acid_base_behavior
            }

            if attribute == "all":
                self.print_details()
            elif attribute == "help":
                print("\nAvailable attributes to search for:")
                for key in attributes_mapping.keys():
                    print(f"- {key.replace('_', ' ').capitalize()}")
                print("Type 'all' to see all details.")
            elif attribute == "clear":
                self.clear_screen()
            elif attribute == "back":
                print("\nGoing back to element selection...")
                return  # Exit the search loop to go back to element selection
            elif attribute == "exit":
                print("\nExiting the search.")
                break
            elif attribute in attributes_mapping:
                print(f"\n{attribute.replace('_', ' ').capitalize()}: {attributes_mapping[attribute]}")
            else:
                print(f"\nAttribute '{attribute}' not found. Please enter a valid attribute or 'all'.")

elements = [
    Element(
        name="Hydrogen",
        symbol="H",
        atomic_number=1,
        atomic_mass=1.008,
        group=1,
        period=1,
        state="Gas",
        ionization_energy=1312,
        electron_configuration="1s¹",
        atomic_radius=53,
        valence_electrons=1,
        reactivity="Highly reactive",
        isotopes={"H-1": 99.985, "H-2": 0.015, "H-3": 0.0},
        heat_of_fusion=0.0,
        heat_of_vaporization=0.449,
        crystal_structure="Hexagonal",
        electronegativity=2.20,
        density=0.08988,
        melting_point=14.01,
        boiling_point=20.28,
        electron_affinity=0.754,
        thermal_conductivity=0.1805,
        specific_heat_capacity=14.304,
        magnetic_properties="Diamagnetic",
        solubility="Soluble in water",
        phase_at_stp="Gas",
        isotopic_mass={"H-1": 1.008},
        atomic_volume=11.2,
        standard_state="Gas",
        covalent_radius=37,
        atomic_weight=1.008,
        lattice_structure="Simple cubic",
        chemical_properties={"Combustion": "Produces H₂O"},
        spectral_data={"UV": "Absorbs at 121.6 nm"},
        bonding_type="Covalent",
        molar_mass=1.008,
        electrochemical_series_position=0.0,
        acid_base_behavior="Neutral"
    ),
    Element(
        name="Helium",
        symbol="He",
        atomic_number=2,
        atomic_mass=4.0026,
        group=18,
        period=1,
        state="Gas",
        ionization_energy=2372,
        electron_configuration="1s²",
        atomic_radius=31,
        valence_electrons=0,
        reactivity="Inert",
        isotopes={"He-3": 0.000137, "He-4": 99.999863},
        heat_of_fusion=0.0,
        heat_of_vaporization=0.085,
        crystal_structure="Hexagonal",
        electronegativity=None,
        density=0.1786,
        melting_point=0.95,
        boiling_point=4.22,
        electron_affinity=None,
        thermal_conductivity=0.1513,
        specific_heat_capacity=5.193,
        magnetic_properties="Diamagnetic",
        solubility="Insoluble in water",
        phase_at_stp="Gas",
        isotopic_mass={"He-4": 4.0026},
        atomic_volume=21.2,
        standard_state="Gas",
        covalent_radius=28,
        atomic_weight=4.0026,
        lattice_structure=None,
        chemical_properties={"Combustion": "None"},
        spectral_data={"UV": "Absorbs at 58.4 nm"},
        bonding_type="Atomic",
        molar_mass=4.0026,
        electrochemical_series_position=None,
        acid_base_behavior="Neutral"
    ),
    Element(
        name="Lithium",
        symbol="Li",
        atomic_number=3,
        atomic_mass=6.94,
        group=1,
        period=2,
        state="Solid",
        ionization_energy=520,
        electron_configuration="1s² 2s¹",
        atomic_radius=152,
        valence_electrons=1,
        reactivity="Moderately reactive",
        isotopes={"Li-6": 7.59, "Li-7": 92.41},
        heat_of_fusion=3.0,
        heat_of_vaporization=1342,
        crystal_structure="Body-centered cubic",
        electronegativity=0.98,
        density=0.534,
        melting_point=453.65,
        boiling_point=1560,
        electron_affinity=0.618,
        thermal_conductivity=84.8,
        specific_heat_capacity=3.58,
        magnetic_properties="Diamagnetic",
        solubility="Soluble in water",
        phase_at_stp="Solid",
        isotopic_mass={"Li-7": 7.016},
        atomic_volume=12.01,
        standard_state="Solid",
        covalent_radius=152,
        atomic_weight=6.94,
        lattice_structure="Face-centered cubic",
        chemical_properties={"Combustion": "Forms Li₂O"},
        spectral_data={"UV": "Absorbs at 670.8 nm"},
        bonding_type="Metallic",
        molar_mass=6.94,
        electrochemical_series_position=-3.04,
        acid_base_behavior="Basic"
    ),
    Element(
        name="Beryllium",
        symbol="Be",
        atomic_number=4,
        atomic_mass=9.0122,
        group=2,
        period=2,
        state="Solid",
        ionization_energy=899,
        electron_configuration="1s² 2s²",
        atomic_radius=112,
        valence_electrons=2,
        reactivity="Moderately reactive",
        isotopes={"Be-9": 100.0},
        heat_of_fusion=1.0,
        heat_of_vaporization=2470,
        crystal_structure="Hexagonal",
        electronegativity=1.57,
        density=1.848,
        melting_point=1560,
        boiling_point=2470,
        electron_affinity=0.0,
        thermal_conductivity=200,
        specific_heat_capacity=1.825,
        magnetic_properties="Diamagnetic",
        solubility="Insoluble in water",
        phase_at_stp="Solid",
        isotopic_mass={"Be-9": 9.0122},
        atomic_volume=4.87,
        standard_state="Solid",
        covalent_radius=88,
        atomic_weight=9.0122,
        lattice_structure="Hexagonal",
        chemical_properties={"Combustion": "Forms BeO"},
        spectral_data={"UV": "Absorbs at 313.0 nm"},
        bonding_type="Metallic",
        molar_mass=9.0122,
        electrochemical_series_position=-1.85,
        acid_base_behavior="Amphoteric"
    ),
    Element(
        name="Boron",
        symbol="B",
        atomic_number=5,
        atomic_mass=10.81,
        group=13,
        period=2,
        state="Solid",
        ionization_energy=800,
        electron_configuration="1s² 2s² 2p¹",
        atomic_radius=88,
        valence_electrons=3,
        reactivity="Reactive",
        isotopes={"B-10": 19.9, "B-11": 80.1},
        heat_of_fusion=0.0,
        heat_of_vaporization=4000,
        crystal_structure="Rhombohedral",
        electronegativity=2.04,
        density=2.46,
        melting_point=2075,
        boiling_point=4000,
        electron_affinity=0.0,
        thermal_conductivity=27.4,
        specific_heat_capacity=1.02,
        magnetic_properties="Diamagnetic",
        solubility="Insoluble in water",
        phase_at_stp="Solid",
        isotopic_mass={"B-11": 11.009},
        atomic_volume=4.4,
        standard_state="Solid",
        covalent_radius=82,
        atomic_weight=10.81,
        lattice_structure="Cubic",
        chemical_properties={"Combustion": "Forms B₂O₃"},
        spectral_data={"UV": "Absorbs at 249.0 nm"},
        bonding_type="Covalent",
        molar_mass=10.81,
        electrochemical_series_position=None,
        acid_base_behavior="Amphoteric"
    ),
    Element(
        name="Carbon",
        symbol="C",
        atomic_number=6,
        atomic_mass=12.011,
        group=14,
        period=2,
        state="Solid",
        ionization_energy=1086.5,
        electron_configuration="1s² 2s² 2p²",
        atomic_radius=70,
        valence_electrons=4,
        reactivity="Moderately reactive",
        isotopes={
            "C-12": 98.89,
            "C-13": 1.11,
            "C-14": 0.0000000001,
            "C-15": 0.0,
            "C-16": 0.0,
            "C-17": 0.0,
            "C-18": 0.0,
            "C-19": 0.0
        },
        heat_of_fusion=105,
        heat_of_vaporization=3825,
        crystal_structure="Diamond cubic",
        electronegativity=2.55,
        density=2.267,
        melting_point=3550,
        boiling_point=4027,
        electron_affinity=121,
        thermal_conductivity=200,
        specific_heat_capacity=0.709,
        magnetic_properties="Diamagnetic",
        solubility="Insoluble in water",
        phase_at_stp="Solid",
        isotopic_mass={"C-12": 12.000},
        atomic_volume=5.27,
        standard_state="Graphite",
        covalent_radius=77,
        atomic_weight=12.011,
        lattice_structure="Face-centered cubic",
        chemical_properties={"Combustion": "Produces CO₂", "Oxidation": "Forms CO"},
        spectral_data={"UV": "Absorbs at 200 nm", "IR": "Active in several ranges"},
        bonding_type="Covalent",
        molar_mass=12.011,
        electrochemical_series_position=None,
        acid_base_behavior="Amphoteric"
    ),
    Element(
        name="Nitrogen",
        symbol="N",
        atomic_number=7,
        atomic_mass=14.007,
        group=15,
        period=2,
        state="Gas",
        ionization_energy=1402,
        electron_configuration="1s² 2s² 2p³",
        atomic_radius=65,
        valence_electrons=5,
        reactivity="Moderately reactive",
        isotopes={"N-14": 99.634, "N-15": 0.366},
        heat_of_fusion=0.0,
        heat_of_vaporization=0.012,
        crystal_structure="Cubic",
        electronegativity=3.04,
        density=0.00125,
        melting_point=63.15,
        boiling_point=77.36,
        electron_affinity=0.07,
        thermal_conductivity=0.024,
        specific_heat_capacity=1.04,
        magnetic_properties="Diamagnetic",
        solubility="Slightly soluble in water",
        phase_at_stp="Gas",
        isotopic_mass={"N-14": 14.003},
        atomic_volume=34.4,
        standard_state="Gas",
        covalent_radius=70,
        atomic_weight=14.007,
        lattice_structure=None,
        chemical_properties={"Combustion": "Forms NO₂"},
        spectral_data={"UV": "Absorbs at 253.7 nm"},
        bonding_type="Covalent",
        molar_mass=14.007,
        electrochemical_series_position=None,
        acid_base_behavior="Basic"
    ), Element(
        name="Oxygen",
        symbol="O",
        atomic_number=8,
        atomic_mass=15.999,
        group=16,
        period=2,
        state="Gas",
        ionization_energy=1314,
        electron_configuration="1s² 2s² 2p⁴",
        atomic_radius=60,
        valence_electrons=6,
        reactivity="Highly reactive",
        isotopes={"O-16": 99.757, "O-17": 0.037, "O-18": 0.205},
        heat_of_fusion=0.0,
        heat_of_vaporization=0.018,
        crystal_structure="Cubic",
        electronegativity=3.44,
        density=0.001429,
        melting_point=54.36,
        boiling_point=90.20,
        electron_affinity=1.46,
        thermal_conductivity=0.025,
        specific_heat_capacity=0.918,
        magnetic_properties="Paramagnetic",
        solubility="Soluble in water",
        phase_at_stp="Gas",
        isotopic_mass={"O-16": 15.994},
        atomic_volume=31.9,
        standard_state="Gas",
        covalent_radius=60,
        atomic_weight=15.999,
        lattice_structure=None,
        chemical_properties={"Combustion": "Forms CO₂"},
        spectral_data={"UV": "Absorbs at 253.7 nm"},
        bonding_type="Covalent",
        molar_mass=15.999,
        electrochemical_series_position=None,
        acid_base_behavior="Basic"
    ),
    Element(
        name="Fluorine",
        symbol="F",
        atomic_number=9,
        atomic_mass=18.998,
        group=17,
        period=2,
        state="Gas",
        ionization_energy=1681,
        electron_configuration="1s² 2s² 2p⁵",
        atomic_radius=50,
        valence_electrons=7,
        reactivity="Highly reactive",
        isotopes={"F-19": 100.0},
        heat_of_fusion=0.0,
        heat_of_vaporization=0.019,
        crystal_structure="Cubic",
        electronegativity=3.98,
        density=0.001696,
        melting_point=53.53,
        boiling_point=85.03,
        electron_affinity=3.40,
        thermal_conductivity=0.025,
        specific_heat_capacity=0.82,
        magnetic_properties="Diamagnetic",
        solubility="Slightly soluble in water",
        phase_at_stp="Gas",
        isotopic_mass={"F-19": 18.998},
        atomic_volume=30.4,
        standard_state="Gas",
        covalent_radius=50,
        atomic_weight=18.998,
        lattice_structure=None,
        chemical_properties={"Combustion": "Forms HF"},
        spectral_data={"UV": "Absorbs at 253.7 nm"},
        bonding_type="Covalent",
        molar_mass=18.998,
        electrochemical_series_position=None,
        acid_base_behavior="Acidic"
    ),
    Element(
        name="Neon",
        symbol="Ne",
        atomic_number=10,
        atomic_mass=20.180,
        group=18,
        period=2,
        state="Gas",
        ionization_energy=2080,
        electron_configuration="1s² 2s² 2p⁶",
        atomic_radius=38,
        valence_electrons=0,
        reactivity="Inert",
        isotopes={"Ne-20": 90.48, "Ne-21": 0.27, "Ne-22": 9.25},
        heat_of_fusion=0.0,
        heat_of_vaporization=1.2,
        crystal_structure="Cubic",
        electronegativity=None,
        density=0.0008999,
        melting_point=24.56,
        boiling_point=27.07,
        electron_affinity=None,
        thermal_conductivity=0.049,
        specific_heat_capacity=1.03,
        magnetic_properties="Diamagnetic",
        solubility="Insoluble in water",
        phase_at_stp="Gas",
        isotopic_mass={"Ne-20": 19.992},
        atomic_volume=22.4,
        standard_state="Gas",
        covalent_radius=38,
        atomic_weight=20.180,
        lattice_structure=None,
        chemical_properties={"Combustion": "None"},
        spectral_data={"UV": "Absorbs at 540.0 nm"},
        bonding_type="Atomic",
        molar_mass=20.180,
        electrochemical_series_position=None,
        acid_base_behavior="Neutral"
    ),
    Element(
        name="Sodium",
        symbol="Na",
        atomic_number=11,
        atomic_mass=22.990,
        group=1,
        period=3,
        state="Solid",
        ionization_energy=496,
        electron_configuration="1s² 2s² 2p⁶ 3s¹",
        atomic_radius=186,
        valence_electrons=1,
        reactivity="Highly reactive",
        isotopes={"Na-23": 100.0},
        heat_of_fusion=2.59,
        heat_of_vaporization=97.79,
        crystal_structure="Body-centered cubic",
        electronegativity=0.93,
        density=0.968,
        melting_point=370.87,
        boiling_point=883,
        electron_affinity=0.548,
        thermal_conductivity=140,
        specific_heat_capacity=1.228,
        magnetic_properties="Paramagnetic",
        solubility="Soluble in water",
        phase_at_stp="Solid",
        isotopic_mass={"Na-23": 22.989},
        atomic_volume=23.7,
        standard_state="Solid",
        covalent_radius=166,
        atomic_weight=22.990,
        lattice_structure="Face-centered cubic",
        chemical_properties={"Combustion": "Forms Na₂O"},
        spectral_data={"UV": "Absorbs at 589.0 nm"},
        bonding_type="Metallic",
        molar_mass=22.990,
        electrochemical_series_position=-2.71,
        acid_base_behavior="Basic"
    ),
    Element(
        name="Magnesium",
        symbol="Mg",
        atomic_number=12,
        atomic_mass=24.305,
        group=2,
        period=3,
        state="Solid",
        ionization_energy=738,
        electron_configuration="1s² 2s² 2p⁶ 3s²",
        atomic_radius=160,
        valence_electrons=2,
        reactivity="Moderately reactive",
        isotopes={"Mg-24": 78.99, "Mg-25": 10.00, "Mg-26": 11.01},
        heat_of_fusion=6.0,
        heat_of_vaporization=1090,
        crystal_structure="Hexagonal",
        electronegativity=1.31,
        density=1.738,
        melting_point=923,
        boiling_point=1380,
        electron_affinity=0.0,
        thermal_conductivity=156,
        specific_heat_capacity=1.017,
        magnetic_properties="Diamagnetic",
        solubility="Insoluble in water",
        phase_at_stp="Solid",
        isotopic_mass={"Mg-24": 23.985},
        atomic_volume=14.2,
        standard_state="Solid",
        covalent_radius=130,
        atomic_weight=24.305,
        lattice_structure="Hexagonal",
        chemical_properties={"Combustion": "Forms MgO"},
        spectral_data={"UV": "Absorbs at 285.2 nm"},
        bonding_type="Metallic",
        molar_mass=24.305,
        electrochemical_series_position=-2.37,
        acid_base_behavior="Basic"
    )
]

# Start the element selection functionality
while True:
    print("\nAvailable Elements:")
    for element in elements:
        print(f"- {element.name}")

    element_name = input("\nEnter the name of the element you want to check (or 'exit' to quit): ").strip().lower()
    
    if element_name == "exit":
        print("\nExiting the element search.")
        break
    
    # Search for the element by name
    found = False
    for element in elements:
        if element.name.lower() == element_name:
            element.search()
            found = True
            break

    if not found:
        print(f"\nElement '{element_name}' not found. Please enter a valid element name.")
