----- GENERAL INFORMATION -----

G01. Names of file(s) or dataset(s) that this README file describes
The dataset contains the following files: 
00_README.txt

01_Metadata.csv
LC_2019Q3.csv - LC_2019Q4.csv
LC_2020Q1.csv - LC_2020Q2.csv - LC_2020Q3.csv - LC_2020Q4.csv
LC_2021Q1.csv - LC_2021Q2.csv - LC_2021Q3.csv - LC_2021Q4.csv
LC_2022Q1.csv - LC_2022Q2.csv - LC_2022Q3.csv - LC_2022Q4.csv

LC-R_QCL1.Rmd - LC-R_QCL2.Rmd - LC-R_QCL3.Rmd
LC-X_QCL1.Rmd - LC-X_QCL2.Rmd - LC-X_QCL3.Rmd
OutlierSettings.txt


G02. Date of creation/last update of the README file
2023-01-06

G03. Name and contact information of Principal Investigator
Eva Beele - eva.beele@kuleuven.be 
Ben Somers - ben.somers@kuleuven.be

G04. ORCID of Principal Investigator
ORCID Eva Beele: 0000-0001-6838-1821
ORCID Ben Somers: 0000-0002-7875-107X

G05. Institution of Principal Investigator
KU Leuven 

G06. Description of the dataset
This dataset presents crowdsourced data from the Leuven.cool network, a citizen science network of around 100 low-cost weather stations (Fine Offset WH2600) distributed across Leuven, Belgium. The data was quality controlled and corrected by a newly developed station specific temperature quality control (QC) and correction procedure. The procedure consists of three levels removing implausible measurements, while also correcting for inter (in between stations) and intra (station-specific) station temperature biases by means of a random-forest approach.

G07. Keywords (author defined)
crowdsourcing, air temperature, citizen weather station, quality control



----- PROJECT INFORMATION -----

P01. Project information
Leuven.cool - The effect of urban green and blue on mitigating urban heat islands and improving thermal comfort 

P02. Project abstract
High air temperatures form a significant problem for human health, leading to an excess mortality of 6% or more than 2 000 extra deaths during the summers of 2003, 2006 and 2010 in Belgium alone. Projections show that climate change will induce increasing average air temperatures and will lead to an increased frequency and severity of heat waves. The consequences of these projections are even greater in urban areas where the urban heat island (UHI) effect can significantly increase air temperatures within the city center compared to their rural and more natural environment. The creation and enhancement of urban green and blue infrastructures (UGIs and UBIs) is one of the most promising solutions for mitigating urban heat through evaporation and shading. These cooling benefits are however highly affected by their spatial composition and configuration. Knowing the optimal spatial configuration of UGI and UBI would help managers and decision makers to plan and manage their urban green and blue in order to maximize their cooling effect. We know from previous research that a well-established urban green and blue infrastructure will lower urban air temperatures and consequently reduce human heat stress, but only a few studies have been able to quantify these heat-related health benefits. In this research we will therefore study the effect of the spatial composition and configuration of urban green and blue on heat mitigation in relation to human health and well-being. This will be done through a combination of remote sensing technology, a dense weather station network and citizens engagement across multiple spatial and temporal scales.

P03. Project funder: Name of funder, type of grant, grant number
FWO - Fellowship strategic basic research - 1SE0621N



----- FILE OVERVIEW -----

F01. Number of files described by the README-file
23 files

F02. List with names of files, description, date of creation of file
00_README_v4.txt: readme file - 2023/01/06

