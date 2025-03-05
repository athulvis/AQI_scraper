# AQI Data from CPCB (Central Pollution Control Board)

[![License](https://img.shields.io/badge/license-GPL_3.0-blue.svg)](LICENSE)

[![scraper](https://github.com/athulvis/AQI_scraper/actions/workflows/scrapper.yml/badge.svg)](https://github.com/athulvis/AQI_scraper/actions/workflows/scrapper.yml)
## Overview

This repository contains Air Quality Index (AQI) data collected from [CPCB (Central Pollution Control Board)](https://cpcb.nic.in/) in India. The data spans from 2015 onwards, providing valuable insights into air quality trends over the years.

## Data Source

The data is sourced from the official CPCB website's download section and is organized by date. Each dataset corresponds to the AQI Bulletin for a specific date and is stored in PDF format.

## Usage

Feel free to explore the data for your analysis or research purposes. The PDF files are organized by date in the `data/` directory.

## Future Work

As part of future enhancements, we plan to implement the following:
- [x] **Pdf to CSV:**Scrape old pdf files and get data to more accessible format like csv 
- [ ] **Cleaning the CSV data:** Use pandas to clean and make a neat database of already scrapped csv data. Also append present data with the old ones.

## Contributing

If you find issues, have suggestions, or want to contribute to the project, please feel free to open an issue or create a pull request. Your input is highly appreciated!

## License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details.

