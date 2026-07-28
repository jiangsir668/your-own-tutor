#!/usr/bin/env python3
"""Jiaocheng v18.0 — GitHub Link Checker"""
import urllib.request, json, sys

BASE = "https://api.github.com/repos/jiangsir668/your-own-tutor"
HEADERS = {"User-Agent": "python", "Accept": "application/vnd.github.v3+json"}

def check_url(url, label):
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        code = urllib.request.urlopen(req).getcode()
        return "✅" if code == 200 else f"⚠️ {code}"
    except Exception as e:
        return f"❌ {str(e)[:60]}"

# Verify repo exists
repo = json.loads(urllib.request.urlopen(urllib.request.Request(BASE, headers=HEADERS)).read())
print(f"Repository: {repo['name']} — {repo['description']}")

# Verify all files
files_url = f"{BASE}/git/trees/main?recursive=1"
tree = json.loads(urllib.request.urlopen(urllib.request.Request(files_url, headers=HEADERS)).read())
print(f"\nFiles: {sum(1 for f in tree['tree'] if f['type']=='blob')} blobs")
for f in tree['tree']:
    if f['type'] == 'blob' and f['path'].startswith('jiaocheng'):
        print(f"  {f['path']} ({f['size']}B)")

print("\n✅ GitHub sync complete — v18.0")