01_Metadata_v2.csv: Metadata of weather stations - 2022/10/21
LC_2019Q3.csv: Leuven.cool data from 2019 Q3 (July, August, September) - 2022/03/18
LC_2019Q4.csv: Leuven.cool data from 2019 Q4 (October, November, December) - 2022/03/18
LC_2020Q1.csv: Leuven.cool data from 2020 Q1 (January, February, March) - 2022/03/18
LC_2020Q2.csv: Leuven.cool data from 2020 Q2 (April, May, June) - 2022/03/18
LC_2020Q3.csv: Leuven.cool data from 2020 Q3 (July, August, September) - 2022/03/18
LC_2020Q4.csv: Leuven.cool data from 2020 Q4 (October, November, December) - 2022/03/18
LC_2021Q1.csv: Leuven.cool data from 2021 Q1 (January, February, March) - 2022/03/18
LC_2021Q2.csv: Leuven.cool data from 2021 Q2 (April, May, June) - 2022/03/18
LC_2021Q3.csv: Leuven.cool data from 2021 Q3 (July, August, September) - 2022/03/18
LC_2021Q4.csv: Leuven.cool data from 2021 Q4 (October, November, December) - 2022/03/18
LC_2022Q1.csv: Leuven.cool data from 2022 Q1 (January, February, March) - 2023/01/06
LC_2022Q2.csv: Leuven.cool data from 2022 Q2 (April, May, June) - 2023/01/06
LC_2022Q3.csv: Leuven.cool data from 2022 Q3 (July, August, September) - 2023/01/06
LC_2022Q4.csv: Leuven.cool data from 2022 Q4 (October, November, December) - 2023/01/06

LC-R_QCL1.Rmd: R markdown script for QCL1 of the LC-R stations - 2022/03/31
LC-R_QCL2.Rmd: R markdown script for QCL2 of the LC-R stations - 2022/03/31
LC-R_QCL3.Rmd: R markdown script for QCL3 of the LC-R stations - 2022/03/31
LC-X_QCL1.Rmd: R markdown script for QCL1 of the LC-X stations - 2022/03/31
LC-X_QCL2.Rmd: R markdown script for QCL2 of the LC-X stations - 2022/03/31
LC-X_QCL3.Rmd: R markdown script for QCL3 of the LC-X stations - 2022/03/31
OutlierSettings.txt: text file for defining outliers settings, needed in QCL1 - 2022/10/21

F03. File formats
.txt, .csv

F04. Software used to generate the data
R

F05. Software necessary to open the file
muliple: R, excel, ..

F06. Relationship between the files
F07. Which version of the dataset is this? Date of this version?
version 1 - 2022/03/31
version 2 - 2022/04/21
	restricted files have been unrestricted 
	sample file was removed
version 3 - 2022/10/21
	00_README_v2.txt is replaced by 00_README_v3.txt
	01_Metadata_v1.csv is replaced by 01_Metadata_v2.csv
	OutlierSettings.txt is replaced by OutlierSettings_v2.txt
version 4 - 2023/01/06
	00_README_v3.txt is replaced by 00_README_v4.txt
	LC_2022Q1.csv - LC_2022Q2.csv - LC_2022Q3.csv - LC_2022Q4.csv are added

F07. Information about the dataset versions and reason for updates
The dataset will be updated every 12 months with new data. 
version 2 - 2022/04/21
* restricted files have been unrestricted 
* sample file was removed
version 3 - 2022/10/21
* 00_README_v2.txt is replaced by 00_README_v3.txt
* 01_Metadata_v1.csv is replaced by 01_Metadata_v2.csv
* OutlierSettings.txt is replaced by OutlierSettings_v2.txt
version 4 - 2023/01/06
* 00_README_v3.txt is replaced by 00_README_v4.txt
* LC_2022Q1.csv - LC_2022Q2.csv - LC_2022Q3.csv - LC_2022Q4.csv are added


F08. Naming conventions for file names
The dataset is made available per 3 months/one quarter > LC_YYYYQX.csv



----- STORAGE INFORMATION -----

S01. Where are the data stored?
The data are stored on RDR: https://doi.org/10.48804/SSRN3F

S02. Links to other available locations of the dataset (e.g. repository)
Everyone can access the non quality controlled and corrected 5 minute aggregated dataset through https://wow.meteo.be/nl/



----- METHODOLOGICAL INFORMATION -----

M01. Date (beginning-end) and place of data collection
Data is collected from July 2019 onwards in Leuven, Belgium

