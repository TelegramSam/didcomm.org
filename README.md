# didcomm.org
![logo](didcomm-logo.png)

This repo contains the content for [https://didcomm.org](https://didcomm.org). The website is intended to be the world's nexus for all things DIDComm -- [the spec](https://identity.foundation/didcomm-messaging/spec/v2.1/), documentation, examples, and a global registry of protocol definitions.

### Contributing

The Decentralized Identity Foundation (DIF) sponsors a [DIDComm Working Group](https://identity.foundation/working-groups/did-comm.html) that meets weekly (Mondays at 3 pm Eastern, 9 pm Central Europe, noon Pacific, 5 am Tokyo) to discuss all things DIDComm. The general public can listen in.

To modify content on this website, raise a PR against something in the `/docs` folder.

To publicly register or modify a DIDComm protocol definition, follow [this guide](./docs/pr-guide.md).

### Building the Site

This site uses MkDocs Material. To build and serve the site locally:

1. Set up a Python virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install the required packages:
   ```
   pip install mkdocs-material
   ```

3. Build the site:
   ```
   mkdocs build
   ```

4. Serve the site locally:
   ```
   mkdocs serve
   ```

### License

All content in this repo is contributed under an [Apache 2.0 license](LICENSE) and must be signed (`git commit -s`) to provide a [Developer Certificate of Origin](https://github.com/apps/dco).