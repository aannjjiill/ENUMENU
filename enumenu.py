import subprocess

def run_command(command):
    """Run shell commands using subprocess"""
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Error executing command: {command}")
        print(f"stderr: {stderr.decode('utf-8')}")
    else:
        print(stdout.decode('utf-8'))

def main():
    # Step 1: Ask for the domain to run waybackurls
    domain = input("Enter the domain (e.g., example.com): ")
    
    # Run waybackurls and store in waybackurls.txt
    print("Running waybackurls...")
    wayback_command = f'echo "http://{domain}" | waybackurls | anew waybackurls.txt'
    run_command(wayback_command)
    
    # Step 2: Ask for hakrawler depth level and run katana and hakrawler
    depth = input("Enter hakrawler depth level (e.g., 3): ")
    print(f"Running katana and hakrawler with depth level {depth}...")
    katana_hakrawler_command = f'cat waybackurls.txt | katana | hakrawler -d {depth} | anew katana_urls.txt'
    run_command(katana_hakrawler_command)
    
    # Step 3: Extract paths and store in all_paths.txt
    print("Extracting paths and storing them in all_paths.txt...")
    extract_paths_command = 'cat katana_urls.txt waybackurls.txt | unfurl format %p | anew all_paths.txt'
    run_command(extract_paths_command)
    
    # Display all enumerated paths
    with open('all_paths.txt', 'r') as f:
        paths = f.readlines()
    print(f"\nEnumerated Paths ({len(paths)} total):")
    for path in paths:
        print(path.strip())
    
    # Step 4: Ask if the user wants to find subdomains
    find_subs = input("\nDo you want to extract subdomains? (y/n): ").lower()
    if find_subs == 'y':
        print("Extracting subdomains and storing them in allsubs.txt...")
        extract_subs_command = 'cat katana_urls.txt waybackurls.txt | unfurl format %d | anew allsubs.txt'
        run_command(extract_subs_command)

        with open('allsubs.txt', 'r') as f:
            subs = f.readlines()
        print(f"\nEnumerated Subdomains ({len(subs)} total):")
        for sub in subs:
            print(sub.strip())
    else:
        print("Skipping subdomain extraction.")

if __name__ == "__main__":
    main()