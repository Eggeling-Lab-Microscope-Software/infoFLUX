# infoFLUX
A compilation of all knowledge I can find on the technical side of MINFLUX.

## What is to come ?
### Repository-wise
+ A portal for discussions
+ issue templates

### Content-wise
+ Completion of the MINFLUX sequence parameters
+ Completion of the MINFLUX data fields
+ Description of how the iterative MINFLUX impletementation operates
+ A guide on how to use the MINFLUX sequence parameters to optimize your measurements
+ Detailed discussion on MINFLUX time resolution

## How to contribute:
### Weird behavior and observations
Should you come across any unexpected or noteworthy behavior that is **reproducible**, please, share your experience. You can do so either by opening an issue or by contacting me directly. I will then add your observation to the list of known hacks and give you credit for your contribution.

### Deep Insights
To all the experienced users and dataminers that might come across this repository: Please, share your knowledge. I am particularly interested in the following:
- The exact way the ``estCoeff`` are calculated and how they are used in the localization process.
- If and how raw photon counts can be extracted from the MINFLUX system.
- How sequence files are parsed and how the MINFLUX system is controlled.
- How MINFLUX responds to losing a particle during a measurement, more precisely, hwo the system decides to start a new cycle and where it jumps.
- The programmatical way to access the MINFLUX system and how to control it. Any news on the API front or effective hacks to control the system from the outside are highly appreciated.

### Parameters and Data fields
Should you see any parameter or data field with the ``unknown`` tag or where information you have differs from the version portrayed here, please, ***open an issue***. Reference the subject of change and fill out the following template in order to contribute:
```markdown
# SUBJECT: The parameter in question.
# Main:
Value:
State what values can be passed to the parameter.

Effect: 
Describe the impact the parameter has on the behavior of the MINFLUX. Also mention any special values like `-1` for an "off"-state

Source: 
State the source of your knowledge in the "Vancouver" citation style. As this is a work in progress, we are also happy with "personal experience", but would be more than happy to see it backed by data.

Hacks:
In here go all the creative ways you found to utilize the parameter in question for your own measurements, i.e. you found a way to make use of the changed behavior beyond the intended use. This is especially interest in the light of 'unlocking' the system.
```

