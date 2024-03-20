# infoFLUX <!-- omit from toc -->
A compilation of all knowledge I can find on the technical side of MINFLUX.

## Using *infoFLUX*
You are welcome to use and contribute to infoFLUX following the guidelines presented below. Should you use the contents of this repository, **please cite *infoFLUX* and its contributors accordingly.**

## What is to come ? <!-- omit from toc -->
### In general
After completing this repository, we aim to archive it and acquire a Zenodo doi for it. After that point in time, it becomes citable and all **contributors of major changes will be listed as authors** of this repository.
### Repository-wise
+ [x] A portal for discussions
+ [ ] Issue templates

### Content-wise
+ [x] Collection of MINFLUX sequence parameters
+ [x] Collection of MINFLUX data field descriptions
+ [ ] List of known MINFLUX hardware
+ [ ] A discussion on limiting factors and expectation horizons
+ [ ] A discussion of how the iterative MINFLUX impletementation operates
+ [ ] A guide on how to use the MINFLUX sequence parameters to optimize your measurements

## What to contribute:
### Weird behavior and observations
Should you come across any unexpected or noteworthy behavior that is **reproducible**, please, share your experience. You can do so either by opening an issue or by contacting me directly. I will then add your observation to the list of known hacks and give you credit for your contribution.

### Deep Insights
To all the experienced users and dataminers that might come across this repository; **Please, share your knowledge.** Topics of interest include but are not limited to:
- The exact way the ``estCoeff`` are calculated and how they are used in the localization process.
- If and how raw photon counts can be extracted from the MINFLUX system.
- How sequence files are parsed and how the MINFLUX system is controlled.
- How MINFLUX responds to losing a particle during a measurement, more precisely, hwo the system decides to start a new cycle and where it jumps.
- The programmatical way to access the MINFLUX system and how to control it. Any news on the API front or effective hacks to control the system from the outside are highly appreciated.

## How to contribute:
### Contribution Policy (Content)
This is a community project without a validating insitution, as of now. Any contribution will have to be **opened as an issue first** and will be implemented only after screening and discussion.  

In general, should you come across any information that collides with your experience, observations or knowledge, we are happy to hear from you. **Please, open an issue and fill the following template.**

In case of typos or other minor contributions, please, open a pull request and it will be implemented shortly. 
### Template (temporary)
```markdown
# SUBJECT: The parameter in question.
# Main:
**Value:**
*State what values can be passed to the parameter.*

**Effect: **
*Describe the impact the parameter has on the behavior of the MINFLUX. Also mention any special values like `-1` for an "off"-state.*

**Source: **
*State the source of your knowledge in the "Vancouver" citation style. As this is a work in progress, we are also happy with "personal experience", but would be more than happy to see it backed by data.*

**Hacks:**
*In here go all the creative ways you found to utilize the parameter in question for your own measurements, i.e. you found a way to make use of the changed behavior beyond the intended use. This is especially interest in the light of 'unlocking' the system.*
```

