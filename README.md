# MaktabKhoone.org video's download link collector

This robot will log in by your credentials into [MaktabKhoone](https://MaktabKhoone.org) and try to extract the download
links of given course.

## Setup:

1. Clone the repository from GitHub:

```shell
git clone https://github.com/Amirmahdikahdouii/MaktabKhooneCrawler.git
```

2. Install requirements:

```shell
cd MaktabKhooneCrawler
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Setup `.env`:

```shell
cp .env.example .env
```

4. Fill **.env** variables with your own credentials
5. Run bot:

```shell
python main.py
```

### Rename files after download:
Remember after extracting links, you will have 2 files:
1. links.txt
2. file_names.txt

You can use `links.txt` for downloading using IDM, and after downloading completed, you will need `file_names.txt` to 
rename downloaded files.

#### For rename files:
```shell
python rename_files.py
```

and for first input, give path where all the downloaded movies are there, then for second input give the path for 
`file_names.txt`

#### Example for inputs:
```shell
/home/user/Downloads/course/
/home/user/Desktop/MaktabKhooneCrawler/file_names.txt
```
