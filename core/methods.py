import json
import os
from pathlib import Path


class Organizer:
    def __init__(self, dir) -> None:
        self.dir = dir

    def organize(self):
        ext_dir = Path(__file__).parent
        file_path = ext_dir / "file_extensions.json"
        with open(file_path, "r") as file:
            extensions = json.load(fp=file)
        files = os.listdir(self.dir)
        for file in files:
            for key, values in extensions.items():
                for value in values:
                    if file.endswith(value):
                        filtered_dir = Path(os.path.join(self.dir, key))
                        if not filtered_dir.exists():
                            Path.mkdir(filtered_dir, exist_ok=True, parents=True)
                        os.rename(
                            os.path.join(self.dir, file),
                            os.path.join(self.dir, key, file),
                        )
                        break

    def organizerPhotos(self):
        ext_dir = Path(__file__).parent
        file_path = ext_dir / "file_extensions.json"
        with open(file_path, "r") as file:
            extensions = json.load(fp=file)
        files = os.listdir(self.dir)
        for file in files:
            ext = extensions["image"]
            for extension in ext:
                if file.endswith(extension):
                    os.rename(
                        os.path.join(self.dir, file),
                        os.path.join(self.dir, "image", file),
                    )

    def organizeVideos(self):
        ext_dir = Path(__file__).parent
        file_path = ext_dir / "file_extensions.json"
        with open(file_path, "r") as file:
            extensions = json.load(fp=file)
        files = os.listdir(self.dir)
        for file in files:
            ext = extensions["video"]
            for extension in ext:
                if file.endswith(extension):
                    os.rename(
                        os.path.join(self.dir, file),
                        os.path.join(self.dir, "video", file),
                    )

    def organizeAudio(self):
        ext_dir = Path(__file__).parent
        file_path = ext_dir / "file_extensions.json"
        with open(file_path, "r") as file:
            extensions = json.load(fp=file)
        files = os.listdir(self.dir)
        for file in files:
            ext = extensions["audio"]
            for extension in ext:
                if file.endswith(extension):
                    os.rename(
                        os.path.join(self.dir, file),
                        os.path.join(self.dir, "audio", file),
                    )

    def organizeProgram(self):
        ext_dir = Path(__file__).parent
        file_path = ext_dir / "file_extensions.json"
        with open(file_path, "r") as file:
            extensions = json.load(fp=file)
        files = os.listdir(self.dir)
        for file in files:
            ext = extensions["program"]
            for extension in ext:
                if file.endswith(extension):
                    os.rename(
                        os.path.join(self.dir, file),
                        os.path.join(self.dir, "program", file),
                    )

    def organizeCompressed(self):
        ext_dir = Path(__file__).parent
        file_path = ext_dir / "file_extensions.json"
        with open(file_path, "r") as file:
            extensions = json.load(fp=file)
        files = os.listdir(self.dir)
        for file in files:
            ext = extensions["compressed"]
            for extension in ext:
                if file.endswith(extension):
                    os.rename(
                        os.path.join(self.dir, file),
                        os.path.join(self.dir, "compressed", file),
                    )

    def organizeText(self):
        ext_dir = Path(__file__).parent
        file_path = ext_dir / "file_extensions.json"
        with open(file_path, "r") as file:
            extensions = json.load(fp=file)
        files = os.listdir(self.dir)
        for file in files:
            ext = extensions["text"]
            for extension in ext:
                if file.endswith(extension):
                    os.rename(
                        os.path.join(self.dir, file),
                        os.path.join(self.dir, "text", file),
                    )
