import os
from mkdocs.plugins import BasePlugin
from mkdocs.structure.nav import Navigation, Section, Link

class ProtocolNavPlugin(BasePlugin):
    def on_nav(self, nav: Navigation, config, files):
        protocols_dir = os.path.join(config['docs_dir'], 'protocols')
        protocols = []

        for root, dirs, files in os.walk(protocols_dir):
            for file in files:
                if file.lower() == 'readme.md':
                    rel_path = os.path.relpath(root, protocols_dir)
                    parts = rel_path.split(os.sep)
                    if len(parts) >= 2:
                        protocol_name = parts[0]
                        version = parts[1]
                        url = f'/{protocol_name}/{version}/'
                        title = f'{protocol_name.replace("-", " ").title()} {version}'
                        protocols.append(Link(title, url))

        protocols_section = Section('Protocols', protocols)
        nav.items.insert(1, protocols_section)  # Insert after Home

        return nav