# package_store.py

# ASCII Banner
print("  ____            _   _           ")
print(" |  _ \          | | (_)          ")
print(" | |_) | ___  ___| |_ _  ___  ___  ")
print(" |  _ < / _ \/ __| __| |/ _ \/ __| ")
print(" | |_) |  __/ (__| |_| |  __/\__ \ ")
print(" |____/ \___|\___|\__|_|\___||___/ ")

def display_menu():
    # ASCII Banner
    print("\nWelcome to the Debian Package Store")

    print("1. List Packages")
    print("2. Install Package")
    print("3. Remove Package")
    print("4. Exit")

def list_packages():
    import subprocess
    print("\nFetching available packages...")
    try:
        # Update package list
        subprocess.run(['sudo', 'apt', 'update'], check=True)
        # List available packages
        result = subprocess.run(['apt', 'list'], capture_output=True, text=True)
        packages = result.stdout.splitlines()[1:21]  # Get first 20 packages
        
        # Create a clean list of package names
        package_list = []
        for pkg in packages:
            try:
                # Extract just the package name before the '/'
                name = pkg.split('/')[0]
                package_list.append(name)
            except:
                continue

        # Display packages with numbers
        print("\nAvailable packages:")
        for i, pkg in enumerate(package_list, 1):
            print(f"{i}. {pkg}")
        
        print("\n[Showing first 20 packages]")
        
        # Ask user to select a package
        while True:
            try:
                choice = input("\nEnter package number to install (or 0 to return to main menu): ")
                if choice == '0':
                    return
                
                choice_idx = int(choice) - 1
                if 0 <= choice_idx < len(package_list):
                    selected_package = package_list[choice_idx]
                    print(f"\nYou selected: {selected_package}")
                    confirm = input(f"Do you want to install {selected_package}? (y/n): ")
                    if confirm.lower() == 'y':
                        install_package(selected_package)
                    break
                else:
                    print("Invalid package number. Please try again.")
            except ValueError:
                print("Please enter a valid number.")
            except Exception as e:
                print(f"Error: {e}")
                break
                
    except subprocess.CalledProcessError as e:
        print(f"Error listing packages: {e}")

def install_package(package_name):
    import subprocess
    import shutil
    
    # Check if we have sudo access
    if shutil.which('sudo') is None:
        print("Error: sudo is required to install packages")
        return

    try:
        # Check if package exists
        check_cmd = ['apt', 'show', package_name]
        result = subprocess.run(check_cmd, capture_output=True, text=True)
        
        if "No packages found" in result.stderr:
            print(f"Package '{package_name}' not found")
            return

        # Install the package
        print(f"Installing {package_name}...")
        install_cmd = ['sudo', 'apt', 'install', '-y', package_name]
        subprocess.run(install_cmd, check=True)

        # Verify installation
        verify_cmd = ['dpkg', '-l', package_name]
        verify_result = subprocess.run(verify_cmd, capture_output=True, text=True)
        
        if package_name in verify_result.stdout and "ii" in verify_result.stdout:
            print(f"\n✓ Package '{package_name}' was successfully installed")
            # Show package version
            version = [line for line in verify_result.stdout.splitlines() if package_name in line][0].split()[2]
            print(f"Version: {version}")
        else:
            print(f"\n⚠ Package '{package_name}' installation could not be verified")
            
    except subprocess.CalledProcessError as e:
        print(f"Error during package installation: {e}")

def update_packages_json(package_name):
    import json
    import os
    
    json_path = os.path.join(os.path.dirname(__file__), 'packages.json')
    try:
        # Read the current packages.json
        with open(json_path, 'r') as f:
            data = json.load(f)
        
        # Remove the package from the list
        data['packages'] = [pkg for pkg in data['packages'] if pkg['name'] != package_name]
        
        # Write back to the file
        with open(json_path, 'w') as f:
            json.dump(data, f, indent=2)
            
        return True
    except Exception as e:
        print(f"Error updating packages.json: {e}")
        return False