# Table of Contentes
- [infoFLUX](#infoflux)
  - [What is to come ?](#what-is-to-come-)
    - [Repository-wise](#repository-wise)
    - [Content-wise](#content-wise)
  - [How to contribute:](#how-to-contribute)
    - [Weird behavior and observations](#weird-behavior-and-observations)
    - [Deep Insights](#deep-insights)
    - [Parameters and Data fields](#parameters-and-data-fields)
- [Table of Contentes](#table-of-contentes)
- [MINFLUX sequence parameters](#minflux-sequence-parameters)
  - [Global parameters](#global-parameters)
    - [`Itr`](#itr)
    - [``bgcSense``](#bgcsense)
    - [``ctrDwellFactor``](#ctrdwellfactor)
    - [``damping``](#damping)
    - [``defaultField``](#defaultfield)
    - [`field`](#field)
    - [`headstart`](#headstart)
    - [``id``](#id)
    - [``liveview``](#liveview)
    - [``locLimit``](#loclimit)
    - [``maxOffTime``](#maxofftime)
    - [``stickiness``](#stickiness)
  - [``Itr`` (Iteration)](#itr-iteration)
    - [``Mode``](#mode)
    - [``_lemn``](#_lemn)
    - [``_lemd``](#_lemd)
    - [``bgcThreshold``](#bgcthreshold)
    - [``ccrLimit``](#ccrlimit)
    - [``estCoeff``](#estcoeff)
    - [``estCoeffA``](#estcoeffa)
    - [``estCoeffL``](#estcoeffl)
    - [``field``](#field-1)
    - [``fldFactor``](#fldfactor)
    - [``patDwellTime``](#patdwelltime)
    - [``patGeoFactor``](#patgeofactor)
    - [``patRepeat``](#patrepeat)
    - [``phtLimit``](#phtlimit)
    - [``pwrFactor``](#pwrfactor)
    - [``wavelength``](#wavelength)
  - [``Mode`` (Mode)](#mode-mode)
    - [``dim``](#dim)
    - [``dmod``](#dmod)
    - [``dpsf``](#dpsf)
    - [``emod``](#emod)
    - [``epsf``](#epsf)
    - [``id``](#id-1)
    - [``modulated``](#modulated)
    - [``pattern``](#pattern)
    - [``phDiaAU``](#phdiaau)
    - [``strategy``](#strategy)
- [MINFLUX data fields](#minflux-data-fields)
  - [How to contribute:](#how-to-contribute-1)
  - [Global fields](#global-fields)
    - [``act``](#act)
    - [``dos``](#dos)
    - [``gri``](#gri)
    - [``itr``](#itr-1)
    - [``sky``](#sky)
    - [``sqi``](#sqi)
    - [``tid``](#tid)
    - [``tim``](#tim)
    - [``vld``](#vld)
  - [``itr`` (iteration)](#itr-iteration-1)
    - [``cfr``](#cfr)
    - [``dcr``](#dcr)
    - [``dmz``](#dmz)
    - [``ecc``](#ecc)
    - [``eco``](#eco)
    - [``efc``](#efc)
    - [``efo``](#efo)
    - [``eox``](#eox)
    - [``eoy``](#eoy)
    - [``ext``](#ext)
    - [``fbg``](#fbg)
    - [``gvx``](#gvx)
    - [``gvy``](#gvy)
    - [``itr``](#itr-2)
    - [``lcx``](#lcx)
    - [``lcy``](#lcy)
    - [``lcz``](#lcz)
    - [``lnc``](#lnc)
    - [``loc``](#loc)
    - [``sta``](#sta)
    - [``tic``](#tic)

# MINFLUX sequence parameters
In this section, we are going explore:
- MINFLUX paramters
- their values
- their effect on the measurement
- the source of knowledge
- and possibly known hacks

In general, MINFLUX sequence files contain nested ``key:value`` parirings. Whenever we refer to such a nested object, we will link to the corresponding section in the document. All known parameters are listed in alphabetical order within their nesting layer. In a later version, when all parameters are acquired, we will sort them by relevant groups.

Default values have been extracted from the `Tracking_2D_Oct2022` sequence. And will probably be removed in a later version.



## Global parameters
### `Itr` 
- **Nested block of instructions that control each individual sequence.**
  
### ``bgcSense``

### ``ctrDwellFactor``

### ``damping``
- **default**: 2
- **value**: any ``integer`` (tested 0-2)
- **effect**: Limits the distance travelled during localization update according to the following equation $$\Delta_{update}=\Delta_{real}\cdot2^{-\text(damping)}$$
- **source**: Abberior Instruments GmbH (personal communication, 2022)
- **hacks**: Setting the parameter to anything less than 2, we observe larger distances between localizations and an increase in track length, especially for fast moving particles (e.g. in biomimetic membranes). Thus, we can increase the microscope's tolerance when following rapid particles. However, it is not entirely known, why this parameter has been introduced. We suspect that it should correct for overshoot during localization updates. 
  
### ``defaultField`` 
- **Nested block of instructions**
  
### `field` 
- **Nested block of instructions**
  
### `headstart`
- **default**: -1 (probably in the 'off' state)
- **value**: ``unknown`` 
- **effect**: ``unknown``
- **source**: sequence files
- **hacks** ``unknown``
  
### ``id``
- **default**: *Name of the Sequence*
- **value**: any ``string``
- **effect**: Recognized name of sequence when used in MINFLUX IMSPECTOR. **Only** this name will be regarded when listing sequences, you have to set it in order for your custom sequence to be recognized. 
- **source**: ``Tested``
- **hacks**: ``unknown``

### ``liveview``
- **default**: ``{'show': ['loc']}``
- **value**: Any from **['cfr', 'dcr', 'eco', 'efo', 'itr', 'lnc', 'loc', 'sta', 'tid', 'tim']**
- **effect**: Display a liveview of the current MINFLUX measurement with the set parameters as color axis.
- **source**: Jonathan Alvelid
- **hacks**: ``unknown``

### ``locLimit``
- **default**: -1
- **value**: Any positive ``integer`` or ``-1`` for the **off**-state.
- **effect**: Set an upper limit for consecutive localizations along a single trace.
- **source**: ``Tested``
- **hacks**: Setting an upper limit is a must when zou expect immobilized particles in your samples. Any other blob artifact, you can tackle with [Blob-B-Gone](https://www.frontiersin.org/articles/10.3389/fbinf.2023.1268899/full).

### ``maxOffTime``
- **default**: 'unspecified' (= **3ms**)
- **value**: Any ``float`` (**untested**)
- **effect**: A time interval that is waited after each full cycle x ``stickiness`` to account for blinking dyes that stay in an off-state for several milliseconds.
- **source**: Francesco Reina (Personal communication, Jan 2024)
- **hacks**: ``unknown``

### ``stickiness``
- **default**: 4
- **value**: any positive ``integer``, and *probably* ``-1`` for the **off**-state.
- **effect**: Numer of total cycle repeats. Should the current iteration terminate without a valid posiion more often than permitted by the `patRepeat` parameter in the corresponding iteration-parameter-container, a new cycle is started. There may be some strange interacton after such an elongated cycle successfully delivered a localization, i.e. that a new scan entire is started for the next localization. This, however, has to be confirmed.
- **source**: Francesco Reina (Personal communication, Jan 2024)
- **hacks**: ``unknown``


## ``Itr`` (Iteration)
### ``Mode``
- **Nested list of instructions**

### ``_lemn``
- **value**: any ``float``, **DO NOT CHANGE**
- **effect**: This value describes the **mean** theoretical localization precision as set by Abberiors (GmbH) simulations. In 2D sequences this only refers to the XY-resolution; in 3D, there two numbers are given, the first referring to the XY-plane, the second one to the Z-Axis.
- **source**: Francesco Reina (Personal communication, Dec 2023)
- **hacks**: ``unknown`` 

### ``_lemd``
- **value**: any ``float``, **DO NOT CHANGE**
- **effect**: This value describes the **median** theoretical localization precision as set by Abberiors (GmbH) simulations. In 2D sequences this only refers to the XY-resolution; in 3D, there two numbers are given, the first referring to the XY-plane, the second one to the Z-Axis.
- **source**: Francesco Reina (Personal communication, Dec 2023)
- **hacks**: ``unknown`` 

### ``bgcThreshold``
- **value**: any positive ``integer`` and ``-1`` for the **off**-state.
- **effect**: Set the number of times the fluorescent background signal should be scanned [Francesco Reina (Personal communication, Jan 2024)]. If the value is higher than ``1``, the results will *probably* be averaged. In the case [``bgcSense``](#bgcsense) is deactivated, it defaults to ``bgcThreshold = 0``.
- **source**: Roman Schmidt (Personal communication, Jan 2024)
- **hacks**: ``unknown`` 
  
### ``ccrLimit``
- **value**: any positive ``float`` and ``-1`` for the **off**-state.
- **effect**: If a positive value is passed, a center freqency check is perfomed, i.e. the *TCP* is added a final scanning spot in the geometrical center at which photons are collected during the final step of the current iteration. Any passed ``float`` value will be treated as an upper limit to the *Center Frequency Ratio* (``CFR``). When surpassed, the current track is terminated and the system will start scaning for other emitters to follow. <br> Enabling the CCR-scan provides the ``CFR`` as well as the *Effective Frequency at the center* (``EFC``) that is the emission frequency measured at the center in addition to the generally collected *Effective Frequency Offset* (``EFO``), i.e. the sum of all collected photons at the *TCP* spots. The ``CFR`` is calculated as follows: 
  
$$ 
CFR = \frac{EFC\space[Hz]}{EFO\space[Hz]}
$$

- **source**: Roman Schmidt (Personal Communication, E-Mail, Jan 2024)
- **hacks**: This will slow down the measurement by a time equal to [``ctrDwellFactor``](#ctrdwellfactor) times [``patDwellTime``](#patdwelltime) **PER** iteration. If you have particularly fast emitters, use a low concentration to ensure singular particles per *region of interest* (see particle density estimation) and disable the ccr-checks by setting ``ccrLimit = -1``.

### ``estCoeff``
- **value**: 
  ```python
  [
    [
      [float, float, float],
      [float, float, float],
      [float, float, float],
    ],
    [
      [float, float, float],
      [float, float, float],
      [float, float, float],
    ]
  ]
  ``` 
- **effect**: ``unknown`` 
- **source**: ``unknown`` 
- **hacks**:``unknown`` 

### ``estCoeffA``
- **value**: 
  ```python
  ['unspecified', 'unspecified', 'unspecified', 'unspecified']
  ```
- **effect**: ``unknown`` 
- **source**: ``unknown`` 
- **hacks**:``unknown`` 

### ``estCoeffL``
- **value**:
  ```python
  ['unspecified', 'unspecified', 'unspecified', 'unspecified']
  ```
- **effect**: ``unknown`` 
- **source**: ``unknown`` 
- **hacks**:``unknown`` 

### ``field``
- **value**: 
  ```python
  [float, float, float]
  ```
- **effect**: ``unknown`` 
- **source**: ``unknown`` 
- **hacks**:``unknown`` 

### ``fldFactor``
- **value**:
  ```python
  [float, float, float]
  ```
- **effect**: ``unknown`` 
- **source**: ``unknown`` 
- **hacks**: ``unknown`` 

### ``patDwellTime``
- **value**: any positive ``float`` value. The unit is **seconds**.
- **effect**: Sets the total amount of time spent during a full ``TCP`` scan-cylce of the current iteration. Each spot of the TCP, excluding the center (only used if the [ccr-check](#ccrlimit) is enabled) will be scanned for a time equal to:
  
  $$t_{spot} = \frac{patDwellTime}{\Psi}$$

  Where $\Psi \in \mathbb{N}$ is the number of vertices of the ``TCP`` (e.g. 3 - triangle/fast, 6 - hexagon).

- **source**: Abberior GmbH (personal communication, 2022)
- **hacks**: ``unknown``

### ``patGeoFactor``
- **value**: any positive ``float`` value.
- **effect**: Controls the TCP diameter. The exact way it is calculated is currently ``unknown``, but we know of the following correspondences: 
  - ``patGeoFactor`` = 0.28 <-> TCP diameter = 100 nm
  - ``patGeoFactor`` = 0.42 <-> TCP diameter = 150 nm
- **source**: Abberior GmbH (personal communication, 2022)
- **hacks**: A smaller TCP forces a smaller area of photon collection thereby limiting the spatial localization error. However, the risk of losing any non fixated particles rises significantly with smaller collection-tolerances. 

### ``patRepeat``
- **value**: any positive ``integer`` or ``0`` for the off state. Probably ``-1`` works as well.
- **effect**: Sets the maximum number the current iteration step is repeated in case of unsuccessful particle localization. The break criterium is most likely ONLY the case when an insufficiet number of photons (<[photon imit](#phtlimit)) is collected during an entire TCP cycle, taking [dwell time](#patdwelltime) seconds. Be aware that setting ``patRepeat`` to zero breaks the sequence as it apparently turns off the iteration entirely (``Tested`` by Agnes Koerfer). A possible cause could be that the ``0`` is interpreted as a ``boolean`` rather than an ``integer``.
- **source**: Jonathan Alvelid
- **hacks**: ``unknown``

### ``phtLimit``
- **value**: any positive ``integer``.
- **effect**: Determins the minimal amount of photons that have to be collected during a singular TCP cycle i.e., during [dwell time](#patdwelltime) seconds, in order for a localization estimation to be considered valid. Apparently, a change requires an update of the [estimation coefficients](#estcoeff), which are especially calculated for the new photon Limit (Francesco Reina, personal communicaltion, 2022 ``???``).
- **source**: Roman Schmidt (Nature communications, 2021)
- **hacks**: Decreasing the photon limit allows for faster tracking as the [dwell time](#patdwelltime) can be reduced correspondingly. However, reducing the statistical sample of photons per localization **drastically** increased variance and renders each measurement more prone to noise. This is especially grave when working with "higher" (MINFLUX standards) particle densities.

### ``pwrFactor``
- **value**: any positive ``integer`` but given as a ``float``. 
- **effect**: This parameter probably affects the excitation laser power during hte current iteration. However, it is ``unknown`` in what exact way this is done.
- **source**: Jonathan Alvelid
- **hacks**: ``unknown``

### ``wavelength``
- **value**: any positive ``float``.
- **effect**: Probably addresses the wavelength used for excitation. However, it is unclear if this parameter changes due to the laser selected via *Imspector* during measurements. Thus, it is possible that the value listed here is just a default.
- **source**: Jonathan Alvelid, Bela Vogler
- **hacks**: ``unknown``


## ``Mode`` (Mode)

### ``dim``
- **value**: any positive ``integer`` from ``{2,3}``. Untested if it takes other values.
- **effect**: Set the spatial (Euclidean) dimension in which to perform the localization.
- **source**: Jonathan Alvelid
- **hacks**: ``unknown``

### ``dmod``
- **value**: any ``string`` probably referencing presets, e.g. ```["both", "axial"]```.
- **effect**: ``unknown``
- **source**: ``unknown``
- **hacks**: ``unknown``

### ``dpsf``
- **value**: custom pickeled object. This is likely a data container.
- **effect**: ``unknown``
- **source**: ``unknown``
- **hacks**: ``unknown``

### ``emod``
- **value**: any ``string`` probably referencing presets, e.g. ```["both", "axial"]```.
- **effect**: ``unknown``
- **source**: ``unknown``
- **hacks**: ``unknown``

### ``epsf``
- **value**: custom pickeled object. This is likely a data container.
- **effect**: ``unknown``
- **source**: ``unknown``
- **hacks**: ``unknown``

### ``id``
- **value**: any ``string``, e.g. ```["prbt", "pt3d", "mxax", "mx13", "mflx"]```.
- **effect**: Set the name of the corresponding iteration. 
- **source**: Jonathan Alvelid
- **hacks**: ``unknown``

### ``modulated``
- **value**: any ``string`` probably referencing presets, e.g. ```["phl", "exc"]```.
- **effect**: ``unknown``
- **source**: ``unknown``
- **hacks**: ``unknown``

### ``pattern``
- **value**: any ``string`` referencing presets ```["hexagon", "square", "octagon", "triangle", "zline", "zline2"]```.
- **effect**: Set or reference the scan pattern, thus the number of vertices within the TCP and correspondingly the grometry of the area or volume that is used for collecting photons.
- **source**: Jonathan Alvelid
- **hacks**: ``unknown``

### ``phDiaAU``
- **value**: any positive ``float``, e.g. ```[1.5, 1.6]```.
- **effect**: Set or reference the pinhole size in Airy Units (AU).
- **source**: Jonathan Alvelid
- **hacks**: ``unknown``

### ``strategy``
- **value**: any ``string`` probably referencing presets, e.g. ```["BL"]```.
- **effect**: ``unknown``
- **source**: ``unknown``
- **hacks**: ``unknown``

# MINFLUX data fields
In the following, we will list:
* All known data fileds in MINFLUX files ``['.json', '.npy']``
* what we know of their contents
* the source of knowledge
* any known hacks

As MINFLUX 3D is controlled by iterating sequences built from nested ``key:value`` pairings, it is little to no wonder that exported files share a similar structure. It seems like data generated by each iteration is dumped into a ``python dictionary``, which can later be saved as either ``.json`` or ``.npy``. All known data fields are listed in alphabetical order within their nesting layer.

## How to contribute:
Should you see any parameter field with the ``unknown`` tag or where information you have differ from the version portrayed here, please, ***open an issue***. Put the parameter of change as the subject and fill out the following template in order to contribute:
```markdown
# SUBJECT: The parameter in question.
# Main:
value:
State what values can be passed to the parameter.

Effect: 
Describe the impact the parameter has on the behavior of the MINFLUX. Also mention any special values like `-1` for an "off"-state

Source: 
State the source of your knowledge in the "Vancouver" citation style. As this is a work in progress, we are also happy with "personal experience", but would be more than happy to see it backed by data.

Hacks:
In here go all the creative ways you found to utilize the parameter in question for your own measurements, i.e. you found a way to make use of the changed behavior beyond the intended use. This is especially interest in the light of 'unlocking' the system.
```

## Global fields

### ``act``
- **value**:
- **effect**:
- **source**:
- **hacks**:

### ``dos``
- **value**:
- **effect**:
- **source**:
- **hacks**:

### ``gri``
- **value**:
- **effect**:
- **source**:
- **hacks**:

### ``itr``
- **value**:
- **effect**:
- **source**:
- **hacks**:

### ``sky``
- **value**:
- **effect**:
- **source**:
- **hacks**:

### ``sqi``
- **value**:
- **effect**:
- **source**:
- **hacks**:

### ``tid``
- **value**:
- **effect**:
- **source**:
- **hacks**:

### ``tim``
- **value**:
- **effect**:
- **source**:
- **hacks**:

### ``vld``
- **value**:
- **effect**:
- **source**:
- **hacks**:

## ``itr`` (iteration)

### ``cfr``
- **value**:
- **effect**:
- **source**:
- **hacks**:

### ``dcr``
- **value**:
- **effect**:
- **source**:
- **hacks**:

### ``dmz``
- **value**:
- **effect**:
- **source**:
- **hacks**:

### ``ecc``
- **value**:
- **effect**:
- **source**:
- **hacks**:

### ``eco``
- **value**:
- **effect**:
- **source**:
- **hacks**:

### ``efc``
- **value**:
- **effect**:
- **source**:
- **hacks**:

### ``efo``
- **value**:
- **effect**:
- **source**:
- **hacks**:

### ``eox``
- **value**:
- **effect**:
- **source**:
- **hacks**:

### ``eoy``
- **value**:
- **effect**:
- **source**:
- **hacks**:

### ``ext``
- **value**:
- **effect**:
- **source**:
- **hacks**:

### ``fbg``
- **value**:
- **effect**:
- **source**:
- **hacks**:

### ``gvx``
- **value**:
- **effect**:
- **source**:
- **hacks**:

### ``gvy``
- **value**:
- **effect**:
- **source**:
- **hacks**:

### ``itr``
- **value**:
- **effect**:
- **source**:
- **hacks**:

### ``lcx``
- **value**:
- **effect**:
- **source**:
- **hacks**:

### ``lcy``
- **value**:
- **effect**:
- **source**:
- **hacks**:

### ``lcz``
- **value**:
- **effect**:
- **source**:
- **hacks**:

### ``lnc``
- **value**:
- **effect**:
- **source**:
- **hacks**:

### ``loc``
- **value**:
- **effect**:
- **source**:
- **hacks**:

### ``sta``
- **value**:
- **effect**:
- **source**:
- **hacks**:

### ``tic``
- **value**:
- **effect**:
- **source**:
- **hacks**:

