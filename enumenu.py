import os
import subprocess
import time

def run_command(command):
    """Run shell commands using subprocess and measure execution time"""
    start_time = time.time()
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    end_time = time.time()
    elapsed_time = end_time - start_time

    if process.returncode != 0:
        print(f"Error executing command: {command}")
        print(f"stderr: {stderr.decode('utf-8')}")
    else:
        print(stdout.decode('utf-8'))
    
    return elapsed_time

def main():
    # Step 1: Ask for the domain and create a directory for it
    domain = input("Enter the domain (e.g., example.com or http://example.com): ").strip()
    
    # Extract domain name without protocol or path
    domain_name = domain.split('//')[-1].split('/')[0]
    
    # Create directory for the domain
    if not os.path.exists(domain_name):
        os.makedirs(domain_name)
    
    # Change working directory to the domain-specific directory
    os.chdir(domain_name)
    
    # Run waybackurls and store in waybackurls.txt
    print("Running waybackurls...")
    wayback_command = f'echo "{domain}" | waybackurls | anew waybackurls.txt'
    wayback_time = run_command(wayback_command)
    
    # Step 2: Ask for hakrawler depth level and run katana and hakrawler
    depth = input("Enter hakrawler depth level (e.g., 3): ").strip()
    katana_depth = input("Enter katana depth level (e.g., 2): ").strip()
    print(f"Running katana and hakrawler with depth level {depth} and katana depth {katana_depth}...")
    
    katana_hakrawler_command = f'cat waybackurls.txt | katana -d {katana_depth} | hakrawler -d {depth} | anew katana_urls.txt'
    katana_hakrawler_time = run_command(katana_hakrawler_command)
    
    # Step 3: Extract paths and store in all_paths.txt
    print("Extracting paths and storing them in all_paths.txt...")
    extract_paths_command = 'cat katana_urls.txt waybackurls.txt | unfurl format %p | anew all_paths.txt'
    paths_time = run_command(extract_paths_command)
    
    # Display all enumerated paths
    with open('all_paths.txt', 'r') as f:
        paths = f.readlines()
    print(f"\nEnumerated Paths ({len(paths)} total):")
    for path in paths:
        print(path.strip())
    
    # Step 4: Ask if the user wants to find subdomains
    find_subs = input("\nDo you want to extract subdomains? (y/n): ").strip().lower()
    if find_subs == 'y':
        print("Extracting subdomains and storing them in allsubs.txt...")
        extract_subs_command = 'cat katana_urls.txt waybackurls.txt | unfurl format %d | anew allsubs.txt'
        subs_time = run_command(extract_subs_command)

        with open('allsubs.txt', 'r') as f:
            subs = f.readlines()
        print(f"\nEnumerated Subdomains ({len(subs)} total):")
        for sub in subs:
            print(sub.strip())
    else:
        print("Skipping subdomain extraction.")
    
    # Estimate total time
    total_time = wayback_time + katana_hakrawler_time + paths_time + (subs_time if find_subs == 'y' else 0)
    print(f"\nEstimated total time for scan: {total_time:.2f} seconds")

if __name__ == "__main__":
    main()
