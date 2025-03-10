# Prediction interface for Cog ⚙️
# https://cog.run/python

from backend.main import SubtitleRemover
from cog import BasePredictor, Input, Path
import os
import requests
import tempfile


class Predictor(BasePredictor):
    def setup(self) -> None:
        """Load the model into memory to make running multiple predictions efficient"""
        # self.model = torch.load("./weights.pth")

    def download_video(self, url: str) -> str:
        try:
            with requests.get(str(url), stream=True) as r:
                r.raise_for_status()
                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp_file:
                    for chunk in r.iter_content(chunk_size=8192):
                        tmp_file.write(chunk)
                    video_path = tmp_file.name
        except requests.exceptions.RequestException as e:
          raise Exception(f"Failed to download video: {e}")
        except Exception as e:
          raise Exception(f"An unexpected error occured when downloading video: {e}")
        
        return video_path


    def predict(
        self,
        video: Path = Input(description="input the video file"),
    ) -> Path:
        """Run a single prediction on the model"""
        # processed_input = preprocess(image)
        # output = self.model(processed_image, scale)
        # return postprocess(output)

        # video is a http path,  download the video to local
        # video_path = self.download_video(video)
        video_path = video
        print("video path: ", video_path)

        sd = SubtitleRemover(video_path, sub_area=None)
        sd.run()
        return f"{os.path.basename(video).rsplit('.', 1)[0]}_no_sub.mp4"
