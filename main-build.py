import subprocess
import argparse

def run_build_script(folder, version):
    """Run the build.py script for a given folder and version."""
    try:
        # Call the build.py script using subprocess
        subprocess.run(
            ['python3', 'build.py', folder, version],
            check=True  # Will raise an error if the script fails
        )
        print(f"Successfully processed {folder} with version {version}")
    except subprocess.CalledProcessError as e:
        print(f"Error while processing {folder}: {e}")

def main():
    # Set up argument parsing for version
    parser = argparse.ArgumentParser(description="Run build.py script for multiple folders with a single version.")
    parser.add_argument('version', help="Version number to use for all folders.")
    args = parser.parse_args()

    folders = [
        'craftable-tridents',
        'craftable-rooted-dirt',
        'craftable-enchanted-golden-apples',
        'copper-door-cutting',
        'craftable-horse-armor',
        'craftable-elytra',
        'craftable-nametags',
        'craftable-chainmail'
        # Add new folders here when needed
    ]
    
    # Get the version from the argument
    version = args.version
    
    # Loop over all folders and execute build.py for each one with the given version
    for folder in folders:
        run_build_script(folder, version)

if __name__ == '__main__':
    main()

