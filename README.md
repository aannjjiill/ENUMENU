# ENUMENU

**ENUMENU** is a simple tool for enumerating historical URLs, paths, and subdomains using several popular command-line utilities such as `waybackurls`, `katana`, `hakrawler`, `unfurl`, and `anew`. The tool helps automate the process of collecting URL paths and subdomains for a given domain.

## Features

- Extract URLs from the Wayback Machine using `waybackurls`.
- Run deep link discovery using `katana` and `hakrawler`.
- Extract all paths and subdomains using `unfurl`.
- Supports different depth levels for `hakrawler`.
- Results are stored in `waybackurls.txt`, `katana_urls.txt`, `all_paths.txt`, and `allsubs.txt`.

## Installation and Usage

Install ENUMENU
Clone the repository and install the tool:

git clone https://github.com/aannjjiill/ENUMENU.git
cd ENUMENU
python3 enumerator.py

### Prerequisites

Make sure you have the following tools installed on your system:

- `waybackurls`
- `katana`
- `hakrawler`
- `unfurl`
- `anew`

You can install them using `go` or your system's package manager. For example, to install `waybackurls` and `hakrawler`, you can run:

```bash
go install github.com/tomnomnom/waybackurls@latest
go install github.com/hakluke/hakrawler@latest
go install github.com/tomnomnom/unfurl@latest
go install github.com/tomnomnom/anew@latest
go install github.com/projectdiscovery/katana/cmd/katana@latest
