# MINFLUX sequence parameters
In this section, we are going explore:
- MINFLUX paramters
- their default values
- their possible values
- their effect on the measurement
- the source of knowledge
- and possibly known hacks

In general, MINFLUX sequence files contain nested key:value parirings. Whenever we refer to such a nested object, we will link to the corresponding section in the document. All known parameters are listed in alphabetical order.

Default values have been extracted from the `Tracking_2D_Oct2022` sequence. And will probably be removed in a later version.

## Table of Contentes
- [MINFLUX sequence parameters](#minflux-sequence-parameters)
  - [Table of Contentes](#table-of-contentes)
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


## Global parameters
### `Itr` 
- **Nested block of instructions that control each individual sequence.**
  
### ``bgcSense``

### ``ctrDwellFactor``

### ``damping``
- **default**: 2
- **possible**: any ``integer`` (tested 0-2)
- **effect**: Limits the distance travelled during localization update according to the following equation $$\Delta_{update}=\Delta_{real}\cdot2^{-\text(damping)}$$
- **source**: Abberior Instruments GmbH (personal communication, 2022)
- **hacks**: Setting the parameter to anything less than 2, we observe larger distances between localizations and an increase in track length, especially for fast moving particles (e.g. in biomimetic membranes). Thus, we can increase the microscope's tolerance when following rapid particles. However, it is not entirely known, why this parameter has been introduced. We suspect that it should correct for overshoot during localization updates. 
### ``defaultField`` 
- **Nested block of instructions**
### `field` 
- **Nested block of instructions**
### `headstart`
- **default**: -1 (probably in the 'off' state)
- **possible**: ``unknown`` 
- **effect**: ``unknown``
- **source**: sequence files
- **hacks** ``unknown``
### ``id``
- **default**: *Name of the Sequence*
- **possible**: any ``string``
- **effect**: Recognized name of sequence when used in MINFLUX IMSPECTOR. **Only** this name will be regarded when listing sequences, you have to set it in order for your custom sequence to be recognized. 
- **source**: ``Tested``
- **hacks**: - 
### ``liveview``
- **default**: ``{'show': ['loc']}``
- **possible**: Any from **['cfr', 'dcr', 'eco', 'efo', 'itr', 'lnc', 'loc', 'sta', 'tid', 'tim']**
- **effect**: Display a liveview of the current MINFLUX measurement with the set parameters as color axis.
- **source**: Jonathan Alvelid
- **hacks**: - 
### ``locLimit``
- **default**: -1
- **possible**: Any positive ``integer`` or ``-1`` for the **off**-state.
- **effect**: Set an upper limit for consecutive localizations along a single trace.
- **source**: ``Tested``
- **hacks**: Setting an upper limit is a must when zou expect immobilized particles in your samples. Any other blob artifact, you can tackle with [Blob-B-Gone](https://www.frontiersin.org/articles/10.3389/fbinf.2023.1268899/full).
### ``maxOffTime``
- **default**: 'unspecified' (= **3ms**)
- **possible**: Any ``float`` (**untested**)
- **effect**: A time interval that is waited after each full cycle x ``stickiness`` to account for blinking dyes that stay in an off-state for several milliseconds.
- **source**: Francesco Reina (Personal communication, Jan 2024)
- **hacks**: -
### ``stickiness``
- **default**: 4
- **possible**: any positive ``integer``, and *probably* ``-1`` for the **off**-state.
- **effect**: Numer of total cycle repeats. Should the current iteration terminate without a valid posiion more often than permitted by the `patRepeat` parameter in the corresponding iteration-parameter-container, a new cycle is started. There may be some strange interacton after such an elongated cycle successfully delivered a localization, i.e. that a new scan entire is started for the next localization. This, however, has to be confirmed.
- **source**: Francesco Reina (Personal communication, Jan 2024)
- **hacks**: -


## Iteration - `Itr`
### ``Mode``
- **Nested block of instructions**

### ``_lemn``
- **possible**: any ``float``, **DO NOT CHANGE**
- **effect**: This value describes the **mean** theoretical localization precision as set by Abberiors (GmbH) simulations. In 2D sequences this only refers to the XY-resolution; in 3D, there two numbers are given, the first referring to the XY-plane, the second one to the Z-Axis.
- **source**: Francesco Reina (Personal communication, Dec 2023)
- **hacks**: - 

### ``_lemd``
- **possible**: any ``float``, **DO NOT CHANGE**
- **effect**: This value describes the **median** theoretical localization precision as set by Abberiors (GmbH) simulations. In 2D sequences this only refers to the XY-resolution; in 3D, there two numbers are given, the first referring to the XY-plane, the second one to the Z-Axis.
- **source**: Francesco Reina (Personal communication, Dec 2023)
- **hacks**: - 

### ``bgcThreshold``
- **possible**: any positive ``integer`` and ``-1`` for the **off**-state.
- **effect**: Set the number of times the fluorescent background signal should be scanned [Francesco Reina (Personal communication, Jan 2024)]. If the value is higher than ``1``, the results will *probably* be averaged. In the case [``bgcSense``](#bgcsense) is deactivated, it defaults to ``bgcThreshold = 0``.
- **source**: Roman Schmidt (Personal communication, Jan 2024)
- **hacks**: - 
  
### ``ccrLimit``
- **possible**: 
- **effect**: 
- **source**: 
- **hacks**:

### ``estCoeff``
- **possible**: 
- **effect**: 
- **source**: 
- **hacks**:

### ``estCoeffA``
- **possible**: 
- **effect**: 
- **source**: 
- **hacks**:

### ``estCoeffL``
- **possible**: 
- **effect**: 
- **source**: 
- **hacks**:

### ``field``
- **possible**: 
- **effect**: 
- **source**: 
- **hacks**:

### ``fldFactor``
- **possible**: 
- **effect**: 
- **source**: 
- **hacks**:

### ``patDwellTime``
- **possible**: 
- **effect**: 
- **source**: 
- **hacks**:

### ``patGeoFactor``
- **possible**: 
- **effect**: 
- **source**: 
- **hacks**:

### ``patRepeat``
- **possible**: 
- **effect**: 
- **source**: 
- **hacks**:

### ``phtLimit``
- **possible**: 
- **effect**: 
- **source**: 
- **hacks**:

### ``pwrFactor``
- **possible**: 
- **effect**: 
- **source**: 
- **hacks**:

### ``wavelength``
- **possible**: 
- **effect**: 
- **source**: 
- **hacks**:
