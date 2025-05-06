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

    def predict(
        self,
        video: Path = Input(description="input the video file"),
    ) -> Path:
        """Run a single prediction on the model"""
        # processed_input = preprocess(image)
        # output = self.model(processed_image, scale)
        # return postprocess(output)

        video_path = str(video)
        sd = SubtitleRemover(video_path, sub_area=None)
        sd.run()
        return sd.video_out_name
