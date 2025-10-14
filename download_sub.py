import requests
import argparse
import h5py

def main():
    parser = argparse.ArgumentParser(description="Download substructure data from DARWIN-1 simulation.")
    parser.add_argument("snapshot", type=int, help="Snapshot number.")
    parser.add_argument("id", type=int, help="Substructure ID.")

    args = parser.parse_args()

    snapshot = args.snapshot
    sub_id = args.id

    id_start,id_end = get_id_range(snapshot,sub_id)

    filename = download_substructure(snapshot, id_start, id_end)
    print(f"Download file: {filename}")

def get_id_range(snapshot, sub_id):
    id_start = (sub_id - 1) // 400 * 400 + 1
    id_end = id_start + 399
    print(f"First guess for substructure ID range: {id_start} - {id_end}")
    
    filename = f"catalog_{snapshot:05d}.hdf5"
    url = f"https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/{snapshot:05d}/{filename}"
    download_file(url, filename)
    print(f"Downloaded catalog file: {filename} for ID range verification.")

    with h5py.File(filename, "r") as f:
        nsub = len(f['sub/halo_index'])
        if id_start > nsub:
            raise ValueError("Substructure ID exceeds the number of substructures in this snapshot.")
        if id_end > nsub:
            id_end = nsub

    print(f"Substructure ID range found: {id_start} - {id_end}")
    return id_start, id_end

def download_substructure(snapshot, id_start, id_end):
    filename = f"sub_{snapshot:05d}.hdf5"
    url = f"https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/{snapshot:05d}/{id_start:03d}_{id_end}/{filename}"
    download_file(url, filename)
    return filename

def download_file(url, filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=4194304):
                # 4 MB 단위로 나눠서 저장 (4194304 bytes)
                if chunk:
                    f.write(chunk)

if __name__ == "__main__":
    main()
