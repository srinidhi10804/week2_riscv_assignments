import shutil
from pathlib import Path

def rename_elf_files(dut_dir: Path, new_name: str):
    elf_files = list(dut_dir.glob("*.elf"))
    for elf_file in elf_files:
        new_file = dut_dir / f"{new_name}.elf"
        elf_file.rename(new_file)
        print(f"Renamed {elf_file} to {new_file}")

def copy_co_directory(src_dir: Path, dst_dir: Path):
    def ignore_ref(dir, contents):
        return ['ref'] if 'ref' in contents else []

    shutil.copytree(src_dir, dst_dir, ignore=ignore_ref)
    print(f"Copied {src_dir} to {dst_dir} (skipping 'ref')")

def process_parent_directory(parent_dir: Path, destination_dir: Path):
    # Ensure destination directory exists
    destination_dir.mkdir(parents=True, exist_ok=True)
    print(f"Destination directory is {destination_dir}")

    for co_dir in parent_dir.iterdir():
        # Skip files and skip the destination directory itself
        if not co_dir.is_dir() or co_dir.resolve() == destination_dir.resolve():
            continue

        dut_dir = co_dir / "dut"
        if dut_dir.is_dir():
            print(f"Processing {co_dir} with dut subdirectory.")
            rename_elf_files(dut_dir, co_dir.name)
            dest_path = destination_dir / co_dir.name
            if dest_path.exists():
                shutil.rmtree(dest_path)
                print(f"Removed existing directory {dest_path}")
            copy_co_directory(co_dir, dest_path)
        else:
            print(f"Skipping {co_dir}: no 'dut' subdirectory.")

if __name__ == "__main__":
    parent_directory = Path("/home/vsysuser/workspace/week2_riscv_assignments")
    destination_directory = parent_directory / "copy_listed"
    process_parent_directory(parent_directory, destination_directory)
