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

    id_start,id_end = get_id_range(snapshot, sub_id)

    filename = download_substructure(snapshot, sub_id, id_start, id_end)
    print(f"Download file: {filename}")

def get_id_range(snapshot, sub_id):
    id_start = sub_id // 1000 * 1000
    id_end = id_start + 999
    
    return id_start, id_end

def download_substructure(snapshot, sub_id, id_start, id_end):
    filename = f"sub_{snapshot:04d}_{sub_id:05d}.hdf5"
    url = f"https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/{snapshot:04d}/{id_start:06d}_{id_end:06d}/{filename}"
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
