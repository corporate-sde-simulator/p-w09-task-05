"""
Build Runner — orchestrates the build process.
This file is clean — the bugs are in the YAML config.
"""

import os
import sys
import subprocess


class BuildRunner:
    def __init__(self):
        self.build_dir = os.getenv('BUILD_DIR', './build')
        self.env = os.getenv('NODE_ENV', 'development')

    def clean(self):
        """Remove previous build artifacts."""
        if os.path.exists(self.build_dir):
            import shutil
            shutil.rmtree(self.build_dir)
        os.makedirs(self.build_dir, exist_ok=True)
        print(f"Cleaned build directory: {self.build_dir}")

    def compile_assets(self):
        """Compile static assets."""
        print(f"Compiling assets for {self.env}...")
        # Simulated compilation
        with open(os.path.join(self.build_dir, 'app.bundle.js'), 'w') as f:
            f.write('// Compiled bundle')
        print("Assets compiled successfully")

    def run(self):
        """Execute the full build pipeline."""
        print("=== Build Runner ===")
        self.clean()
        self.compile_assets()
        print(f"Build complete (env: {self.env})")
        return True


if __name__ == '__main__':
    runner = BuildRunner()
    success = runner.run()
    sys.exit(0 if success else 1)
