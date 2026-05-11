#!/usr/bin/env python
"""
Deployment preparation script for Wealth Navigator
Prepares the app for deployment to Render, Heroku, or other hosting services
"""

import os
import sys
import subprocess

def check_requirements():
    """Check if all required files exist"""
    required_files = [
        'requirements.txt',
        'Procfile',
        'render.yaml',
        'run.py',
        'app/__init__.py',
        'templates/base.html',
        'templates/home.html'
    ]
    
    print("📋 Checking required files...")
    missing = []
    for file in required_files:
        if os.path.exists(file):
            print(f"  ✓ {file}")
        else:
            print(f"  ✗ {file} (MISSING)")
            missing.append(file)
    
    return len(missing) == 0

def check_git():
    """Check if git is initialized and configured"""
    print("\n📚 Checking Git configuration...")
    
    if not os.path.exists('.git'):
        print("  ✗ Git repository not initialized")
        return False
    
    print("  ✓ Git repository found")
    
    # Check for uncommitted changes
    try:
        result = subprocess.run(['git', 'status', '--porcelain'], 
                              capture_output=True, text=True, timeout=5)
        if result.stdout.strip():
            print(f"  ⚠ Uncommitted changes found:\n{result.stdout}")
            return True
        else:
            print("  ✓ All changes committed")
            return True
    except Exception as e:
        print(f"  ⚠ Could not check git status: {e}")
        return True

def check_dependencies():
    """Check if dependencies are listed in requirements.txt"""
    print("\n🔧 Checking dependencies...")
    
    required_deps = ['Flask', 'gunicorn', 'openpyxl']
    
    with open('requirements.txt', 'r') as f:
        content = f.read()
    
    for dep in required_deps:
        if dep in content:
            print(f"  ✓ {dep}")
        else:
            print(f"  ✗ {dep} (MISSING)")
    
    return True

def main():
    print("=" * 60)
    print("🚀 Wealth Navigator - Deployment Preparation")
    print("=" * 60)
    
    # Change to app directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Run checks
    files_ok = check_requirements()
    git_ok = check_git()
    deps_ok = check_dependencies()
    
    print("\n" + "=" * 60)
    if files_ok and git_ok and deps_ok:
        print("✅ Ready for deployment!")
        print("\nNext steps:")
        print("1. Push to GitHub: git push origin main")
        print("2. Create account on Render.com")
        print("3. Connect your GitHub repository")
        print("4. Deploy using the DEPLOYMENT_GUIDE.md")
        print("\n📚 See DEPLOYMENT_GUIDE.md for detailed instructions")
    else:
        print("❌ Some checks failed. Please fix the issues above.")
        sys.exit(1)
    
    print("=" * 60)

if __name__ == "__main__":
    main()