def remove_package(package_name):
    import subprocess
    import shutil
    
    # Check if we have sudo access
    if shutil.which('sudo') is None:
        print("Error: sudo is required to remove packages")
        return

    try:
        # Check if package is installed
        check_cmd = ['dpkg', '-l', package_name]
        result = subprocess.run(check_cmd, capture_output=True, text=True)
        
        if package_name not in result.stdout:
            print(f"Package '{package_name}' is not installed")
            return

        # Remove the package
        print(f"Removing {package_name}...")
        remove_cmd = ['sudo', 'apt', 'remove', '-y', package_name]
        subprocess.run(remove_cmd, check=True)

        # Verify removal
        verify_cmd = ['dpkg', '-l', package_name]
        verify_result = subprocess.run(verify_cmd, capture_output=True, text=True)
        
        if package_name not in verify_result.stdout or "ii" not in verify_result.stdout:
            print(f"\n✓ Package '{package_name}' was successfully removed")
            # Update packages.json
            if update_packages_json(package_name):
                print(f"✓ Removed {package_name} from packages.json")
            else:
                print(f"⚠ Failed to update packages.json")
        else:
            print(f"\n⚠ Package '{package_name}' removal could not be verified")
            
    except subprocess.CalledProcessError as e:
        print(f"Error during package removal: {e}")

def main():
    import subprocess
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            list_packages()
        elif choice == '2':
            search_term = input("Enter package name to search: ")
            try:
                result = subprocess.run(['apt-cache', 'search', search_term], 
                                     capture_output=True, text=True)
                if result.stdout:
                    print("\nSearch results:")
                    print(result.stdout)
                else:
                    print("No packages found matching your search.")
                package_name = input("\nEnter package name to install (or press Enter to cancel): ")
                if package_name.strip():
                    install_package(package_name)
            except Exception as e:
                print(f"Error searching for package: {e}")
        elif choice == '3':
            try:
                # Common packages to display
                common_packages = [
                    ("abiword", "Efficient, featureful word processor"),
                    ("apache2", "Apache HTTP Server"),
                    ("apt-utils", "Package management utilities"),
                    ("gimp", "GNU Image Manipulation Program"),
                    ("git", "Fast, scalable, distributed revision control system"),
                    ("nodejs", "evented I/O for V8 javascript"),
                    ("python3", "Interactive high-level object-oriented language"),
                    ("vim", "Vi IMproved - enhanced vi editor")
                ]

                # Get list of installed packages
                print("\nFetching installed packages...")
                result = subprocess.run(['dpkg', '-l'], capture_output=True, text=True)
                
                # Parse installed packages
                installed_packages = []
                installed_set = set()  # To track installed packages

                # First process installed packages
                print("\nCurrently Installed Packages:")
                count = 0
                for line in result.stdout.splitlines()[5:]:  # Skip header lines
                    parts = line.split()
                    if len(parts) >= 2 and parts[0] == "ii":  # Only show installed packages
                        pkg_name = parts[1]
                        pkg_desc = " ".join(parts[3:]) if len(parts) > 3 else ""
                        installed_packages.append(pkg_name)
                        installed_set.add(pkg_name)
                        count += 1
                        print(f"{count}. {pkg_name} - {pkg_desc} [Installed]")

                # Then show common packages if not already shown
                print("\nCommon Packages Available for Removal:")
                for pkg_name, pkg_desc in common_packages:
                    if pkg_name not in installed_set:
                        # Check if package is actually installed
                        check_cmd = ['dpkg', '-l', pkg_name]
                        check_result = subprocess.run(check_cmd, capture_output=True, text=True)
                        if pkg_name in check_result.stdout and "ii" in check_result.stdout:
                            count += 1
                            installed_packages.append(pkg_name)
                            print(f"{count}. {pkg_name} - {pkg_desc}")
                
                if not installed_packages:
                    print("No packages found")
                    continue
                    
                while True:
                    choice = input("\nEnter package number to remove (or 0 to return to main menu): ")
                    if choice == '0':
                        break
                        
                    try:
                        choice_idx = int(choice) - 1
                        if 0 <= choice_idx < len(installed_packages):
                            selected_package = installed_packages[choice_idx]
                            print(f"\nYou selected: {selected_package}")
                            confirm = input(f"Are you sure you want to remove {selected_package}? (y/n): ")
                            if confirm.lower() == 'y':
                                remove_package(selected_package)
                            break
                        else:
                            print("Invalid package number. Please try again.")
                    except ValueError:
                        print("Please enter a valid number.")
                        
            except subprocess.CalledProcessError as e:
                print(f"Error fetching installed packages: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()