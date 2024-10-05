# didcomm.org
![logo](didcomm-logo.png)

This repo contains the content for [https://didcomm.org](https://didcomm.org). The website is intended to be the world's nexus for all things DIDComm -- [the spec](https://identity.foundation/didcomm-messaging/spec/v2.1/), documentation, examples, and a global registry of protocol definitions.

## Running the site locally

This site is built using Hugo. To run a local copy for testing, follow these steps:

1. Install Hugo (if not already installed):
   ```
   sudo apt-get install hugo
   ```

2. Navigate to the `hugo_site` directory:
   ```
   cd /repos/didcomm.org/hugo_site
   ```

3. Start the Hugo development server:
   ```
   hugo server -D
   ```

4. Open your web browser and go to `http://localhost:1313` to view the site.

### Contributing

The Decentralized Identity Foundation (DIF) sponsors a [DIDComm Working Group](https://identity.foundation/working-groups/did-comm.html) that meets weekly (Mondays at 3 pm Eastern, 9 pm Central Europe, noon Pacific, 5 am Tokyo) to discuss all things DIDComm. The general public can listen in.

To modify static HTML on this website, raise a PR against something in the `/hugo_site` folder.

To publicly register or modify a DIDComm protocol definition, follow [this guide](./docs/pr-guide.md).

### License

All content in this repo is contributed under an [Apache 2.0 license](LICENSE) and must be signed (`git commit -s`) to provide a [Developer Certificate of Origin](https://github.com/apps/dco).