import os

if "CI" in os.environ and "GITHUB_RUN_ID" in os.environ:
    print("Running on GitHub Actions")
else:
    print("Not running on GitHub Actions")
