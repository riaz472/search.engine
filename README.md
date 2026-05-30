---
title: Nexus Search Ultimate
emoji: 🔍
colorFrom: blue
colorTo: green
sdk: docker
app_port: 7860
pinned: false
---

# Nexus Search Ultimate

A privacy-respecting metasearch engine powered by [SearXNG](https://github.com/searxng/searxng).
Users are neither tracked nor profiled.

## Deployment

### Hugging Face Spaces (Docker)
This repository is configured as a Hugging Face Docker Space on port `7860`.
Push to the `main` branch to trigger an automatic redeploy.

### PythonAnywhere (WSGI)
Point your PythonAnywhere WSGI config at `wsgi.py`:

```python
import sys, os
sys.path.insert(0, '/path/to/search.engine')
os.environ.setdefault('SEARXNG_SETTINGS_PATH', '/path/to/search.engine/searx/settings.yml')
from wsgi import application
```

### Local development
```bash
pip install -r requirements.txt
python -m searx.webapp
```

## License
[AGPL-3.0](LICENSE)
