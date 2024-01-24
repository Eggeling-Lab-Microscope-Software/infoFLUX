# infoFLUX
A compilation of all knowledge I can find on the technical side of MINFLUX.

# Table of Contentes
- [infoFLUX](#infoflux)
- [Table of Contentes](#table-of-contentes)
- [MINFLUX sequence parameters](#minflux-sequence-parameters)
  - [How to contribute:](#how-to-contribute)
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
  - [Iteration - `Itr`](#iteration---itr)
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

# MINFLUX sequence parameters
In this section, we are going explore:
- MINFLUX paramters
- their default values
- their input values
- their effect on the measurement
- the source of knowledge
- and possibly known hacks

In general, MINFLUX sequence files contain nested key:value parirings. Whenever we refer to such a nested object, we will link to the corresponding section in the document. All known parameters are listed in alphabetical order. In a later version, when all parameters are acquired, we will sort them by relevant groups.

Default values have been extracted from the `Tracking_2D_Oct2022` sequence. And will probably be removed in a later version.

## How to contribute:
Should you see any parameter field with the ``unknown`` tag or where information you have differ from the version portrayed here, please, ***open an issue***. Put the parameter of change as the subject and fill out the following template in order to contribute:
```markdown
# SUBJECT: The parameter in question.
# Main:
Input:
State what values can be passed to the parameter.

Effect: 
Describe the impact the parameter has on the behavior of the MINFLUX. Also mention any special inputs like `-1` for an "off"-state

Source: 
State the source of your knowledge in the "Vancouver" citation style. As this is a work in progress, we are also happy with "personal experience", but would be more than happy to see it backed by data.

Hacks:
In here go all the creative ways you found to utilize the parameter in question for your own measurements, i.e. you found a way to make use of the changed behavior beyond the intended use. This is especially interest in the light of 'unlocking' the system.
```

## Global parameters
### `Itr` 
- **Nested block of instructions that control each individual sequence.**
  
### ``bgcSense``

### ``ctrDwellFactor``

### ``damping``
- **default**: 2
- **input**: any ``integer`` (tested 0-2)
- **effect**: Limits the distance travelled during localization update according to the following equation $$\Delta_{update}=\Delta_{real}\cdot2^{-\text(damping)}$$
- **source**: Abberior Instruments GmbH (personal communication, 2022)
- **hacks**: Setting the parameter to anything less than 2, we observe larger distances between localizations and an increase in track length, especially for fast moving particles (e.g. in biomimetic membranes). Thus, we can increase the microscope's tolerance when following rapid particles. However, it is not entirely known, why this parameter has been introduced. We suspect that it should correct for overshoot during localization updates. 
  
### ``defaultField`` 
- **Nested block of instructions**
  
### `field` 
- **Nested block of instructions**
  
### `headstart`
- **default**: -1 (probably in the 'off' state)
- **input**: ``unknown`` 
- **effect**: ``unknown``
- **source**: sequence files
- **hacks** ``unknown``
  
### ``id``
- **default**: *Name of the Sequence*
- **input**: any ``string``
- **effect**: Recognized name of sequence when used in MINFLUX IMSPECTOR. **Only** this name will be regarded when listing sequences, you have to set it in order for your custom sequence to be recognized. 
- **source**: ``Tested``
- **hacks**: - 

### ``liveview``
- **default**: ``{'show': ['loc']}``
- **input**: Any from **['cfr', 'dcr', 'eco', 'efo', 'itr', 'lnc', 'loc', 'sta', 'tid', 'tim']**
- **effect**: Display a liveview of the current MINFLUX measurement with the set parameters as color axis.
- **source**: Jonathan Alvelid
- **hacks**: - 

### ``locLimit``
- **default**: -1
- **input**: Any positive ``integer`` or ``-1`` for the **off**-state.
- **effect**: Set an upper limit for consecutive localizations along a single trace.
- **source**: ``Tested``
- **hacks**: Setting an upper limit is a must when zou expect immobilized particles in your samples. Any other blob artifact, you can tackle with [Blob-B-Gone](https://www.frontiersin.org/articles/10.3389/fbinf.2023.1268899/full).

### ``maxOffTime``
- **default**: 'unspecified' (= **3ms**)
- **input**: Any ``float`` (**untested**)
- **effect**: A time interval that is waited after each full cycle x ``stickiness`` to account for blinking dyes that stay in an off-state for several milliseconds.
- **source**: Francesco Reina (Personal communication, Jan 2024)
- **hacks**: -

### ``stickiness``
- **default**: 4
- **input**: any positive ``integer``, and *probably* ``-1`` for the **off**-state.
- **effect**: Numer of total cycle repeats. Should the current iteration terminate without a valid posiion more often than permitted by the `patRepeat` parameter in the corresponding iteration-parameter-container, a new cycle is started. There may be some strange interacton after such an elongated cycle successfully delivered a localization, i.e. that a new scan entire is started for the next localization. This, however, has to be confirmed.
- **source**: Francesco Reina (Personal communication, Jan 2024)
- **hacks**: -


## Iteration - `Itr`
### ``Mode``
- **Nested block of instructions**

### ``_lemn``
- **input**: any ``float``, **DO NOT CHANGE**
- **effect**: This value describes the **mean** theoretical localization precision as set by Abberiors (GmbH) simulations. In 2D sequences this only refers to the XY-resolution; in 3D, there two numbers are given, the first referring to the XY-plane, the second one to the Z-Axis.
- **source**: Francesco Reina (Personal communication, Dec 2023)
- **hacks**: - 

### ``_lemd``
- **input**: any ``float``, **DO NOT CHANGE**
- **effect**: This value describes the **median** theoretical localization precision as set by Abberiors (GmbH) simulations. In 2D sequences this only refers to the XY-resolution; in 3D, there two numbers are given, the first referring to the XY-plane, the second one to the Z-Axis.
- **source**: Francesco Reina (Personal communication, Dec 2023)
- **hacks**: - 

### ``bgcThreshold``
- **input**: any positive ``integer`` and ``-1`` for the **off**-state.
- **effect**: Set the number of times the fluorescent background signal should be scanned [Francesco Reina (Personal communication, Jan 2024)]. If the value is higher than ``1``, the results will *probably* be averaged. In the case [``bgcSense``](#bgcsense) is deactivated, it defaults to ``bgcThreshold = 0``.
- **source**: Roman Schmidt (Personal communication, Jan 2024)
- **hacks**: - 
  
### ``ccrLimit``
- **input**: any positive ``float`` and ``-1`` for the **off**-state.
- **effect**: If a positive value is passed, a center freqency check is perfomed, i.e. the *TCP* is added a final scanning spot in the geometrical center at which photons are collected during the final step of the current iteration. Any passed ``float`` value will be treated as an upper limit to the *Center Frequency Ratio* (``CFR``). When surpassed, the current track is terminated and the system will start scaning for other emitters to follow. <br> Enabling the CCR-scan provides the ``CFR`` as well as the *Effective Frequency at the center* (``EFC``) that is the emission frequency measured at the center in addition to the generally collected *Effective Frequency Offset* (``EFO``), i.e. the sum of all collected photons at the *TCP* spots. The ``CFR`` is calculated as follows: 
  
$$ 
CFR = \frac{EFC\space[Hz]}{EFO\space[Hz]}
$$

- **source**: Roman Schmidt (Personal Communication, E-Mail, Jan 2024)
- **hacks**: This will slow down the measurement by a time equal to [``ctrDwellFactor``](#ctrdwellfactor) times [``patDwellTime``](#patdwelltime) **PER** iteration. If you have particularly fast emitters, use a low concentration to ensure singular particles per *region of interest* (see particle density estimation) and disable the ccr-checks by setting ``ccrLimit = -1``.

### ``estCoeff``
- **input**: 
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
- **input**: 
  ```python
  ['unspecified', 'unspecified', 'unspecified', 'unspecified']
  ```
- **effect**: ``unknown`` 
- **source**: ``unknown`` 
- **hacks**:``unknown`` 

### ``estCoeffL``
- **input**:
  ```python
  ['unspecified', 'unspecified', 'unspecified', 'unspecified']
  ```
- **effect**: ``unknown`` 
- **source**: ``unknown`` 
- **hacks**:``unknown`` 

### ``field``
- **input**: 
  ```python
  [float, float, float]
  ```
- **effect**: ``unknown`` 
- **source**: ``unknown`` 
- **hacks**:``unknown`` 

### ``fldFactor``
- **input**:
  ```python
  [float, float, float]
  ```
- **effect**: ``unknown`` 
- **source**: ``unknown`` 
- **hacks**: ``unknown`` 

### ``patDwellTime``
- **input**: any positive ``float`` value. The unit is **seconds**.
- **effect**: Sets the total amount of time spent during a full ``TCP`` scan-cylce of the current iteration. Each spot of the TCP, excluding the center (only used if the [ccr-check](#ccrlimit) is enabled) will be scanned for a time equal to:
  
  $$t_{spot} = \frac{patDwellTime}{\Psi}$$

  Where $`\Psi \in\natnums`$ is the number of vertices of the ``TCP`` (e.g. 3 - triangle/fast, 6 - hexagon).

- **source**: Abberior GmbH (personal communication, 2022)
- **hacks**:

### ``patGeoFactor``
- **input**: 
- **effect**: 
- **source**: 
- **hacks**:

### ``patRepeat``
- **input**: 
- **effect**: 
- **source**: 
- **hacks**:

### ``phtLimit``
- **input**: 
- **effect**: 
- **source**: 
- **hacks**:

### ``pwrFactor``
- **input**: 
- **effect**: 
- **source**: 
- **hacks**:

### ``wavelength``
- **input**: 
- **effect**: 
- **source**: 
- **hacks**:
