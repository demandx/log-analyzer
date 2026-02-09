import subprocess

def read_syslog(lines: int = 100) -> str:
    """
    Reads last N lines from /var/log/syslog using Linux tail command
    """
    try:
        result = subprocess.run(
            ["tail", "-n", str(lines), "/var/log/syslog"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout

    except subprocess.CalledProcessError as e:
        return f"Error reading syslog: {e}"

    except Exception as e:
        return f"Unexpected error: {e}"
