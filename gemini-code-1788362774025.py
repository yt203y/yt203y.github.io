import os

# Define publication dataset
publications = [
    {
        "filename": "2021-01-01-octadist-tool-calculating-distortion.md",
        "title": "OctaDist: A tool for calculating distortion parameters in spin crossover and coordination complexes",
        "permalink": "/publication/2021-octadist-tool-calculating-distortion",
        "excerpt": "A cross-platform tool designed to compute octahedral distortion parameters in spin crossover and coordination chemistry systems.",
        "date": "2021-01-01",
        "venue": "Dalton Transactions",
        "citation": "Tantirungrotechai, Y., et al. (2021). &quot;OctaDist: A tool for calculating distortion parameters in spin crossover and coordination complexes.&quot; <i>Dalton Transactions</i>, 50(3), 1086–1096.",
        "body": "OctaDist provides automated calculations for octahedral distortion parameters ($\\\\zeta$, $\\\\Sigma$, and $\\\\Theta$) in transition metal coordination complexes and spin-crossover compounds."
    },
    {
        "filename": "2026-01-01-enhanced-cooperative-lithium-halide.md",
        "title": "Enhanced Cooperative Lithium Halide Recognition by Heteroditopic Halogen Bonding (XB) Macrocycles",
        "permalink": "/publication/2026-enhanced-cooperative-lithium-halide",
        "excerpt": "Investigation of heteroditopic halogen-bonding macrocycles for selective lithium halide extraction.",
        "date": "2026-01-01",
        "venue": "Inorganic Chemistry",
        "citation": "Tantirungrotechai, Y., et al. (2026). &quot;Enhanced Cooperative Lithium Halide Recognition by Heteroditopic Halogen Bonding (XB) Macrocycles.&quot; <i>Inorganic Chemistry</i>, 65(1), 441–453.",
        "body": "Density functional theory (DFT) calculations and experimental methods were employed to assess cooperative binding and halogen bonding interactions in macrocyclic host systems for lithium halide recognition."
    },
    {
        "filename": "2023-09-01-room-temperature-lewis-acid.md",
        "title": "Room-Temperature Lewis Acid Organocatalysts for Bulk Ring-Opening Polymerization",
        "permalink": "/publication/2023-room-temperature-lewis-acid",
        "excerpt": "Exploration of organocatalysts for ambient-temperature ring-opening polymerization reactions.",
        "date": "2023-09-01",
        "venue": "Macromolecular Chemistry and Physics",
        "citation": "Tantirungrotechai, Y., et al. (2023). &quot;Room-Temperature Lewis Acid Organocatalysts for Bulk Ring-Opening Polymerization.&quot; <i>Macromolecular Chemistry and Physics</i>, 224(17).",
        "body": "This study evaluates Lewis acid organocatalysts capable of initiating solvent-free ring-opening polymerization at room temperature."
    },
    {
        "filename": "2017-12-01-microwave-assisted-one-pot.md",
        "title": "Microwave-assisted one-pot functionalization of metal-organic framework MIL-53(Al)-NH2",
        "permalink": "/publication/2017-microwave-assisted-one-pot",
        "excerpt": "Efficient microwave-driven synthesis and functionalization of functionalized aluminum-based MOFs.",
        "date": "2017-12-01",
        "venue": "Catalysis Science & Technology",
        "citation": "Tantirungrotechai, Y., et al. (2017). &quot;Microwave-assisted one-pot functionalization of metal-organic framework MIL-53(Al)-NH2.&quot; <i>Catalysis Science & Technology</i>, 7(24), 6069–6079.",
        "body": "Demonstrates a streamlined, one-pot microwave synthetic route to modify the internal pore environment of MIL-53(Al)-NH2 for catalytic applications."
    },
    {
        "filename": "2014-12-01-mechanism-ni-nhc-catalyst.md",
        "title": "Mechanism of Ni N-heterocyclic carbene catalyst for C-O bond hydrogenolysis of diphenyl ether",
        "permalink": "/publication/2014-mechanism-ni-nhc-catalyst",
        "excerpt": "DFT computational study on the pathway of Ni-NHC mediated C–O cleavage in ether model compounds.",
        "date": "2014-12-01",
        "venue": "Dalton Transactions",
        "citation": "Tantirungrotechai, Y., et al. (2014). &quot;Mechanism of Ni N-heterocyclic carbene catalyst for C-O bond hydrogenolysis of diphenyl ether.&quot; <i>Dalton Transactions</i>, 43(48), 18123–18133.",
        "body": "Quantum chemical modeling of the nickel N-heterocyclic carbene-catalyzed hydrogenolysis mechanism targeting aryl C–O bond cleavage in biomass-derived ether models."
    },
    {
        "filename": "2010-09-01-dft-investigation-triacetin.md",
        "title": "A DFT investigation of methanolysis and hydrolysis of triacetin",
        "permalink": "/publication/2010-dft-investigation-triacetin",
        "excerpt": "Comparative DFT study on transesterification and hydrolysis reactions of short-chain triglycerides.",
        "date": "2010-09-01",
        "venue": "Journal of Molecular Structure: THEOCHEM",
        "citation": "Tantirungrotechai, Y., et al. (2010). &quot;A DFT investigation of methanolysis and hydrolysis of triacetin.&quot; <i>Journal of Molecular Structure: THEOCHEM</i>, 955(1-3), 23–32.",
        "body": "Detailed energy profiles and catalytic pathways for acid/base-catalyzed methanolysis and hydrolysis of triacetin."
    },
    {
        "filename": "2010-04-01-performance-dft-dispersion-zeolite.md",
        "title": "Performance study of DFT with empirical dispersion corrections on adsorbate-zeolite interactions",
        "permalink": "/publication/2010-performance-dft-dispersion-zeolite",
        "excerpt": "Benchmarking dispersion-corrected DFT methods (DFT-D) against experimental adsorption energies in zeolites.",
        "date": "2010-04-01",
        "venue": "Journal of Molecular Structure: THEOCHEM",
        "citation": "Tantirungrotechai, Y., et al. (2010). &quot;Performance study of DFT with empirical dispersion corrections... on adsorbate-zeolite interactions.&quot; <i>Journal of Molecular Structure: THEOCHEM</i>, 945(1-3), 85–88.",
        "body": "Evaluates the accuracy of Grimme-type empirical dispersion corrections applied to density functional theory for non-covalent interactions in microporous zeolitic cavities."
    },
    {
        "filename": "2009-09-01-mechanistic-investigation-dimethylnaphthalene-zeolite.md",
        "title": "Mechanistic investigation on 1,5- to 2,6-dimethylnaphthalene isomerization catalyzed by acidic beta zeolite: ONIOM study",
        "permalink": "/publication/2009-mechanistic-investigation-dimethylnaphthalene-zeolite",
        "excerpt": "Hybrid ONIOM QM/MM computational modeling of alkyl shift isomerization inside H-Beta zeolite pores.",
        "date": "2009-09-01",
        "venue": "Journal of Physical Chemistry C",
        "citation": "Tantirungrotechai, Y., et al. (2009). &quot;Mechanistic investigation on 1,5- to 2,6-dimethylnaphthalene isomerization catalyzed by acidic beta zeolite: ONIOM study.&quot; <i>Journal of Physical Chemistry C</i>, 113(36), 16128–16137.",
        "body": "Uses a two-layer ONIOM methodology to examine steric confinement and electronic factors governing dimethylnaphthalene isomerization in acidic zeolite channels."
    },
    {
        "filename": "2000-02-01-dielectric-virial-coefficient-potentials.md",
        "title": "The dielectric virial coefficient and model intermolecular potentials",
        "permalink": "/publication/2000-dielectric-virial-coefficient-potentials",
        "excerpt": "Theoretical analysis linking dielectric virial coefficients to intermolecular potential energy surfaces.",
        "date": "2000-02-01",
        "venue": "Physical Chemistry Chemical Physics",
        "citation": "Tantirungrotechai, Y., et al. (2000). &quot;The dielectric virial coefficient and model intermolecular potentials.&quot; <i>Physical Chemistry Chemical Physics</i>, 2(4), 429–434.",
        "body": "Theoretical derivations and numerical simulations connecting the second dielectric virial coefficient ($B_\\\\epsilon$) with anisotropic pair potentials."
    },
    {
        "filename": "1999-11-01-second-dielectric-virial-gay-berne.md",
        "title": "The second dielectric virial coefficient of the dipolar Gay–Berne fluid",
        "permalink": "/publication/1999-second-dielectric-virial-gay-berne",
        "excerpt": "Statistical mechanical study of electrostatic and orientation effects in anisotropic Gay-Berne fluids.",
        "date": "1999-11-01",
        "venue": "Canadian Journal of Chemistry",
        "citation": "Tantirungrotechai, Y., et al. (1999). &quot;The second dielectric virial coefficient of the dipolar Gay–Berne fluid.&quot; <i>Canadian Journal of Chemistry</i>, 77(11), 1946–1950.",
        "body": "Calculations of $B_\\\\epsilon$ for non-spherical dipolar particles using the Gay-Berne model potential."
    },
    {
        "filename": "2006-01-01-scaling-factors-vibrational-frequencies.md",
        "title": "Scaling factors for vibrational frequencies and zero-point vibrational energies of recently developed functionals",
        "permalink": "/publication/2006-scaling-factors-vibrational-frequencies",
        "excerpt": "Harmonic frequency and ZPE scale factors derived across modern density functional theory approximations.",
        "date": "2006-01-01",
        "venue": "Journal of Molecular Structure: THEOCHEM",
        "citation": "Tantirungrotechai, Y., et al. (2006). &quot;Scaling factors for vibrational frequencies and zero-point vibrational energies of recently developed functionals.&quot; <i>Journal of Molecular Structure: THEOCHEM</i>, 760(1-3), 189–192.",
        "body": "Systematic optimization of empirical scaling factors for infrared frequencies and zero-point energies using modern exchange-correlation functionals."
    },
    {
        "filename": "2002-10-01-proton-shielding-benzene-complexes.md",
        "title": "Proton shielding calculations in C6H6...H-CX3 complexes",
        "permalink": "/publication/2002-proton-shielding-benzene-complexes",
        "excerpt": "Ab initio nuclear magnetic shielding computations for C-H...pi hydrogen-bonded molecular complexes.",
        "date": "2002-10-01",
        "venue": "Physical Chemistry Chemical Physics",
        "citation": "Tantirungrotechai, Y., et al. (2002). &quot;Proton shielding calculations in C6H6...H-CX3 complexes.&quot; <i>Physical Chemistry Chemical Physics</i>, 4(19), 4619–4622.",
        "body": "GIAO-DFT calculations analyzing changes in $^1\\\\text{H}$ NMR chemical shielding tensors induced by $\\\\text{C–H}\\\\cdots\\\\pi$ interactions with benzene."
    },
    {
        "filename": "1999-12-01-molecular-electric-properties-dft.md",
        "title": "Molecular electric properties: An assessment of recently developed functionals",
        "permalink": "/publication/1999-molecular-electric-properties-dft",
        "excerpt": "Benchmarking dipole moments and polarizabilities predicted by early-generation DFT functionals.",
        "date": "1999-12-01",
        "venue": "Chemical Physics Letters",
        "citation": "Tantirungrotechai, Y., et al. (1999). &quot;Molecular electric properties: An assessment of recently developed functionals.&quot; <i>Chemical Physics Letters</i>, 299(5), 465–472.",
        "body": "Assessment of exchange-correlation functionals for predicting molecular dipole moments, static polarizabilities, and hyperpolarizabilities."
    },
    {
        "filename": "2023-10-01-iridium-complexes-luminescence-sensing.md",
        "title": "Iridium(III) complexes based on cyanomethane and cyanamide ligands with luminescence quenching properties for Fe(III) sensing",
        "permalink": "/publication/2023-iridium-complexes-luminescence-sensing",
        "excerpt": "Design and photophysical investigation of Ir(III) complexes for turn-off ferric ion luminescence detection.",
        "date": "2023-10-01",
        "venue": "Polyhedron",
        "citation": "Tantirungrotechai, Y., et al. (2023). &quot;Iridium(III) complexes based on cyanomethane and cyanamide ligands with luminescence quenching properties for Fe(III) sensing.&quot; <i>Polyhedron</i>, 243, 116540.",
        "body": "Synthesized nitrile/cyanamide-bound $\\\\text{Ir(III)}$ complexes and characterized their selective emission quenching in the presence of $\\\\text{Fe}^{3+}$ ions."
    },
    {
        "filename": "2021-09-01-half-sandwich-ruthenium-complexes.md",
        "title": "Half-sandwich ruthenium (II) p-cymene complexes based on organophosphorus ligands",
        "permalink": "/publication/2021-half-sandwich-ruthenium-complexes",
        "excerpt": "Synthesis, characterization, and structural properties of organophosphorus Ru(II) arena complexes.",
        "date": "2021-09-01",
        "venue": "Polyhedron",
        "citation": "Tantirungrotechai, Y., et al. (2021). &quot;Half-sandwich ruthenium (II) p-cymene complexes based on organophosphorus ligands.&quot; <i>Polyhedron</i>, 204, 115244.",
        "body": "Structural and spectroscopic characterization of piano-stool ruthenium(II) $p$-cymene complexes bearing tertiary phosphine/phosphite ligands."
    },
    {
        "filename": "2012-09-01-redox-coupled-spin-crossover-cobalt.md",
        "title": "Redox coupled-spin crossover in cobalt beta-diketonate complexes",
        "permalink": "/publication/2012-redox-coupled-spin-crossover-cobalt",
        "excerpt": "Spectroscopic and magnetic study of valence tautomerism and spin transitions in Co complexes.",
        "date": "2012-09-01",
        "venue": "Polyhedron",
        "citation": "Tantirungrotechai, Y., et al. (2012). &quot;Redox coupled-spin crossover in cobalt beta-diketonate complexes.&quot; <i>Polyhedron</i>, 42(1), 291–301.",
        "body": "Investigation of electron transfer coupled with spin state switching in cobalt $\\\\beta$-diketonate coordination architectures."
    },
    {
        "filename": "2012-02-01-photoactive-azoimine-dyes.md",
        "title": "Photoactive azoimine dyes: Computational and experimental investigation",
        "permalink": "/publication/2012-photoactive-azoimine-dyes",
        "excerpt": "Combined TD-DFT and experimental characterization of electronic transitions in azoimine dyes.",
        "date": "2012-02-01",
        "venue": "Spectrochimica Acta Part A: Molecular and Biomolecular Spectroscopy",
        "citation": "Tantirungrotechai, Y., et al. (2012). &quot;Photoactive azoimine dyes: Computational and experimental investigation.&quot; <i>Spectrochimica Acta Part A</i>, 86, 538–546.",
        "body": "Time-dependent density functional theory (TD-DFT) modeling of UV-Vis absorption spectra and photoisomerization processes in functionalized azoimine systems."
    },
    {
        "filename": "2012-08-01-exploring-photochemistry-phenylazopyridine.md",
        "title": "Exploring photochemistry of 2-(phenylazo)pyridine dye by using TDDFT/DFT methods",
        "permalink": "/publication/2012-exploring-photochemistry-phenylazopyridine",
        "excerpt": "Theoretical evaluation of cis-trans photoisomerization pathways in 2-(phenylazo)pyridine.",
        "date": "2012-08-01",
        "venue": "Canadian Journal of Chemical Engineering",
        "citation": "Tantirungrotechai, Y., et al. (2012). &quot;Exploring photochemistry of 2-(phenylazo)pyridine dye by using TDDFT/DFT methods.&quot; <i>Canadian Journal of Chemical Engineering</i>, 90(4), 860–864.",
        "body": "Calculated potential energy surfaces for ground and low-lying excited states governing the photochemical conversion of phenylazopyridine derivatives."
    },
    {
        "filename": "2026-01-01-pectin-bcg-film-sensor-gaba.md",
        "title": "Eco-friendly pectin/BCG film sensor: a smartphone-compatible platform for GABA detection",
        "permalink": "/publication/2026-pectin-bcg-film-sensor-gaba",
        "excerpt": "Development of a biopolymer optical sensor coupled with smartphone colorimetry for GABA quantification.",
        "date": "2026-01-01",
        "venue": "Microchemical Journal",
        "citation": "Tantirungrotechai, Y., et al. (2026). &quot;Eco-friendly pectin/BCG film sensor: a smartphone-compatible platform for GABA detection.&quot; <i>Microchemical Journal</i>, 224, 117881.",
        "body": "Fabrication of a pectin-bromocresol green (BCG) composite film used as a portable, eco-friendly colorimetric test strip for GABA analysis via digital image processing."
    },
    {
        "filename": "2025-05-01-dye-adsorption-mcm41.md",
        "title": "Dye adsorption selectivity in pristine and aluminum-doped MCM-41 mesoporous silica",
        "permalink": "/publication/2025-dye-adsorption-mcm41",
        "excerpt": "Computational and experimental assessment of dye uptake selectivity in mesoporous silica systems.",
        "date": "2025-05-01",
        "venue": "Polyhedron",
        "citation": "Tantirungrotechai, Y., et al. (2025). &quot;Dye adsorption selectivity in pristine and aluminum-doped MCM-41 mesoporous silica.&quot; <i>Polyhedron</i>, 279, 117651.",
        "body": "Analyzes the effect of framework Al-substitution on the surface electrostatic potential and selective dye binding capacity of MCM-41 material."
    },
    {
        "filename": "2025-03-01-theoretical-study-graphene-quantum-dots.md",
        "title": "Theoretical study of hydrogen/methyl chalcogenides adsorption on pristine/doped GQDs",
        "permalink": "/publication/2025-theoretical-study-graphene-quantum-dots",
        "excerpt": "DFT study of gas sensing capabilities of functionalized graphene quantum dots toward volatile chalcogenides.",
        "date": "2025-03-01",
        "venue": "Chemical Papers",
        "citation": "Tantirungrotechai, Y., et al. (2025). &quot;Theoretical study of hydrogen/methyl chalcogenides adsorption on pristine/doped GQDs.&quot; <i>Chemical Papers</i>, 79(3), 1577–1600.",
        "body": "Evaluates adsorption energies, charge transfer, and electronic response of heteroatom-doped graphene quantum dots exposed to trace sulfide and selenide species."
    },
    {
        "filename": "2026-02-01-gibellula-scorpioides-metabolites.md",
        "title": "Chemical and biological profiling of bioactive metabolites from Gibellula scorpioides",
        "permalink": "/publication/2026-gibellula-scorpioides-metabolites",
        "excerpt": "Isolation, structure elucidation, and bioactivity evaluation of natural products from entomopathogenic fungi.",
        "date": "2026-02-01",
        "venue": "Scientific Reports",
        "citation": "Tantirungrotechai, Y., et al. (2026). &quot;Chemical and biological profiling of bioactive metabolites from Gibellula scorpioides.&quot; <i>Scientific Reports</i>, 16(1), 35326.",
        "body": "Spectroscopic characterization and biological activity testing of fungal secondary metabolites extracted from *Gibellula scorpioides*."
    },
    {
        "filename": "2024-03-01-nanostructured-lipid-carriers-stability.md",
        "title": "Effect of Functional Groups in Lipid Molecules on Stability of Nanostructured Lipid Carriers",
        "permalink": "/publication/2024-nanostructured-lipid-carriers-stability",
        "excerpt": "Molecular dynamics and experimental investigation of lipid functional groups on NLC drug carrier formulation.",
        "date": "2024-03-01",
        "venue": "ACS Omega",
        "citation": "Tantirungrotechai, Y., et al. (2024). &quot;Effect of Functional Groups in Lipid Molecules on Stability of Nanostructured Lipid Carriers.&quot; <i>ACS Omega</i>, 9(9), 11012–11024.",
        "body": "Molecular dynamics simulations examining surfactant-lipid interactions and nanoparticle phase stability in nanostructured lipid carrier formulations."
    },
    {
        "filename": "2019-07-01-in-silico-mitragynine-metabolism.md",
        "title": "In silico investigation of mitragynine and 7-hydroxymitragynine metabolism",
        "permalink": "/publication/2019-in-silico-mitragynine-metabolism",
        "excerpt": "Computational modeling of cytochrome P450-mediated metabolic pathways of primary Kratom alkaloids.",
        "date": "2019-07-01",
        "venue": "BMC Research Notes",
        "citation": "Tantirungrotechai, Y., et al. (2019). &quot;In silico investigation of mitragynine and 7-hydroxymitragynine metabolism.&quot; <i>BMC Research Notes</i>, 12(1), 4461.",
        "body": "Docking and reactivity predictions for major bioactive alkaloids from *Mitragyna speciosa* interacting with hepatic CYP enzyme isoforms."
    },
    {
        "filename": "2018-06-01-md-study-pdgf-aptamer.md",
        "title": "Effect of PDGF-B aptamer on PDGFRbeta/PDGF-B interaction: MD study",
        "permalink": "/publication/2018-md-study-pdgf-aptamer",
        "excerpt": "Atomistic molecular dynamics study on aptamer-mediated inhibition of growth factor receptor binding.",
        "date": "2018-06-01",
        "venue": "Journal of Molecular Graphics and Modelling",
        "citation": "Tantirungrotechai, Y., et al. (2018). &quot;Effect of PDGF-B aptamer on PDGFRbeta/PDGF-B interaction: MD study.&quot; <i>Journal of Molecular Graphics and Modelling</i>, 82, 145–156.",
        "body": "Simulations revealing binding energetics, conformational stability, and competitive inhibition mechanisms of a DNA aptamer targeting PDGF-BB."
    }
]

output_dir = "_publications"

# Create directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Generate individual markdown files
for pub in publications:
    file_path = os.path.join(output_dir, pub["filename"])
    content = f"""---
title: "{pub['title']}"
collection: publications
permalink: {pub['permalink']}
excerpt: '{pub['excerpt']}'
date: {pub['date']}
venue: '{pub['venue']}'
paperurl: ''
citation: '{pub['citation']}'
---

{pub['body']}
"""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Successfully generated {len(publications)} publication Markdown files in '{output_dir}/'.")