# Table of Contentes <!-- omit from toc -->
- [MINFLUX sequence parameters](#minflux-sequence-parameters)
  - [Global parameters](#global-parameters)
  - [``Itr`` (Iteration)](#itr-iteration)
  - [``Mode`` (Mode)](#mode-mode)
- [MINFLUX data fields](#minflux-data-fields)
  - [Global fields](#global-fields)
  - [``itr`` (iteration)](#itr-iteration-1)


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
- **default**: ``false``
- **value**: any ``integer`` (tested 0-10) and ``false`` for the **off**-state.
- **effect**: Determins if and how many times the background level is gauge during the current iteration. If the value is higher than ``1``/``true``, the results will *probably* be averaged. If the value is set to ``0``, the background level is not gauged at all. This is especially useful when working with samples that have a high background signal, e.g. due to autofluorescence or a high concentration of fluorescent dyes.
- **source**: Francesco Reina (personal communication, 2022)
- **hacks**:  ``unknown``

### ``ctrDwellFactor``
- **default**: 0.16
- **value**: any positive ``float``
- **effect**: Controls the fraction of the [``patDwellTime``](#patdwelltime) that is spent on the center frequency check. It is useful to set aside a time similar to the individual spot dwell time to ensure a reliable center frequency check. Keep in mind that the center frequency check is only performed if the [``ccrLimit``](#ccrlimit) is set to a positive value and that it will slow down the measurement by a time equal to [``ctrDwellFactor``](#ctrdwellfactor) times [``patDwellTime``](#patdwelltime) **PER** iteration.
- **source**: Jonatan Alvelid (Personal communication, Jan 2024)

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
- **source**: Jonatan Alvelid (Personal communication, Jan 2024)
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
- **effect**: Coefficients used in the position estimation. They are generated by Abberior using a simulated version of their MINFLUX 3D system. Apparently, they are effected by the photon limit and dwell time (``subject of discussion``).
- **source**: Abberior Instruments (Personal Communication, 2022)
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
- **effect**: Controls the TCP diameter. 
  - The used diameter caluclates as follows:
  $$\text{TCP diameter} = \text{patGeoFactor} \cdot 360\text{nm}$$
  * The following values are known to be used in tracking:
    |``patGeoFactor``|Diameter|Usecase
    |---|---|---|
    |0.28|100 nm|2D tracking
    |0.42|150 nm|2D tracking
- **source**: Abberior GmbH (personal communication, 2022)
- **hacks**: A smaller TCP forces a smaller area of photon collection thereby limiting the spatial localization error. However, the risk of losing any non fixated particles rises significantly with smaller collection-tolerances. 

### ``patRepeat``
- **value**: any positive ``integer`` or ``0`` for the off state. Probably ``-1`` works as well.
- **effect**: Sets the maximum number the current iteration step is repeated in case of unsuccessful particle localization. The break criterium is most likely ONLY the case when an insufficiet number of photons (<[photon imit](#phtlimit)) is collected during an entire TCP cycle, taking [dwell time](#patdwelltime) seconds. Be aware that setting ``patRepeat`` to zero breaks the sequence as it apparently turns off the iteration entirely (``Tested`` by Agnes Koerfer). A possible cause could be that the ``0`` is interpreted as a ``boolean`` rather than an ``integer``.
- **source**: Jonatan Alvelid (Personal communication, Jan 2024)
- **hacks**: ``unknown``

### ``phtLimit``
- **value**: any positive ``integer``.
- **effect**: Determins the minimal amount of photons that have to be collected during a singular TCP cycle i.e., during [dwell time](#patdwelltime) seconds, in order for a localization estimation to be considered valid. Apparently, a change requires an update of the [estimation coefficients](#estcoeff), which are especially calculated for the new photon Limit (Francesco Reina, personal communicaltion, 2022 ``???``).
- **source**: Roman Schmidt (Nature communications, 2021)
- **hacks**: Decreasing the photon limit allows for faster tracking as the [dwell time](#patdwelltime) can be reduced correspondingly. However, reducing the statistical sample of photons per localization **drastically** increased variance and renders each measurement more prone to noise. This is especially grave when working with "higher" (MINFLUX standards) particle densities.

### ``pwrFactor``
- **value**: any positive ``integer`` but given as a ``float``. 
- **effect**: This parameter probably affects the excitation laser power during hte current iteration. However, it is ``unknown`` in what exact way this is done.
- **source**: Jonatan Alvelid (Personal communication, Jan 2024)
- **hacks**: ``unknown``

### ``wavelength``
- **value**: any positive ``float``.
- **effect**: Probably addresses the wavelength used for excitation. However, it is unclear if this parameter changes due to the laser selected via *Imspector* during measurements. Thus, it is possible that the value listed here is just a default.
- **source**: 
  - Jonatan Alvelid (Personal communication, Jan 2024)
  - Bela Vogler
- **hacks**: ``unknown``


## ``Mode`` (Mode)

### ``dim``
- **value**: any positive ``integer`` from ``{2,3}``. Untested if it takes other values.
- **effect**: Set the spatial (Euclidean) dimension in which to perform the localization.
- **source**: Jonatan Alvelid (Personal communication, Jan 2024)
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
- **source**: Jonatan Alvelid (Personal communication, Jan 2024)
- **hacks**: ``unknown``

### ``modulated``
- **value**: any ``string`` probably referencing presets, e.g. ```["phl", "exc"]```.
- **effect**: ``unknown``
- **source**: ``unknown``
- **hacks**: ``unknown``

### ``pattern``
- **value**: any ``string`` referencing presets ```["hexagon", "square", "octagon", "triangle", "zline", "zline2"]```.
- **effect**: Set or reference the scan pattern, thus the number of vertices within the TCP and correspondingly the grometry of the area or volume that is used for collecting photons.
- **source**: Jonatan Alvelid (Personal communication, Jan 2024)
- **hacks**: ``unknown``

### ``phDiaAU``
- **value**: any positive ``float``, e.g. ```[1.5, 1.6]```.
- **effect**: Set or reference the pinhole size in Airy Units (AU).
- **source**: Jonatan Alvelid (Personal communication, Jan 2024)
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

## Global fields

### ``act``
- **value**: ``Boolean``
- **content**: States if the activation laser has been used during the localization. This is potentially only useful for imaging applications.
- **source**: Talk @SciLifeLab (Abberior, Oct 2023)
- **hacks**: ``unknown``

### ``dos``
- **value**: Any positive ``integer``.
- **content**: ``unknown``
- **source**: ``unknown``
- **hacks**: ``unknown``

### ``gri``
- **value**: Any positive ``integer``.
- **content**: Grid scan position during initial iteration.
- **source**: Jonatan Alvelid (Personal communication, Jan 2024)
- **hacks**:``unknown``

### ``itr``
- **value**: ``python list`` 
- **content**: Container for iteration specific readouts. Will have as many entries as [``iterations``](#itr-iteration) have been specified int he sequence.
- **source**: ``Common knowledge``
- **hacks**: ``unknown``

### ``sky``
- **value**: Any positive ``integer``
- **content**: The maximum number of repetitions taken to localize the emitter. Limited by the [``stickiness``](#stickiness) parameter. This value is recorded per trajectory. 
- **source**: Talk @SciLifeLab (Abberior, Oct 2023)
- **hacks**: As surpassing the [``stickiness``](#stickiness) threshold is a breaking condition for tracking photon burst events, it is useful for checking this condition in your data and adjusting filters.

### ``sqi``
- **value**: Probably any positive ``integer``. Observed ``0``.
- **content**: ``unknown``
- **source**: ``unknown``
- **hacks**: ``unknown``

### ``tid``
- **value**: Any positive ``integer``.
- **content**: The ``track-id (tid) `` is given to each sucessfully concluded photon burst trace. Localizations with the same ``tid`` are recorded for the "same" photon burst event. This is however **NOT** a valid measure to separate single particles, as they can be recorded in continuation under one single ``tid``.
- **source**: Talk @SciLifeLab (Abberior, Oct 2023)
- **hacks**: Can be used in paraview for color coding or for fundamental track separation in post. 

### ``tim``
- **value**: Any positive ``float``.
- **content**: States the time in seconds of sucessful position estimation relative to the point in time the measurement has been started. 
- **source**: Talk @SciLifeLab (Abberior, Oct 2023)
- **hacks**: ``unknown``

### ``vld``
- **value**: ``Boolean``
- **content**: States the validity of the estimated position.
- **source**: Talk @SciLifeLab (Abberior, Oct 2023)
- **hacks**:  Usually, only valid localizations are exported (checkbox in Imspector). However, non-valid localizations can be used to DEBUG the system. As the value is given per localization, it is an easy filter parameter.

## ``itr`` (iteration)

### ``cfr``
- **value**: Any positive ``float``.
- **content**: The ``center-frequency-ratio (cfr)`` calculated for the current iteration. This filed is only filled if the [``ccrLimit``](#ccrlimit) is set to a positive value, which enables the scan in the center of the TCP.
- **source**: Talk @SciLifeLab (Abberior, Oct 2023)
- **hacks**: As the ccr check is triggered after the scan for photons but before the localization has beed updated, it is essentially useless in the last iterations of tracking applications since particles are constantly in motion.

### ``dcr``
- **value**: Any positive ``float`` $\in [0.0, 1.0]$.
- **content**: The ``detector-count-ratio (dcr)`` between two detenction channels. It is calcuated as follow:
  $$
  \text{dcr} = \frac{\text{ECO}_1}{\text{ECO}_1+ \text{ECO}_2}
  $$
- **source**: Talk @SciLifeLab (Abberior, Oct 2023)
- **hacks**: Can be used to determine the emission ratio of each dye per localization. 

### ``dmz``
- **value**: Any ``float``.
- **content**: Beam deflection parameter. Probably deformable mirror Z-deflection.
- **source**: Talk @SciLifeLab (Abberior, Oct 2023)
- **hacks**: Can probably be used to troubleshoot or debug 3D applications.

### ``ecc``
- **value**: Any positive ``integer``.
- **content**: The ``effective-count-(at)-center (ecc)`` states the sum of photons collected during the center scan. It is only calculated and expressed in case the [ccrLimit](#ccrlimit) is given a positive value.
- **source**: Talk @SciLifeLab (Abberior, Oct 2023)
- **hacks**: ``unknwon``

### ``eco``
- **value**: Any positive ``integer``.
- **content**: The ``effective-count-(at)-offset (eco)`` states the sum of photons collected during all TCP cycles.
- **source**: Talk @SciLifeLab (Abberior, Oct 2023)
- **hacks**: ``unknwon``

### ``efc``
- **value**: Any positive ``float``.
- **content**: The ``effective-frequency-(at)-center (efc)`` states the emission frequency of photons collected during the center scan. It is only calculated and expressed in case the [ccrLimit](#ccrlimit) is given a positive value. It is calculated as follows: 
  $$
  \text{EFC}=\frac{\text{ECC}}{o \cdot t_{dwell}}
  $$
  With $o$ being the [ctrDwellFactor](#ctrdwellfactor).
- **source**: Talk @SciLifeLab (Abberior, Oct 2023)
- **hacks**: Can be used to filter out multiple emitters in close space for imaging applications in post. Can also be used to determine the number of cycles used to debug the system.

### ``efo``
- **value**: Any positive ``float``.
- **content**: The ``effective-frequency-(at)-offset (efo)`` states the total emission frequency of photons collected during all TCP cycles. It is calculated as follows: 
  $$
  \text{EFO}=\frac{\text{ECO}}{k \cdot t_{dwell}}
  $$
  With $k$ being the number of TCP cycles used.
- **source**: Talk @SciLifeLab (Abberior, Oct 2023)
- **hacks**: Can be used to filter out multiple emitters in close space for imaging applications in post. Can also be used to determine the number of cycles used to debug the system.
 
### ``eox``
- **value**: Any ``float``.
- **content**: Beam deflection parameter. Probably EOD offset in X-direction. 
- **source**: Talk @SciLifeLab (Abberior, Oct 2023)
- **hacks**: ``unknown``

### ``eoy``
- **value**: Any ``float``.
- **content**: Beam deflection parameter. Probably EOD offset in Y-direction. 
- **source**: Talk @SciLifeLab (Abberior, Oct 2023)
- **hacks**: ``unknown``

### ``ext``
- **value**: 
  ```python
  [float, float, float]
  ```
- **content**: TCP extend. It is unclear if it is just the diameter or the extend in XYZ. As of now, no asymmetric TCPs are known.
- **source**: Talk @SciLifeLab (Abberior, Oct 2023)
- **hacks**: ``unknown``

### ``fbg``
- **value**: Any ``float``.
- **content**: Photon detection frequency of the background. Only determined if [bgcSense](#bgcsense) is enabled.
- **source**: Jonatan Alvelid (Personal communication, Jan 2024)
- **hacks**: ``unknown``

### ``gvx``
- **value**: Any ``float``.
- **content**: Beam deflection parameter. Probably Galvo offset in X-direction. 
- **source**: Talk @SciLifeLab (Abberior, Oct 2023)
- **hacks**: ``unknown``

### ``gvy``
- **value**: Any ``float``.
- **content**: Beam deflection parameter. Probably Galvo offset in Y-direction. 
- **source**: Talk @SciLifeLab (Abberior, Oct 2023)
- **hacks**: ``unknown``

### ``itr``
- **value**: Any positive ``integer`` $\in[0,\text{num}_{iterations})$
- **content**: Iteration ID. Only the last one will retrun a localization.
- **source**: Talk @SciLifeLab (Abberior, Oct 2023)
- **hacks**: ``unknown``

### ``lcx``
- **value**: Any ``float``.
- **content**: Deflection parameter of ``unknown`` relevance.
- **source**: Talk @SciLifeLab (Abberior, Oct 2023)
- **hacks**: ``unknown``

### ``lcy``
- **value**: Any ``float``.
- **content**: Deflection parameter of ``unknown`` relevance.
- **source**: Talk @SciLifeLab (Abberior, Oct 2023)
- **hacks**: ``unknown``

### ``lcz``
- **value**: Any ``float``.
- **content**:  Deflection parameter of ``unknown`` relevance.
- **source**: Talk @SciLifeLab (Abberior, Oct 2023)
- **hacks**: ``unknown``

### ``lnc``
- **value**: 
  ```python
  [float, float, float]
  ```
- **content**: Uncoreccted localization estimate in meters. Entries correspond to XYZ with a biased estimator.
- **source**: Jonatan Alvelid (Personal communication, Jan 2024)
- **hacks**: ``unknown``

### ``loc``
- **value**: 
  ```python
  [float, float, float]
  ```
- **content**: Coreccted localization estimate in meters. Entries correspond to XYZ after the estimator has been *unbiased*. Will only be produced by the last iteration.
- **source**: ``Known``
- **hacks**: ``unknown``

### ``sta``
- **value**: Probably any ``integer``. ``0`` has been observed.
- **content**: Status. This probably corresponds to a catalog of Error messages used to DEBUG.
- **source**: Jonatan Alvelid (Personal communication, Jan 2024)
- **hacks**: ``unknown``

### ``tic``
- **value**: Any positive ``integer``.
- **content**: A parameter of the used FPGA. Probably the internal clock tic.
- **source**: Talk @SciLifeLab (Abberior, Oct 2023)
- **hacks**: ``unknown``

