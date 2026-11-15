"""
Generates:
1. data/revision/physics/physics-revision.md
2. data/revision/chemistry/chemistry-revision.md
"""
import os

os.makedirs("data/revision/physics", exist_ok=True)
os.makedirs("data/revision/chemistry", exist_ok=True)

# 1. physics-revision.md
PHYSICS_MD = """# General Science – Physics Revision Notes & Formula Cheat Sheet
> **Exam-Ready Reference | Competitive Exams (RRB ALP, CDS, CAPF, SSC, State PSC)**

---

## 1. UNITS & DIMENSIONS CHEAT SHEET

| Physical Quantity | SI Unit | Dimensional Formula | Key Relation |
| :--- | :--- | :---: | :--- |
| **Force** | Newton (N) | $[M L T^{-2}]$ | $F = m \\cdot a$ ($1 \\text{ N} = 10^5 \\text{ dynes}$) |
| **Work / Energy** | Joule (J) | $[M L^2 T^{-2}]$ | $W = F \\cdot d$ ($1 \\text{ J} = 10^7 \\text{ ergs}$) |
| **Power** | Watt (W) | $[M L^2 T^{-3}]$ | $P = W / t$ ($1 \\text{ HP} = 746 \\text{ W}$) |
| **Pressure / Stress**| Pascal (Pa) | $[M L^{-1} T^{-2}]$ | $P = F / A$ ($1 \\text{ bar} = 10^5 \\text{ Pa}$) |
| **Electric Charge** | Coulomb (C) | $[I T]$ | $Q = I \\cdot t$ |
| **Electric Potential**| Volt (V) | $[M L^2 T^{-3} I^{-1}]$ | $V = W / Q$ |
| **Resistance** | Ohm ($\\Omega$) | $[M L^2 T^{-3} I^{-2}]$ | $R = V / I$ |

---

## 2. MOTION & MECHANICS FORMULAS

### Equations of Uniformly Accelerated Motion
$$v = u + at$$
$$s = ut + \\frac{1}{2}at^2$$
$$v^2 = u^2 + 2as$$
$$s_n = u + \\frac{a}{2}(2n - 1) \\quad (\\text{Distance in } n\\text{-th second})$$

* **Under Gravity (Vertical Motion):** Replace $a$ with $+g$ (downward) or $-g$ (upward). $g \\approx 9.8 \\text{ m/s}^2$.
* **Max Height Reached:** $H_{\\max} = \\frac{u^2}{2g}$
* **Time of Flight:** $T = \\frac{2u}{g}$

---

## 3. GRAVITATION & SATELLITE DYNAMICS
* **Universal Law of Gravitation:** $F = G \\frac{m_1 m_2}{r^2} \\quad (G = 6.674 \\times 10^{-11} \\text{ N}\\cdot\\text{m}^2/\\text{kg}^2)$
* **Acceleration Due to Gravity:** $g = \\frac{GM}{R^2}$
  * Variation with Height $h$: $g' = g\\left(1 - \\frac{2h}{R}\\right)$
  * Variation with Depth $d$: $g' = g\\left(1 - \\frac{d}{R}\\right) \\implies g = 0 \\text{ at Earth's center!}$
  * $g$ is maximum at **Poles** and minimum at **Equator** due to Earth's equatorial bulge and rotation.
* **Escape Velocity from Earth:** $v_e = \\sqrt{2gR} \\approx 11.2 \\text{ km/s}$
* **Orbital Velocity:** $v_o = \\sqrt{gR} \\approx 7.92 \\text{ km/s} \\implies v_e = \\sqrt{2} \\cdot v_o$
* **Geostationary Satellite:** Altitude $\\approx 35,786 \\text{ km}$, orbital period = 24 hours, rotates West to East.

---

## 4. WORK, ENERGY & POWER
* **Kinetic Energy:** $KE = \\frac{1}{2}mv^2 = \\frac{p^2}{2m}$ *(where $p = mv$ is momentum)*.
  * *Trap:* If momentum increases by 100%, KE increases by $300\\%$.
* **Potential Energy:** $PE = mgh$
* **Work-Energy Theorem:** Net work done on an object equals its change in kinetic energy: $W_{\\text{net}} = \\Delta KE$.

---

## 5. OPTICS & LIGHT

### Mirrors and Lenses Formulas
* **Mirror Formula:** $\\frac{1}{f} = \\frac{1}{v} + \\frac{1}{u}$ (Magnification $m = -\\frac{v}{u}$)
* **Lens Formula:** $\\frac{1}{f} = \\frac{1}{v} - \\frac{1}{u}$ (Magnification $m = +\\frac{v}{u}$)
* **Power of a Lens:** $P = \\frac{1}{f \\text{ (in meters)}}$ (Unit: Dioptre, D).
  * Convex Lens: $f > 0, P > 0$ (Converging).
  * Concave Lens: $f < 0, P < 0$ (Diverging).

### Human Eye Defects & Corrective Lenses
| Eye Defect | Symptoms | Cause | Corrective Lens |
| :--- | :--- | :--- | :--- |
| **Myopia** (Near-sightedness) | Cannot see distant objects clearly | Elongated eyeball; focal length too short | **Concave Lens** |
| **Hypermetropia** (Far-sightedness) | Cannot see nearby objects clearly | Eyeball too short; focal length too long | **Convex Lens** |
| **Presbyopia** (Old-age sight) | Ciliary muscles lose flexibility | Aging | **Bifocal Lens** |
| **Astigmatism** | Cannot focus on horizontal/vertical simultaneously | Irregular cornea curvature | **Cylindrical Lens** |

* **Total Internal Reflection (TIR):** Occurs when light travels from denser to rarer medium and angle of incidence $>$ critical angle.
  * *Applications:* Optical fibers, mirages in deserts, sparkling of diamonds, endoscopy.

---

## 6. ELECTRICITY & MAGNETISM
* **Ohm's Law:** $V = I \\cdot R$
* **Resistance & Resistivity:** $R = \\rho \\frac{L}{A}$
* **Resistors in Series:** $R_{\\text{eq}} = R_1 + R_2 + R_3$ (Current is same, voltage divides).
* **Resistors in Parallel:** $\\frac{1}{R_{\\text{eq}}} = \\frac{1}{R_1} + \\frac{1}{R_2} + \\frac{1}{R_3}$ (Voltage is same, current divides).
* **Joule's Heating Effect:** $H = I^2 R t = V I t = \\frac{V^2}{R} t$
* **Commercial Unit of Electrical Energy:** $1 \\text{ kWh (Unit)} = 3.6 \\times 10^6 \\text{ Joules}$.
"""

