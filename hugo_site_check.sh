#!/bin/bash

HUGO_DIR="/repos/didcomm.org/hugo_site"

echo "Checking Hugo site structure..."

# Check for hugo.toml
if [ -f "$HUGO_DIR/hugo.toml" ]; then
    echo "✅ hugo.toml found"
else
    echo "❌ hugo.toml not found"
fi

# Check for content directory
if [ -d "$HUGO_DIR/content" ]; then
    echo "✅ content directory found"
else
    echo "❌ content directory not found"
fi

# Check for layouts directory
if [ -d "$HUGO_DIR/layouts" ]; then
    echo "✅ layouts directory found"
else
    echo "❌ layouts directory not found"
fi

# Check for markdown files in content directory
if [ "$(find "$HUGO_DIR/content" -name "*.md" | wc -l)" -gt 0 ]; then
    echo "✅ Markdown files found in content directory"
else
    echo "❌ No markdown files found in content directory"
fi

echo "Hugo site structure check complete."