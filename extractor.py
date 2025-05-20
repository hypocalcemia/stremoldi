import subprocess

def extract_strings_from_file(file_path, limit=1000):
    result = subprocess.run(["strings", file_path], capture_output=True, text=True)
    lines = result.stdout.splitlines()
    return list(set(lines))[:limit]  # deduplicated and truncated
