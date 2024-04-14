class EnvironmentController:
    def __init__(self):
        pass

    def parse_env_file(self, env_file_path: str) -> dict[str, str]:
        env_vars = {}
        with open(env_file_path, 'r') as file:
            for line in file:
                # Skip lines that start with a comment
                if line.startswith('#') or not line.strip():
                    continue
                # Remove leading and trailing whitespace
                parts = line.strip().split('=', 1)
                if len(parts) != 2:
                    print(f"Skipping invalid line: {line}")
                    continue
                key, value = parts
                env_vars[key.strip()] = value.strip()
        return env_vars