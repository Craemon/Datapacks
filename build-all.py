import subprocess
import argparse

def main():
    # Set up argument parsing for version
    parser = argparse.ArgumentParser(description="Run build.py script for multiple folders with a single version.")
    parser.add_argument('version', help="Version number to use for all folders.")
    args = parser.parse_args()
    
    # Get the version from the argument
    version = args.version
    
    # Run Main Scripts
    subprocess.run(['python3','general-build-main.py', version])
    subprocess.run(['python3','crafting-build-main.py', version])

if __name__ == '__main__':
    main()

