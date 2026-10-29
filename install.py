"""Install the Swayleo workflows from an extracted library; preview by default."""
from pathlib import Path
import argparse
import shutil
import hashlib
import json
import re

def digest_tree(path):
    return {str(f.relative_to(path)):hashlib.sha256(f.read_bytes()).hexdigest()
            for f in path.rglob('*') if f.is_file()}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply',action='store_true',help='Copy skills after reviewing the preview')
    parser.add_argument('--destination',type=Path,default=Path.home()/'.codex'/'skills')
    parser.add_argument('--skill',action='append',help='Install only a named skill; repeat to select several')
    parser.add_argument('--external',action='append',help='Opt in to an external source/skill ID, or all; see EXTERNAL-SKILLS.md')
    args=parser.parse_args()
    source=Path(__file__).resolve().parent/'skills'
    if not source.is_dir():parser.error('Extract the complete library ZIP first; skills/ is missing.')
    available={p.name:p for p in source.iterdir() if (p/'SKILL.md').is_file()}
    names=args.skill or ([] if args.external else sorted(available))
    unknown=set(names)-available.keys()
    if unknown:parser.error('Unknown skills: '+', '.join(sorted(unknown)))
    for name in names:
        src=available[name];dst=args.destination/name
        if dst.exists():
            state='already identical' if digest_tree(src)==digest_tree(dst) else 'existing version differs'
            print(f'SKIP {name}: {state}; no overwrite')
            continue
        print(f'{"INSTALL" if args.apply else "PREVIEW"} {name} -> {dst}')
        if args.apply:
            dst.parent.mkdir(parents=True,exist_ok=True)
            shutil.copytree(src,dst)
            if digest_tree(src)!=digest_tree(dst):raise RuntimeError(f'Copy verification failed: {name}')
    if args.external:
        root=Path(__file__).resolve().parent
        catalogue=json.loads((root/'external-manifest.json').read_text(encoding='utf-8'))['skills']
        ext_by_id={row['id']:row for row in catalogue}
        requested=sorted(ext_by_id) if 'all' in args.external else args.external
        unknown=set(requested)-ext_by_id.keys()
        if unknown:parser.error('Unknown external IDs: '+', '.join(sorted(unknown)))
        for skill_id in requested:
            row=ext_by_id[skill_id]
            if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',row['name']):parser.error('Unsupported external name')
            src=(root/row['path']).resolve().parent
            if not src.is_relative_to((root/'external').resolve()):parser.error('External source escapes library')
            dst=args.destination/row['name']
            if dst.exists():
                print(f'SKIP {skill_id}: destination exists; no overwrite')
                continue
            print(f'{"INSTALL" if args.apply else "PREVIEW"} external {skill_id} -> {dst}')
            if args.apply:
                dst.parent.mkdir(parents=True,exist_ok=True)
                shutil.copytree(src,dst)
                if digest_tree(src)!=digest_tree(dst):raise RuntimeError(f'Copy verification failed: {skill_id}')
                package=root/'external'/skill_id.split('/')[0]
                shutil.copy2(package/'SOURCE.json',dst/'UPSTREAM-SOURCE.json')
                for notice in package.glob('LICENSE*'):
                    if notice.is_file():shutil.copy2(notice,dst/('UPSTREAM-'+notice.name))
    print('Vendor source snapshots stay in vendor/. Install their official plugins and required tools separately.')
    if not args.apply:print('Preview only. Use --apply to copy the selected Swayleo skills.')

if __name__=='__main__':main()
