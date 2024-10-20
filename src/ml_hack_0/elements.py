from typing import Tuple

import aiko_services as aiko

__all__ = [ "Test" ]

# --------------------------------------------------------------------------- #

class Test(aiko.PipelineElement):
    def __init__(self, context):
        context.set_protocol("test:0")
        context.get_implementation("PipelineElement").__init__(self, context)

    def process_frame(self, stream, images) -> Tuple[aiko.StreamEvent, dict]:
        for image in images:
            height = image.shape[0]
            width = image.shape[1]
            self.logger.debug(
                f"{self.my_id()}: width: {width}, height: {height}")
        return aiko.StreamEvent.OKAY, {"images": images}

# --------------------------------------------------------------------------- #
