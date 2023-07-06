# Wikipedia Scrapper
> Create datasets of English and Dutch sentences

## Features
- Generate Large amounts of labeled and unlabled datasets
- Mix of English and Dutch sentences

## Quickstart Guide
```bash 
py wiki_scraper.py <mode> <lang> <max_lines> <out_file>
```
  - `mode`: train or test (gen w/ or w/o lang prefix)
  - `lang`: en, nl, en:nl, or rand
  - `max_lines`: max lines of generated data file
  - `out_file`: path to output file

## Arguements
### Mode
> Mode to generate data
- `train`: Generate labled data
- `test`: Generate unlabled test data
  
### Lang
> Language to generate output
- `en`: English
- `nl`: Dutch
- `en:nl`: rough 50:50 ratio of English to Dutch
- `rand`: random English and Dutch text

### Max Lines
> Maximum lines to generate (default word count per line is 15)

### Out File
> File to write out to

## Examples
### Example Training Data
```
en|a large area of derelict contaminated land and is highly visible from the M275
en|at the gateway to Portsmouth.Several redevelopment plans have been proposed for visual improvements to
nl|Kejawan is een bestuurslaag in het regentschap Bondowoso van de provincie Oost-Java, Indonesië. Kejawan
en|Borjabad is a municipality located in the province of Soria, Castile and León, Spain.
nl|De Nederlandse kampioenschappen sprint 1994 voor mannen en vrouwen vormden een schaatsevenement dat onder
nl|van de KNSB over de sprintvierkamp (2x 500, 2x 1000 meter) werd verreden. Het
nl|plaats in het weekend van 5 en 6 maart op de semi-overdekte ijsbaan van
nl|sportcentrum De Uithof in Den Haag, tegelijkertijd met de Nederlandse kampioenschappen schaatsen allround 1994
```
> Training Data will always start with 'en' or 'nl' followed by the '|' character and matches the following regex: `^(?:en|nl)\|(.*)$`

### Example Testing Data
```
door A24. Op 23 oktober 2020 ging de film in première op streamingdienst Apple
Garisheh (Persian: گريشه, also Romanized as Garīsheh and Gerīsheh) is a village in Moqam
District, Shibkaveh District, Bandar Lengeh County, Hormozgan Province, Iran. At the 2006 census, its
The Commandos had the honor of playing in the first AFL regular season game
June 19, 1987, losing to the Pittsburgh Gladiators 46-48 at the Civic Arena. The
picked up their first win in franchise history the following week, when they defeated
Denver Dynamite, by a score of 36-20 in their home opener. The Commandos finished
van het district Trebišov.Zemplín telt 396 inwoners waarvan de meerderheid Hongaren zijn.Zemplín was de
```
