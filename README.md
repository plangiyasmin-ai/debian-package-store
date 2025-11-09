# Debian Package Store

A command-line interface tool for managing Debian packages with an interactive menu system.

```
  ____            _   _           
 |  _ \          | | (_)          
 | |_) | ___  ___| |_ _  ___  ___  
 |  _ < / _ \/ __| __| |/ _ \/ __| 
 | |_) |  __/ (__| |_| |  __/\__ \ 
 |____/ \___|\___|\__|_|\___||___/ 
```

## Features

- 📦 Interactive package management interface
- 📋 List available packages with descriptions
- ⬇️ Easy package installation with verification
- ❌ Package removal with confirmation
- 🔄 Automatic synchronization with local package database
- ✅ Installation verification system
- 🔍 Package search functionality

## Requirements

- Python 3.x
- Debian-based Linux distribution
- sudo privileges for package operations

## Installation

1. Clone the repository:
```bash
git clone https://github.com/plangiyasmin-ai/debian-package-store.git
cd debian-package-store
```

2. Make sure you have proper permissions:
```bash
chmod +x package_store.py
```

## Usage

Run the script:
```bash
python3 package_store.py
```

### Main Menu Options

1. **List Packages**
   - Shows a numbered list of available packages
   - Displays package descriptions
   - Allows direct installation from the list

2. **Install Package**
   - Search for packages
   - View detailed package information
   - Install with automatic verification

3. **Remove Package**
   - List installed packages
   - Remove packages with confirmation
   - Automatic removal verification
   - Syncs with packages database

4. **Exit**
   - Safely exit the program

## Features in Detail

### Package Installation
- Checks package availability before installation
- Verifies successful installation
- Shows package version after installation
- Handles errors gracefully

### Package Removal
- Lists currently installed packages
- Shows common packages separately
- Confirms before removal
- Verifies successful removal
- Updates local package database

### Package Listing
- Shows package descriptions
- Organizes by categories
- Numbers packages for easy selection
- Updates package list automatically

## File Structure

- `package_store.py` - Main program file
- `packages.json` - Local package database
- `README.md` - Documentation
- `logo_design.md` - Logo design documentation

## Error Handling

The program includes comprehensive error handling for:
- Missing sudo privileges
- Network connectivity issues
- Package not found
- Installation/removal failures
- Database synchronization errors

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Debian Package Management System
- Python Community
- All contributors to this project

## Contact

Yasmin Plangi - plangiyasmin-ai

Project Link: [https://github.com/plangiyasmin-ai/debian-package-store](https://github.com/plangiyasmin-ai/debian-package-store)

![License:
MIT](https://img.shields.io/badge
/License-MIT-blue.svg)
![Version](https://img.shields.io
/badge/Version-0.1-alpha-yellow
.svg)