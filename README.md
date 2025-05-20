# Stremoldi

Stremoldi is a reverse engineering tool that uses a local LLM to filter out unimportant strings from a binary.
We use it to filter out debug messages, usage templates, error codes, API keys, tokens or passwords, commands or flags, registry paths, URLs, IPs, and malware-like messages from a binary. It is a simple and lightweight tool that can be used to extract valuable information from a binary.

## Usage

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

2. You also need to install Microsoft.Sysinternals.Strings with winget:

```bash
winget install Microsoft.Sysinternals.Strings
```


2. Run the script:

```bash
python main.py
```

3. The script will output the filtered strings. You can then use them for further analysis or further processing. For example, you can use them to extract credentials, IPs, or URLs from a binary.

## Limitations

- The script currently uses a local LLM (OpenAI's GPT-3.5-turbo) to filter out strings. This means that the script is limited to the model's capabilities and cannot handle more complex scenarios.
- The script currently uses a simple prompt to filter out strings. This means that the script is limited to the model's capabilities and cannot handle more complex scenarios.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.