M02. Aim for which the data were collected
Data is collected within the Leuven.cool project. 
The gaol of this project is to measure the microclimate in Leuven and investigate the mitigating effects of green and blue infrastructures. 

M03. Data collecting method
The weather stations were installed following a strict protocol. See accompanying publication for a detailed description.

M04. Information about data processing methods, the instrument & calibration and quality assurance procedures
The instrument and data processing methods- including the quality control and correction method - are described in the accompanying publication



----- DATA ACCESS AND SHARING -----

A01. Recommended citation for the dataset
Beele, Eva; Somers, Ben; Reyniers, Maarten; Aerts, Raf, 2022, "Replication Data for: Quality control and correction method for air temperature data from a citizen science weather station network in Leuven, Belgium", https://doi.org/10.48804/SSRN3F, KU Leuven RDR, v2, UNF:6:BxcNuUlMt85ET9gSFdtClw== [fileUNF] 

A02. License information, restrictions on use
This dataset is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License.: https://creativecommons.org/licenses/by-nc/4.0/. When using this dataset you must give appropriate credit, provide a link to the license, and indicate if changes were made. You may not use the material for commercial purposes.

A03. Confidentiality information
This dataset is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License.: https://creativecommons.org/licenses/by-nc/4.0/. When using this dataset you must give appropriate credit, provide a link to the license, and indicate if changes were made. You may not use the material for commercial purposes.


----- DATA SPECIFIC INFORMATION (ABOUT THE DATA THEMSELVES) -----

D01. Full names and definitions for columns and rows
Metadata.csv contains info on the weather station's ID, LAT, LON, ALT, LCZ, LC, building_height, SVF, installation_height. Columns = attributes, rows = weather stations 
LC_YYYUQX.csv contains the observations of the weather stations. Columns = attributes, rows = weather stations

D02. Explanation of abbreviations & units of measurements
Metadata.csv: 
	ID = Station's ID (ex. LC-XXX) [-]
	LAT = latitute (rounded to 3 decimals for privacy reasons) [-]
	LON = longitude (rounded to 3 decimals for privacy reasons) [-]
	ALT = altitude above sea level [m]
	LCZ = local climate zone [-]. For details: see accompanying publictation.
	LC = main landcover directly around weather station (0 = impervious/1= green) [-]
	building_height = mean building height in circular buffer 10m around weather station [m]
	SVF = mean sky view factor in circular buffer 10m around weather station [-]
	installation_height = installation height of weather station [m]

LC_YYYYQX.csv: 
	DATEUTC = Date and time (UTC) in POSIXct format: YYYY-MM-DD HH:MM:SS
	ID = Station's ID (ex. LC-XXX) [-]
 	LC_HUMIDITY = Relative humidity [%]
	LC_DWPTEMP = Dew point temperature [°C]
	LC_n = Number of 16 second observations in 10 minutes aggregate
	LC_RAD = Solar radiation [W/m2]
	LC_RAININ = Rain intensity [mm/h]
	LC_DAILYRAIN = Daily rain sum [mm]
	LC_WINDDIR = Wind direction [°]
	LC_WINDSPEED = Wind speed [m/s]
	Date = Date in YYYY-MM-DD
	Year = Year in YYYY
	Month = Month in MM
	Day = Day in DD
	Hour = Hour in HH
	Minute = Minute in MM
	LC_RAD60 = Weighted radiation during last 60 minutes [W/m2]
	LC_TEMP_QCL0 = Temperature at QCL0 [°C]
	LC_TEMP_QCL1 = Temperature at QCL1 [°C]
	LC_TEMP_QCL2 = Temperature at QCL2 [°C]
	LC_TEMP_QCL3 = Temperature at QCL3 [°C]

D03. Symbols for missing data
NA



----- RELATIONSHIPS -----

R01. Publications based on this dataset
Beele, E., Reyniers, M., Aerts, R., and Somers, B.: 
Quality control and correction method for air temperature data from a citizen science weather station network in Leuven, Belgium , Earth Syst. Sci. Data, 14, 4681–4717, 
https://doi.org/10.5194/essd-14-4681-2022, 2022.