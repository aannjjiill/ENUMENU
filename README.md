# ENUMENU

**ENUMENU** is a simple tool for enumerating historical URLs, paths, and subdomains using several popular command-line utilities such as `waybackurls`, `katana`, `hakrawler`, `unfurl`, and `anew`. This tool automates the process of collecting URL paths and subdomains for a given domain, helping you with quick and efficient enumeration.

## Features

- Extract URLs from the Wayback Machine using `waybackurls`.
- Perform deep link discovery using `katana` and `hakrawler`.
- Extract all URL paths and subdomains using `unfurl`.
- Supports customizable depth levels for `hakrawler` scans.
- Saves results to organized output files:
  - `waybackurls.txt`: URLs from Wayback Machine.
  - `katana_urls.txt`: Discovered URLs via `katana` and `hakrawler`.
  - `all_paths.txt`: Extracted URL paths.
  - `allsubs.txt`: Extracted subdomains (optional).

## Installation and Usage

### Clone the Repository

First, clone the repository to your local machine and run the tool:

```bash
git clone https://github.com/aannjjiill/ENUMENU.git
cd ENUMENU
python3 enumenu.py

```
## Prerequisites
Before using ENUMENU, ensure you have the following tools installed on your system:
- waybackurls
- katana
- hakrawler
- unfurl
- anew

You can install them using go or your system's package manager. For example, to install waybackurls and hakrawler, run the following commands:
```bash
go install github.com/tomnomnom/waybackurls@latest
go install github.com/hakluke/hakrawler@latest
go install github.com/tomnomnom/unfurl@latest
go install github.com/tomnomnom/anew@latest
go install github.com/projectdiscovery/katana/cmd/katana@latest
````
## Credits
This tool utilizes the following open-source utilities:
- waybackurls
- katana
- hakrawler
- unfurl
- anew
  
## 
Thanks to <a href=https://github.com/projectdiscovery>ProjectDiscovery</a>, <a href=https://github.com/tomnomnom>tomnomnom</a> and <a href=https://github.com/hakluke/>hakluke</a> for creating these amazing tools!