with open("data/revision/physics/physics-revision.md", "w", encoding="utf-8") as f:
    f.write(PHYSICS_MD)
print("Wrote data/revision/physics/physics-revision.md")


# 2. chemistry-revision.md
CHEMISTRY_MD = """# General Science – Chemistry Revision Notes
> **Exam-Ready Reference | Competitive Exams (RRB ALP, CDS, CAPF, SSC, State PSC)**

---

## 1. ATOMIC STRUCTURE & PERIODIC TABLE

### Fundamental Subatomic Particles
| Particle | Discoverer | Charge (C) | Mass (kg) | Location |
| :--- | :--- | :---: | :---: | :--- |
| **Proton** | E. Goldstein (named by Rutherford) | $+1.602 \\times 10^{-19}$ | $1.6726 \\times 10^{-27}$ | Nucleus |
| **Neutron**| James Chadwick (1932) | 0 (Neutral) | $1.6749 \\times 10^{-27}$ | Nucleus |
| **Electron**| J.J. Thomson (1897) | $-1.602 \\times 10^{-19}$ | $9.109 \\times 10^{-31}$ | Extra-nuclear shells |

### Periodic Trends Summary
* Across a **Period** (Left $\\to$ Right):
  * Atomic Radius: **Decreases** (due to increased nuclear charge).
  * Ionization Energy: **Increases**.
  * Electronegativity: **Increases** (Fluorine is most electronegative: 4.0).
* Down a **Group** (Top $\\to$ Bottom):
  * Atomic Radius: **Increases** (new shells added).
  * Ionization Energy: **Decreases**.
  * Metallic Character: **Increases** (Cesium/Francium most electropositive).

---

## 2. COMMON CHEMICAL COMPOUNDS & NAMES (HIGH-FREQUENCY EXAM TABLE)

| Common Name | Chemical Name | Chemical Formula | Key Practical Use |
| :--- | :--- | :--- | :--- |
| **Baking Soda** | Sodium Hydrogen Carbonate | $\\text{NaHCO}_3$ | Baking, antacid, fire extinguishers |
| **Washing Soda** | Sodium Carbonate Decahydrate | $\\text{Na}_2\\text{CO}_3 \\cdot 10\\text{H}_2\\text{O}$ | Glass, soap, softening hard water |
| **Bleaching Powder** | Calcium Oxychloride | $\\text{CaOCl}_2$ | Disinfectant for water, bleaching agent |
| **Plaster of Paris** | Calcium Sulphate Hemihydrate | $\\text{CaSO}_4 \\cdot \\frac{1}{2}\\text{H}_2\\text{O}$ | Bone fracture casts, statues, false ceilings |
| **Gypsum** | Calcium Sulphate Dihydrate | $\\text{CaSO}_4 \\cdot 2\\text{H}_2\\text{O}$ | Cement manufacturing (retards setting time)|
| **Quicklime** | Calcium Oxide | $\\text{CaO}$ | Glass, cement, white-washing |
| **Slaked Lime** | Calcium Hydroxide | $\\text{Ca(OH)}_2$ | White washing, soil neutralization |
| **Caustic Soda** | Sodium Hydroxide | $\\text{NaOH}$ | Soap, paper, petroleum refining |
| **Laughing Gas** | Nitrous Oxide | $\\text{N}_2\\text{O}$ | Anesthesia, dentistry |
| **Tear Gas** | Chloroacetophenone / CS | $\\text{C}_8\\text{H}_7\\text{ClO}$ | Riot control |
| **Dry Ice** | Solid Carbon Dioxide | $\\text{CO}_2 \\text{ (s)}$ | Deep refrigeration without liquid phase |
| **Heavy Water** | Deuterium Oxide | $\\text{D}_2\\text{O}$ | Moderator in nuclear reactors |
| **Vinegar** | Dilute Acetic Acid | $\\text{CH}_3\\text{COOH}$ (5–8%) | Food preservative |

---

## 3. ACIDS, BASES & PH VALUES

### Natural Sources of Organic Acids
* **Citric Acid:** Lemons, Oranges, Citrus fruits
* **Tartaric Acid:** Tamarind, Grapes, Unripe mangoes
* **Lactic Acid:** Curd, Sour milk
* **Acetic Acid:** Vinegar
* **Oxalic Acid:** Tomatoes, Spinach
* **Formic (Methanoic) Acid:** Ant sting, Nettle leaf sting
* **Malic Acid:** Apples

### pH Scale Reference Values (at 25°C)
* Neutral Water: 7.0
* Human Blood: **7.35 – 7.45** (Slightly basic)
* Gastric Juice (Stomach HCl): **1.2 – 1.8** (Strongly acidic)
* Pure Milk: 6.5 – 6.7
* Acid Rain: $< 5.6$
* Seawater: 7.8 – 8.3

---

## 4. METALS, NON-METALS & IMPORTANT ALLOYS

| Alloy | Composition | Primary Uses |
| :--- | :--- | :--- |
| **Brass** | $\\text{Cu } (70\\%) + \\text{Zn } (30\\%)$ | Utensils, musical instruments, ammunition |
| **Bronze** | $\\text{Cu } (88\\%) + \\text{Sn } (12\\%)$ | Statues, medals, coins, bearings |
| **Stainless Steel** | $\\text{Fe } (74\\%) + \\text{Cr } (18\\%) + \\text{Ni } (8\\%) + \\text{C } (<1\\%)$ | Surgical instruments, cutlery, kitchenware |
| **Solder** | $\\text{Pb } (50\\%) + \\text{Sn } (50\\%)$ | Joining electrical circuit wires (Low MP) |
| **Duralumin** | $\\text{Al } (95\\%) + \\text{Cu } (4\\%) + \\text{Mg } (0.5\\%) + \\text{Mn } (0.5\\%)$ | Aircraft bodies, space vehicles (Light & strong)|
| **German Silver** | $\\text{Cu } (60\\%) + \\text{Zn } (20\\%) + \\text{Ni } (20\\%)$ | Utensils (Note: Contains **NO Silver!**) |
| **Amalgam** | Any metal alloyed with **Mercury (Hg)** | Dental fillings (Iron does NOT form amalgam)|
"""

with open("data/revision/chemistry/chemistry-revision.md", "w", encoding="utf-8") as f:
    f.write(CHEMISTRY_MD)
print("Wrote data/revision/chemistry/chemistry-revision.md")

