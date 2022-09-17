from datetime import datetime

from config.config import BASE_DIR
from pathlib import Path


def move_user_pic(user_id, file_path: Path):
    target_folder = Path(BASE_DIR / "src" / "static" / str(user_id))  # /src/static/101/
    target_folder.mkdir(exist_ok=True)
    file = file_path.rename(target_folder / Path(str(datetime.now().strftime("%I_%M_%S")) + file_path.name)) # /src/static/101/name.jpg
    size = file.stat().st_size
    file_name_for_db = f"/static/{user_id}/{file.name}"
    return file_name_for_db, size


def delete_user_pic(file_path: str):
    filename = Path(f"{BASE_DIR}/src{file_path}")
    try:
        filename.unlink()
    except FileNotFoundError as err:
        print(err)
